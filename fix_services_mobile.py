import re

ui_path = 'C:/Users/roopc/.gemini/antigravity/brain/c93a1649-f9d8-443c-9da6-d0a3b3a80bd0/scratch/rebuild_ui.py'
with open(ui_path, 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the hardcoded inline grid style with the responsive class 'grid-3'
c = c.replace('<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px;">', '<div class="grid-3">')

with open(ui_path, 'w', encoding='utf-8') as f:
    f.write(c)

print("Fixed Services page mobile responsiveness.")
