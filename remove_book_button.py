# -*- coding: utf-8 -*-
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)

for filepath in html_files:
    if 'node_modules' in filepath or 'venv' in filepath:
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Remove the Book Consultation button from the header navigation
    updated_content = re.sub(
        r'<a href="(?:contact\.html|#contact)" class="btn btn-primary"[^>]*>Book Consultation</a>',
        r'',
        content
    )
    
    if content != updated_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)

print("Removed Book Consultation button from header navigation.")
