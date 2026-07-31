import os

filepath = "index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('fa-shield-check', 'fa-clipboard-check')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Icon fixed")
