import json
with open("frappe/config.js", "r", encoding="utf-8") as f:
    code = f.read().replace("window.CONFIG_FRAPPE = ", "").strip()
    if code.endswith(";"): code = code[:-1]
    data = json.loads(code)

for group in data["sidebar"]:
    print(f"Group: {group['title']}")
    for child in group["children"]:
        print(f" - {child['title']} (Route: {child['route']})")
        if child['route'] not in data["contents"]:
            print("   -> MISSING CONTENT!")
