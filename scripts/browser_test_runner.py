import asyncio
import json
import subprocess
import time
import urllib.request
import os
import sys
import websockets

sys.stdout.reconfigure(encoding='utf-8')

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
CDP_PORT = 9222
BASE_URL = "http://localhost:3000"

async def run_browser_tests():
    profile_dir = os.path.join(os.environ.get("TEMP", "."), f"edge_test_profile_{int(time.time()*1000)}")
    cmd = [
        EDGE_PATH,
        "--headless=new",
        f"--remote-debugging-port={CDP_PORT}",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-cache",
        "--disable-application-cache",
        f"--user-data-dir={profile_dir}",
        BASE_URL
    ]
    
    proc = subprocess.Popen(cmd)
    await asyncio.sleep(2)

    try:
        # Find page ws url
        req = urllib.request.urlopen(f"http://127.0.0.1:{CDP_PORT}/json")
        targets = json.loads(req.read().decode())
        page_target = None
        for t in targets:
            if t.get("type") == "page" and "localhost:3000" in t.get("url", ""):
                page_target = t
                break
        
        if not page_target:
            for t in targets:
                if t.get("type") == "page":
                    page_target = t
                    break

        if not page_target:
            print("ERROR: No page target found in CDP targets.")
            return

        ws_url = page_target["webSocketDebuggerUrl"]
        print(f"Connecting to CDP WebSocket: {ws_url}")

        async with websockets.connect(ws_url, max_size=25_000_000) as ws:
            msg_id = 0
            console_logs = []

            async def send_cmd(method, params=None):
                nonlocal msg_id
                msg_id += 1
                payload = {"id": msg_id, "method": method, "params": params or {}}
                await ws.send(json.dumps(payload))
                while True:
                    res = json.loads(await ws.recv())
                    if "method" in res:
                        if res["method"] == "Runtime.consoleAPICalled":
                            log_type = res["params"]["type"]
                            args = [str(a.get("value", a.get("description", ""))) for a in res["params"]["args"]]
                            console_logs.append(f"[{log_type.upper()}] {' '.join(args)}")
                        elif res["method"] == "Runtime.exceptionThrown":
                            details = res["params"]["exceptionDetails"]
                            ex_url = details.get('url', 'inline')
                            ex_line = details.get('lineNumber', 0)
                            console_logs.append(f"[EXCEPTION in {ex_url}:{ex_line}] {details.get('text')} - {details.get('exception', {}).get('description')}")
                    if res.get("id") == payload["id"]:
                        return res.get("result", {})

            # Enable domains
            await send_cmd("Runtime.enable")
            await send_cmd("Page.enable")
            await send_cmd("DOM.enable")
            await send_cmd("Log.enable")
            await send_cmd("Network.enable")
            await send_cmd("Network.setCacheDisabled", {"cacheDisabled": True})
            await send_cmd("Page.reload", {"ignoreCache": True})

            async def eval_js(expression):
                res = await send_cmd("Runtime.evaluate", {
                    "expression": expression,
                    "returnByValue": True,
                    "awaitPromise": True
                })
                if "exceptionDetails" in res:
                    print(f"JS Eval Error: {res['exceptionDetails']}")
                return res.get("result", {}).get("value")

            # Allow DOM / scripts to execute
            await asyncio.sleep(1)

            print("\n--- INITIAL CONSOLE LOGS ---")
            for log in console_logs:
                print(" ", log)

            print("\n--- TEST SUITE: PAGE BOOTSTRAP & INITIAL VIEW ---")
            title = await eval_js("document.title")
            print(f"Document Title: {title}")
            
            raw_html = await eval_js("document.getElementById('mainContent')?.innerHTML || ''")
            print(f"Main Content Raw HTML: {repr(raw_html)}")
            main_html_len = len(raw_html)

            # Test navigation to every view
            views = [
                ("home", "home"),
                ("transfers", "transfers"),
                ("players", "players"),
                ("clubs", "clubs"),
                ("news", "news"),
                ("market", "market"),
                ("compare", "compare"),
                ("credits", "copyright")
            ]
            print("\n--- TEST SUITE: ROUTING & VIEWS ---")
            for v_name, v_target in views:
                print(f"Testing view: {v_name}...")
                await eval_js(f"window.bluegunApp.navigateTo('{v_name}')")
                await asyncio.sleep(0.5)
                has_content = await eval_js("document.getElementById('mainContent')?.children.length > 0")
                active_nav = await eval_js(f"document.querySelector('.nav-link[data-view=\"{v_target}\"]')?.classList.contains('active') || false")
                print(f"  View '{v_name}': rendered={has_content}, nav_active={active_nav}")
                assert has_content, f"View {v_name} rendered empty content!"

            print("\n--- TEST SUITE: PLAYER PROFILE VIEW ---")
            await eval_js("window.bluegunApp.navigateTo('player-profile', { playerId: 'florian-wirtz' })")
            await asyncio.sleep(0.5)
            player_name = await eval_js("document.querySelector('.player-big-name')?.innerText || ''")
            has_radar = await eval_js("document.querySelector('#playerRadarContainer svg') !== null")
            has_market_chart = await eval_js("document.querySelector('#playerValuationChart svg') !== null")
            print(f"  Player Profile: Name='{player_name}', RadarChart={has_radar}, MarketChart={has_market_chart}")
            assert player_name != "", "Player profile name is empty!"
            assert has_radar, "Player radar chart did not render!"
            assert has_market_chart, "Player market valuation chart did not render!"

            print("\n--- TEST SUITE: CLUB INTELLIGENCE VIEW & TABS ---")
            await eval_js("window.bluegunApp.navigateTo('club-profile', { clubId: 'real-madrid' })")
            await asyncio.sleep(0.5)
            club_name = await eval_js("document.querySelector('.club-title-big')?.innerText || ''")
            print(f"  Club Profile: Name='{club_name}'")
            assert club_name != "", "Club profile name is empty!"
            
            tabs = ['squad', 'injuries', 'suspensions', 'transfers', 'contracts', 'statistics']
            for tab in tabs:
                res = await eval_js(f"""
                    (() => {{
                        const btn = document.querySelector('[data-club-tab="{tab}"]');
                        if (btn) {{
                            btn.click();
                            return true;
                        }}
                        return false;
                    }})()
                """)
                await asyncio.sleep(0.3)
                tab_content = await eval_js("document.querySelector('.club-tab-content-mount')?.children.length > 0")
                print(f"  Club Tab '{tab}': clicked={res}, has_content={tab_content}")
                assert res and tab_content, f"Club Tab {tab} failed to render content!"

            print("\n--- TEST SUITE: EGO CLASH COMPARISON VIEW ---")
            await eval_js("window.bluegunApp.navigateTo('compare')")
            await asyncio.sleep(0.5)
            h2h_rows = await eval_js("document.querySelectorAll('.h2h-stat-row').length")
            compare_radar = await eval_js("document.querySelector('#comparisonRadarContainer svg') !== null")
            print(f"  Ego Clash: H2H Stats Rows={h2h_rows}, Compare Radar={compare_radar}")
            assert h2h_rows > 0, "No H2H stats rows rendered in compare view!"
            assert compare_radar, "Comparison radar chart did not render!"

            print("\n--- TEST SUITE: GLOBAL SEARCH MODAL ---")
            await eval_js("window.bluegunApp.openSearchModal()")
            await asyncio.sleep(0.3)
            search_open = await eval_js("document.getElementById('searchModal')?.classList.contains('active')")
            
            # Type search query "Wirtz"
            await eval_js("""
                (() => {
                    const inp = document.getElementById('globalSearchInput');
                    inp.value = 'Wirtz';
                    inp.dispatchEvent(new Event('input'));
                })()
            """)
            await asyncio.sleep(0.3)
            results_count = await eval_js("document.querySelectorAll('#globalSearchResults .search-result-item').length")
            print(f"  Search Modal: Open={search_open}, Results for 'Wirtz'={results_count}")
            await eval_js("window.bluegunApp.closeSearchModal()")

            print("\n--- TEST SUITE: NOTIFICATION & LEGAL MODALS ---")
            await eval_js("document.getElementById('btnNotifications')?.click()")
            await asyncio.sleep(0.3)
            notif_open = await eval_js("document.getElementById('notifModal')?.classList.contains('active')")
            print(f"  Notification Modal: Open={notif_open}")
            await eval_js("document.getElementById('closeNotifBtn')?.click()")

            await eval_js("window.bluegunApp.openLegalModal('privacy')")
            await asyncio.sleep(0.3)
            legal_title = await eval_js("document.getElementById('legalModalTitle')?.innerText")
            print(f"  Legal Modal: Title='{legal_title}'")
            await eval_js("window.bluegunApp.closeLegalModal()")

            print("\n--- TEST SUITE: SOURCE INSPECTOR MODAL ---")
            await eval_js("window.bluegunApp.openSourceModal('IMG-001')")
            await asyncio.sleep(0.3)
            src_modal_open = await eval_js("document.getElementById('sourceModal')?.classList.contains('active')")
            src_content_len = await eval_js("document.getElementById('sourceModalBody')?.innerHTML.length || 0")
            print(f"  Source Modal: Open={src_modal_open}, Content Length={src_content_len}")
            await eval_js("window.bluegunApp.closeSourceModal()")

            print("\n--- CAPTURED CONSOLE LOGS & WARNINGS ---")
            if console_logs:
                for log in console_logs:
                    print(" ", log)
            else:
                print("  Clean console! Zero errors or unhandled exceptions logged.")

    finally:
        proc.terminate()

if __name__ == "__main__":
    asyncio.run(run_browser_tests())
