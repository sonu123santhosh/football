import asyncio
import json
import subprocess
import time
import urllib.request
import os
import websockets

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
CDP_PORT = 9223
BASE_URL = "http://localhost:3000"

async def check_syntax_error():
    cmd = [
        EDGE_PATH,
        "--headless=new",
        f"--remote-debugging-port={CDP_PORT}",
        "--disable-gpu",
        "--no-sandbox",
        "--user-data-dir=" + os.path.join(os.environ.get("TEMP", "."), "edge_test_profile_2"),
        "about:blank"
    ]
    
    proc = subprocess.Popen(cmd)
    await asyncio.sleep(2)

    try:
        req = urllib.request.urlopen(f"http://127.0.0.1:{CDP_PORT}/json")
        targets = json.loads(req.read().decode())
        page_target = [t for t in targets if t.get("type") == "page"][0]
        ws_url = page_target["webSocketDebuggerUrl"]

        async with websockets.connect(ws_url) as ws:
            msg_id = 0
            async def send_cmd(method, params=None):
                nonlocal msg_id
                msg_id += 1
                payload = {"id": msg_id, "method": method, "params": params or {}}
                await ws.send(json.dumps(payload))
                while True:
                    res = json.loads(await ws.recv())
                    if "method" in res:
                        if res["method"] == "Runtime.exceptionThrown":
                            print("EXACT EXCEPTION DETAILS:", json.dumps(res["params"], indent=2))
                    if res.get("id") == payload["id"]:
                        return res.get("result", {})

            await send_cmd("Runtime.enable")
            await send_cmd("Debugger.enable")
            await send_cmd("Page.enable")
            
            # Navigate and listen
            payload = {"id": 999, "method": "Page.navigate", "params": {"url": BASE_URL}}
            await ws.send(json.dumps(payload))
            
            for _ in range(50):
                res = json.loads(await ws.recv())
                if "method" in res:
                    m = res["method"]
                    if m == "Runtime.exceptionThrown":
                        print("EXCEPTION:", json.dumps(res["params"], indent=2))
                    elif m == "Debugger.scriptFailedToParse":
                        print("SCRIPT FAILED TO PARSE:", json.dumps(res["params"], indent=2))

    finally:
        proc.terminate()

asyncio.run(check_syntax_error())
