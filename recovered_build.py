import os
import json

# ==========================================
# HELPER: CODE BLOCK
# ==========================================
def create_code_block(title, code):
    return f"""
    <div class="code-block">
      <div class="code-block-header">
        <div class="terminal-header-left">
          <div class="terminal-dots">
            <div class="terminal-dot red"></div>
            <div class="terminal-dot yellow"></div>
            <div class="terminal-dot green"></div>
          </div>
          <div class="terminal-title">{title}</div>
        </div>
        <button class="copy-code-btn" aria-label="Copiar código" title="Copiar código">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
            <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
          </svg>
        </button>
      </div>
      <div class="code-block-content">
        <pre><code contenteditable="true" spellcheck="false">{code}</code></pre>
      </div>
    </div>
    """

# ==========================================
# 1. FRAPPE HR SITE DATA
# ==========================================
FRAPPE_SITE_TITLE = 'Frappe HR'
frappe_sidebar_data = [
  {
    'id': 'intro',
    'title': 'Introducción',
    'children': [
      { 'id': 'introduction', 'title': 'Frappe HR', 'route': 'introduction.html' },
      { 'id': 'videos', 'title': 'Videos', 'route': 'videos.html' }
    ]
  },
  {
    'id': 'mobile',
    'title': 'Frappe HR Móvil',
    'children': [
      { 'id': 'mobile-app-installation', 'title': 'Instalación de App Móvil', 'route': 'mobile-app-installation.html' },
      { 'id': 'push-notification', 'title': 'Notificaciones Push', 'route': 'push-notification.html' }
    ]
  },
  {
    'id': 'org',
    'title': 'Gestión de la Organización',
    'children': [
      { 'id': 'employee', 'title': 'Empleado', 'route': 'employee.html' }
    ]
  }
]
frappe_pages = [child for group in frappe_sidebar_data for child in group['children']]
frappe_contents = {
  'introduction.html': {
    'title': 'Frappe HR',
    'content': f"""
      <p>Frappe HR es un software de nómina y recursos humanos de código abierto, moderno y fácil de usar para todas las organizaciones.</p>
      <div class="callout">
        <div class="callout-icon">💡</div>
        <div class="callout-content"><p><strong>Nota importante:</strong> Frappe HR es altamente personalizable.</p></div>
      </div>
      <img src="https://docs.frappe.io/files/imagee5004c.png" alt="Employee Profile Screenshot" />
      <h2 id="why-frappe-hr">Por qué Frappe HR</h2>
      <p>Las empresas suelen tener problemas con procesos de RR.HH. dispersos...</p>
      <details>
        <summary>Ver un ejemplo de configuración avanzada (Código)</summary>
        <div class="details-content">
          <p>Puedes configurar Frappe HR usando su API en Python.</p>
          {create_code_block("api_example.py", '''import frappe

def create_employee(name, department):
    emp = frappe.get_doc({
        "doctype": "Employee",
        "employee_name": name,
        "department": department,
        "status": "Active"
    })
    emp.insert()
    return emp.name''')}
        </div>
      </details>
    """
  },
  'videos.html': {
    'title': 'Videos',
    'content': """
      <h2 id="talks">Charlas y Seminarios Web</h2>
      <p>El módulo de Recursos Humanos cubre los procesos relacionados con el departamento de RR.HH.</p>
    """
  },
  'mobile-app-installation.html': { 'title': 'Instalación de App Móvil', 'content': '<p>Guía de instalación de la app móvil de Frappe HR.</p>' },
  'push-notification.html': { 'title': 'Notificaciones Push', 'content': '<p>Configuración de notificaciones push.</p>' },
  'employee.html': { 'title': 'Empleado', 'content': '<p>Gestión de empleados en Frappe HR.</p>' }
}

# ==========================================
# 2. PYTHON SITE DATA
# ==========================================
PYTHON_SITE_TITLE = 'Python Docs'
python_sidebar_data = [
  {
    'id': 'py-intro', 'title': 'Primeros Pasos',
    'children': [ { 'id': 'py-installation', 'title': 'Instalación y Entorno', 'route': 'installation.html' } ]
  },
  {
    'id': 'py-fundamentals', 'title': 'Fundamentos',
    'children': [ { 'id': 'py-syntax', 'title': 'Sintaxis Fundamental', 'route': 'syntax.html' } ]
  },
  {
    'id': 'py-paradigms', 'title': 'Paradigmas',
    'children': [
      { 'id': 'py-functional', 'title': 'Programación Funcional', 'route': 'functional.html' },
      { 'id': 'py-oop', 'title': 'Programación Orientada a Objetos', 'route': 'oop.html' }
    ]
  }
]
python_pages = [child for group in python_sidebar_data for child in group['children']]
python_contents = {
  'installation.html': {
    'title': '1. Instalación y Entorno',
    'content': f"""
      <h2 id="instalacion">Instalación</h2>
      <p>Descarga la versión oficial en <a href="https://python.org">python.org</a>.</p>
      <h2 id="verificacion">Verificación</h2>
      {create_code_block("terminal", "python --version")}
      <h2 id="entornos-virtuales">Entornos Virtuales</h2>
      {create_code_block("terminal", "python -m venv venv")}
    """
  },
  'syntax.html': {
    'title': '2. Sintaxis Fundamental',
    'content': f"""
      <h2 id="variables">Variables y Tipos de Datos</h2>
      <p>Variables: <code>x = 10</code></p>
      <h2 id="estructuras">Estructuras de Control</h2>
      {create_code_block("estructuras.py", '''if x > 5:
    print("Mayor")
elif x == 5:
    print("Igual")
else:
    print("Menor")''')}
    """
  },
  'functional.html': {
    'title': '3. Programación Funcional',
    'content': f"""
      <h2 id="lambdas">Lambdas</h2>
      {create_code_block("lambdas.py", "suma = lambda a, b: a + b")}
      <h2 id="map-filter-reduce">Map/Filter/Reduce</h2>
      {create_code_block("map_filter.py", '''numeros = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x**2, numeros))
pares = list(filter(lambda x: x % 2 == 0, numeros))''')}
    """
  },
  'oop.html': {
    'title': '4. Programación Orientada a Objetos (POO)',
    'content': f"""
      <h2 id="definicion">Definición</h2>
      {create_code_block("vehiculo.py", '''class Vehiculo:
    def __init__(self, marca):
        self.marca = marca  # Atributo

    def arrancar(self):  # Método
        return f"{self.marca} arrancando"''')}
    """
  }
}

# ==========================================
# 3. GIT SITE DATA
# ==========================================
GIT_SITE_TITLE = 'Git Docs'
git_sidebar_data = [
  {
    'id': 'git-intro', 'title': 'Conceptos Básicos',
    'children': [
      { 'id': 'git-introduction', 'title': 'Introducción a Git', 'route': 'introduction.html' },
      { 'id': 'git-commands', 'title': 'Comandos Fundamentales', 'route': 'commands.html' }
    ]
  },
  {
    'id': 'git-workflows', 'title': 'Flujos de Trabajo',
    'children': [ { 'id': 'git-branches', 'title': 'Ramas y Merges', 'route': 'branches.html' } ]
  }
]
git_pages = [child for group in git_sidebar_data for child in group['children']]
git_contents = {
  'introduction.html': {
    'title': 'Introducción a Git',
    'content': f"""
      <p>Git es un sistema de control de versiones distribuido gratuito y de código abierto diseñado para manejar todo, desde proyectos pequeños hasta muy grandes, con rapidez y eficiencia.</p>
      <div class="callout">
        <div class="callout-icon">📌</div>
        <div class="callout-content"><p><strong>Nota:</strong> Git no es lo mismo que GitHub. Git es la herramienta local, GitHub es la plataforma en línea.</p></div>
      </div>
      <h2 id="config-basica">Configuración Básica</h2>
      {create_code_block("terminal", "git config --global user.name 'Tu Nombre'\\ngit config --global user.email 'tu@email.com'")}
    """
  },
  'commands.html': {
    'title': 'Comandos Fundamentales',
    'content': f"""
      <h2 id="init">Inicializar un repositorio</h2>
      {create_code_block("terminal", "git init")}
      <h2 id="add-commit">Añadir y confirmar cambios</h2>
      {create_code_block("terminal", "git add .\\ngit commit -m 'Mi primer commit'")}
      <h2 id="push">Subir cambios remotos</h2>
      {create_code_block("terminal", "git push origin main")}
    """
  },
  'branches.html': {
    'title': 'Ramas y Merges',
    'content': f"""
      <h2 id="branches">Crear y cambiar de rama</h2>
      {create_code_block("terminal", "git checkout -b nueva-rama")}
      <h2 id="merge">Fusionar ramas (Merge)</h2>
      {create_code_block("terminal", "git checkout main\\ngit merge nueva-rama")}
    """
  }
}

# ==========================================
# 4. LINUX SITE DATA
# ==========================================
LINUX_SITE_TITLE = 'Linux Docs'
linux_sidebar_data = [
  {
    'id': 'linux-intro', 'title': 'Fundamentos',
    'children': [
      { 'id': 'linux-introduction', 'title': 'Introducción a Linux', 'route': 'introduction.html' },
      { 'id': 'linux-nav', 'title': 'Navegación de Archivos', 'route': 'navigation.html' }
    ]
  },
  {
    'id': 'linux-admin', 'title': 'Administración',
    'children': [ { 'id': 'linux-permissions', 'title': 'Permisos y Usuarios', 'route': 'permissions.html' } ]
  }
]
linux_pages = [child for group in linux_sidebar_data for child in group['children']]
linux_contents = {
  'introduction.html': {
    'title': 'Introducción a Linux',
    'content': f"""
      <p>Linux es una familia de sistemas operativos de código abierto tipo Unix basados en el kernel de Linux. Es ampliamente utilizado en servidores, supercomputadoras y dispositivos integrados.</p>
      <h2 id="distros">Distribuciones (Distros) Populares</h2>
      <ul>
        <li>Ubuntu: Ideal para principiantes.</li>
        <li>Debian: Muy estable, utilizado en servidores.</li>
        <li>Arch Linux: Para usuarios avanzados.</li>
      </ul>
    """
  },
  'navigation.html': {
    'title': 'Navegación de Archivos',
    'content': f"""
      <h2 id="pwd-ls">¿Dónde estoy y qué hay aquí?</h2>
      {create_code_block("terminal", "pwd\\nls -la")}
      <h2 id="cd">Moverse entre directorios</h2>
      {create_code_block("terminal", "cd /var/www/html\\ncd ..")}
    """
  },
  'permissions.html': {
    'title': 'Permisos y Usuarios',
    'content': f"""
      <h2 id="chmod">Cambiar permisos</h2>
      {create_code_block("terminal", "chmod 755 archivo.sh\\nchmod +x script.py")}
      <h2 id="chown">Cambiar propietario</h2>
      {create_code_block("terminal", "sudo chown root:root archivo.txt")}
    """
  }
}

# ==========================================
# 5. SALES IT SITE DATA
# ==========================================
SALES_SITE_TITLE = 'Ventas IT'
sales_sidebar_data = [
  {
    'id': 'sales-intro', 'title': 'Fundamentos de Ventas',
    'children': [
      { 'id': 'sales-introduction', 'title': 'El Rol del Representante IT', 'route': 'introduction.html' },
      { 'id': 'sales-cycle', 'title': 'Ciclo de Venta de Software', 'route': 'cycle.html' }
    ]
  },
  {
    'id': 'sales-crm', 'title': 'Gestión de Clientes',
    'children': [ { 'id': 'sales-crm-management', 'title': 'Uso de CRM y Relaciones', 'route': 'crm.html' } ]
  }
]
sales_pages = [child for group in sales_sidebar_data for child in group['children']]
sales_contents = {
  'introduction.html': {
    'title': 'El Rol del Representante IT',
    'content': f"""
      <p>El Representante de Ventas IT es un híbrido entre un vendedor tradicional y un consultor tecnológico. Su objetivo es entender los problemas de negocio del cliente y ofrecer soluciones de software que aporten valor.</p>
      <h2 id="habilidades">Habilidades Clave</h2>
      <ul>
        <li>Conocimiento técnico de los productos (SaaS, On-Premise, Cloud).</li>
        <li>Habilidades de comunicación y negociación B2B.</li>
        <li>Resolución de problemas de negocio.</li>
      </ul>
    """
  },
  'cycle.html': {
    'title': 'Ciclo de Venta de Software',
    'content': f"""
      <h2 id="fases">Las 5 Fases Principales</h2>
      <ol>
        <li><strong>Prospección:</strong> Identificar posibles clientes y contactarlos (Cold Outreach).</li>
        <li><strong>Cualificación (Discovery):</strong> Evaluar si el cliente tiene presupuesto, autoridad, necesidad y un tiempo definido (Metodología BANT).</li>
        <li><strong>Demostración:</strong> Mostrar el producto adaptado a las necesidades del cliente (Demo Custom).</li>
        <li><strong>Propuesta y Negociación:</strong> Discutir licencias, implementación y seguridad (SLA, NDA).</li>
        <li><strong>Cierre (Won):</strong> Firma del contrato y transición al equipo de Customer Success.</li>
      </ol>
    """
  },
  'crm.html': {
    'title': 'Uso de CRM y Relaciones',
    'content': f"""
      <h2 id="crm-importance">La importancia del CRM</h2>
      <p>Herramientas como Salesforce, HubSpot o Pipedrive son esenciales para el seguimiento de cuentas. En ventas IT (B2B), el ciclo de venta puede durar desde 3 meses hasta 2 años.</p>
      <div class="callout">
        <div class="callout-icon">💡</div>
        <div class="callout-content"><p><strong>Consejo de Oro:</strong> Documenta cada interacción, email y llamada en el CRM. El seguimiento constante es lo que cierra tratos, no una presentación mágica.</p></div>
      </div>
    """
  }
}

# ==========================================
# MASTER HTML GENERATOR FUNCTION
# ==========================================

def get_dropdown_html(base_path):
    return f"""
        <button class="tech-dropdown-btn">
            <span class="header-space-name">Cambiar Tecnología</span>
            <svg class="header-chevron" viewBox="0 0 20 20" fill="currentColor" width="16" height="16"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
        </button>
        <div class="tech-dropdown-menu">
            <a href="{base_path}introduction.html" class="tech-dropdown-item">Frappe HR</a>
            <a href="{base_path}python/installation.html" class="tech-dropdown-item">Python Docs</a>
            <a href="{base_path}git/introduction.html" class="tech-dropdown-item">Git Docs</a>
            <a href="{base_path}linux/introduction.html" class="tech-dropdown-item">Linux Docs</a>
            <a href="{base_path}sales/introduction.html" class="tech-dropdown-item">Ventas IT</a>
            <hr style="margin: 4px 0; border-color: var(--outline-gray-1);">
            <a href="{base_path}all.html" class="tech-dropdown-item" style="color: var(--color-green-600); font-weight: 600;">Todo en Uno</a>
        </div>
    """

def build_sidebar_html(sidebar_data, current_route):
    html = ''
    for group in sidebar_data:
        html += f"""
          <div class="sidebar-group">
            <button class="sidebar-group-btn" data-group-id="{group['id']}" aria-expanded="true">
              <svg class="sidebar-arrow expanded" viewBox="0 0 12 12" fill="currentColor"><path d="M4 8.54V3.46c0-.4.455-.64.787-.41l3.628 2.54a.5.5 0 010 .82L4.787 8.95A.5.5 0 014 8.54z"/></svg>
              <span class="sidebar-group-title">{group['title']}</span>
            </button>
            <div class="sidebar-children" id="{group['id']}-children" style="display: block;">
              <div class="sidebar-list">
        """
        for child in group['children']:
            is_active = 'active' if child['route'] == current_route else ''
            aria_current = 'aria-current="page"' if child['route'] == current_route else ''
            child_route_no_ext = child['route'].replace('.html', '')
            html += f"""
            <div class="sidebar-item">
              <a href="{child['route']}" class="sidebar-link {is_active}" data-route="{child_route_no_ext}" {aria_current}>
                <span class="sidebar-link-title">{child['title']}</span>
              </a>
            </div>
            """
        html += "</div></div></div>"
    return html

def generate_html_page(page_def, index, all_pages, all_contents, sidebar_data, site_title, base_path, out_dir):
  route = page_def['route']
  title = page_def['title']
  
  content_html = all_contents.get(route, {}).get('content', f'<p>Contenido placeholder para {title}</p>')

  prev_page = all_pages[index - 1] if index > 0 else None
  next_page = all_pages[index + 1] if index < len(all_pages) - 1 else None
  
  prev_nav_html = f"""<a href="{prev_page['route']}" class="page-nav-link prev"><svg class="page-nav-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg><div class="page-nav-text"><span class="page-nav-label">Anterior</span><span class="page-nav-title">{prev_page['title']}</span></div></a>""" if prev_page else ""
  next_nav_html = f"""<a href="{next_page['route']}" class="page-nav-link next"><div class="page-nav-text"><span class="page-nav-label">Siguiente</span><span class="page-nav-title">{next_page['title']}</span></div><svg class="page-nav-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg></a>""" if next_page else ""

  sidebar_html = build_sidebar_html(sidebar_data, route)
  dropdown_html = get_dropdown_html(base_path)
  search_data = [{'title': p['title'], 'route': p['route']} for p in all_pages]

  html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - {site_title}</title>
    <link rel="stylesheet" href="{base_path}css/variables.css">
    <link rel="stylesheet" href="{base_path}css/reset.css">
    <link rel="stylesheet" href="{base_path}css/typography.css">
    <link rel="stylesheet" href="{base_path}css/layout.css">
    <link rel="stylesheet" href="{base_path}css/sidebar.css">
    <link rel="stylesheet" href="{base_path}css/content.css">
    <link rel="stylesheet" href="{base_path}css/toc.css">
    <link rel="stylesheet" href="{base_path}css/navigation.css">
    <link rel="stylesheet" href="{base_path}css/components.css">
    <link rel="stylesheet" href="{base_path}css/responsive.css">
    <style>
      .tech-dropdown {{ position: relative; }}
      .tech-dropdown-btn {{ display: flex; align-items: center; gap: 8px; background: transparent; border: none; cursor: pointer; padding: 4px; border-radius: var(--radius); transition: background-color var(--transition-fast); }}
      .tech-dropdown-btn:hover {{ background-color: var(--surface-gray-2); }}
      .tech-dropdown-menu {{ position: absolute; top: 100%; left: 0; margin-top: 8px; background-color: var(--surface-white); border: 1px solid var(--outline-gray-1); border-radius: var(--radius); box-shadow: var(--shadow-lg); min-width: 200px; display: none; flex-direction: column; padding: 4px; z-index: 100; }}
      .tech-dropdown-menu.is-open {{ display: flex; }}
      .tech-dropdown-item {{ padding: 8px 12px; color: var(--ink-gray-9); text-decoration: none; font-size: var(--text-sm); border-radius: var(--radius-sm); }}
      .tech-dropdown-item:hover {{ background-color: var(--surface-gray-2); }}
      .search-results-list {{ max-height: 400px; overflow-y: auto; padding: 8px 0; }}
      .search-result-item {{ display: block; padding: 12px 16px; color: var(--ink-gray-9); text-decoration: none; border-bottom: 1px solid var(--outline-gray-1); }}
      .search-result-item:hover {{ background-color: var(--surface-gray-1); }}
    </style>
</head>
<body>
    <div class="site-container">
        <!-- Header -->
        <header class="site-header">
            <div class="header-left tech-dropdown">
                {dropdown_html}
            </div>
            <nav class="header-nav"></nav>
            <div class="header-actions">
                <button class="search-btn" id="search-btn">
                    <svg class="search-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                    <span class="search-kbd" id="search-shortcut">Ctrl+K</span>
                </button>
                <div class="header-divider"></div>
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
        
        <!-- Mobile Header -->
        <header class="mobile-header">
            <div class="header-left tech-dropdown">
                <button class="mobile-menu-btn" id="mobile-menu-btn">
                    <svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
                </button>
                {dropdown_html}
            </div>
            <button class="search-btn" id="mobile-search-btn">
                <svg class="search-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
            </button>
        </header>

        <!-- Main Body -->
        <div class="site-body">
            <!-- Left Sidebar -->
            <aside class="wiki-sidebar" id="mobile-sidebar">
                <nav class="sidebar-nav">
                    {sidebar_html}
                </nav>
            </aside>
            <div class="mobile-sidebar-overlay" id="mobile-overlay"></div>

            <!-- Main Content -->
            <main class="wiki-main">
                <article class="wiki-article">
                    <div class="page-header">
                        <h1 class="page-title" id="page-title">{title}</h1>
                    </div>
                    <div class="wiki-content prose prose-sm max-w-none scroll-smooth" id="wiki-content">
                        {content_html}
                    </div>
                    <nav class="page-nav"><div class="page-nav-links">{prev_nav_html}{next_nav_html}</div></nav>
                </article>
            </main>

            <!-- Right Sidebar TOC -->
            <aside class="wiki-toc">
                <nav class="toc-sidebar">
                    <h3 class="toc-title">En esta página</h3>
                    <ul class="toc-list" id="wiki-toc-list"></ul>
                </nav>
            </aside>
        </div>
    </div>

    <!-- Search Modal -->
    <div class="search-modal-overlay" id="search-overlay">
        <div class="search-modal" id="search-modal">
            <div class="search-header">
                <svg class="search-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                <input type="text" class="search-input" id="search-input" placeholder="Buscar documentación...">
                <button class="search-close" id="search-close"><svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg></button>
            </div>
            <div class="search-results-list" id="search-results"></div>
            <div class="search-results-empty" id="search-empty">Escribe para buscar...</div>
        </div>
    </div>
    <script>window.SEARCH_DATA = {json.dumps(search_data)};</script>
    <script src="{base_path}js/app.js"></script>
</body>
</html>"""
  filepath = os.path.join(out_dir, route)
  with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
  print(f'Generated {filepath}')

# ==========================================
# ALL-IN-ONE PAGE GENERATOR
# ==========================================
def generate_all_in_one():
    base_path = ""
    dropdown_html = get_dropdown_html(base_path)
    
    # Recopilar todos los contenidos en orden
    all_content = []
    
    # Helper to append sections
    def append_domain(domain_title, pages, contents):
        all_content.append(f'<h1 id="domain-{domain_title.lower().replace(" ", "-")}" style="font-size: 3rem; border-bottom: 2px solid var(--color-green-600); padding-bottom: 1rem; margin-top: 4rem;">{domain_title}</h1>')
        for page in pages:
            route = page['route']
            title = page['title']
            content = contents.get(route, {}).get('content', '')
            # En la página all-in-one, los h2 se vuelven importantes para la TOC. Añadiremos un subtítulo h2 por página si no lo tiene, o h2 para la pág.
            all_content.append(f'<h2 id="page-{route.replace(".html", "")}" style="color: var(--color-green-600); margin-top: 3rem;">{title}</h2>')
            all_content.append(content)
            all_content.append("<hr style='margin: 40px 0;'>")

    append_domain("Frappe HR", frappe_pages, frappe_contents)
    append_domain("Python Docs", python_pages, python_contents)
    append_domain("Git Docs", git_pages, git_contents)
    append_domain("Linux Docs", linux_pages, linux_contents)
    append_domain("Ventas IT", sales_pages, sales_contents)
    
    full_content_html = "\\n".join(all_content)

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Todo en Uno - Documentación Completa</title>
    <link rel="stylesheet" href="{base_path}css/variables.css">
    <link rel="stylesheet" href="{base_path}css/reset.css">
    <link rel="stylesheet" href="{base_path}css/typography.css">
    <link rel="stylesheet" href="{base_path}css/layout.css">
    <link rel="stylesheet" href="{base_path}css/sidebar.css">
    <link rel="stylesheet" href="{base_path}css/content.css">
    <link rel="stylesheet" href="{base_path}css/toc.css">
    <link rel="stylesheet" href="{base_path}css/navigation.css">
    <link rel="stylesheet" href="{base_path}css/components.css">
    <link rel="stylesheet" href="{base_path}css/responsive.css">
    <style>
      .tech-dropdown {{ position: relative; }}
      .tech-dropdown-btn {{ display: flex; align-items: center; gap: 8px; background: transparent; border: none; cursor: pointer; padding: 4px; border-radius: var(--radius); transition: background-color var(--transition-fast); }}
      .tech-dropdown-btn:hover {{ background-color: var(--surface-gray-2); }}
      .tech-dropdown-menu {{ position: absolute; top: 100%; left: 0; margin-top: 8px; background-color: var(--surface-white); border: 1px solid var(--outline-gray-1); border-radius: var(--radius); box-shadow: var(--shadow-lg); min-width: 200px; display: none; flex-direction: column; padding: 4px; z-index: 100; }}
      .tech-dropdown-menu.is-open {{ display: flex; }}
      .tech-dropdown-item {{ padding: 8px 12px; color: var(--ink-gray-9); text-decoration: none; font-size: var(--text-sm); border-radius: var(--radius-sm); }}
      .tech-dropdown-item:hover {{ background-color: var(--surface-gray-2); }}
      /* Ocultar barra lateral izquierda en Todo-en-Uno para dar más espacio */
      .wiki-sidebar {{ display: none; }}
      @media (min-width: 1024px) {{ .wiki-main {{ padding-left: 0; }} }}
    </style>
</head>
<body>
    <div class="site-container">
        <header class="site-header">
            <div class="header-left tech-dropdown">
                {dropdown_html}
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
                {dropdown_html}
            </div>
        </header>

        <div class="site-body">
            <main class="wiki-main">
                <article class="wiki-article">
                    <div class="page-header">
                        <h1 class="page-title" id="page-title">Documentación Completa (Todo en Uno)</h1>
                        <p style="color: var(--ink-gray-5); margin-top: 10px;">Esta página contiene la documentación completa de todas las tecnologías para fácil lectura o búsqueda (Ctrl+F).</p>
                    </div>
                    <div class="wiki-content prose prose-sm max-w-none scroll-smooth" id="wiki-content">
                        {full_content_html}
                    </div>
                </article>
            </main>
            <aside class="wiki-toc">
                <nav class="toc-sidebar">
                    <h3 class="toc-title">En esta página</h3>
                    <ul class="toc-list" id="wiki-toc-list"></ul>
                </nav>
            </aside>
        </div>
    </div>
    <script>window.SEARCH_DATA = [];</script>
    <script src="{base_path}js/app.js"></script>
</body>
</html>"""
    with open('all.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Generated ./all.html")

# ==========================================
# 4. BUILD PROCESS
# ==========================================

def build_site(pages, contents, sidebar, title, base_path, out_dir):
    print(f"Building {title} Site...")
    if not os.path.exists(out_dir) and out_dir != ".":
        os.makedirs(out_dir)
    for idx, page in enumerate(pages):
        generate_html_page(page, idx, pages, contents, sidebar, title, base_path, out_dir)

build_site(frappe_pages, frappe_contents, frappe_sidebar_data, FRAPPE_SITE_TITLE, "", ".")
build_site(python_pages, python_contents, python_sidebar_data, PYTHON_SITE_TITLE, "../", "python")
build_site(git_pages, git_contents, git_sidebar_data, GIT_SITE_TITLE, "../", "git")
build_site(linux_pages, linux_contents, linux_sidebar_data, LINUX_SITE_TITLE, "../", "linux")
build_site(sales_pages, sales_contents, sales_sidebar_data, SALES_SITE_TITLE, "../", "sales")

print("Building All-in-One Page...")
generate_all_in_one()

print('Build Complete!')
