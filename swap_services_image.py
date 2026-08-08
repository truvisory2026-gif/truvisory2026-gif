import re

ui_path = 'C:/Users/roopc/.gemini/antigravity/brain/c93a1649-f9d8-443c-9da6-d0a3b3a80bd0/scratch/rebuild_ui.py'
with open(ui_path, 'r', encoding='utf-8') as f:
    c = f.read()

# The services page is using ind_manufacturing_1786206358131.png
# Let's replace it with ind_it_saas_1786206333027.png
services_start = c.find('services_main =')
services_end = c.find('create_html(\'services.html\'', services_start)
services_section = c[services_start:services_end]
services_section = services_section.replace('assets/images/ind_manufacturing_1786206358131.png', 'assets/images/ind_it_saas_1786206333027.png', 1)
c = c[:services_start] + services_section + c[services_end:]

with open(ui_path, 'w', encoding='utf-8') as f:
    f.write(c)

print("Swapped services hero image.")
