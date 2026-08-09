import re

ui_path = r'C:\Users\roopc\.gemini\antigravity\brain\c93a1649-f9d8-443c-9da6-d0a3b3a80bd0\scratch\rebuild_ui.py'
with open(ui_path, 'r', encoding='utf-8') as f:
    ui = f.read()

# Target the exact string for the Trust Strip container
old_strip = r'<div class="container" style="display: flex; justify-content: center; gap: 24px; align-items: center; flex-wrap: wrap; font-size: 0.875rem; color: var(--text-main); font-weight: 500;">'
new_strip = r'<div class="container trust-strip-box" style="font-size: 0.875rem; color: var(--text-main); font-weight: 500;">'
ui = ui.replace(old_strip, new_strip)

with open(ui_path, 'w', encoding='utf-8') as f:
    f.write(ui)

css_path = r'C:\Users\roopc\OneDrive\Desktop\truvisory\style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Add CSS for .trust-strip-box
new_css = """
/* Trust Strip Box Formatting */
.trust-strip-box {
  display: flex;
  justify-content: center;
  gap: 24px;
  align-items: center;
  flex-wrap: wrap;
}
@media (max-width: 768px) {
  .trust-strip-box {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    background-color: #f8f9fa;
    border: 1px solid var(--border-medium);
    border-radius: 8px;
    padding: 16px;
    gap: 12px;
    width: 100%;
    box-sizing: border-box;
  }
  .trust-strip-box span {
    display: flex;
    align-items: flex-start; /* Ensure checkmark aligns with text if it wraps */
    width: 100%;
    border-bottom: 1px solid #eaeaea;
    padding-bottom: 8px;
    line-height: 1.4;
  }
  .trust-strip-box span:last-child {
    border-bottom: none;
    padding-bottom: 0;
  }
}
"""

if ".trust-strip-box" not in css:
    css += new_css
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)

print("Updated rebuild_ui.py and style.css.")
