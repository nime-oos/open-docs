import re

with open("build.py", "r", encoding="utf-8") as f:
    code = f.read()

# Replace build_sidebar_html definition safely
old_func_pattern = r"def build_sidebar_html\(sidebar_data, current_route, prefix=''\):[\s\S]*?return \"\\n\"\.join\(html\)"
new_func = """def build_sidebar_html(sidebar_data, current_route, prefix='', anchor_mode=False):
    html = []
    for group in sidebar_data:
        html.append('<div class="sidebar-group">')
        html.append(f'<div class="sidebar-group-title" onclick="toggleSidebarGroup(this)">')
        html.append(f'<span>{group["title"]}</span>')
        html.append('<svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>')
        html.append('</div>')
        html.append('<div class="sidebar-group-content" style="display: block;">')
        for child in group["children"]:
            active_class = " active" if child["route"] == current_route else ""
            if anchor_mode:
                href = f"#{child['route'].replace('.html', '')}"
            else:
                href = f"{prefix}{child['route']}"
            html.append(f'<a href="{href}" class="sidebar-link{active_class}">{child["title"]}</a>')
        html.append('</div>')
        html.append('</div>')
    return "\\n".join(html)"""

code = re.sub(old_func_pattern, new_func, code)

# Ensure no duplicate definition exists
code = code.replace("def build_sidebar_html(sidebar_data, current_route, prefix='', anchor_mode=False):", "###DEF_START###")
code = re.sub(r"def build_sidebar_html[\s\S]*?return \"\\n\"\.join\(html\)", "", code)
code = code.replace("###DEF_START###", new_func)

with open("build.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Fixed build_sidebar_html definition.")
