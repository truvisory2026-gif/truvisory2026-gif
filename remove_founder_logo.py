import re

ui_path = 'C:/Users/roopc/.gemini/antigravity/brain/c93a1649-f9d8-443c-9da6-d0a3b3a80bd0/scratch/rebuild_ui.py'
with open(ui_path, 'r', encoding='utf-8') as f:
    c = f.read()

# Remove the logo image for the founder in about_main
# I'll just replace the specific img tag with nothing
c = c.replace('<img src="assets/images/logo.png" style="width: 100%; height: 250px; object-fit: contain; padding: 20px; background: #fff;" alt="Nivya Jain">', '')

with open(ui_path, 'w', encoding='utf-8') as f:
    f.write(c)

print("Founder logo removed.")
