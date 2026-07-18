import json

with open("frappe/config.js", "r", encoding="utf-8") as f:
    code = f.read().replace("window.CONFIG_FRAPPE = ", "").strip()
    if code.endswith(";"): code = code[:-1]
    data = json.loads(code)

for route, page in data["contents"].items():
    content = page["content"]
    if len(content) < 100:
        print(f"Short/Empty: {page['title']} - length: {len(content)}")
        print(f"Content: {content}\n")
