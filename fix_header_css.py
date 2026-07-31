# -*- coding: utf-8 -*-
css_path = 'assets/css/styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Make sure nav links are really large and spaced equally
import re
css = re.sub(r'(\.nav-links a\s*\{[^\}]+?font-size:\s*)1\.15rem', r'\g<1>1.25rem', css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS typography increased.")
