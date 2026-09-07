import asyncio
import json
import subprocess
import time
import urllib.request
import os
import websockets

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
CDP_PORT = 9224

async def test_modules():
    cmd = [
        EDGE_PATH,
        "--headless=new",
        f"--remote-debugging-port={CDP_PORT}",
        "--disable-gpu",
        "--no-sandbox",
        "--user-data-dir=" + os.path.join(os.environ.get("TEMP", "."), "edge_test_profile_3"),
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
                    if res.get("id") == payload["id"]:
                        return res.get("result", {})

            await send_cmd("Runtime.enable")
            await send_cmd("Page.enable")
            await send_cmd("Page.navigate", {"url": "http://localhost:3000"})
            await asyncio.sleep(1)

            modules = ["data.js", "sources.js", "chart.js", "components.js", "app.js"]
            for m in modules:
                expr = f"import('/js/{m}?t=' + Date.now())"
                res = await send_cmd("Runtime.evaluate", {
                    "expression": expr,
                    "awaitPromise": True
                })
                print(f"Loading {m}:")
                if "exceptionDetails" in res:
                    print(f"  FAILED with exception:\n", json.dumps(res["exceptionDetails"], indent=2))
                else:
                    print("  SUCCESS!")
    finally:
        proc.terminate()

asyncio.run(test_modules())
