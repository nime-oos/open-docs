import re

with open('recovered_build.py', 'r', encoding='utf-8') as f:
    old_code = f.read()

with open('build.py', 'r', encoding='utf-8') as f:
    new_code = f.read()

def extract_block(code, start_marker, end_marker):
    start_idx = code.find(start_marker)
    if start_idx == -1: return None
    end_idx = code.find(end_marker, start_idx)
    if end_idx == -1: return None
    return code[start_idx:end_idx]

# Extract frappe data block
frappe_block = extract_block(old_code, "frappe_sidebar_data = [", "# ==========================================\n# 2. PYTHON SITE DATA")
# Extract python data block
python_block = extract_block(old_code, "python_sidebar_data = [", "# ==========================================\n# 3. GIT SITE DATA")
if not python_block: # maybe it ended at the master html generator
    python_block = extract_block(old_code, "python_sidebar_data = [", "# ==========================================\n# MASTER HTML GENERATOR")
    
if not frappe_block or not python_block:
    print("Could not extract blocks from old code.")
    exit(1)

# Now replace in new_code
new_frappe_start = new_code.find("frappe_sidebar_data = [")
new_frappe_end = new_code.find("# ==========================================\n# 2. PYTHON SITE DATA")
new_code = new_code[:new_frappe_start] + frappe_block + new_code[new_frappe_end:]

new_python_start = new_code.find("python_sidebar_data = [")
new_python_end = new_code.find("# ==========================================\n# 3. GIT SITE DATA")
new_code = new_code[:new_python_start] + python_block + new_code[new_python_end:]

# Update the dropdown text
new_code = new_code.replace('<span class="header-space-name">Cambiar Tecnología</span>', '<span class="header-space-name">Nime Open Docs</span>')

# Fix all.html \n issue
# In generate_all_in_one():
# full_content_html = "\\n".join(all_content) -> full_content_html = "\n".join(all_content)
new_code = new_code.replace('full_content_html = "\\n".join(all_content)', 'full_content_html = "\\n".join(all_content)')
# Wait! In python string, if I write "\\n".join(), it's literally backslash n. I need it to be "\n".join().
# But wait, in Python, if I want to output '\n' into the generated HTML file, I can just use "\n".
new_code = new_code.replace('full_content_html = "\\\\n".join(all_content)', 'full_content_html = "\\n".join(all_content)')

with open('build.py', 'w', encoding='utf-8') as f:
    f.write(new_code)

print("Patch applied to build.py successfully.")
