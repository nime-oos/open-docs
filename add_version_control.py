import json

with open("git/config.js", "r", encoding="utf-8") as f:
    code = f.read().replace("window.CONFIG_GIT = ", "").strip()
    if code.endswith(";"): code = code[:-1]
    data = json.loads(code)

content = """
<h2 style="color: var(--color-green-600); margin-top: 16px; border-bottom: 1px solid var(--outline-gray-1); padding-bottom: 8px;">¿Qué es Git?</h2>
<p style="margin-top: 16px; color: var(--ink-gray-8);">Git es el estándar de la industria para el sistema de control de versiones distribuido. Fue creado originalmente por Linus Torvalds en 2005 y actualmente es mantenido por Junio Hamano. Su propósito principal es:</p>
<ul style="margin-top: 16px; margin-bottom: 32px;">
    <li style="margin-bottom: 8px;"><strong>Rastrear modificaciones:</strong> Mantener un historial detallado de los cambios realizados en el código fuente.</li>
    <li style="margin-bottom: 8px;"><strong>Auditoría de autoría:</strong> Identificar qué desarrollador implementó cada cambio.</li>
    <li><strong>Colaboración asíncrona:</strong> Permitir que múltiples ingenieros trabajen en el mismo proyecto simultáneamente sin sobrescribir el trabajo del otro.</li>
</ul>

<h2 style="color: var(--color-green-600); margin-top: 32px; border-bottom: 1px solid var(--outline-gray-1); padding-bottom: 8px;">Glosario de Conceptos Clave</h2>
<p style="margin-top: 16px; color: var(--ink-gray-8);">Para dominar Git, es fundamental comprender su terminología principal:</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin-top: 16px; margin-bottom: 32px;">
    <div style="background: var(--surface-gray-1); padding: 16px; border-radius: 8px; border: 1px solid var(--outline-gray-1);">
        <strong style="color: var(--color-green-600); font-size: 1.1rem;">Repository (Repositorio)</strong>
        <p style="margin-top: 8px; color: var(--ink-gray-7);">El directorio de trabajo donde Git inicializa y gestiona todo el historial del proyecto.</p>
    </div>
    <div style="background: var(--surface-gray-1); padding: 16px; border-radius: 8px; border: 1px solid var(--outline-gray-1);">
        <strong style="color: var(--color-green-600); font-size: 1.1rem;">Clone (Clonar)</strong>
        <p style="margin-top: 8px; color: var(--ink-gray-7);">La acción de descargar y duplicar un repositorio remoto completo en un entorno local.</p>
    </div>
    <div style="background: var(--surface-gray-1); padding: 16px; border-radius: 8px; border: 1px solid var(--outline-gray-1);">
        <strong style="color: var(--color-green-600); font-size: 1.1rem;">Stage (Área de preparación)</strong>
        <p style="margin-top: 8px; color: var(--ink-gray-7);">Un espacio intermedio donde se indexan o seleccionan los archivos modificados específicos que se incluirán en la próxima confirmación.</p>
    </div>
    <div style="background: var(--surface-gray-1); padding: 16px; border-radius: 8px; border: 1px solid var(--outline-gray-1);">
        <strong style="color: var(--color-green-600); font-size: 1.1rem;">Commit (Confirmación)</strong>
        <p style="margin-top: 8px; color: var(--ink-gray-7);">Una instantánea inmutable del estado del código en un momento específico.</p>
    </div>
    <div style="background: var(--surface-gray-1); padding: 16px; border-radius: 8px; border: 1px solid var(--outline-gray-1);">
        <strong style="color: var(--color-green-600); font-size: 1.1rem;">Branch (Rama)</strong>
        <p style="margin-top: 8px; color: var(--ink-gray-7);">Una línea de desarrollo paralela e independiente. Permite trabajar en nuevas características o correcciones (bug fixes) sin comprometer la estabilidad del código base principal.</p>
    </div>
    <div style="background: var(--surface-gray-1); padding: 16px; border-radius: 8px; border: 1px solid var(--outline-gray-1);">
        <strong style="color: var(--color-green-600); font-size: 1.1rem;">Merge (Fusión)</strong>
        <p style="margin-top: 8px; color: var(--ink-gray-7);">El proceso de integrar los cambios de una rama hacia otra.</p>
    </div>
    <div style="background: var(--surface-gray-1); padding: 16px; border-radius: 8px; border: 1px solid var(--outline-gray-1);">
        <strong style="color: var(--color-green-600); font-size: 1.1rem;">Pull</strong>
        <p style="margin-top: 8px; color: var(--ink-gray-7);">Sincronización entrante; descarga e integra los últimos cambios del repositorio remoto al entorno local.</p>
    </div>
    <div style="background: var(--surface-gray-1); padding: 16px; border-radius: 8px; border: 1px solid var(--outline-gray-1);">
        <strong style="color: var(--color-green-600); font-size: 1.1rem;">Push</strong>
        <p style="margin-top: 8px; color: var(--ink-gray-7);">Sincronización saliente; sube las confirmaciones locales al repositorio remoto.</p>
    </div>
</div>

<h2 style="color: var(--color-green-600); margin-top: 32px; border-bottom: 1px solid var(--outline-gray-1); padding-bottom: 8px;">El Flujo de Trabajo Local</h2>
<p style="margin-top: 16px; color: var(--ink-gray-8);">El ciclo de vida básico de los archivos dentro de un repositorio de Git funciona de la siguiente manera:</p>
<ul style="margin-top: 16px; margin-bottom: 24px;">
    <li style="margin-bottom: 8px;"><strong>Inicialización:</strong> Al ejecutar Git en una carpeta, se crea un directorio oculto (<code>.git</code>) que actúa como el motor de seguimiento del historial.</li>
    <li style="margin-bottom: 8px;"><strong>Modificación:</strong> Cualquier archivo que sea alterado, añadido o eliminado adquiere el estado de Modificado.</li>
    <li style="margin-bottom: 8px;"><strong>Preparación (Staging):</strong> Los archivos modificados que se desean guardar se envían al Stage.</li>
    <li><strong>Confirmación (Commit):</strong> Los archivos en el Stage se empaquetan en un Commit permanente.</li>
</ul>

<div style="background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-blue-600); margin: 24px 0; border-radius: 4px;">
    <strong>📘 Nota técnica:</strong> Para optimizar el rendimiento y el almacenamiento, Git no guarda una copia completa de cada archivo en cada commit, sino que registra únicamente las diferencias o cambios realizados.
</div>

<h2 style="color: var(--color-green-600); margin-top: 32px; border-bottom: 1px solid var(--outline-gray-1); padding-bottom: 8px;">Arquitectura Distribuida y Plataformas Remotas</h2>

<h3 style="margin-top: 24px;">Trabajo Local vs. Remoto</h3>
<p style="margin-top: 8px; color: var(--ink-gray-8);">Una de las mayores ventajas de Git es su naturaleza distribuida. La gran mayoría de las operaciones (preparar archivos, crear commits, revisar el historial, cambiar de ramas) ocurren estrictamente de manera local en tu computadora, sin necesidad de conexión a internet. Solo los comandos <strong>Push</strong> y <strong>Pull</strong> interactúan con los servidores externos.</p>

<h3 style="margin-top: 24px;">Git vs. GitHub</h3>
<p style="margin-top: 8px; color: var(--ink-gray-8);">Es crucial diferenciar la herramienta del servicio de alojamiento:</p>
<ul style="margin-top: 16px; margin-bottom: 32px;">
    <li style="margin-bottom: 8px;"><strong>Git:</strong> Es el motor o software de control de versiones subyacente.</li>
    <li><strong>GitHub / GitLab / Bitbucket:</strong> Son plataformas de alojamiento en la nube. GitHub (actualmente propiedad de Microsoft) es el mayor anfitrión de código fuente del mundo y proporciona una interfaz web y herramientas colaborativas construidas sobre la tecnología de Git.</li>
</ul>

<h2 style="color: var(--color-green-600); margin-top: 32px; border-bottom: 1px solid var(--outline-gray-1); padding-bottom: 8px;">¿Por qué adoptar Git?</h2>
<p style="margin-top: 16px; font-size: 1.05rem; font-weight: 500; color: var(--ink-gray-9); background: var(--surface-gray-1); padding: 24px; border-radius: 8px; border-left: 4px solid var(--color-green-600);">
    Utilizado por más del 70% de los desarrolladores a nivel global, Git es indispensable porque facilita el trabajo distribuido desde cualquier lugar del mundo, proporciona una trazabilidad absoluta de cada línea de código y ofrece una red de seguridad inestimable al permitir revertir el proyecto a versiones estables anteriores en caso de fallos.
</p>
"""

# Append the new route to the sidebar under "intro" group
for group in data["sidebar"]:
    if group["id"] == "intro":
        group["children"].append({
            "route": "version_control.html",
            "title": "Control de Versiones"
        })

# Add the content
data["contents"]["version_control.html"] = {
    "title": "Control de Versiones",
    "content": content
}

js_content = f"window.CONFIG_GIT = {json.dumps(data, indent=2)};\n"
with open("git/config.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Added Control de Versiones to Git")
