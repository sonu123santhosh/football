"""
Fix not_found error raising in backend/app/routes/clubs.py
"""

with open(r"c:\Users\LENOVO\Desktop\web\backend\app\routes\clubs.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace if not club: not_found(...) with if not club: raise not_found(...)
content = content.replace("    if not club:\n        not_found(", "    if not club:\n        raise not_found(")

with open(r"c:\Users\LENOVO\Desktop\web\backend\app\routes\clubs.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated backend/app/routes/clubs.py: properly raising not_found exceptions!")
