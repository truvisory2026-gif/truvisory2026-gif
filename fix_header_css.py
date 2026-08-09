import re

# Update rebuild_ui.py to use header-btn
ui_path = r'C:\Users\roopc\.gemini\antigravity\brain\c93a1649-f9d8-443c-9da6-d0a3b3a80bd0\scratch\rebuild_ui.py'
with open(ui_path, 'r', encoding='utf-8') as f:
    ui = f.read()

ui = ui.replace('class="btn btn-gold desktop-only"', 'class="header-btn desktop-only"')

with open(ui_path, 'w', encoding='utf-8') as f:
    f.write(ui)

# Update style.css
css_path = r'C:\Users\roopc\OneDrive\Desktop\truvisory\style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Make sure we don't duplicate .header-btn
if '.header-btn {' in css:
    css = re.sub(r'\.header-btn\s*\{[^}]*\}', '', css)

if '.desktop-nav {' in css:
    # Modify desktop-nav
    css = re.sub(r'\.desktop-nav\s*\{[^}]*\}', 
                 '.desktop-nav {\n  display: flex;\n  gap: 10px;\n  align-items: center;\n  flex-wrap: nowrap;\n}', css)

if '.desktop-nav a {' in css:
    # Modify desktop-nav a
    css = re.sub(r'\.desktop-nav a\s*\{[^}]*\}', 
                 '.desktop-nav a {\n  font-size: 12.5px;\n  color: var(--text-muted);\n  font-weight: 500;\n  position: relative;\n  padding-bottom: 4px;\n  white-space: nowrap;\n}', css)

header_btn_css = """
.header-btn {
  height: 34px;
  width: 125px;
  padding: 0 10px;
  border-radius: 5px;
  font-size: 11.5px;
  font-weight: 600;
  background-color: var(--accent-gold);
  color: #172033;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-left: auto;
  text-decoration: none;
  transition: background-color 0.3s;
  flex-shrink: 0;
  white-space: nowrap;
}
.header-btn:hover {
  background-color: var(--accent-gold-hover);
}
"""

css += header_btn_css

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS updated.")
