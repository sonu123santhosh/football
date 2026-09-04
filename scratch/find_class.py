import glob
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

for js_file in glob.glob(r"c:\Users\LENOVO\Desktop\web\js\*.js"):
    print("Checking", js_file)
    with open(js_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for idx, line in enumerate(lines):
        # Look for suspicious class usage outside quotes/comments
        if re.search(r'\bclass\b', line):
            if "class=" not in line and "classList" not in line and "class " not in line and "className" not in line and "class:" not in line and "'class'" not in line and '"class"' not in line:
                print(f"  Line {idx+1}: {line.strip()}")
