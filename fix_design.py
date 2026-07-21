with open("js/spa_app.js", "r") as f:
    code = f.read()

# 1. Fix the sidebar button design and text
old_sidebar_init = """    let sidebarHTML = `
      <div style="padding: 0 16px 16px 16px;">
        <a href="?tech=${currentTech}&page=all" class="tech-dropdown-item" style="background-color: var(--surface-gray-2); font-weight: 600; color: var(--color-green-600); justify-content: center; text-align: center;">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="margin-right:8px;"><path d="M4 6h16v2H4zm0 5h16v2H4zm0 5h16v2H4z"/></svg>
          Todo en Uno
        </a>
      </div>
    `;"""

new_sidebar_init = """    let sidebarHTML = `
      <div style="padding: 12px 16px 20px 16px; border-bottom: 1px solid var(--outline-gray-1); margin-bottom: 16px;">
        <a href="?tech=${currentTech}&page=all" class="btn btn-secondary" style="width: 100%; display: flex; justify-content: center; align-items: center; gap: 8px; font-size: 0.875rem; padding: 10px 16px; border-radius: 8px; background-color: var(--surface-gray-1);">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path>
            <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>
          </svg>
          Vista Continua
        </a>
      </div>
    `;"""

code = code.replace(old_sidebar_init, new_sidebar_init)

# 2. Fix "Documentación Completa:" in the page title
old_title_logic = "document.getElementById('page-title').innerText = `Documentación Completa: ${config.title}`;"
new_title_logic = "document.getElementById('page-title').innerText = `Manual Completo: ${config.title}`;"

code = code.replace(old_title_logic, new_title_logic)

with open("js/spa_app.js", "w") as f:
    f.write(code)
print("Applied design fixes")
