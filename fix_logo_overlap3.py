# -*- coding: utf-8 -*-
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)
for filepath in html_files:
    if 'node_modules' in filepath or 'venv' in filepath:
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Make logo bigger (160px) and increase the gap to the right (margin-right: 120px)
    updated_content = re.sub(
        r'<img src="assets/images/logo\.png"[^>]+>',
        r'<img src="assets/images/logo.png" alt="Truvisory Logo" style="height: 160px; width: auto; margin-right: 120px; object-fit: contain;">',
        content
    )
    
    if content != updated_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)

print("Updated logo size and spacing again.")
