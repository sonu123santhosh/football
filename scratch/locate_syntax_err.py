import asyncio
import json
import subprocess
import time
import urllib.request
import os
import websockets

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
CDP_PORT = 9225

async def isolate_syntax_error():
    cmd = [
        EDGE_PATH,
        "--headless=new",
        f"--remote-debugging-port={CDP_PORT}",
        "--disable-gpu",
        "--no-sandbox",
        "--user-data-dir=" + os.path.join(os.environ.get("TEMP", "."), "edge_test_profile_4"),
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

            with open(r"c:\Users\LENOVO\Desktop\web\js\components.js", "r", encoding="utf-8") as f:
                code = f.read()

            import re
            # Replace import ... from '...'; with comment
            mod_code = re.sub(r'import\s+.*?from\s+[\'"].*?[\'"];?', '// import ...', code)
            # Replace export function/const/let with function/const/let
            mod_code = re.sub(r'export\s+', '', mod_code)

            res = await send_cmd("Runtime.compileScript", {
                "expression": mod_code,
                "sourceURL": "http://localhost:3000/js/components.js",
                "persistScript": False
            })
            print("CompileScript Result:", json.dumps(res, indent=2))

    finally:
        proc.terminate()

asyncio.run(isolate_syntax_error())
