# -*- coding: utf-8 -*-
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)
for filepath in html_files:
    if 'node_modules' in filepath or 'venv' in filepath:
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # We will use transform to scale the logo up significantly to bypass transparent padding.
    # To prevent overlap, we add a very large margin-right (250px)
    updated_content = re.sub(
        r'<img src="assets/images/logo\.png"[^>]+>',
        r'<img src="assets/images/logo.png" alt="Truvisory Logo" style="height: 100px; width: auto; transform: scale(3.5); transform-origin: left center; margin-right: 250px; object-fit: contain;">',
        content
    )
    
    if content != updated_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)

print("Updated logo to use aggressive scaling.")
