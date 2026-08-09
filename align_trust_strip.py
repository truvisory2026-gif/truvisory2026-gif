import re

ui_path = r'C:\Users\roopc\.gemini\antigravity\brain\c93a1649-f9d8-443c-9da6-d0a3b3a80bd0\scratch\rebuild_ui.py'
with open(ui_path, 'r', encoding='utf-8') as f:
    ui = f.read()

# Replace the inline flex styles with the new class "trust-strip"
old_strip = r'class="container" style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; font-size: 0.875rem; color: var(--text-main); font-weight: 500;"'
new_strip = r'class="container trust-strip" style="font-size: 0.875rem; color: var(--text-main); font-weight: 500;"'
ui = ui.replace(old_strip, new_strip)

with open(ui_path, 'w', encoding='utf-8') as f:
    f.write(ui)

print("Updated rebuild_ui.py with trust-strip class.")

css_path = r'C:\Users\roopc\OneDrive\Desktop\truvisory\style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Add the new CSS rules for the trust strip
trust_strip_css = """
/* Trust Strip Formatting */
.trust-strip {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
}
@media (max-width: 768px) {
  .trust-strip {
    flex-direction: column;
    align-items: flex-start;
    gap: 16px;
  }
}
"""
if ".trust-strip" not in css:
    css += trust_strip_css

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css with mobile alignment for trust strip.")
