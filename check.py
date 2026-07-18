with open("build.py", "r", encoding="utf-8") as f:
    code = f.read()

import re
frappe_sidebar = re.search(r"frappe_sidebar_data = (\[.*?\])\n[a-z_]+_pages = ", code, re.DOTALL)
if frappe_sidebar:
    data = eval(frappe_sidebar.group(1))
    sidebar_pages = [child["route"] for group in data for child in group["children"]]
    print("Sidebar pages:", len(sidebar_pages))

# Just run a quick check of what's in the dicts
