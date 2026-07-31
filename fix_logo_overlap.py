# -*- coding: utf-8 -*-
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)
for filepath in html_files:
    if 'node_modules' in filepath or 'venv' in filepath:
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the inline style on the logo with a safer layout-based sizing
    # It was: style="height: 150px; transform: scale(2.4); transform-origin: left center; margin-right: 150px;"
    # I will change it to just: style="height: 250px; margin-right: 60px;" and remove the scale transform entirely.
    
    updated_content = re.sub(
        r'<img src="assets/images/logo\.png"[^>]+>',
        r'<img src="assets/images/logo.png" alt="Truvisory Logo" style="height: 220px; margin-right: 80px; object-fit: contain; margin-top: 10px; margin-bottom: 10px;">',
        content
    )
    
    # Check if anything changed
    if content != updated_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)

print("Fixed logo overlapping.")
