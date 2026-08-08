import os

ui_path = 'C:/Users/roopc/.gemini/antigravity/brain/c93a1649-f9d8-443c-9da6-d0a3b3a80bd0/scratch/rebuild_ui.py'
with open(ui_path, 'r', encoding='utf-8', errors='ignore') as f:
    ui_content = f.read()

# Fix encoding errors in seo text (specifically replacing the bad token ?)
ui_content = ui_content.replace('?', '—')
ui_content = ui_content.replace('?', '—')

with open(ui_path, 'w', encoding='utf-8') as f:
    f.write(ui_content)

css_path = 'C:/Users/roopc/OneDrive/Desktop/truvisory/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

css_content = css_content.replace('--text-main: #1F2937;', '--text-main: #000000;')
css_content = css_content.replace('--text-muted: #4B5563;', '--text-muted: #1a1a1a;')
css_content = css_content.replace('--text-light: #9CA3AF;', '--text-light: #4B5563;')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Fixed encodings and colors properly.")
