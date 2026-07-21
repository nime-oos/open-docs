import json

content = """
<p>
    <strong>¿Qué es Git?</strong><br>
    Es un sistema de control de versiones.<br>
    Ayuda a mantener un registro de los cambios realizados en el código.<br>
    Se utiliza principalmente para colaborar en el código con otras personas.
</p>

<h3 style="color: var(--color-green-600); margin-top: 24px;">¿Cuándo usar Git?</h3>
<ul>
    <li><strong>Trabajo en paralelo:</strong> En proyectos del mundo real, generalmente hay múltiples desarrolladores trabajando al mismo tiempo. Git es necesario para asegurar que no haya conflictos de código entre ellos.</li>
    <li><strong>Reversión de cambios:</strong> Los requerimientos de los proyectos suelen cambiar con frecuencia. Git permite a los desarrolladores revertir cambios y regresar a una versión más antigua y estable del código.</li>
</ul>

<h3 style="color: var(--color-green-600); margin-top: 24px;">Aprendizaje mediante Ejemplos (Comandos Básicos)</h3>
<p>La imagen muestra tres ejemplos fundamentales de comandos de Git:</p>

<div style="margin-bottom: 24px;">
    <strong>Inicializar un repositorio:</strong>
    <pre style="background: var(--surface-gray-2); padding: 12px; border-radius: 6px; margin: 8px 0; border: 1px solid var(--outline-gray-1);"><code>git init</code></pre>
    <p style="margin-top: 4px; color: var(--ink-gray-6);">Uso: Crea o inicializa un nuevo repositorio Git local.</p>
</div>

<div style="margin-bottom: 24px;">
    <strong>Añadir archivos:</strong>
    <pre style="background: var(--surface-gray-2); padding: 12px; border-radius: 6px; margin: 8px 0; border: 1px solid var(--outline-gray-1);"><code>git add .</code></pre>
    <p style="margin-top: 4px; color: var(--ink-gray-6);">Uso: Añade todos los archivos actuales al área de preparación (staging area).</p>
</div>

<div style="margin-bottom: 24px;">
    <strong>Confirmar cambios:</strong>
    <pre style="background: var(--surface-gray-2); padding: 12px; border-radius: 6px; margin: 8px 0; border: 1px solid var(--outline-gray-1);"><code>git commit -m "First commit"</code></pre>
    <p style="margin-top: 4px; color: var(--ink-gray-6);">Uso: Guarda (hace un commit de) los cambios en el repositorio con un mensaje descriptivo.</p>
</div>

<h3 style="color: var(--color-green-600); margin-top: 24px;">¿Qué cambia según el sistema operativo?</h3>
<p>Los comandos de Git son exactamente los mismos sin importar si usas Windows, Mac o Linux.</p>
<p>La única diferencia real radica en la terminal o línea de comandos que utilices para ejecutar dichos comandos.</p>

<div style="background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-green-500); margin: 24px 0; border-radius: 4px;">
    <strong>💡 Nota:</strong> Se hace una distinción entre Git (la herramienta) y las plataformas de alojamiento basadas en Git, como GitHub, GitLab y Bitbucket.
</div>
"""

config = {
    "title": "Git Docs",
    "sidebar": [
        {
            "id": "conceptos",
            "title": "Conceptos Principales",
            "children": [
                {
                    "route": "introduction.html",
                    "title": "Introducción"
                }
            ]
        }
    ],
    "contents": {
        "introduction.html": {
            "title": "Introducción a Git",
            "content": content
        }
    }
}

js_content = f"window.CONFIG_GIT = {json.dumps(config, indent=2)};\n"
with open("git/config.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Created git/config.js")
