# -*- coding: utf-8 -*-
import os
import re

css_path = 'assets/css/styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Increase font size of nav links
css = re.sub(r'(\.nav-links a\s*\{[^\}]+?font-size:\s*)0\.95rem', r'\g<1>1.1rem', css)

# Increase gap between nav links
css = re.sub(r'(\.nav-links\s*\{[^\}]+?gap:\s*)2rem', r'\g<1>2.5rem', css)

# Add nav-actions button scaling if not exists
if '.nav-actions .btn' not in css:
    css += "\n\n/* Enhanced Nav Buttons */\n.nav-actions .btn { font-size: 1.05rem; padding: 12px 24px; }\n"
else:
    css = re.sub(r'(\.nav-actions \.btn\s*\{)', r'\1 font-size: 1.05rem; padding: 12px 24px;', css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# Update logo scale in all HTML files
import glob

html_files = glob.glob('**/*.html', recursive=True)
for filepath in html_files:
    if 'node_modules' in filepath or 'venv' in filepath:
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find logo img tag and update scale/margin
    updated_content = re.sub(r'scale\(2\.0\)', r'scale(2.4)', content)
    updated_content = re.sub(r'margin-right:\s*120px', r'margin-right: 150px', updated_content)
    
    # Check if anything changed
    if content != updated_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)

print("Updated nav sizing and spacing.")
