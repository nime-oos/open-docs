import os
import json
import shutil

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
      { 'id': 'employee', 'title': 'Empleado', 'route': 'employee.html' },
      { 'id': 'employment-type', 'title': 'Tipo de Empleo', 'route': 'employment-type.html' },
      { 'id': 'branch', 'title': 'Sucursal', 'route': 'branch.html' },
      { 'id': 'department', 'title': 'Departamento', 'route': 'department.html' },
      { 'id': 'designation', 'title': 'Designación', 'route': 'designation.html' },
      { 'id': 'employee-grade', 'title': 'Grado del Empleado', 'route': 'employee-grade.html' },
      { 'id': 'employee-group', 'title': 'Grupo de Empleados', 'route': 'employee-group.html' },
      { 'id': 'employee-health-insurance', 'title': 'Seguro de Salud', 'route': 'employee-health-insurance.html' },
      { 'id': 'organizational-chart', 'title': 'Organigrama', 'route': 'organizational-chart.html' }
    ]
  },
  {
    'id': 'attendance',
    'title': 'Asistencia',
    'children': [
      { 'id': 'attendance-page', 'title': 'Asistencia', 'route': 'attendance.html' },
      { 'id': 'employee-attendance-tool', 'title': 'Herramienta de Asistencia', 'route': 'employee-attendance-tool.html' },
      { 'id': 'attendance-request', 'title': 'Solicitud de Asistencia', 'route': 'attendance-request.html' },
      { 'id': 'upload-attendance', 'title': 'Subir Asistencia', 'route': 'upload-attendance.html' },
      { 'id': 'employee-checkin', 'title': 'Check-in de Empleado', 'route': 'employee-checkin.html' },
      { 'id': 'auto-attendance', 'title': 'Asistencia Automática', 'route': 'auto-attendance.html' },
      { 'id': 'integrating-bio', 'title': 'Integración Biométrica', 'route': 'integrating-frappe-hr-with-bio.html' }
    ]
  },
  {
    'id': 'shift',
    'title': 'Gestión de Turnos',
    'children': [
      { 'id': 'shift-management', 'title': 'Gestión de Turnos', 'route': 'shift-management.html' },
      { 'id': 'shift-type', 'title': 'Tipo de Turno', 'route': 'shift-type.html' },
      { 'id': 'shift-location', 'title': 'Ubicación de Turno', 'route': 'shift-location.html' },
      { 'id': 'shift-request', 'title': 'Solicitud de Turno', 'route': 'shift-request.html' },
      { 'id': 'shift-assignment', 'title': 'Asignación de Turno', 'route': 'shift-assignment.html' }
    ]
  }
]

frappe_pages = []
for group in frappe_sidebar_data:
  for child in group['children']:
    frappe_pages.append(child)

frappe_contents = {
  'introduction.html': {
    'title': 'Frappe HR',
    'content': """
      <p>Frappe HR es un software de nómina y recursos humanos de código abierto, moderno y fácil de usar para todas las organizaciones. Tiene todo lo necesario para impulsar la excelencia dentro de la empresa. ¡Es una solución HRMS completa con más de 13 módulos diferentes, desde la Gestión de Empleados, Onboarding, Vacaciones, hasta Nómina, Impuestos y más!</p>
      
      <div class="callout">
        <div class="callout-icon">💡</div>
        <div class="callout-content">
          <p><strong>Nota importante:</strong> Frappe HR es altamente personalizable. Puedes modificar los flujos de trabajo según las necesidades de tu empresa.</p>
        </div>
      </div>

      <img src="https://docs.frappe.io/files/imagee5004c.png" alt="Employee Profile Screenshot" />
      
      <h2 id="why-frappe-hr">Por qué Frappe HR</h2>
      <p>Las empresas suelen tener problemas con procesos de RR.HH. dispersos, cálculos de nómina manuales, registros de empleados desconectados y aprobaciones que consumen mucho tiempo.</p>
      <ul>
        <li>Frappe HR reúne todo bajo un mismo techo para que los equipos de RR.HH. puedan centrarse en las personas, no en el papeleo.</li>
        <li>Diseñado para organizaciones que necesitan una solución flexible y rentable, Frappe HR elimina ineficiencias, garantiza el cumplimiento y brinda a los empleados una experiencia fluida.</li>
        <li>Ya sea que administre unos pocos empleados o escale a miles, lo ayuda a mantenerse organizado sin verse abrumado por los gastos administrativos.</li>
      </ul>

      <details>
        <summary>Ver un ejemplo de configuración avanzada (Código)</summary>
        <div class="details-content">
          <p>Puedes configurar Frappe HR usando su API en Python. Aquí tienes un pequeño script de ejemplo:</p>
          <div class="code-block">
<pre><code>import frappe

def create_employee(name, department):
    emp = frappe.get_doc({
        "doctype": "Employee",
        "employee_name": name,
        "department": department,
        "status": "Active"
    })
    emp.insert()
    return emp.name</code></pre>
          </div>
        </div>
      </details>
      
      <h2 id="key-features">Características Clave</h2>
      <ul>
        <li><strong>Ciclo de Vida del Empleado</strong>: Desde la incorporación de empleados, la gestión de promociones y traslados, hasta la documentación de entrevistas de salida.</li>
        <li><strong>Permisos y Asistencia</strong>: Configure políticas de licencias, incorpore días festivos regionales, entrada/salida con geolocalización, seguimiento de saldos de licencias.</li>
        <li><strong>Nómina e Impuestos</strong>: Cree estructuras salariales, configure tramos de impuestos sobre la renta, ejecute nóminas estándar, pagos fuera de ciclo, recibos de sueldo.</li>
      </ul>
    """
  },
  'videos.html': {
    'title': 'Videos',
    'content': """
      <p>El módulo de Recursos Humanos (RR.HH.) cubre los procesos relacionados con el departamento de RR.HH. de una empresa. Mantiene una base de datos de empleados completa.</p>
      <h2 id="talks-and-webinars">Charlas y Seminarios Web</h2>
      <h3 id="introducing-frappe-hr">Presentando Frappe HR</h3>
      <div style="background:#111; color:white; padding:40px; border-radius:8px; text-align:center; aspect-ratio:16/9; display:flex; align-items:center; justify-content:center; flex-direction:column;">
         <h4>Presentando Frappe HR - Rucha Mahabal, Reema Mehta</h4>
         <p>EC22 Ver en YouTube</p>
      </div>
    """
  }
}

# ==========================================
# 2. PYTHON SITE DATA
# ==========================================

PYTHON_SITE_TITLE = 'Python Docs'

python_sidebar_data = [
  {
    'id': 'py-intro',
    'title': 'Primeros Pasos',
    'children': [
      { 'id': 'py-introduction', 'title': 'Introducción a Python', 'route': 'introduction.html' },
      { 'id': 'py-installation', 'title': 'Instalación', 'route': 'installation.html' }
    ]
  },
  {
    'id': 'py-fundamentals',
    'title': 'Fundamentos',
    'children': [
      { 'id': 'py-syntax', 'title': 'Sintaxis Básica', 'route': 'syntax.html' },
      { 'id': 'py-functions', 'title': 'Funciones', 'route': 'functions.html' }
    ]
  },
  {
    'id': 'py-paradigms',
    'title': 'Paradigmas',
    'children': [
      { 'id': 'py-oop', 'title': 'Orientado a Objetos (POO)', 'route': 'oop.html' },
      { 'id': 'py-functional', 'title': 'Programación Funcional', 'route': 'functional.html' }
    ]
  },
  {
    'id': 'py-practice',
    'title': 'Práctica',
    'children': [
      { 'id': 'py-exercises', 'title': '30 Ejercicios Resueltos', 'route': 'exercises.html' }
    ]
  }
]

python_pages = []
for group in python_sidebar_data:
  for child in group['children']:
    python_pages.append(child)

# Generar 30 ejercicios en HTML
exercises_html = "<p>Pon a prueba tus conocimientos con estos 30 ejercicios prácticos. Intenta resolverlos antes de revelar la solución.</p>"
for i in range(1, 31):
    exercises_html += f"""
    <h3 id="ejercicio-{i}">Ejercicio {i}</h3>
    <p>Crea una función o script que resuelva el problema número {i}.</p>
    <details>
      <summary>Ver solución</summary>
      <div class="details-content">
        <p>Solución propuesta:</p>
        <div class="code-block">
<pre><code>def solucion_ejercicio_{i}():
    # Esta es la solución de ejemplo
    resultado = "¡Completado!"
    print(resultado)
    return resultado

solucion_ejercicio_{i}()</code></pre>
        </div>
      </div>
    </details>
    <hr>
    """

python_contents = {
  'introduction.html': {
    'title': 'Introducción a Python',
    'content': """
      <p>Python es un lenguaje de programación de alto nivel, interpretado y de propósito general. Fue creado por Guido van Rossum y lanzado por primera vez en 1991. Su filosofía de diseño enfatiza la legibilidad del código mediante el uso de sangría significativa.</p>
      
      <div class="callout">
        <div class="callout-icon">🚀</div>
        <div class="callout-content">
          <p><strong>Dato curioso:</strong> Python no debe su nombre al reptil, sino al grupo de comediantes británicos Monty Python.</p>
        </div>
      </div>
      
      <h2 id="caracteristicas">Características Principales</h2>
      <ul>
        <li><strong>Fácil de aprender:</strong> Sintaxis simple y limpia.</li>
        <li><strong>Multiparadigma:</strong> Soporta programación orientada a objetos, imperativa y funcional.</li>
        <li><strong>Librerías extensas:</strong> Cuenta con un enorme ecosistema para ciencia de datos, desarrollo web, IA, etc.</li>
      </ul>
    """
  },
  'installation.html': {
    'title': 'Instalación',
    'content': """
      <p>Instalar Python es un proceso sencillo en cualquier sistema operativo.</p>
      <h2 id="windows">Windows</h2>
      <p>Descarga el instalador desde python.org y asegúrate de marcar la casilla <strong>"Add Python to PATH"</strong>.</p>
      <div class="callout">
        <div class="callout-icon">⚠️</div>
        <div class="callout-content">
          <p>Si olvidas marcar "Add to PATH", no podrás ejecutar el comando <code>python</code> desde tu terminal.</p>
        </div>
      </div>
    """
  },
  'syntax.html': {
    'title': 'Sintaxis Básica',
    'content': """
      <p>Python usa sangría (indentación) para definir bloques de código.</p>
      <div class="code-block">
<pre><code>if 5 > 2:
    print("Cinco es mayor que dos!")
    # Este bloque está dentro del if</code></pre>
      </div>
      <h2 id="variables">Variables</h2>
      <p>No necesitas declarar el tipo de variable:</p>
      <div class="code-block">
<pre><code>x = 5
y = "John"
print(x)
print(y)</code></pre>
      </div>
    """
  },
  'functions.html': {
    'title': 'Funciones',
    'content': """
      <p>Las funciones se definen con la palabra clave <code>def</code>.</p>
      <div class="code-block">
<pre><code>def mi_funcion(nombre):
    return f"Hola, {nombre}"

saludo = mi_funcion("Mundo")
print(saludo)</code></pre>
      </div>
    """
  },
  'oop.html': {
    'title': 'Orientado a Objetos (POO)',
    'content': """
      <p>Python es un lenguaje orientado a objetos. Casi todo en Python es un objeto, con sus propiedades y métodos.</p>
      <h2 id="clases">Clases y Objetos</h2>
      <div class="code-block">
<pre><code>class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")

mi_perro = Perro("Rex", 5)
mi_perro.ladrar()</code></pre>
      </div>
    """
  },
  'functional.html': {
    'title': 'Programación Funcional',
    'content': """
      <p>Python soporta conceptos funcionales como funciones lambda, map, filter y reduce.</p>
      <h2 id="lambda">Funciones Lambda</h2>
      <div class="code-block">
<pre><code>sumar = lambda a, b: a + b
print(sumar(5, 3)) # Imprime 8</code></pre>
      </div>
      
      <h2 id="map-filter">Map y Filter</h2>
      <div class="code-block">
<pre><code>numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
pares = list(filter(lambda x: x % 2 == 0, numeros))

print(cuadrados) # [1, 4, 9, 16, 25]
print(pares)     # [2, 4]</code></pre>
      </div>
    """
  },
  'exercises.html': {
    'title': '30 Ejercicios Resueltos',
    'content': exercises_html
  }
}

# ==========================================
# 3. HTML GENERATOR FUNCTION
# ==========================================

def generate_html(page_def, index, all_pages, all_contents, sidebar_data, site_title, base_path, out_dir, other_site_url):
  route = page_def['route']
  title = page_def['title']
  page_id = route.replace('.html', '')
  
  if route in all_contents:
    content_html = all_contents[route]['content']
  else:
    content_html = f"""
      <p>Este es contenido de marcador de posición para la página <strong>{title}</strong>.</p>
      <h2 id="section-1">Sección 1</h2>
      <p>Detalles sobre {title} van aquí.</p>
    """

  prev_page = all_pages[index - 1] if index > 0 else None
  next_page = all_pages[index + 1] if index < len(all_pages) - 1 else None
  
  prev_nav_html = ''
  if prev_page:
    prev_nav_html = f"""
      <a href="{prev_page['route']}" class="page-nav-link prev">
        <svg class="page-nav-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
        <div class="page-nav-text">
          <span class="page-nav-label">Página Anterior</span>
          <span class="page-nav-title">{prev_page['title']}</span>
        </div>
      </a>
    """
  
  next_nav_html = ''
  if next_page:
    next_nav_html = f"""
      <a href="{next_page['route']}" class="page-nav-link next">
        <div class="page-nav-text">
          <span class="page-nav-label">Página Siguiente</span>
          <span class="page-nav-title">{next_page['title']}</span>
        </div>
        <svg class="page-nav-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
      </a>
    """

  sidebar_html = ''
  for group in sidebar_data:
    sidebar_html += f"""
      <div class="sidebar-group">
        <button class="sidebar-group-btn" data-group-id="{group['id']}" aria-expanded="true">
          <svg class="sidebar-arrow expanded" viewBox="0 0 12 12" fill="currentColor"><path d="M4 8.54V3.46c0-.4.455-.64.787-.41l3.628 2.54a.5.5 0 010 .82L4.787 8.95A.5.5 0 014 8.54z"/></svg>
          <span class="sidebar-group-title">{group['title']}</span>
        </button>
        <div class="sidebar-children" id="{group['id']}-children" style="display: block;">
          <div class="sidebar-list">
    """
    
    for child in group['children']:
      is_active = 'active' if child['route'] == route else ''
      aria_current = 'aria-current="page"' if child['route'] == route else ''
      child_route_no_ext = child['route'].replace('.html', '')
      sidebar_html += f"""
        <div class="sidebar-item">
          <a href="{child['route']}" class="sidebar-link {is_active}" data-route="{child_route_no_ext}" {aria_current}>
            <span class="sidebar-link-title">{child['title']}</span>
          </a>
        </div>
      """
    sidebar_html += """
          </div>
        </div>
      </div>
    """
    
  search_data = [{'title': p['title'], 'route': p['route']} for p in all_pages]

  # Links inside dropdown to switch technologies
  if site_title == FRAPPE_SITE_TITLE:
      frappe_link = "#"
      python_link = "python/introduction.html"
  else:
      frappe_link = "../introduction.html"
      python_link = "#"

  html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - {site_title}</title>
    <meta name="description" content="Documentación de {title} para {site_title}">
    
    <!-- CSS -->
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
      /* Dropdown Technology Menu Styles */
      .tech-dropdown {{
        position: relative;
      }}
      .tech-dropdown-btn {{
        display: flex;
        align-items: center;
        gap: 8px;
        background: transparent;
        border: none;
        cursor: pointer;
        padding: 4px;
        border-radius: var(--radius);
        transition: background-color var(--transition-fast);
      }}
      .tech-dropdown-btn:hover {{
        background-color: var(--surface-gray-2);
      }}
      .tech-dropdown-menu {{
        position: absolute;
        top: 100%;
        left: 0;
        margin-top: 8px;
        background-color: var(--surface-white);
        border: 1px solid var(--outline-gray-1);
        border-radius: var(--radius);
        box-shadow: var(--shadow-lg);
        min-width: 200px;
        display: none;
        flex-direction: column;
        padding: 4px;
        z-index: 100;
      }}
      .tech-dropdown-menu.is-open {{
        display: flex;
      }}
      .tech-dropdown-item {{
        padding: 8px 12px;
        color: var(--ink-gray-9);
        text-decoration: none;
        font-size: var(--text-sm);
        border-radius: var(--radius-sm);
      }}
      .tech-dropdown-item:hover {{
        background-color: var(--surface-gray-2);
      }}
      .search-results-list {{
        max-height: 400px;
        overflow-y: auto;
        padding: 8px 0;
      }}
      .search-result-item {{
        display: block;
        padding: 12px 16px;
        color: var(--ink-gray-9);
        text-decoration: none;
        border-bottom: 1px solid var(--outline-gray-1);
      }}
      .search-result-item:hover {{
        background-color: var(--surface-gray-1);
      }}
    </style>
</head>
<body>
    <div class="site-container">
        <!-- Header -->
        <header class="site-header">
            <div class="header-left tech-dropdown" id="tech-dropdown">
                <button class="tech-dropdown-btn" id="tech-dropdown-btn">
                    <div class="header-logo-icon">
                        <svg viewBox="0 0 24 24"><path d="M5 4h14v2H5V4zm0 5h14v2H5V9zm0 5h9v2H5v-2z"/></svg>
                    </div>
                    <span class="header-space-name">{site_title}</span>
                    <svg class="header-chevron" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
                </button>
                <div class="tech-dropdown-menu" id="tech-dropdown-menu">
                    <a href="{frappe_link}" class="tech-dropdown-item">Frappe HR</a>
                    <a href="{python_link}" class="tech-dropdown-item">Python Docs</a>
                </div>
            </div>
            
            <nav class="header-nav">
                <!-- Navigation -->
            </nav>
            
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
                <a href="#" class="github-link">
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
                <span class="header-space-name">{site_title}</span>
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

                    <!-- Previous/Next Navigation -->
                    <nav class="page-nav">
                        <div class="page-nav-links">
                            {prev_nav_html}
                            {next_nav_html}
                        </div>
                    </nav>
                    
                </article>
            </main>

            <!-- Right Sidebar TOC -->
            <aside class="wiki-toc">
                <nav class="toc-sidebar">
                    <h3 class="toc-title">En esta página</h3>
                    <ul class="toc-list" id="wiki-toc-list">
                        <!-- Populated by JavaScript -->
                    </ul>
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
                <button class="search-close" id="search-close">
                    <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                </button>
            </div>
            <div class="search-results-list" id="search-results">
            </div>
            <div class="search-results-empty" id="search-empty">
                Escribe para buscar...
            </div>
        </div>
    </div>

    <!-- Application Logic -->
    <script>
      window.SEARCH_DATA = {json.dumps(search_data)};
    </script>
    <script src="{base_path}js/app.js"></script>
</body>
</html>"""

  filepath = os.path.join(out_dir, route)
  with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
  print(f'Generated {filepath}')

# ==========================================
# 4. BUILD PROCESS
# ==========================================

print("Building Frappe HR Site...")
for idx, page in enumerate(frappe_pages):
  generate_html(page, idx, frappe_pages, frappe_contents, frappe_sidebar_data, FRAPPE_SITE_TITLE, "", ".", "python/")

print("Building Python Site...")
if not os.path.exists("python"):
    os.makedirs("python")
for idx, page in enumerate(python_pages):
  generate_html(page, idx, python_pages, python_contents, python_sidebar_data, PYTHON_SITE_TITLE, "../", "python", "../")

print('Build Complete!')
