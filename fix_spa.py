import re

with open("js/spa_app.js", "r") as f:
    code = f.read()

# 1. Update sidebarHTML initialization
new_sidebar_init = """    let sidebarHTML = `
      <div style="padding: 0 16px 16px 16px;">
        <a href="?tech=${currentTech}&page=all" class="tech-dropdown-item" style="background-color: var(--surface-gray-2); font-weight: 600; color: var(--color-green-600); justify-content: center; text-align: center;">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="margin-right:8px;"><path d="M4 6h16v2H4zm0 5h16v2H4zm0 5h16v2H4z"/></svg>
          Todo en Uno
        </a>
      </div>
    `;"""

code = code.replace("let sidebarHTML = '';", new_sidebar_init)

# 2. Update content rendering logic
content_logic_old = """    // Content
    const pageData = config.contents[currentRoute] || { title: 'No encontrado', content: '<p>Página no encontrada.</p>' };
    document.title = `${pageData.title} - ${config.title}`;
    document.getElementById('page-title').innerText = pageData.title;
    document.getElementById('wiki-content').innerHTML = pageData.content;

    // Prev / Next Nav"""

content_logic_new = """    // Content
    if (currentPage === 'all') {
        document.title = `Todo en Uno - ${config.title}`;
        document.getElementById('page-title').innerText = `Documentación Completa: ${config.title}`;
        
        let allContentHTML = '';
        for (const route in config.contents) {
            const pageData = config.contents[route];
            const pageId = route.replace('.html', '');
            allContentHTML += `
            <div id="${pageId}" style="padding-top: 20px;">
                <h2 style="color: var(--color-green-600); border-bottom: 1px solid var(--outline-gray-1); padding-bottom: 8px; margin-top: 40px;">${pageData.title}</h2>
                ${pageData.content}
            </div>
            `;
        }
        document.getElementById('wiki-content').innerHTML = allContentHTML;
    } else {
        const pageData = config.contents[currentRoute] || { title: 'No encontrado', content: '<p>Página no encontrada.</p>' };
        document.title = `${pageData.title} - ${config.title}`;
        document.getElementById('page-title').innerText = pageData.title;
        document.getElementById('wiki-content').innerHTML = pageData.content;
    }

    // Prev / Next Nav"""

code = code.replace(content_logic_old, content_logic_new)

# 3. Fix nav logic to hide if page=all
nav_logic_old = """    document.getElementById('spa-nav-links').innerHTML = navHTML;"""
nav_logic_new = """    document.getElementById('spa-nav-links').innerHTML = currentPage === 'all' ? '' : navHTML;"""

code = code.replace(nav_logic_old, nav_logic_new)


# 4. In case of page=all, make sure we don't accidentally set currentRoute incorrectly early on
# The current code says:
# const pageRoute = currentPage + '.html';
# if (!config.contents[pageRoute] && allPages.length > 0) {
#     currentPage = allPages[0].route.replace('.html', '');
# }
# const currentRoute = currentPage + '.html';
# We need to bypass this if currentPage === 'all'

fallback_old = """    const pageRoute = currentPage + '.html';
    if (!config.contents[pageRoute] && allPages.length > 0) {
        currentPage = allPages[0].route.replace('.html', '');
    }
    const currentRoute = currentPage + '.html';"""

fallback_new = """    let currentRoute = currentPage + '.html';
    if (currentPage !== 'all') {
        const pageRoute = currentPage + '.html';
        if (!config.contents[pageRoute] && allPages.length > 0) {
            currentPage = allPages[0].route.replace('.html', '');
            currentRoute = currentPage + '.html';
        }
    }"""

code = code.replace(fallback_old, fallback_new)

with open("js/spa_app.js", "w") as f:
    f.write(code)
print("Updated content logic for page=all")
