import os
import json

# Read build.py dynamically to grab variables
code = ""
with open("build.py", "r", encoding="utf-8") as f:
    code = f.read()

# We can literally just execute build.py in a safe way or strip the function calls at the end
clean_code = code.split("def get_dropdown_html")[0]

exec(clean_code)

# Now we have frappe_sidebar_data, frappe_contents, etc. in locals()
techs = [
    ("frappe", FRAPPE_SITE_TITLE, locals().get("frappe_sidebar_data"), locals().get("frappe_contents")),
    ("python", PYTHON_SITE_TITLE, locals().get("python_sidebar_data"), locals().get("python_contents")),
    ("git", GIT_SITE_TITLE, locals().get("git_sidebar_data"), locals().get("git_contents")),
    ("linux", LINUX_SITE_TITLE, locals().get("linux_sidebar_data"), locals().get("linux_contents")),
    ("sales", SALES_SITE_TITLE, locals().get("sales_sidebar_data"), locals().get("sales_contents"))
]

for folder, title, sidebar, contents in techs:
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    data = {
        "id": folder,
        "title": title,
        "sidebar": sidebar,
        "contents": contents
    }
    
    js_content = f"window.CONFIG_{folder.upper()} = {json.dumps(data)};\n"
    with open(f"{folder}/config.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"Exported {folder}/config.js")

# Central registry
registry = [
    {"id": "frappe", "title": FRAPPE_SITE_TITLE},
    {"id": "python", "title": PYTHON_SITE_TITLE},
    {"id": "git", "title": GIT_SITE_TITLE},
    {"id": "linux", "title": LINUX_SITE_TITLE},
    {"id": "sales", "title": SALES_SITE_TITLE}
]

if not os.path.exists("js"):
    os.makedirs("js")
with open("js/technologies.js", "w", encoding="utf-8") as f:
    f.write(f"window.TECHNOLOGIES = {json.dumps(registry)};\n")
print("Exported js/technologies.js")

