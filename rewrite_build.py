import re
with open("build.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update Dropdown HTML
code = code.replace('<a href="{base_path}introduction.html" class="tech-dropdown-item">Frappe HR</a>', '<a href="{base_path}frappe/introduction.html" class="tech-dropdown-item">Frappe HR</a>')

# 2. Update build_site call for Frappe HR
code = code.replace('build_site(frappe_pages, frappe_contents, frappe_sidebar_data, FRAPPE_SITE_TITLE, "", ".")', 'build_site(frappe_pages, frappe_contents, frappe_sidebar_data, FRAPPE_SITE_TITLE, "../", "frappe")')

# 3. Add json dump generation for content_data.js
# This will be added right before generate_all_in_one is called.
generate_js_func = """
import json

def generate_js_data():
    all_data = {
        "Frappe HR": { "sidebar": frappe_sidebar_data, "contents": frappe_contents, "prefix": "frappe/" },
        "Python Docs": { "sidebar": python_sidebar_data, "contents": python_contents, "prefix": "python/" },
        "Git Docs": { "sidebar": git_sidebar_data, "contents": git_contents, "prefix": "git/" },
        "Linux Docs": { "sidebar": linux_sidebar_data, "contents": linux_contents, "prefix": "linux/" },
        "Ventas IT": { "sidebar": sales_sidebar_data, "contents": sales_contents, "prefix": "sales/" }
    }
    
    js_code = f"window.CONTENT_DATABASE = {json.dumps(all_data)};\\n"
    if not os.path.exists("js"): os.makedirs("js")
    with open("js/content_data.js", "w", encoding="utf-8") as f:
        f.write(js_code)
    print("Generated js/content_data.js")
"""

# Replace generate_all_in_one completely.
new_generate_all = """
def generate_all_in_one():
    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Todo en Uno - Documentación Completa</title>
    <link rel="stylesheet" href="css/variables.css">
    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/typography.css">
    <link rel="stylesheet" href="css/layout.css">
    <link rel="stylesheet" href="css/sidebar.css">
    <link rel="stylesheet" href="css/content.css">
    <link rel="stylesheet" href="css/toc.css">
    <link rel="stylesheet" href="css/navigation.css">
    <link rel="stylesheet" href="css/components.css">
    <link rel="stylesheet" href="css/responsive.css">
    <style>
      .tech-dropdown {{ position: relative; }}
      .tech-dropdown-btn {{ display: flex; align-items: center; gap: 8px; background: transparent; border: none; cursor: pointer; padding: 4px; border-radius: var(--radius); transition: background-color var(--transition-fast); }}
      .tech-dropdown-btn:hover {{ background-color: var(--surface-gray-2); }}
      .tech-dropdown-menu {{ position: absolute; top: 100%; left: 0; margin-top: 8px; background-color: var(--surface-white); border: 1px solid var(--outline-gray-1); border-radius: var(--radius); box-shadow: var(--shadow-lg); min-width: 200px; display: none; flex-direction: column; padding: 4px; z-index: 100; }}
      .tech-dropdown-menu.is-open {{ display: flex; }}
      .tech-dropdown-item {{ padding: 8px 12px; color: var(--ink-gray-9); text-decoration: none; font-size: var(--text-sm); border-radius: var(--radius-sm); }}
      .tech-dropdown-item:hover {{ background-color: var(--surface-gray-2); }}
    </style>
</head>
<body>
    <div class="site-container">
        <header class="site-header">
            <div class="header-left tech-dropdown">
                {get_dropdown_html("")}
            </div>
            <nav class="header-nav"></nav>
            <div class="header-actions">
                <button class="theme-toggle" id="theme-toggle" aria-label="Toggle theme">
                    <div class="theme-knob">
                        <svg id="theme-sun" class="theme-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
                        <svg id="theme-moon" class="theme-icon" style="display:none" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
                    </div>
                </button>
                <div class="header-divider"></div>
                <a href="https://github.com/JACC34" class="github-link" target="_blank" rel="noopener noreferrer">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
                </a>
            </div>
        </header>

        <header class="mobile-header">
            <div class="header-left tech-dropdown">
                {get_dropdown_html("")}
            </div>
        </header>

        <div class="site-body">
            <!-- Left Sidebar -->
            <aside class="wiki-sidebar" id="mobile-sidebar">
                <nav class="sidebar-nav" id="dynamic-sidebar">
                    <!-- JS will populate sidebar -->
                </nav>
            </aside>
            <div class="mobile-sidebar-overlay" id="mobile-overlay"></div>

            <main class="wiki-main">
                <article class="wiki-article">
                    <div class="page-header">
                        <h1 class="page-title" id="page-title">Documentación Completa (Todo en Uno)</h1>
                        <p style="color: var(--ink-gray-5); margin-top: 10px;">Esta página contiene la documentación completa generada dinámicamente de todas las tecnologías.</p>
                    </div>
                    <div class="wiki-content prose prose-sm max-w-none scroll-smooth" id="dynamic-content">
                        <!-- JS will populate content -->
                        <div style="text-align:center; padding: 40px; color: var(--ink-gray-5);">Cargando documentación...</div>
                    </div>
                </article>
            </main>
        </div>
    </div>
    <script>window.SEARCH_DATA = [];</script>
    <script src="js/content_data.js"></script>
    <script src="js/dynamic_all.js"></script>
    <script src="js/app.js"></script>
</body>
</html>'''
    with open('all.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Generated ./all.html")
"""

code = re.sub(r"def generate_all_in_one\(\):[\s\S]*?print\(\"Generated \./all\.html\"\)", generate_js_func + "\n" + new_generate_all, code)

# Add generate_js_data call
code = code.replace("print(\"Building All-in-One Page...\")", "print(\"Generating JS Content Database...\")\ngenerate_js_data()\nprint(\"Building All-in-One Page...\")")

with open("build.py", "w", encoding="utf-8") as f:
    f.write(code)

print("build.py updated successfully.")
