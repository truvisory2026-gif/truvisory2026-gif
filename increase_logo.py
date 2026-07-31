# -*- coding: utf-8 -*-
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)

for filepath in html_files:
    if 'node_modules' in filepath or 'venv' in filepath:
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Increase the logo height from 120px to 160px
    updated_content = re.sub(
        r'<img src="assets/images/logo\.png" alt="Truvisory Logo" style="height: 120px;',
        r'<img src="assets/images/logo.png" alt="Truvisory Logo" style="height: 160px;',
        content
    )
    
    if content != updated_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)

print("Increased logo height to 160px.")
