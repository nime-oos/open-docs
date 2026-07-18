import re

with open('build_v3.py', 'r', encoding='utf-8') as f:
    v3 = f.read()
with open('build.py', 'r', encoding='utf-8') as f:
    current = f.read()

def extract_block(code, start, end):
    s = code.find(start)
    e = code.find(end, s)
    if s == -1 or e == -1: return None
    return code[s:e]

v3_frappe = extract_block(v3, "frappe_sidebar_data = [", "# ==========================================\n# 2. PYTHON SITE DATA")
v3_python = extract_block(v3, "python_sidebar_data = [", "# ==========================================\n# 3. HTML GENERATOR")

if not v3_frappe or not v3_python:
    print("Could not extract from v3!")
    exit(1)

cur_frappe_start = current.find("frappe_sidebar_data = [")
cur_frappe_end = current.find("# ==========================================\n# 2. PYTHON SITE DATA")

current = current[:cur_frappe_start] + v3_frappe + current[cur_frappe_end:]

cur_python_start = current.find("python_sidebar_data = [")
cur_python_end = current.find("# ==========================================\n# 3. GIT SITE DATA")

current = current[:cur_python_start] + v3_python + current[cur_python_end:]

with open('build.py', 'w', encoding='utf-8') as f:
    f.write(current)
print("Restored successfully!")
