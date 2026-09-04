import glob
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

for fpath in glob.glob(r"c:\Users\LENOVO\Desktop\web\js\*.js"):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check for unquoted http
    for idx, line in enumerate(content.splitlines()):
        if "http" in line:
            # Check if http is outside quotes
            stripped = line.strip()
            # If line has http without :// or quotes
            if not ('"http' in line or "'http" in line or "`http" in line or "//" in line or "/*" in line or "* " in line):
                print(f"File {fpath} Line {idx+1}: {stripped}")
