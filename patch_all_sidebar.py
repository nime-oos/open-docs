with open("build.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update build_sidebar_html definition
code = code.replace("def build_sidebar_html(sidebar_data, current_route):", "def build_sidebar_html(sidebar_data, current_route, prefix=''):")
code = code.replace("href=\"{child['route']}\"", "href=\"{prefix}{child['route']}\"")

# 2. Update generate_all_in_one logic
all_sidebar_logic = """
    all_sidebar_html = ""
    all_sidebar_html += f"<div style='padding: 8px; font-weight: bold; color: var(--color-green-600); margin-top: 10px;'>{FRAPPE_SITE_TITLE}</div>"
    all_sidebar_html += build_sidebar_html(frappe_sidebar_data, "", "")
    all_sidebar_html += f"<div style='padding: 8px; font-weight: bold; color: var(--color-green-600); margin-top: 10px;'>{PYTHON_SITE_TITLE}</div>"
    all_sidebar_html += build_sidebar_html(python_sidebar_data, "", "python/")
    all_sidebar_html += f"<div style='padding: 8px; font-weight: bold; color: var(--color-green-600); margin-top: 10px;'>{GIT_SITE_TITLE}</div>"
    all_sidebar_html += build_sidebar_html(git_sidebar_data, "", "git/")
    all_sidebar_html += f"<div style='padding: 8px; font-weight: bold; color: var(--color-green-600); margin-top: 10px;'>{LINUX_SITE_TITLE}</div>"
    all_sidebar_html += build_sidebar_html(linux_sidebar_data, "", "linux/")
    all_sidebar_html += f"<div style='padding: 8px; font-weight: bold; color: var(--color-green-600); margin-top: 10px;'>{SALES_SITE_TITLE}</div>"
    all_sidebar_html += build_sidebar_html(sales_sidebar_data, "", "sales/")

    full_content_html = "\\n".join(all_content)
"""
code = code.replace("    full_content_html = \"\\n\".join(all_content)", all_sidebar_logic)

# 3. Add sidebar to HTML structure in generate_all_in_one
sidebar_html_block = """
        <div class="site-body">
            <!-- Left Sidebar -->
            <aside class="wiki-sidebar" id="mobile-sidebar">
                <nav class="sidebar-nav">
                    {all_sidebar_html}
                </nav>
            </aside>
            <div class="mobile-sidebar-overlay" id="mobile-overlay"></div>
            
            <main class="wiki-main">
"""
code = code.replace("""        <div class="site-body">\n            <main class="wiki-main">""", sidebar_html_block)

# 4. Remove the CSS that hides the sidebar
code = code.replace("      /* Ocultar barra lateral izquierda en Todo-en-Uno para dar más espacio */\n      .wiki-sidebar { display: none; }\n      @media (min-width: 1024px) { .wiki-main { padding-left: 0; } }", "")

with open("build.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Patched all.html sidebar logic")
