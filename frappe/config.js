window.CONFIG_FRAPPE = {
  "id": "frappe",
  "title": "Frappe HR",
  "sidebar": [
    {
      "id": "intro",
      "title": "Introducci\u00f3n",
      "children": [
        {
          "id": "introduction",
          "title": "Frappe HR",
          "route": "introduction.html"
        },
        {
          "id": "videos",
          "title": "Videos",
          "route": "videos.html"
        }
      ]
    },
    {
      "id": "mobile",
      "title": "Frappe HR M\u00f3vil",
      "children": [
        {
          "id": "mobile-app-installation",
          "title": "Instalaci\u00f3n de App M\u00f3vil",
          "route": "mobile-app-installation.html"
        },
        {
          "id": "push-notification",
          "title": "Notificaciones Push",
          "route": "push-notification.html"
        }
      ]
    },
    {
      "id": "org",
      "title": "Gesti\u00f3n de la Organizaci\u00f3n",
      "children": [
        {
          "id": "employee",
          "title": "Empleado",
          "route": "employee.html"
        },
        {
          "id": "employment-type",
          "title": "Tipo de Empleo",
          "route": "employment-type.html"
        },
        {
          "id": "branch",
          "title": "Sucursal",
          "route": "branch.html"
        },
        {
          "id": "department",
          "title": "Departamento",
          "route": "department.html"
        },
        {
          "id": "designation",
          "title": "Designaci\u00f3n",
          "route": "designation.html"
        },
        {
          "id": "employee-grade",
          "title": "Grado del Empleado",
          "route": "employee-grade.html"
        },
        {
          "id": "employee-group",
          "title": "Grupo de Empleados",
          "route": "employee-group.html"
        },
        {
          "id": "employee-health-insurance",
          "title": "Seguro de Salud",
          "route": "employee-health-insurance.html"
        },
        {
          "id": "organizational-chart",
          "title": "Organigrama",
          "route": "organizational-chart.html"
        }
      ]
    },
    {
      "id": "attendance",
      "title": "Asistencia",
      "children": [
        {
          "id": "attendance-page",
          "title": "Asistencia",
          "route": "attendance.html"
        },
        {
          "id": "employee-attendance-tool",
          "title": "Herramienta de Asistencia",
          "route": "employee-attendance-tool.html"
        },
        {
          "id": "attendance-request",
          "title": "Solicitud de Asistencia",
          "route": "attendance-request.html"
        },
        {
          "id": "upload-attendance",
          "title": "Subir Asistencia",
          "route": "upload-attendance.html"
        },
        {
          "id": "employee-checkin",
          "title": "Check-in de Empleado",
          "route": "employee-checkin.html"
        },
        {
          "id": "auto-attendance",
          "title": "Asistencia Autom\u00e1tica",
          "route": "auto-attendance.html"
        },
        {
          "id": "integrating-bio",
          "title": "Integraci\u00f3n Biom\u00e9trica",
          "route": "integrating-frappe-hr-with-bio.html"
        }
      ]
    },
    {
      "id": "shift",
      "title": "Gesti\u00f3n de Turnos",
      "children": [
        {
          "id": "shift-management",
          "title": "Gesti\u00f3n de Turnos",
          "route": "shift-management.html"
        },
        {
          "id": "shift-type",
          "title": "Tipo de Turno",
          "route": "shift-type.html"
        },
        {
          "id": "shift-location",
          "title": "Ubicaci\u00f3n de Turno",
          "route": "shift-location.html"
        },
        {
          "id": "shift-request",
          "title": "Solicitud de Turno",
          "route": "shift-request.html"
        },
        {
          "id": "shift-assignment",
          "title": "Asignaci\u00f3n de Turno",
          "route": "shift-assignment.html"
        }
      ]
    }
  ],
  "contents": {
    "introduction.html": {
      "title": "Frappe HR",
      "content": "\n      <p>Frappe HR es un software de n\u00f3mina y recursos humanos de c\u00f3digo abierto, moderno y f\u00e1cil de usar para todas las organizaciones. Tiene todo lo necesario para impulsar la excelencia dentro de la empresa. \u00a1Es una soluci\u00f3n HRMS completa con m\u00e1s de 13 m\u00f3dulos diferentes, desde la Gesti\u00f3n de Empleados, Onboarding, Vacaciones, hasta N\u00f3mina, Impuestos y m\u00e1s!</p>\n      \n      <div class=\"callout\">\n        <div class=\"callout-icon\">\ud83d\udca1</div>\n        <div class=\"callout-content\">\n          <p><strong>Nota importante:</strong> Frappe HR es altamente personalizable. Puedes modificar los flujos de trabajo seg\u00fan las necesidades de tu empresa.</p>\n        </div>\n      </div>\n\n      <img src=\"https://docs.frappe.io/files/imagee5004c.png\" alt=\"Employee Profile Screenshot\" />\n      \n      <h2 id=\"why-frappe-hr\">Por qu\u00e9 Frappe HR</h2>\n      <p>Las empresas suelen tener problemas con procesos de RR.HH. dispersos, c\u00e1lculos de n\u00f3mina manuales, registros de empleados desconectados y aprobaciones que consumen mucho tiempo.</p>\n      <ul>\n        <li>Frappe HR re\u00fane todo bajo un mismo techo para que los equipos de RR.HH. puedan centrarse en las personas, no en el papeleo.</li>\n        <li>Dise\u00f1ado para organizaciones que necesitan una soluci\u00f3n flexible y rentable, Frappe HR elimina ineficiencias, garantiza el cumplimiento y brinda a los empleados una experiencia fluida.</li>\n        <li>Ya sea que administre unos pocos empleados o escale a miles, lo ayuda a mantenerse organizado sin verse abrumado por los gastos administrativos.</li>\n      </ul>\n\n      <details>\n        <summary>Ver un ejemplo de configuraci\u00f3n avanzada (C\u00f3digo)</summary>\n        <div class=\"details-content\">\n          <p>Puedes configurar Frappe HR usando su API en Python. Aqu\u00ed tienes un peque\u00f1o script de ejemplo (puedes editar el c\u00f3digo abajo):</p>\n          \n    <div class=\"code-block\">\n      <div class=\"code-block-header\">\n        <div class=\"terminal-dots\">\n          <div class=\"terminal-dot red\"></div>\n          <div class=\"terminal-dot yellow\"></div>\n          <div class=\"terminal-dot green\"></div>\n        </div>\n        <div class=\"terminal-title\">api_example.py</div>\n      </div>\n      <div class=\"code-block-content\">\n        <pre><code contenteditable=\"true\" spellcheck=\"false\">import frappe\n\ndef create_employee(name, department):\n    emp = frappe.get_doc({\n        \"doctype\": \"Employee\",\n        \"employee_name\": name,\n        \"department\": department,\n        \"status\": \"Active\"\n    })\n    emp.insert()\n    return emp.name</code></pre>\n      </div>\n    </div>\n    \n        </div>\n      </details>\n      \n      <h2 id=\"key-features\">Caracter\u00edsticas Clave</h2>\n      <ul>\n        <li><strong>Ciclo de Vida del Empleado</strong>: Desde la incorporaci\u00f3n de empleados, la gesti\u00f3n de promociones y traslados, hasta la documentaci\u00f3n de entrevistas de salida.</li>\n        <li><strong>Permisos y Asistencia</strong>: Configure pol\u00edticas de licencias, incorpore d\u00edas festivos regionales, entrada/salida con geolocalizaci\u00f3n, seguimiento de saldos de licencias.</li>\n        <li><strong>N\u00f3mina e Impuestos</strong>: Cree estructuras salariales, configure tramos de impuestos sobre la renta, ejecute n\u00f3minas est\u00e1ndar, pagos fuera de ciclo, recibos de sueldo.</li>\n      </ul>\n    "
    },
    "videos.html": {
      "title": "Videos",
      "content": "\n      <p>El m\u00f3dulo de Recursos Humanos (RR.HH.) cubre los procesos relacionados con el departamento de RR.HH. de una empresa. Mantiene una base de datos de empleados completa.</p>\n      <h2 id=\"talks-and-webinars\">Charlas y Seminarios Web</h2>\n      <h3 id=\"introducing-frappe-hr\">Presentando Frappe HR</h3>\n      <div style=\"background:#111; color:white; padding:40px; border-radius:8px; text-align:center; aspect-ratio:16/9; display:flex; align-items:center; justify-content:center; flex-direction:column;\">\n         <h4>Presentando Frappe HR - Rucha Mahabal, Reema Mehta</h4>\n         <p>EC22 Ver en YouTube</p>\n      </div>\n    "
    },
    "mobile-app-installation.html": {
      "title": "Instalaci\u00f3n de App M\u00f3vil",
      "content": "\n<p>La secci\u00f3n de <strong>Instalaci\u00f3n de App M\u00f3vil</strong> es un m\u00f3dulo fundamental de Frappe HR dise\u00f1ado para optimizar las operaciones de recursos humanos.</p>\n\n<h3>Caracter\u00edsticas Principales</h3>\n<ul>\n    <li>Automatizaci\u00f3n completa de flujos de trabajo relacionados con Instalaci\u00f3n de App M\u00f3vil.</li>\n    <li>Integraci\u00f3n perfecta con el resto de m\u00f3dulos del ERP.</li>\n    <li>Reportes anal\u00edticos en tiempo real.</li>\n</ul>\n\n<h3>C\u00f3mo utilizar este m\u00f3dulo</h3>\n<p>Para acceder a esta funci\u00f3n, dir\u00edgete al men\u00fa principal de Frappe HR, selecciona <em>Frappe HR M\u00f3vil</em> y haz clic en <strong>Instalaci\u00f3n de App M\u00f3vil</strong>. Desde all\u00ed podr\u00e1s gestionar registros, configurar permisos y supervisar m\u00e9tricas.</p>\n\n<div style=\"background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-green-500); margin: 20px 0; border-radius: 4px;\">\n    <strong>\ud83d\udca1 Tip Pro:</strong> Puedes usar el atajo <code>Ctrl+G</code> para abrir el buscador global y escribir \"Instalaci\u00f3n de App M\u00f3vil\" para acceder a\u00fan m\u00e1s r\u00e1pido.\n</div>\n\n<p>Para m\u00e1s detalles t\u00e9cnicos sobre la configuraci\u00f3n avanzada de Instalaci\u00f3n de App M\u00f3vil, por favor consulta la documentaci\u00f3n oficial del framework Frappe o contacta con el administrador del sistema.</p>\n"
    },
    "push-notification.html": {
      "title": "Notificaciones Push",
      "content": "\n<p>La secci\u00f3n de <strong>Notificaciones Push</strong> es un m\u00f3dulo fundamental de Frappe HR dise\u00f1ado para optimizar las operaciones de recursos humanos.</p>\n\n<h3>Caracter\u00edsticas Principales</h3>\n<ul>\n    <li>Automatizaci\u00f3n completa de flujos de trabajo relacionados con Notificaciones Push.</li>\n    <li>Integraci\u00f3n perfecta con el resto de m\u00f3dulos del ERP.</li>\n    <li>Reportes anal\u00edticos en tiempo real.</li>\n</ul>\n\n<h3>C\u00f3mo utilizar este m\u00f3dulo</h3>\n<p>Para acceder a esta funci\u00f3n, dir\u00edgete al men\u00fa principal de Frappe HR, selecciona <em>Frappe HR M\u00f3vil</em> y haz clic en <strong>Notificaciones Push</strong>. Desde all\u00ed podr\u00e1s gestionar registros, configurar permisos y supervisar m\u00e9tricas.</p>\n\n<div style=\"background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-green-500); margin: 20px 0; border-radius: 4px;\">\n    <strong>\ud83d\udca1 Tip Pro:</strong> Puedes usar el atajo <code>Ctrl+G</code> para abrir el buscador global y escribir \"Notificaciones Push\" para acceder a\u00fan m\u00e1s r\u00e1pido.\n</div>\n\n<p>Para m\u00e1s detalles t\u00e9cnicos sobre la configuraci\u00f3n avanzada de Notificaciones Push, por favor consulta la documentaci\u00f3n oficial del framework Frappe o contacta con el administrador del sistema.</p>\n"
    },
    "employee.html": {
      "title": "Empleado",
      "content": "\n<p>La secci\u00f3n de <strong>Empleado</strong> es un m\u00f3dulo fundamental de Frappe HR dise\u00f1ado para optimizar las operaciones de recursos humanos.</p>\n\n<h3>Caracter\u00edsticas Principales</h3>\n<ul>\n    <li>Automatizaci\u00f3n completa de flujos de trabajo relacionados con Empleado.</li>\n    <li>Integraci\u00f3n perfecta con el resto de m\u00f3dulos del ERP.</li>\n    <li>Reportes anal\u00edticos en tiempo real.</li>\n</ul>\n\n<h3>C\u00f3mo utilizar este m\u00f3dulo</h3>\n<p>Para acceder a esta funci\u00f3n, dir\u00edgete al men\u00fa principal de Frappe HR, selecciona <em>Gesti\u00f3n de la Organizaci\u00f3n</em> y haz clic en <strong>Empleado</strong>. Desde all\u00ed podr\u00e1s gestionar registros, configurar permisos y supervisar m\u00e9tricas.</p>\n\n<div style=\"background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-green-500); margin: 20px 0; border-radius: 4px;\">\n    <strong>\ud83d\udca1 Tip Pro:</strong> Puedes usar el atajo <code>Ctrl+G</code> para abrir el buscador global y escribir \"Empleado\" para acceder a\u00fan m\u00e1s r\u00e1pido.\n</div>\n\n<p>Para m\u00e1s detalles t\u00e9cnicos sobre la configuraci\u00f3n avanzada de Empleado, por favor consulta la documentaci\u00f3n oficial del framework Frappe o contacta con el administrador del sistema.</p>\n"
    },
    "employment-type.html": {
      "title": "Tipo de Empleo",
      "content": "\n<p>La secci\u00f3n de <strong>Tipo de Empleo</strong> es un m\u00f3dulo fundamental de Frappe HR dise\u00f1ado para optimizar las operaciones de recursos humanos.</p>\n\n<h3>Caracter\u00edsticas Principales</h3>\n<ul>\n    <li>Automatizaci\u00f3n completa de flujos de trabajo relacionados con Tipo de Empleo.</li>\n    <li>Integraci\u00f3n perfecta con el resto de m\u00f3dulos del ERP.</li>\n    <li>Reportes anal\u00edticos en tiempo real.</li>\n</ul>\n\n<h3>C\u00f3mo utilizar este m\u00f3dulo</h3>\n<p>Para acceder a esta funci\u00f3n, dir\u00edgete al men\u00fa principal de Frappe HR, selecciona <em>Gesti\u00f3n de la Organizaci\u00f3n</em> y haz clic en <strong>Tipo de Empleo</strong>. Desde all\u00ed podr\u00e1s gestionar registros, configurar permisos y supervisar m\u00e9tricas.</p>\n\n<div style=\"background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-green-500); margin: 20px 0; border-radius: 4px;\">\n    <strong>\ud83d\udca1 Tip Pro:</strong> Puedes usar el atajo <code>Ctrl+G</code> para abrir el buscador global y escribir \"Tipo de Empleo\" para acceder a\u00fan m\u00e1s r\u00e1pido.\n</div>\n\n<p>Para m\u00e1s detalles t\u00e9cnicos sobre la configuraci\u00f3n avanzada de Tipo de Empleo, por favor consulta la documentaci\u00f3n oficial del framework Frappe o contacta con el administrador del sistema.</p>\n"
    },
    "branch.html": {
      "title": "Sucursal",
      "content": "\n<p>La secci\u00f3n de <strong>Sucursal</strong> es un m\u00f3dulo fundamental de Frappe HR dise\u00f1ado para optimizar las operaciones de recursos humanos.</p>\n\n<h3>Caracter\u00edsticas Principales</h3>\n<ul>\n    <li>Automatizaci\u00f3n completa de flujos de trabajo relacionados con Sucursal.</li>\n    <li>Integraci\u00f3n perfecta con el resto de m\u00f3dulos del ERP.</li>\n    <li>Reportes anal\u00edticos en tiempo real.</li>\n</ul>\n\n<h3>C\u00f3mo utilizar este m\u00f3dulo</h3>\n<p>Para acceder a esta funci\u00f3n, dir\u00edgete al men\u00fa principal de Frappe HR, selecciona <em>Gesti\u00f3n de la Organizaci\u00f3n</em> y haz clic en <strong>Sucursal</strong>. Desde all\u00ed podr\u00e1s gestionar registros, configurar permisos y supervisar m\u00e9tricas.</p>\n\n<div style=\"background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-green-500); margin: 20px 0; border-radius: 4px;\">\n    <strong>\ud83d\udca1 Tip Pro:</strong> Puedes usar el atajo <code>Ctrl+G</code> para abrir el buscador global y escribir \"Sucursal\" para acceder a\u00fan m\u00e1s r\u00e1pido.\n</div>\n\n<p>Para m\u00e1s detalles t\u00e9cnicos sobre la configuraci\u00f3n avanzada de Sucursal, por favor consulta la documentaci\u00f3n oficial del framework Frappe o contacta con el administrador del sistema.</p>\n"
    },
    "department.html": {
      "title": "Departamento",
      "content": "\n<p>La secci\u00f3n de <strong>Departamento</strong> es un m\u00f3dulo fundamental de Frappe HR dise\u00f1ado para optimizar las operaciones de recursos humanos.</p>\n\n<h3>Caracter\u00edsticas Principales</h3>\n<ul>\n    <li>Automatizaci\u00f3n completa de flujos de trabajo relacionados con Departamento.</li>\n    <li>Integraci\u00f3n perfecta con el resto de m\u00f3dulos del ERP.</li>\n    <li>Reportes anal\u00edticos en tiempo real.</li>\n</ul>\n\n<h3>C\u00f3mo utilizar este m\u00f3dulo</h3>\n<p>Para acceder a esta funci\u00f3n, dir\u00edgete al men\u00fa principal de Frappe HR, selecciona <em>Gesti\u00f3n de la Organizaci\u00f3n</em> y haz clic en <strong>Departamento</strong>. Desde all\u00ed podr\u00e1s gestionar registros, configurar permisos y supervisar m\u00e9tricas.</p>\n\n<div style=\"background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-green-500); margin: 20px 0; border-radius: 4px;\">\n    <strong>\ud83d\udca1 Tip Pro:</strong> Puedes usar el atajo <code>Ctrl+G</code> para abrir el buscador global y escribir \"Departamento\" para acceder a\u00fan m\u00e1s r\u00e1pido.\n</div>\n\n<p>Para m\u00e1s detalles t\u00e9cnicos sobre la configuraci\u00f3n avanzada de Departamento, por favor consulta la documentaci\u00f3n oficial del framework Frappe o contacta con el administrador del sistema.</p>\n"
    },
    "designation.html": {
      "title": "Designaci\u00f3n",
      "content": "\n<p>La secci\u00f3n de <strong>Designaci\u00f3n</strong> es un m\u00f3dulo fundamental de Frappe HR dise\u00f1ado para optimizar las operaciones de recursos humanos.</p>\n\n<h3>Caracter\u00edsticas Principales</h3>\n<ul>\n    <li>Automatizaci\u00f3n completa de flujos de trabajo relacionados con Designaci\u00f3n.</li>\n    <li>Integraci\u00f3n perfecta con el resto de m\u00f3dulos del ERP.</li>\n    <li>Reportes anal\u00edticos en tiempo real.</li>\n</ul>\n\n<h3>C\u00f3mo utilizar este m\u00f3dulo</h3>\n<p>Para acceder a esta funci\u00f3n, dir\u00edgete al men\u00fa principal de Frappe HR, selecciona <em>Gesti\u00f3n de la Organizaci\u00f3n</em> y haz clic en <strong>Designaci\u00f3n</strong>. Desde all\u00ed podr\u00e1s gestionar registros, configurar permisos y supervisar m\u00e9tricas.</p>\n\n<div style=\"background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-green-500); margin: 20px 0; border-radius: 4px;\">\n    <strong>\ud83d\udca1 Tip Pro:</strong> Puedes usar el atajo <code>Ctrl+G</code> para abrir el buscador global y escribir \"Designaci\u00f3n\" para acceder a\u00fan m\u00e1s r\u00e1pido.\n</div>\n\n<p>Para m\u00e1s detalles t\u00e9cnicos sobre la configuraci\u00f3n avanzada de Designaci\u00f3n, por favor consulta la documentaci\u00f3n oficial del framework Frappe o contacta con el administrador del sistema.</p>\n"
    },
    "employee-grade.html": {
      "title": "Grado del Empleado",
      "content": "\n<p>La secci\u00f3n de <strong>Grado del Empleado</strong> es un m\u00f3dulo fundamental de Frappe HR dise\u00f1ado para optimizar las operaciones de recursos humanos.</p>\n\n<h3>Caracter\u00edsticas Principales</h3>\n<ul>\n    <li>Automatizaci\u00f3n completa de flujos de trabajo relacionados con Grado del Empleado.</li>\n    <li>Integraci\u00f3n perfecta con el resto de m\u00f3dulos del ERP.</li>\n    <li>Reportes anal\u00edticos en tiempo real.</li>\n</ul>\n\n<h3>C\u00f3mo utilizar este m\u00f3dulo</h3>\n<p>Para acceder a esta funci\u00f3n, dir\u00edgete al men\u00fa principal de Frappe HR, selecciona <em>Gesti\u00f3n de la Organizaci\u00f3n</em> y haz clic en <strong>Grado del Empleado</strong>. Desde all\u00ed podr\u00e1s gestionar registros, configurar permisos y supervisar m\u00e9tricas.</p>\n\n<div style=\"background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-green-500); margin: 20px 0; border-radius: 4px;\">\n    <strong>\ud83d\udca1 Tip Pro:</strong> Puedes usar el atajo <code>Ctrl+G</code> para abrir el buscador global y escribir \"Grado del Empleado\" para acceder a\u00fan m\u00e1s r\u00e1pido.\n</div>\n\n<p>Para m\u00e1s detalles t\u00e9cnicos sobre la configuraci\u00f3n avanzada de Grado del Empleado, por favor consulta la documentaci\u00f3n oficial del framework Frappe o contacta con el administrador del sistema.</p>\n"
    },
    "employee-group.html": {
      "title": "Grupo de Empleados",
      "content": "\n<p>La secci\u00f3n de <strong>Grupo de Empleados</strong> es un m\u00f3dulo fundamental de Frappe HR dise\u00f1ado para optimizar las operaciones de recursos humanos.</p>\n\n<h3>Caracter\u00edsticas Principales</h3>\n<ul>\n    <li>Automatizaci\u00f3n completa de flujos de trabajo relacionados con Grupo de Empleados.</li>\n    <li>Integraci\u00f3n perfecta con el resto de m\u00f3dulos del ERP.</li>\n    <li>Reportes anal\u00edticos en tiempo real.</li>\n</ul>\n\n<h3>C\u00f3mo utilizar este m\u00f3dulo</h3>\n<p>Para acceder a esta funci\u00f3n, dir\u00edgete al men\u00fa principal de Frappe HR, selecciona <em>Gesti\u00f3n de la Organizaci\u00f3n</em> y haz clic en <strong>Grupo de Empleados</strong>. Desde all\u00ed podr\u00e1s gestionar registros, configurar permisos y supervisar m\u00e9tricas.</p>\n\n<div style=\"background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-green-500); margin: 20px 0; border-radius: 4px;\">\n    <strong>\ud83d\udca1 Tip Pro:</strong> Puedes usar el atajo <code>Ctrl+G</code> para abrir el buscador global y escribir \"Grupo de Empleados\" para acceder a\u00fan m\u00e1s r\u00e1pido.\n</div>\n\n<p>Para m\u00e1s detalles t\u00e9cnicos sobre la configuraci\u00f3n avanzada de Grupo de Empleados, por favor consulta la documentaci\u00f3n oficial del framework Frappe o contacta con el administrador del sistema.</p>\n"
    },
    "employee-health-insurance.html": {
      "title": "Seguro de Salud",
      "content": "\n<p>La secci\u00f3n de <strong>Seguro de Salud</strong> es un m\u00f3dulo fundamental de Frappe HR dise\u00f1ado para optimizar las operaciones de recursos humanos.</p>\n\n<h3>Caracter\u00edsticas Principales</h3>\n<ul>\n    <li>Automatizaci\u00f3n completa de flujos de trabajo relacionados con Seguro de Salud.</li>\n    <li>Integraci\u00f3n perfecta con el resto de m\u00f3dulos del ERP.</li>\n    <li>Reportes anal\u00edticos en tiempo real.</li>\n</ul>\n\n<h3>C\u00f3mo utilizar este m\u00f3dulo</h3>\n<p>Para acceder a esta funci\u00f3n, dir\u00edgete al men\u00fa principal de Frappe HR, selecciona <em>Gesti\u00f3n de la Organizaci\u00f3n</em> y haz clic en <strong>Seguro de Salud</strong>. Desde all\u00ed podr\u00e1s gestionar registros, configurar permisos y supervisar m\u00e9tricas.</p>\n\n<div style=\"background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-green-500); margin: 20px 0; border-radius: 4px;\">\n    <strong>\ud83d\udca1 Tip Pro:</strong> Puedes usar el atajo <code>Ctrl+G</code> para abrir el buscador global y escribir \"Seguro de Salud\" para acceder a\u00fan m\u00e1s r\u00e1pido.\n</div>\n\n<p>Para m\u00e1s detalles t\u00e9cnicos sobre la configuraci\u00f3n avanzada de Seguro de Salud, por favor consulta la documentaci\u00f3n oficial del framework Frappe o contacta con el administrador del sistema.</p>\n"
    },
    "organizational-chart.html": {
      "title": "Organigrama",
      "content": "\n<p>La secci\u00f3n de <strong>Organigrama</strong> es un m\u00f3dulo fundamental de Frappe HR dise\u00f1ado para optimizar las operaciones de recursos humanos.</p>\n\n<h3>Caracter\u00edsticas Principales</h3>\n<ul>\n    <li>Automatizaci\u00f3n completa de flujos de trabajo relacionados con Organigrama.</li>\n    <li>Integraci\u00f3n perfecta con el resto de m\u00f3dulos del ERP.</li>\n    <li>Reportes anal\u00edticos en tiempo real.</li>\n</ul>\n\n<h3>C\u00f3mo utilizar este m\u00f3dulo</h3>\n<p>Para acceder a esta funci\u00f3n, dir\u00edgete al men\u00fa principal de Frappe HR, selecciona <em>Gesti\u00f3n de la Organizaci\u00f3n</em> y haz clic en <strong>Organigrama</strong>. Desde all\u00ed podr\u00e1s gestionar registros, configurar permisos y supervisar m\u00e9tricas.</p>\n\n<div style=\"background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-green-500); margin: 20px 0; border-radius: 4px;\">\n    <strong>\ud83d\udca1 Tip Pro:</strong> Puedes usar el atajo <code>Ctrl+G</code> para abrir el buscador global y escribir \"Organigrama\" para acceder a\u00fan m\u00e1s r\u00e1pido.\n</div>\n\n<p>Para m\u00e1s detalles t\u00e9cnicos sobre la configuraci\u00f3n avanzada de Organigrama, por favor consulta la documentaci\u00f3n oficial del framework Frappe o contacta con el administrador del sistema.</p>\n"
    },
    "attendance.html": {
      "title": "Asistencia",
      "content": "\n<p>La secci\u00f3n de <strong>Asistencia</strong> es un m\u00f3dulo fundamental de Frappe HR dise\u00f1ado para optimizar las operaciones de recursos humanos.</p>\n\n<h3>Caracter\u00edsticas Principales</h3>\n<ul>\n    <li>Automatizaci\u00f3n completa de flujos de trabajo relacionados con Asistencia.</li>\n    <li>Integraci\u00f3n perfecta con el resto de m\u00f3dulos del ERP.</li>\n    <li>Reportes anal\u00edticos en tiempo real.</li>\n</ul>\n\n<h3>C\u00f3mo utilizar este m\u00f3dulo</h3>\n<p>Para acceder a esta funci\u00f3n, dir\u00edgete al men\u00fa principal de Frappe HR, selecciona <em>Asistencia</em> y haz clic en <strong>Asistencia</strong>. Desde all\u00ed podr\u00e1s gestionar registros, configurar permisos y supervisar m\u00e9tricas.</p>\n\n<div style=\"background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-green-500); margin: 20px 0; border-radius: 4px;\">\n    <strong>\ud83d\udca1 Tip Pro:</strong> Puedes usar el atajo <code>Ctrl+G</code> para abrir el buscador global y escribir \"Asistencia\" para acceder a\u00fan m\u00e1s r\u00e1pido.\n</div>\n\n<p>Para m\u00e1s detalles t\u00e9cnicos sobre la configuraci\u00f3n avanzada de Asistencia, por favor consulta la documentaci\u00f3n oficial del framework Frappe o contacta con el administrador del sistema.</p>\n"
    },
    "employee-attendance-tool.html": {
      "title": "Herramienta de Asistencia",
      "content": "\n<p>La secci\u00f3n de <strong>Herramienta de Asistencia</strong> es un m\u00f3dulo fundamental de Frappe HR dise\u00f1ado para optimizar las operaciones de recursos humanos.</p>\n\n<h3>Caracter\u00edsticas Principales</h3>\n<ul>\n    <li>Automatizaci\u00f3n completa de flujos de trabajo relacionados con Herramienta de Asistencia.</li>\n    <li>Integraci\u00f3n perfecta con el resto de m\u00f3dulos del ERP.</li>\n    <li>Reportes anal\u00edticos en tiempo real.</li>\n</ul>\n\n<h3>C\u00f3mo utilizar este m\u00f3dulo</h3>\n<p>Para acceder a esta funci\u00f3n, dir\u00edgete al men\u00fa principal de Frappe HR, selecciona <em>Asistencia</em> y haz clic en <strong>Herramienta de Asistencia</strong>. Desde all\u00ed podr\u00e1s gestionar registros, configurar permisos y supervisar m\u00e9tricas.</p>\n\n<div style=\"background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-green-500); margin: 20px 0; border-radius: 4px;\">\n    <strong>\ud83d\udca1 Tip Pro:</strong> Puedes usar el atajo <code>Ctrl+G</code> para abrir el buscador global y escribir \"Herramienta de Asistencia\" para acceder a\u00fan m\u00e1s r\u00e1pido.\n</div>\n\n<p>Para m\u00e1s detalles t\u00e9cnicos sobre la configuraci\u00f3n avanzada de Herramienta de Asistencia, por favor consulta la documentaci\u00f3n oficial del framework Frappe o contacta con el administrador del sistema.</p>\n"
    },
    "attendance-request.html": {
      "title": "Solicitud de Asistencia",
      "content": "\n<p>La secci\u00f3n de <strong>Solicitud de Asistencia</strong> es un m\u00f3dulo fundamental de Frappe HR dise\u00f1ado para optimizar las operaciones de recursos humanos.</p>\n\n<h3>Caracter\u00edsticas Principales</h3>\n<ul>\n    <li>Automatizaci\u00f3n completa de flujos de trabajo relacionados con Solicitud de Asistencia.</li>\n    <li>Integraci\u00f3n perfecta con el resto de m\u00f3dulos del ERP.</li>\n    <li>Reportes anal\u00edticos en tiempo real.</li>\n</ul>\n\n<h3>C\u00f3mo utilizar este m\u00f3dulo</h3>\n<p>Para acceder a esta funci\u00f3n, dir\u00edgete al men\u00fa principal de Frappe HR, selecciona <em>Asistencia</em> y haz clic en <strong>Solicitud de Asistencia</strong>. Desde all\u00ed podr\u00e1s gestionar registros, configurar permisos y supervisar m\u00e9tricas.</p>\n\n<div style=\"background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-green-500); margin: 20px 0; border-radius: 4px;\">\n    <strong>\ud83d\udca1 Tip Pro:</strong> Puedes usar el atajo <code>Ctrl+G</code> para abrir el buscador global y escribir \"Solicitud de Asistencia\" para acceder a\u00fan m\u00e1s r\u00e1pido.\n</div>\n\n<p>Para m\u00e1s detalles t\u00e9cnicos sobre la configuraci\u00f3n avanzada de Solicitud de Asistencia, por favor consulta la documentaci\u00f3n oficial del framework Frappe o contacta con el administrador del sistema.</p>\n"
    },
    "upload-attendance.html": {
      "title": "Subir Asistencia",
      "content": "\n<p>La secci\u00f3n de <strong>Subir Asistencia</strong> es un m\u00f3dulo fundamental de Frappe HR dise\u00f1ado para optimizar las operaciones de recursos humanos.</p>\n\n<h3>Caracter\u00edsticas Principales</h3>\n<ul>\n    <li>Automatizaci\u00f3n completa de flujos de trabajo relacionados con Subir Asistencia.</li>\n    <li>Integraci\u00f3n perfecta con el resto de m\u00f3dulos del ERP.</li>\n    <li>Reportes anal\u00edticos en tiempo real.</li>\n</ul>\n\n<h3>C\u00f3mo utilizar este m\u00f3dulo</h3>\n<p>Para acceder a esta funci\u00f3n, dir\u00edgete al men\u00fa principal de Frappe HR, selecciona <em>Asistencia</em> y haz clic en <strong>Subir Asistencia</strong>. Desde all\u00ed podr\u00e1s gestionar registros, configurar permisos y supervisar m\u00e9tricas.</p>\n\n<div style=\"background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-green-500); margin: 20px 0; border-radius: 4px;\">\n    <strong>\ud83d\udca1 Tip Pro:</strong> Puedes usar el atajo <code>Ctrl+G</code> para abrir el buscador global y escribir \"Subir Asistencia\" para acceder a\u00fan m\u00e1s r\u00e1pido.\n</div>\n\n<p>Para m\u00e1s detalles t\u00e9cnicos sobre la configuraci\u00f3n avanzada de Subir Asistencia, por favor consulta la documentaci\u00f3n oficial del framework Frappe o contacta con el administrador del sistema.</p>\n"
    },
    "employee-checkin.html": {
      "title": "Check-in de Empleado",
      "content": "\n<p>La secci\u00f3n de <strong>Check-in de Empleado</strong> es un m\u00f3dulo fundamental de Frappe HR dise\u00f1ado para optimizar las operaciones de recursos humanos.</p>\n\n<h3>Caracter\u00edsticas Principales</h3>\n<ul>\n    <li>Automatizaci\u00f3n completa de flujos de trabajo relacionados con Check-in de Empleado.</li>\n    <li>Integraci\u00f3n perfecta con el resto de m\u00f3dulos del ERP.</li>\n    <li>Reportes anal\u00edticos en tiempo real.</li>\n</ul>\n\n<h3>C\u00f3mo utilizar este m\u00f3dulo</h3>\n<p>Para acceder a esta funci\u00f3n, dir\u00edgete al men\u00fa principal de Frappe HR, selecciona <em>Asistencia</em> y haz clic en <strong>Check-in de Empleado</strong>. Desde all\u00ed podr\u00e1s gestionar registros, configurar permisos y supervisar m\u00e9tricas.</p>\n\n<div style=\"background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-green-500); margin: 20px 0; border-radius: 4px;\">\n    <strong>\ud83d\udca1 Tip Pro:</strong> Puedes usar el atajo <code>Ctrl+G</code> para abrir el buscador global y escribir \"Check-in de Empleado\" para acceder a\u00fan m\u00e1s r\u00e1pido.\n</div>\n\n<p>Para m\u00e1s detalles t\u00e9cnicos sobre la configuraci\u00f3n avanzada de Check-in de Empleado, por favor consulta la documentaci\u00f3n oficial del framework Frappe o contacta con el administrador del sistema.</p>\n"
    },
    "auto-attendance.html": {
      "title": "Asistencia Autom\u00e1tica",
      "content": "\n<p>La secci\u00f3n de <strong>Asistencia Autom\u00e1tica</strong> es un m\u00f3dulo fundamental de Frappe HR dise\u00f1ado para optimizar las operaciones de recursos humanos.</p>\n\n<h3>Caracter\u00edsticas Principales</h3>\n<ul>\n    <li>Automatizaci\u00f3n completa de flujos de trabajo relacionados con Asistencia Autom\u00e1tica.</li>\n    <li>Integraci\u00f3n perfecta con el resto de m\u00f3dulos del ERP.</li>\n    <li>Reportes anal\u00edticos en tiempo real.</li>\n</ul>\n\n<h3>C\u00f3mo utilizar este m\u00f3dulo</h3>\n<p>Para acceder a esta funci\u00f3n, dir\u00edgete al men\u00fa principal de Frappe HR, selecciona <em>Asistencia</em> y haz clic en <strong>Asistencia Autom\u00e1tica</strong>. Desde all\u00ed podr\u00e1s gestionar registros, configurar permisos y supervisar m\u00e9tricas.</p>\n\n<div style=\"background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-green-500); margin: 20px 0; border-radius: 4px;\">\n    <strong>\ud83d\udca1 Tip Pro:</strong> Puedes usar el atajo <code>Ctrl+G</code> para abrir el buscador global y escribir \"Asistencia Autom\u00e1tica\" para acceder a\u00fan m\u00e1s r\u00e1pido.\n</div>\n\n<p>Para m\u00e1s detalles t\u00e9cnicos sobre la configuraci\u00f3n avanzada de Asistencia Autom\u00e1tica, por favor consulta la documentaci\u00f3n oficial del framework Frappe o contacta con el administrador del sistema.</p>\n"
    },
    "integrating-frappe-hr-with-bio.html": {
      "title": "Integraci\u00f3n Biom\u00e9trica",
      "content": "\n<p>La secci\u00f3n de <strong>Integraci\u00f3n Biom\u00e9trica</strong> es un m\u00f3dulo fundamental de Frappe HR dise\u00f1ado para optimizar las operaciones de recursos humanos.</p>\n\n<h3>Caracter\u00edsticas Principales</h3>\n<ul>\n    <li>Automatizaci\u00f3n completa de flujos de trabajo relacionados con Integraci\u00f3n Biom\u00e9trica.</li>\n    <li>Integraci\u00f3n perfecta con el resto de m\u00f3dulos del ERP.</li>\n    <li>Reportes anal\u00edticos en tiempo real.</li>\n</ul>\n\n<h3>C\u00f3mo utilizar este m\u00f3dulo</h3>\n<p>Para acceder a esta funci\u00f3n, dir\u00edgete al men\u00fa principal de Frappe HR, selecciona <em>Asistencia</em> y haz clic en <strong>Integraci\u00f3n Biom\u00e9trica</strong>. Desde all\u00ed podr\u00e1s gestionar registros, configurar permisos y supervisar m\u00e9tricas.</p>\n\n<div style=\"background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-green-500); margin: 20px 0; border-radius: 4px;\">\n    <strong>\ud83d\udca1 Tip Pro:</strong> Puedes usar el atajo <code>Ctrl+G</code> para abrir el buscador global y escribir \"Integraci\u00f3n Biom\u00e9trica\" para acceder a\u00fan m\u00e1s r\u00e1pido.\n</div>\n\n<p>Para m\u00e1s detalles t\u00e9cnicos sobre la configuraci\u00f3n avanzada de Integraci\u00f3n Biom\u00e9trica, por favor consulta la documentaci\u00f3n oficial del framework Frappe o contacta con el administrador del sistema.</p>\n"
    },
    "shift-management.html": {
      "title": "Gesti\u00f3n de Turnos",
      "content": "\n<p>La secci\u00f3n de <strong>Gesti\u00f3n de Turnos</strong> es un m\u00f3dulo fundamental de Frappe HR dise\u00f1ado para optimizar las operaciones de recursos humanos.</p>\n\n<h3>Caracter\u00edsticas Principales</h3>\n<ul>\n    <li>Automatizaci\u00f3n completa de flujos de trabajo relacionados con Gesti\u00f3n de Turnos.</li>\n    <li>Integraci\u00f3n perfecta con el resto de m\u00f3dulos del ERP.</li>\n    <li>Reportes anal\u00edticos en tiempo real.</li>\n</ul>\n\n<h3>C\u00f3mo utilizar este m\u00f3dulo</h3>\n<p>Para acceder a esta funci\u00f3n, dir\u00edgete al men\u00fa principal de Frappe HR, selecciona <em>Gesti\u00f3n de Turnos</em> y haz clic en <strong>Gesti\u00f3n de Turnos</strong>. Desde all\u00ed podr\u00e1s gestionar registros, configurar permisos y supervisar m\u00e9tricas.</p>\n\n<div style=\"background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-green-500); margin: 20px 0; border-radius: 4px;\">\n    <strong>\ud83d\udca1 Tip Pro:</strong> Puedes usar el atajo <code>Ctrl+G</code> para abrir el buscador global y escribir \"Gesti\u00f3n de Turnos\" para acceder a\u00fan m\u00e1s r\u00e1pido.\n</div>\n\n<p>Para m\u00e1s detalles t\u00e9cnicos sobre la configuraci\u00f3n avanzada de Gesti\u00f3n de Turnos, por favor consulta la documentaci\u00f3n oficial del framework Frappe o contacta con el administrador del sistema.</p>\n"
    },
    "shift-type.html": {
      "title": "Tipo de Turno",
      "content": "\n<p>La secci\u00f3n de <strong>Tipo de Turno</strong> es un m\u00f3dulo fundamental de Frappe HR dise\u00f1ado para optimizar las operaciones de recursos humanos.</p>\n\n<h3>Caracter\u00edsticas Principales</h3>\n<ul>\n    <li>Automatizaci\u00f3n completa de flujos de trabajo relacionados con Tipo de Turno.</li>\n    <li>Integraci\u00f3n perfecta con el resto de m\u00f3dulos del ERP.</li>\n    <li>Reportes anal\u00edticos en tiempo real.</li>\n</ul>\n\n<h3>C\u00f3mo utilizar este m\u00f3dulo</h3>\n<p>Para acceder a esta funci\u00f3n, dir\u00edgete al men\u00fa principal de Frappe HR, selecciona <em>Gesti\u00f3n de Turnos</em> y haz clic en <strong>Tipo de Turno</strong>. Desde all\u00ed podr\u00e1s gestionar registros, configurar permisos y supervisar m\u00e9tricas.</p>\n\n<div style=\"background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-green-500); margin: 20px 0; border-radius: 4px;\">\n    <strong>\ud83d\udca1 Tip Pro:</strong> Puedes usar el atajo <code>Ctrl+G</code> para abrir el buscador global y escribir \"Tipo de Turno\" para acceder a\u00fan m\u00e1s r\u00e1pido.\n</div>\n\n<p>Para m\u00e1s detalles t\u00e9cnicos sobre la configuraci\u00f3n avanzada de Tipo de Turno, por favor consulta la documentaci\u00f3n oficial del framework Frappe o contacta con el administrador del sistema.</p>\n"
    },
    "shift-location.html": {
      "title": "Ubicaci\u00f3n de Turno",
      "content": "\n<p>La secci\u00f3n de <strong>Ubicaci\u00f3n de Turno</strong> es un m\u00f3dulo fundamental de Frappe HR dise\u00f1ado para optimizar las operaciones de recursos humanos.</p>\n\n<h3>Caracter\u00edsticas Principales</h3>\n<ul>\n    <li>Automatizaci\u00f3n completa de flujos de trabajo relacionados con Ubicaci\u00f3n de Turno.</li>\n    <li>Integraci\u00f3n perfecta con el resto de m\u00f3dulos del ERP.</li>\n    <li>Reportes anal\u00edticos en tiempo real.</li>\n</ul>\n\n<h3>C\u00f3mo utilizar este m\u00f3dulo</h3>\n<p>Para acceder a esta funci\u00f3n, dir\u00edgete al men\u00fa principal de Frappe HR, selecciona <em>Gesti\u00f3n de Turnos</em> y haz clic en <strong>Ubicaci\u00f3n de Turno</strong>. Desde all\u00ed podr\u00e1s gestionar registros, configurar permisos y supervisar m\u00e9tricas.</p>\n\n<div style=\"background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-green-500); margin: 20px 0; border-radius: 4px;\">\n    <strong>\ud83d\udca1 Tip Pro:</strong> Puedes usar el atajo <code>Ctrl+G</code> para abrir el buscador global y escribir \"Ubicaci\u00f3n de Turno\" para acceder a\u00fan m\u00e1s r\u00e1pido.\n</div>\n\n<p>Para m\u00e1s detalles t\u00e9cnicos sobre la configuraci\u00f3n avanzada de Ubicaci\u00f3n de Turno, por favor consulta la documentaci\u00f3n oficial del framework Frappe o contacta con el administrador del sistema.</p>\n"
    },
    "shift-request.html": {
      "title": "Solicitud de Turno",
      "content": "\n<p>La secci\u00f3n de <strong>Solicitud de Turno</strong> es un m\u00f3dulo fundamental de Frappe HR dise\u00f1ado para optimizar las operaciones de recursos humanos.</p>\n\n<h3>Caracter\u00edsticas Principales</h3>\n<ul>\n    <li>Automatizaci\u00f3n completa de flujos de trabajo relacionados con Solicitud de Turno.</li>\n    <li>Integraci\u00f3n perfecta con el resto de m\u00f3dulos del ERP.</li>\n    <li>Reportes anal\u00edticos en tiempo real.</li>\n</ul>\n\n<h3>C\u00f3mo utilizar este m\u00f3dulo</h3>\n<p>Para acceder a esta funci\u00f3n, dir\u00edgete al men\u00fa principal de Frappe HR, selecciona <em>Gesti\u00f3n de Turnos</em> y haz clic en <strong>Solicitud de Turno</strong>. Desde all\u00ed podr\u00e1s gestionar registros, configurar permisos y supervisar m\u00e9tricas.</p>\n\n<div style=\"background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-green-500); margin: 20px 0; border-radius: 4px;\">\n    <strong>\ud83d\udca1 Tip Pro:</strong> Puedes usar el atajo <code>Ctrl+G</code> para abrir el buscador global y escribir \"Solicitud de Turno\" para acceder a\u00fan m\u00e1s r\u00e1pido.\n</div>\n\n<p>Para m\u00e1s detalles t\u00e9cnicos sobre la configuraci\u00f3n avanzada de Solicitud de Turno, por favor consulta la documentaci\u00f3n oficial del framework Frappe o contacta con el administrador del sistema.</p>\n"
    },
    "shift-assignment.html": {
      "title": "Asignaci\u00f3n de Turno",
      "content": "\n<p>La secci\u00f3n de <strong>Asignaci\u00f3n de Turno</strong> es un m\u00f3dulo fundamental de Frappe HR dise\u00f1ado para optimizar las operaciones de recursos humanos.</p>\n\n<h3>Caracter\u00edsticas Principales</h3>\n<ul>\n    <li>Automatizaci\u00f3n completa de flujos de trabajo relacionados con Asignaci\u00f3n de Turno.</li>\n    <li>Integraci\u00f3n perfecta con el resto de m\u00f3dulos del ERP.</li>\n    <li>Reportes anal\u00edticos en tiempo real.</li>\n</ul>\n\n<h3>C\u00f3mo utilizar este m\u00f3dulo</h3>\n<p>Para acceder a esta funci\u00f3n, dir\u00edgete al men\u00fa principal de Frappe HR, selecciona <em>Gesti\u00f3n de Turnos</em> y haz clic en <strong>Asignaci\u00f3n de Turno</strong>. Desde all\u00ed podr\u00e1s gestionar registros, configurar permisos y supervisar m\u00e9tricas.</p>\n\n<div style=\"background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-green-500); margin: 20px 0; border-radius: 4px;\">\n    <strong>\ud83d\udca1 Tip Pro:</strong> Puedes usar el atajo <code>Ctrl+G</code> para abrir el buscador global y escribir \"Asignaci\u00f3n de Turno\" para acceder a\u00fan m\u00e1s r\u00e1pido.\n</div>\n\n<p>Para m\u00e1s detalles t\u00e9cnicos sobre la configuraci\u00f3n avanzada de Asignaci\u00f3n de Turno, por favor consulta la documentaci\u00f3n oficial del framework Frappe o contacta con el administrador del sistema.</p>\n"
    }
  }
};
