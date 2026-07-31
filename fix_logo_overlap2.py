# -*- coding: utf-8 -*-
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)
for filepath in html_files:
    if 'node_modules' in filepath or 'venv' in filepath:
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Fix header logo: height 120px is large but safe, margin-right 80px pushes the Home button away safely.
    # The current code is: style="height: 220px; margin-right: 80px; object-fit: contain; margin-top: 10px; margin-bottom: 10px;"
    
    updated_content = re.sub(
        r'<img src="assets/images/logo\.png"[^>]+>',
        r'<img src="assets/images/logo.png" alt="Truvisory Logo" style="height: 130px; width: auto; margin-right: 80px; object-fit: contain;">',
        content
    )
    
    # Check if anything changed
    if content != updated_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)

print("Fixed logo layout overlap.")
