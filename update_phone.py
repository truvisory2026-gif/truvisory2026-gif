import re

ui_path = 'C:/Users/roopc/.gemini/antigravity/brain/c93a1649-f9d8-443c-9da6-d0a3b3a80bd0/scratch/rebuild_ui.py'
with open(ui_path, 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the WhatsApp placeholder
c = c.replace('919999999999', '919930426774')

with open(ui_path, 'w', encoding='utf-8') as f:
    f.write(c)

print("WhatsApp number updated.")
