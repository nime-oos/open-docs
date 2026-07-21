import json

with open("git/config.js", "r", encoding="utf-8") as f:
    code = f.read().replace("window.CONFIG_GIT = ", "").strip()
    if code.endswith(";"): code = code[:-1]
    data = json.loads(code)

content = """
<p style="font-size: 1.1rem; line-height: 1.6; color: var(--ink-gray-8);">
    <strong>¿Qué es Git?</strong><br>
    Git es un sistema de control de versiones distribuido, diseñado para rastrear de manera eficiente todos los cambios realizados en el código fuente durante el ciclo de vida del desarrollo de software. Es una herramienta fundamental que permite a los equipos colaborar de forma segura en proyectos de cualquier escala, manteniendo un historial inmutable y detallado de cada modificación.
</p>

<h3 style="color: var(--color-green-600); margin-top: 32px; border-bottom: 1px solid var(--outline-gray-1); padding-bottom: 8px;">¿Cuándo usar Git?</h3>
<ul style="margin-top: 16px;">
    <li style="margin-bottom: 12px;"><strong>Trabajo en paralelo:</strong> En proyectos del mundo real, generalmente hay múltiples desarrolladores trabajando al mismo tiempo. Git es vital para ramificar el trabajo y asegurar que no haya conflictos destructivos de código entre ellos.</li>
    <li><strong>Reversión de cambios:</strong> Los requerimientos de los proyectos suelen cambiar con frecuencia. Git permite a los desarrolladores navegar por el historial, revertir errores y regresar a una versión más antigua y estable del código de manera instantánea.</li>
</ul>

<h3 style="color: var(--color-green-600); margin-top: 32px; border-bottom: 1px solid var(--outline-gray-1); padding-bottom: 8px;">Aprendizaje mediante Ejemplos (Comandos Básicos)</h3>
<p style="margin-top: 16px; margin-bottom: 24px;">A continuación se muestran tres ejemplos fundamentales de comandos de Git:</p>

<div style="margin-bottom: 24px;">
    <strong>Inicializar un repositorio:</strong>
    <p style="margin-top: 4px; margin-bottom: 12px; color: var(--ink-gray-6);">Uso: Crea o inicializa un nuevo repositorio Git local.</p>
    <div class="code-block">
      <div class="code-block-header">
        <div class="terminal-dots">
          <div class="terminal-dot red"></div>
          <div class="terminal-dot yellow"></div>
          <div class="terminal-dot green"></div>
        </div>
        <div class="terminal-title">terminal</div>
      </div>
      <div class="code-block-content">
        <pre><code contenteditable="true" spellcheck="false">git init</code></pre>
      </div>
    </div>
</div>

<div style="margin-bottom: 24px;">
    <strong>Añadir archivos:</strong>
    <p style="margin-top: 4px; margin-bottom: 12px; color: var(--ink-gray-6);">Uso: Añade todos los archivos actuales al área de preparación (staging area).</p>
    <div class="code-block">
      <div class="code-block-header">
        <div class="terminal-dots">
          <div class="terminal-dot red"></div>
          <div class="terminal-dot yellow"></div>
          <div class="terminal-dot green"></div>
        </div>
        <div class="terminal-title">terminal</div>
      </div>
      <div class="code-block-content">
        <pre><code contenteditable="true" spellcheck="false">git add .</code></pre>
      </div>
    </div>
</div>

<div style="margin-bottom: 24px;">
    <strong>Confirmar cambios:</strong>
    <p style="margin-top: 4px; margin-bottom: 12px; color: var(--ink-gray-6);">Uso: Guarda (hace un commit de) los cambios en el repositorio con un mensaje descriptivo.</p>
    <div class="code-block">
      <div class="code-block-header">
        <div class="terminal-dots">
          <div class="terminal-dot red"></div>
          <div class="terminal-dot yellow"></div>
          <div class="terminal-dot green"></div>
        </div>
        <div class="terminal-title">terminal</div>
      </div>
      <div class="code-block-content">
        <pre><code contenteditable="true" spellcheck="false">git commit -m "First commit"</code></pre>
      </div>
    </div>
</div>

<h3 style="color: var(--color-green-600); margin-top: 32px; border-bottom: 1px solid var(--outline-gray-1); padding-bottom: 8px;">¿Qué cambia según el sistema operativo?</h3>
<p style="margin-top: 16px;">Los comandos de Git son exactamente los mismos sin importar si usas Windows, Mac o Linux.</p>
<p>La única diferencia real radica en la terminal o línea de comandos que utilices para ejecutar dichos comandos (ej. Git Bash en Windows vs. Terminal en macOS).</p>

<div style="background-color: var(--surface-gray-1); padding: 16px; border-left: 4px solid var(--color-green-600); margin: 32px 0; border-radius: 4px;">
    <strong>💡 Nota:</strong> Es importante hacer una distinción entre Git (la herramienta de línea de comandos de control de versiones local) y las plataformas de alojamiento basadas en Git (servicios en la nube), mencionando alternativas comerciales y populares como GitHub, GitLab y Bitbucket.
</div>
"""

# Update sidebar logic: Group = Introducción, Child = Conceptos Principales
data["sidebar"] = [
    {
        "id": "intro",
        "title": "Introducción",
        "children": [
            {
                "route": "introduction.html",
                "title": "Conceptos Principales"
            }
        ]
    }
]
data["contents"]["introduction.html"]["content"] = content
data["contents"]["introduction.html"]["title"] = "Conceptos Principales de Git"

js_content = f"window.CONFIG_GIT = {json.dumps(data, indent=2)};\n"
with open("git/config.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Updated git/config.js with no-hide blocks, better description and fixed hierarchy")
