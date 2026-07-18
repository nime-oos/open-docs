import json

with open("frappe/config.js", "r", encoding="utf-8") as f:
    code = f.read().replace("window.CONFIG_FRAPPE = ", "").strip()
    if code.endswith(";"): code = code[:-1]
    data = json.loads(code)

sidebar = data["sidebar"]
contents = data["contents"]

for group in sidebar:
    for child in group["children"]:
        route = child["route"]
        title = child["title"]
        if route not in contents:
            # Generate mock content
            html = f"""
<p>La sección de <strong>{title}</strong> es un módulo fundamental de Frappe HR diseñado para optimizar las operaciones de recursos humanos.</p>

<h3>Características Principales</h3>
<ul>
    <li>Automatización completa de flujos de trabajo relacionados con {title}.</li>
    <li>Integración perfecta con el resto de módulos del ERP.</li>
    <li>Reportes analíticos en tiempo real.</li>
</ul>

<h3>Cómo utilizar este módulo</h3>
<p>Para acceder a esta función, dirígete al menú principal de Frappe HR, selecciona <em>{group['title']}</em> y haz clic en <strong>{title}</strong>. Desde allí podrás gestionar registros, configurar permisos y supervisar métricas.</p>

<div style="background-color: var(--surface-gray-2); padding: 16px; border-left: 4px solid var(--color-green-500); margin: 20px 0; border-radius: 4px;">
    <strong>💡 Tip Pro:</strong> Puedes usar el atajo <code>Ctrl+G</code> para abrir el buscador global y escribir "{title}" para acceder aún más rápido.
</div>

<p>Para más detalles técnicos sobre la configuración avanzada de {title}, por favor consulta la documentación oficial del framework Frappe o contacta con el administrador del sistema.</p>
"""
            contents[route] = {
                "title": title,
                "content": html
            }

js_content = f"window.CONFIG_FRAPPE = {json.dumps(data, indent=2)};\n"
with open("frappe/config.js", "w", encoding="utf-8") as f:
    f.write(js_content)
print("Filled missing Frappe content!")
