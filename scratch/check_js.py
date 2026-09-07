import os
import re

js_dir = r"c:\Users\LENOVO\Desktop\web\js"
files = ["app.js", "components.js", "chart.js", "data.js", "sources.js"]

for fname in files:
    fpath = os.path.join(js_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check braces, parentheses, brackets matching
    stack = []
    in_single = False
    in_double = False
    in_template = False
    in_comment_single = False
    in_comment_multi = False
    escape = False

    i = 0
    line = 1
    col = 1
    errors = []
    while i < len(content):
        c = content[i]
        nxt = content[i+1] if i+1 < len(content) else ""
        
        if c == '\n':
            line += 1
            col = 0
            if in_comment_single:
                in_comment_single = False
        
        col += 1

        if in_comment_single:
            i += 1
            continue
        if in_comment_multi:
            if c == '*' and nxt == '/':
                in_comment_multi = False
                i += 2
                col += 1
                continue
            i += 1
            continue
        
        if not in_single and not in_double and not in_template:
            if c == '/' and nxt == '/':
                in_comment_single = True
                i += 2
                continue
            if c == '/' and nxt == '*':
                in_comment_multi = True
                i += 2
                continue

        if escape:
            escape = False
            i += 1
            continue

        if c == '\\':
            escape = True
            i += 1
            continue

        if c == "'" and not in_double and not in_template:
            in_single = not in_single
            i += 1
            continue
        if c == '"' and not in_single and not in_template:
            in_double = not in_double
            i += 1
            continue
        if c == '`' and not in_single and not in_double:
            in_template = not in_template
            i += 1
            continue

        if not in_single and not in_double and not in_template:
            if c in "({[":
                stack.append((c, line, col))
            elif c in ")}]":
                if not stack:
                    errors.append(f"Unmatched closing '{c}' at {line}:{col}")
                else:
                    top, tline, tcol = stack.pop()
                    matching = {'(': ')', '{': '}', '[': ']'}
                    if matching[top] != c:
                        errors.append(f"Mismatched bracket '{top}' at {tline}:{tcol} closed by '{c}' at {line}:{col}")

        i += 1

    while stack:
        top, tline, tcol = stack.pop()
        errors.append(f"Unclosed '{top}' from {tline}:{tcol}")

    print(f"=== {fname} ===")
    if errors:
        for err in errors[:10]:
            print("  ERROR:", err)
        if len(errors) > 10:
            print(f"  ... and {len(errors)-10} more errors")
    else:
        print("  Syntax/Brackets: OK")
