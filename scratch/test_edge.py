import subprocess
import time
import json
import urllib.request

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# Launch Edge with remote debugging
cmd = [
    edge_path,
    "--headless=new",
    "--remote-debugging-port=9222",
    "--disable-gpu",
    "--no-sandbox",
    "http://localhost:3000"
]

proc = subprocess.Popen(cmd)
time.sleep(2)

try:
    # Query DevTools targets
    req = urllib.request.urlopen("http://127.0.0.1:9222/json")
    targets = json.loads(req.read().decode())
    print("DevTools targets:", targets)
finally:
    proc.terminate()
