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

frappe_contents = {
  'introduction.html': {
    'title': 'Frappe HR',
    'content': f"""
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
          <p>Puedes configurar Frappe HR usando su API en Python. Aquí tienes un pequeño script de ejemplo (puedes editar el código abajo):</p>
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
      { 'id': 'py-installation', 'title': 'Instalación y Entorno', 'route': 'installation.html' }
    ]
  },
  {
    'id': 'py-fundamentals',
    'title': 'Fundamentos',
    'children': [
      { 'id': 'py-syntax', 'title': 'Sintaxis Fundamental', 'route': 'syntax.html' }
    ]
  },
  {
    'id': 'py-paradigms',
    'title': 'Paradigmas',
    'children': [
      { 'id': 'py-functional', 'title': 'Programación Funcional', 'route': 'functional.html' },
      { 'id': 'py-oop', 'title': 'Programación Orientada a Objetos', 'route': 'oop.html' }
    ]
  },
  {
    'id': 'py-practice',
    'title': 'Práctica',
    'children': [
      { 'id': 'py-exercises', 'title': '30 Ejercicios Prácticos', 'route': 'exercises.html' }
    ]
  }
]

python_pages = []
for group in python_sidebar_data:
  for child in group['children']:
    python_pages.append(child)

exercises_list = [
    ("Hola Mundo", 'print("Hola")'),
    ("Suma", 'a+b'),
    ("Par/Impar", 'if n%2==0'),
    ("Factorial", 'math.factorial(n)'),
    ("Fibonacci", 'a, b = b, a+b'),
    ("Invertir String", 's[::-1]'),
    ("Contar Vocales", "sum(1 for c in s if c in 'aeiou')"),
    ("Lista de cuadrados", '[x**2 for x in range(10)]'),
    ("Promedio de lista", 'sum(l)/len(l)'),
    ("Diccionario", 'd = {"clave": "valor"}; print(d["clave"])'),
    ("POO Clase Persona", 'class Persona:\n    def __init__(self, n, e):\n        self.n=n\n        self.e=e'),
    ("Herencia", 'class Empleado(Persona):\n    pass'),
    ("Lambda", 'f = lambda x: x*2'),
    ("Map", 'list(map(lambda x: x**2, lista))'),
    ("Filter", 'list(filter(lambda x: x>10, lista))'),
    ("Manejo de errores", 'try:\n    x = 1/0\nexcept:\n    print("Error")'),
    ("Leer archivo", 'with open("file.txt", "r") as f:\n    contenido = f.read()'),
    ("Escribir archivo", 'with open("file.txt", "w") as f:\n    f.write("Hola")'),
    ("Ordenamiento", 'lista.sort()'),
    ("Palíndromo", 's == s[::-1]'),
    ("Set (unicos)", 'list(set(lista))'),
    ("Tabla multiplicar", 'for i in range(1,11):\n    print(n*i)'),
    ("Primos", 'es_primo = all(n % i != 0 for i in range(2, int(n**0.5)+1))'),
    ("Decorador", 'def decorador(f):\n    def wrapper():\n        return f()\n    return wrapper'),
    ("Generador", 'def gen():\n    yield 1'),
    ("Fecha actual", 'from datetime import datetime\ndatetime.now()'),
    ("Busqueda", 'if item in lista:\n    print("Encontrado")'),
    ("Tuplas", 'a, b = (1, 2)'),
    ("Args/Kwargs", 'def f(*args, **kwargs):\n    pass'),
    ("List Comprehension Complejo", '[x for x in lista if x>0]')
]

exercises_html = "<p>Pon a prueba tus conocimientos con estos 30 ejercicios prácticos. Puedes editar el código directamente en tu navegador. Haz clic para revelar el resumen de la lógica.</p>"
for i, (title, logic) in enumerate(exercises_list, start=1):
    exercises_html += f"""
    <h3 id="ejercicio-{i}">Ejercicio {i}: {title}</h3>
    <details>
      <summary>Ver resumen de la lógica</summary>
      <div class="details-content">
        {create_code_block(f"ejercicio_{i}.py", logic)}
      </div>
    </details>
    <hr>
    """

python_contents = {
  'installation.html': {
    'title': '1. Instalación y Entorno',
    'content': f"""
      <p>Instalar Python y preparar tu entorno correctamente es el primer paso.</p>
      <h2 id="instalacion">Instalación</h2>
      <p>Descarga la versión oficial en <a href="https://python.org">python.org</a>.</p>
      
      <h2 id="verificacion">Verificación</h2>
      <p>Ejecuta el siguiente comando en tu terminal para verificar la instalación:</p>
      {create_code_block("terminal", "python --version")}

      <h2 id="entornos-virtuales">Entornos Virtuales</h2>
      <p>Usa siempre entornos virtuales para aislar dependencias de tus proyectos.</p>
      {create_code_block("terminal", "python -m venv venv")}
    """
  },
  'syntax.html': {
    'title': '2. Sintaxis Fundamental',
    'content': f"""
      <p>Python es un lenguaje interpretado, tipado dinámico y fuertemente tipado.</p>
      <h2 id="variables">Variables y Tipos de Datos</h2>
      <p>Variables: <code>x = 10</code></p>
      <p>Tipos de datos: <code>int, float, str, bool, list, dict, tuple, set</code>.</p>
      
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
      <p>Python permite pasar funciones como objetos de primera clase.</p>
      <h2 id="lambdas">Lambdas</h2>
      <p>Funciones anónimas:</p>
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
      <p>Define la estructura mediante clases y objetos.</p>
      <h2 id="definicion">Definición</h2>
      {create_code_block("vehiculo.py", '''class Vehiculo:
    def __init__(self, marca):
        self.marca = marca  # Atributo

    def arrancar(self):  # Método
        return f"{self.marca} arrancando"''')}
    """
  },
  'exercises.html': {
    'title': '30 Ejercicios Prácticos (Resúmenes de Lógica)',
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
      python_link = "python/installation.html"
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
                <button class="tech-dropdown-btn">
                    <span class="header-space-name">{site_title}</span>
                    <svg class="header-chevron" viewBox="0 0 20 20" fill="currentColor" width="16" height="16"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
                </button>
                <div class="tech-dropdown-menu">
                    <a href="{frappe_link}" class="tech-dropdown-item">Frappe HR</a>
                    <a href="{python_link}" class="tech-dropdown-item">Python Docs</a>
                </div>
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
