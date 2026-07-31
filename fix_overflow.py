# -*- coding: utf-8 -*-
import glob
import re

# 1. Fix HTML: Reduce scale to 2.5 and margin to 120px
html_files = glob.glob('**/*.html', recursive=True)
for filepath in html_files:
    if 'node_modules' in filepath or 'venv' in filepath:
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    updated_content = re.sub(
        r'<img src="assets/images/logo\.png"[^>]+>',
        r'<img src="assets/images/logo.png" alt="Truvisory Logo" style="height: 100px; width: auto; transform: scale(2.6); transform-origin: left center; margin-right: 100px; object-fit: contain;">',
        content
    )
    
    if content != updated_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)

# 2. Fix CSS: Reduce gaps and font sizes so menu fits
css_path = 'assets/css/styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Decrease font size of nav links
css = re.sub(r'(\.nav-links a\s*\{[^\}]+?font-size:\s*)1\.1rem', r'\g<1>0.95rem', css)
# Decrease gap
css = re.sub(r'(\.nav-links\s*\{[^\}]+?gap:\s*)2\.5rem', r'\g<1>1.5rem', css)

# Decrease button padding in nav
if '.nav-actions .btn { font-size: 1.05rem; padding: 12px 24px; }' in css:
    css = css.replace('.nav-actions .btn { font-size: 1.05rem; padding: 12px 24px; }', 
                      '.nav-actions .btn { font-size: 0.95rem; padding: 10px 18px; }')
else:
    css = re.sub(r'(\.nav-actions \.btn\s*\{[^\}]+?padding:\s*)12px 24px', r'\g<1>10px 18px', css)
    css = re.sub(r'(\.nav-actions \.btn\s*\{[^\}]+?font-size:\s*)1\.05rem', r'\g<1>0.95rem', css)

# Ensure the overall nav container has no massive padding constraints that hide things
# Also, if .container has max-width, let's bump it up slightly for headers if possible? No, stick to grid.

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Compacted nav menu to ensure Book Consultation is visible.")
