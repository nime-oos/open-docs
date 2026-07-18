import json
with open("frappe/config.js", "r", encoding="utf-8") as f:
    code = f.read().replace("window.CONFIG_FRAPPE = ", "").strip()
    if code.endswith(";"): code = code[:-1]
    data = json.loads(code)

for route, page in data["contents"].items():
    print(f"[{len(page['content'])}] {page['title']}")
