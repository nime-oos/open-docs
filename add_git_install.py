import json

with open("git/config.js", "r", encoding="utf-8") as f:
    code = f.read().replace("window.CONFIG_GIT = ", "").strip()
    if code.endswith(";"): code = code[:-1]
    data = json.loads(code)

content = """
<p style="font-size: 1.1rem; line-height: 1.6; color: var(--ink-gray-8);">
    Puedes descargar Git de forma gratuita desde <a href="https://git-scm.com" target="_blank" style="color: var(--color-green-600); font-weight: 500;">git-scm.com</a>.
</p>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-top: 24px; margin-bottom: 24px;">
    <div style="background: var(--surface-gray-1); padding: 16px; border-radius: 8px; border-left: 4px solid var(--color-blue-600);">
        <strong style="color: var(--ink-gray-9); font-size: 1.1rem;">🖥️ Windows</strong>
        <p style="margin-top: 8px; color: var(--ink-gray-7);">Descarga y ejecuta el instalador. Haz clic en "Siguiente" para aceptar las configuraciones recomendadas. Esto instalará Git y Git Bash.</p>
    </div>
    <div style="background: var(--surface-gray-1); padding: 16px; border-radius: 8px; border-left: 4px solid var(--color-gray-800);">
        <strong style="color: var(--ink-gray-9); font-size: 1.1rem;">🍎 macOS</strong>
        <p style="margin-top: 8px; color: var(--ink-gray-7);">Si usas Homebrew, abre la Terminal y ejecuta el comando de instalación. O bien, descarga el archivo .dmg y arrastra Git a Aplicaciones.</p>
        <div class="code-block" style="margin-top: 12px;">
            <div class="code-block-header">
                <div class="terminal-dots"><div class="terminal-dot red"></div><div class="terminal-dot yellow"></div><div class="terminal-dot green"></div></div>
                <div class="terminal-title">terminal</div>
            </div>
            <div class="code-block-content"><pre><code spellcheck="false">brew install git</code></pre></div>
        </div>
    </div>
    <div style="background: var(--surface-gray-1); padding: 16px; border-radius: 8px; border-left: 4px solid var(--color-orange-600);">
        <strong style="color: var(--ink-gray-9); font-size: 1.1rem;">🐧 Linux</strong>
        <p style="margin-top: 8px; color: var(--ink-gray-7);">Abre tu terminal y usa tu gestor de paquetes. Por ejemplo, en Ubuntu/Debian utiliza APT.</p>
        <div class="code-block" style="margin-top: 12px;">
            <div class="code-block-header">
                <div class="terminal-dots"><div class="terminal-dot red"></div><div class="terminal-dot yellow"></div><div class="terminal-dot green"></div></div>
                <div class="terminal-title">terminal</div>
            </div>
            <div class="code-block-content"><pre><code spellcheck="false">sudo apt-get install git</code></pre></div>
        </div>
    </div>
</div>

<p style="color: var(--ink-gray-8); margin-bottom: 24px;">Después de la instalación, podrás usar Git desde tu terminal o símbolo del sistema.</p>

<div style="background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-green-500); margin: 24px 0; border-radius: 4px;">
    <strong>💡 Consejo para principiantes:</strong> Instalar Git es seguro y siempre puedes desinstalarlo más tarde si lo deseas.
</div>

<h2 style="color: var(--color-green-600); margin-top: 40px; border-bottom: 1px solid var(--outline-gray-1); padding-bottom: 8px;">Git Bash (Solo Windows)</h2>
<p style="margin-top: 16px; color: var(--ink-gray-8);">Git Bash es una terminal para Windows que te permite usar comandos de Git y comandos Unix tradicionales (como <code>ls</code> y <code>pwd</code>).</p>
<ul style="margin-top: 16px; margin-bottom: 24px;">
    <li style="margin-bottom: 8px;">Después de instalar Git, puedes encontrar Git Bash en tu menú de Inicio.</li>
    <li>Puedes usar Git Bash al igual que el Símbolo del sistema.</li>
</ul>

<div style="margin-bottom: 24px;">
    <strong>Ejemplo: Abrir Git Bash</strong>
    <p style="margin-top: 4px; margin-bottom: 12px; color: var(--ink-gray-6);">Haz clic en Inicio, escribe "Git Bash" y abre la aplicación.</p>
    <strong>Ejemplo: Primer Comando en Git Bash</strong>
    <div class="code-block" style="margin-top: 8px;">
      <div class="code-block-header">
        <div class="terminal-dots"><div class="terminal-dot red"></div><div class="terminal-dot yellow"></div><div class="terminal-dot green"></div></div>
        <div class="terminal-title">terminal</div>
      </div>
      <div class="code-block-content">
        <pre><code spellcheck="false">ls\nDesktop  Documents  Downloads  Pictures</code></pre>
      </div>
    </div>
    <p style="margin-top: 8px; color: var(--ink-gray-6); font-size: 0.9rem;">Este comando enumera los archivos en tu carpeta actual.</p>
</div>

<h2 style="color: var(--color-green-600); margin-top: 40px; border-bottom: 1px solid var(--outline-gray-1); padding-bottom: 8px;">Verificando tu Instalación</h2>
<p style="margin-top: 16px; color: var(--ink-gray-8);">Después de instalar, comprueba que Git funciona abriendo tu terminal (o Git Bash en Windows) y ejecutando:</p>

<div class="code-block" style="margin-top: 16px; margin-bottom: 16px;">
  <div class="code-block-header">
    <div class="terminal-dots"><div class="terminal-dot red"></div><div class="terminal-dot yellow"></div><div class="terminal-dot green"></div></div>
    <div class="terminal-title">terminal</div>
  </div>
  <div class="code-block-content">
    <pre><code spellcheck="false">git --version\ngit version 2.43.0.windows.1</code></pre>
  </div>
</div>
<p style="color: var(--ink-gray-8);">Si Git está instalado, verás algo como <code>git version X.Y.Z</code>. Si ves un error, intenta cerrar y volver a abrir tu terminal, o comprueba que Git esté en tu PATH.</p>

<h2 style="color: var(--color-green-600); margin-top: 40px; border-bottom: 1px solid var(--outline-gray-1); padding-bottom: 8px;">Editor por Defecto</h2>
<p style="margin-top: 16px; color: var(--ink-gray-8);">Durante la instalación, Git te pide que elijas un editor de texto por defecto. Este es el programa que se abrirá cuando necesites escribir mensajes largos (como para los commits).</p>

<div style="display: flex; flex-direction: column; gap: 16px; margin-top: 16px; margin-bottom: 24px;">
    <div>
        <strong>Configurar VS Code como Editor:</strong>
        <div class="code-block" style="margin-top: 8px;">
          <div class="code-block-header">
            <div class="terminal-dots"><div class="terminal-dot red"></div><div class="terminal-dot yellow"></div><div class="terminal-dot green"></div></div>
            <div class="terminal-title">terminal</div>
          </div>
          <div class="code-block-content">
            <pre><code spellcheck="false">git config --global core.editor "code --wait"</code></pre>
          </div>
        </div>
    </div>
    <div>
        <strong>Configurar Notepad (Windows):</strong>
        <p style="font-size: 0.9rem; color: var(--ink-gray-6); margin-bottom: 8px;">Si no estás seguro, simplemente elige el predeterminado (Notepad en Windows). Siempre puedes cambiar esto más tarde.</p>
        <div class="code-block">
          <div class="code-block-header">
            <div class="terminal-dots"><div class="terminal-dot red"></div><div class="terminal-dot yellow"></div><div class="terminal-dot green"></div></div>
            <div class="terminal-title">terminal</div>
          </div>
          <div class="code-block-content">
            <pre><code spellcheck="false">git config --global core.editor "notepad"</code></pre>
          </div>
        </div>
    </div>
</div>

<h2 style="color: var(--color-green-600); margin-top: 40px; border-bottom: 1px solid var(--outline-gray-1); padding-bottom: 8px;">Entorno PATH</h2>
<p style="margin-top: 16px; color: var(--ink-gray-8);">Elegir añadir Git a tu <code>PATH</code> significa que puedes usar comandos de Git en cualquier ventana de terminal. Es muy recomendable para la mayoría de los usuarios hacer esto durante la instalación. Si omites esto, solo podrás usar Git en Git Bash (en Windows) o en la Terminal predeterminada.</p>

<h3 style="margin-top: 32px;">Cómo añadir Git al PATH después de la Instalación</h3>
<div style="margin-top: 16px; background: var(--surface-gray-1); padding: 16px; border-radius: 8px; border: 1px solid var(--outline-gray-1); margin-bottom: 16px;">
    <strong>Windows:</strong>
    <ol style="margin-top: 12px; margin-left: 16px; color: var(--ink-gray-7);">
        <li style="margin-bottom: 8px;">Busca "Variables de entorno" en el menú de Inicio y ábrelo.</li>
        <li style="margin-bottom: 8px;">Haz clic en "Variables de entorno..." y busca la variable "Path" bajo "Variables del sistema".</li>
        <li style="margin-bottom: 8px;">Haz clic en "Editar", luego "Nuevo", y añade la ruta a tus carpetas bin y cmd de Git (por ejemplo, <code>C:\Program Files\Git\bin</code> y <code>C:\Program Files\Git\cmd</code>).</li>
        <li>Haz clic en Aceptar para guardar. Reinicia tu terminal.</li>
    </ol>
</div>

<div style="margin-top: 16px; background: var(--surface-gray-1); padding: 16px; border-radius: 8px; border: 1px solid var(--outline-gray-1); margin-bottom: 16px;">
    <strong>macOS:</strong>
    <p style="margin-top: 8px; color: var(--ink-gray-7);">Si instalaste con Homebrew, tu PATH usualmente se configura automáticamente. Si no, abre la Terminal y añade esta línea a tu <code>~/.zshrc</code> o <code>~/.bash_profile</code>:</p>
    <div class="code-block" style="margin-top: 12px; margin-bottom: 8px;">
      <div class="code-block-header">
        <div class="terminal-dots"><div class="terminal-dot red"></div><div class="terminal-dot yellow"></div><div class="terminal-dot green"></div></div>
        <div class="terminal-title">.zshrc</div>
      </div>
      <div class="code-block-content"><pre><code spellcheck="false">export PATH="/usr/local/bin:$PATH"</code></pre></div>
    </div>
    <p style="color: var(--ink-gray-7); font-size: 0.9rem;">Guarda el archivo y ejecuta <code>source ~/.zshrc</code>.</p>
</div>

<div style="margin-top: 16px; background: var(--surface-gray-1); padding: 16px; border-radius: 8px; border: 1px solid var(--outline-gray-1); margin-bottom: 32px;">
    <strong>Linux:</strong>
    <p style="margin-top: 8px; color: var(--ink-gray-7);">La mayoría de los gestores de paquetes añaden Git al PATH automáticamente. Si no, añade esta línea a tu <code>~/.bashrc</code> o <code>~/.profile</code>:</p>
    <div class="code-block" style="margin-top: 12px; margin-bottom: 8px;">
      <div class="code-block-header">
        <div class="terminal-dots"><div class="terminal-dot red"></div><div class="terminal-dot yellow"></div><div class="terminal-dot green"></div></div>
        <div class="terminal-title">.bashrc</div>
      </div>
      <div class="code-block-content"><pre><code spellcheck="false">export PATH="/usr/bin:$PATH"</code></pre></div>
    </div>
    <p style="color: var(--ink-gray-7); font-size: 0.9rem;">Guarda el archivo y ejecuta <code>source ~/.bashrc</code>.</p>
</div>

<h2 style="color: var(--color-green-600); margin-top: 40px; border-bottom: 1px solid var(--outline-gray-1); padding-bottom: 8px;">Saltos de Línea (Line Endings)</h2>
<p style="margin-top: 16px; color: var(--ink-gray-8);">Git puede convertir los saltos de línea en archivos de texto. En Windows, generalmente es mejor seleccionar <strong>"Checkout Windows-style, commit Unix-style line endings"</strong>. Esto ayuda a prevenir problemas cuando compartes código con personas que utilizan diferentes sistemas operativos (Linux/macOS).</p>

<h2 style="color: var(--color-green-600); margin-top: 40px; border-bottom: 1px solid var(--outline-gray-1); padding-bottom: 8px;">Actualizar o Desinstalar Git</h2>
<ul style="margin-top: 16px; margin-bottom: 32px; color: var(--ink-gray-8);">
    <li style="margin-bottom: 16px;">
        <strong>Actualizar:</strong> Descarga y ejecuta el instalador más reciente, o usa tu gestor de paquetes (por ejemplo, <code>brew upgrade git</code> o <code>sudo apt-get upgrade git</code>). Es una buena idea mantener Git actualizado para obtener las últimas características y correcciones de seguridad.
    </li>
    <li>
        <strong>Desinstalar:</strong> Usa "Agregar o quitar programas" en Windows, o tu gestor de paquetes en Mac/Linux.
    </li>
</ul>

<h2 style="color: var(--color-orange-600); margin-top: 40px; border-bottom: 1px solid var(--outline-gray-1); padding-bottom: 8px;">Solución de Problemas (Troubleshooting)</h2>
<p style="margin-top: 16px; color: var(--ink-gray-8);">Si tienes problemas instalando o ejecutando Git, ¡no te preocupes! Aquí hay soluciones a algunos de los problemas más comunes.</p>

<div style="background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-green-500); margin: 24px 0; border-radius: 4px;">
    <strong>💡 Consejo:</strong> Si algo no funciona de inmediato, intenta cerrar y volver a abrir tu terminal, o reiniciar tu computadora.
</div>

<div style="display: flex; flex-direction: column; gap: 16px; margin-bottom: 40px;">
    <div style="background: var(--surface-white); padding: 16px; border-radius: 8px; border: 1px solid var(--outline-gray-1); box-shadow: var(--shadow-sm);">
        <h4 style="color: var(--ink-gray-9); margin-bottom: 8px;">❌ "git is not recognized as an internal or external command"</h4>
        <p style="color: var(--ink-gray-7);"><strong>Solución:</strong> Git no está en el PATH de tu sistema. Asegúrate de haberlo instalado y reinicia tu terminal. Si es necesario, añade la carpeta bin de Git a tu PATH como se explicó arriba.</p>
    </div>
    <div style="background: var(--surface-white); padding: 16px; border-radius: 8px; border: 1px solid var(--outline-gray-1); box-shadow: var(--shadow-sm);">
        <h4 style="color: var(--ink-gray-9); margin-bottom: 8px;">❌ Errores de permiso ("Permission denied")</h4>
        <p style="color: var(--ink-gray-7);"><strong>Solución:</strong> En Windows, ejecuta Git Bash o tu terminal como administrador. En macOS/Linux, usa <code>sudo</code> antes del comando si es estrictamente necesario.</p>
    </div>
    <div style="background: var(--surface-white); padding: 16px; border-radius: 8px; border: 1px solid var(--outline-gray-1); box-shadow: var(--shadow-sm);">
        <h4 style="color: var(--ink-gray-9); margin-bottom: 8px;">❌ Errores SSL o HTTPS al clonar/empujar</h4>
        <p style="color: var(--ink-gray-7);"><strong>Solución:</strong> Comprueba tu conexión a internet. Asegúrate de que tu versión de Git esté actualizada para tener los certificados raíz más recientes.</p>
    </div>
    <div style="background: var(--surface-white); padding: 16px; border-radius: 8px; border: 1px solid var(--outline-gray-1); box-shadow: var(--shadow-sm);">
        <h4 style="color: var(--ink-gray-9); margin-bottom: 8px;">❌ Versión incorrecta de Git</h4>
        <p style="color: var(--ink-gray-7);"><strong>Solución:</strong> Comprueba la versión instalada con <code>git --version</code>. Descarga la última versión de git-scm.com si es necesario.</p>
    </div>
</div>
"""

# Append the new route to the sidebar under "intro" group
for group in data["sidebar"]:
    if group["id"] == "intro":
        group["children"].append({
            "route": "installation.html",
            "title": "Instalación de Git"
        })

data["contents"]["installation.html"] = {
    "title": "Instalación de Git",
    "content": content
}

js_content = f"window.CONFIG_GIT = {json.dumps(data, indent=2)};\n"
with open("git/config.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Added Installation to Git")
