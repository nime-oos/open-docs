import re

with open("build.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. In all.html, the left sidebar links need to be anchor links.
# build_sidebar_html needs a parameter to generate anchor links instead of standard links.
# Let's replace the build_sidebar_html definition.
new_build_sidebar_html = """def build_sidebar_html(sidebar_data, current_route, prefix='', anchor_mode=False):
    html = []
    for group in sidebar_data:
        html.append('<div class="sidebar-group">')
        html.append(f'<div class="sidebar-group-title" onclick="toggleSidebarGroup(this)">')
        html.append(f'<span>{group["title"]}</span>')
        html.append('<svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>')
        html.append('</div>')
        html.append('<div class="sidebar-group-content" style="display: block;">')
        for child in group['children']:
            active_class = " active" if child["route"] == current_route else ""
            if anchor_mode:
                href = f"#{child['route'].replace('.html', '')}"
            else:
                href = f"{prefix}{child['route']}"
            html.append(f'<a href="{href}" class="sidebar-link{active_class}">{child["title"]}</a>')
        html.append('</div>')
        html.append('</div>')
    return "\\n".join(html)
"""
# Replace the old definition with this one.
code = re.sub(r"def build_sidebar_html.*?return \"\\n\"\.join\(html\)", new_build_sidebar_html, code, flags=re.DOTALL)

# 2. Update generate_all_in_one to pass anchor_mode=True
all_sidebar_logic = """
    all_sidebar_html = ""
    all_sidebar_html += f"<div style='padding: 8px; font-weight: bold; color: var(--color-green-600); margin-top: 10px;'>{FRAPPE_SITE_TITLE}</div>"
    all_sidebar_html += build_sidebar_html(frappe_sidebar_data, "", "", anchor_mode=True)
    all_sidebar_html += f"<div style='padding: 8px; font-weight: bold; color: var(--color-green-600); margin-top: 10px;'>{PYTHON_SITE_TITLE}</div>"
    all_sidebar_html += build_sidebar_html(python_sidebar_data, "", "python/", anchor_mode=True)
    all_sidebar_html += f"<div style='padding: 8px; font-weight: bold; color: var(--color-green-600); margin-top: 10px;'>{GIT_SITE_TITLE}</div>"
    all_sidebar_html += build_sidebar_html(git_sidebar_data, "", "git/", anchor_mode=True)
    all_sidebar_html += f"<div style='padding: 8px; font-weight: bold; color: var(--color-green-600); margin-top: 10px;'>{LINUX_SITE_TITLE}</div>"
    all_sidebar_html += build_sidebar_html(linux_sidebar_data, "", "linux/", anchor_mode=True)
    all_sidebar_html += f"<div style='padding: 8px; font-weight: bold; color: var(--color-green-600); margin-top: 10px;'>{SALES_SITE_TITLE}</div>"
    all_sidebar_html += build_sidebar_html(sales_sidebar_data, "", "sales/", anchor_mode=True)

    full_content_html = "\\n".join(all_content)
"""
code = re.sub(r"    all_sidebar_html = \"\".*?full_content_html = \"\\n\"\.join\(all_content\)", all_sidebar_logic, code, flags=re.DOTALL)

# 3. Remove right sidebar TOC from generate_all_in_one HTML
# Find <aside class="wiki-toc"> ... </aside> inside the generate_all_in_one html structure
code = re.sub(r"            <aside class=\"wiki-toc\">.*?</aside>", "", code, flags=re.DOTALL)

# 4. The user said "algunas paginas no estan agregafas agarra un script que consiga la informacino de todas las pafinas que que esten el all".
# That means we shouldn't iterate over `frappe_pages` (which is derived from sidebar_data),
# but instead iterate over EVERY key in `frappe_contents`!
# Let's change append_domain in generate_all_in_one.
append_domain_new = """    def append_domain(title, contents_dict):
        all_content.append(f"<h1 style='color: var(--color-green-700); margin-top: 60px; font-size: 2.5rem; border-bottom: 2px solid var(--color-green-500); padding-bottom: 10px;'>{title}</h1>")
        for route, data in contents_dict.items():
            page_id = route.replace('.html', '')
            all_content.append(f"<div id='{page_id}' style='padding-top: 20px; margin-top: -20px;'>")
            all_content.append(f"<h2 style='color: var(--color-green-600); margin-top: 40px;' id='page-{page_id}'>{data['title']}</h2>")
            all_content.append(data['content'])
            all_content.append("</div>")
            all_content.append("<hr style='margin: 40px 0;'>")
"""
code = re.sub(r"    def append_domain.*?all_content\.append\(\"<hr style='margin: 40px 0;'>\"\)", append_domain_new, code, flags=re.DOTALL)

# Update the calls to append_domain
code = code.replace("append_domain(\"Frappe HR\", frappe_pages, frappe_contents)", "append_domain(\"Frappe HR\", frappe_contents)")
code = code.replace("append_domain(\"Python Docs\", python_pages, python_contents)", "append_domain(\"Python Docs\", python_contents)")
code = code.replace("append_domain(\"Git Docs\", git_pages, git_contents)", "append_domain(\"Git Docs\", git_contents)")
code = code.replace("append_domain(\"Linux Docs\", linux_pages, linux_contents)", "append_domain(\"Linux Docs\", linux_contents)")
code = code.replace("append_domain(\"Ventas IT\", sales_pages, sales_contents)", "append_domain(\"Ventas IT\", sales_contents)")


with open("build.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Fixed logic for all.html")
