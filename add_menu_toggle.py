import os
import re

for dirpath, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith('.html'):
            filepath = os.path.join(dirpath, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if menu-toggle already exists
            if 'class="menu-toggle"' not in content:
                # Add the menu-toggle just before the nav-links
                content = re.sub(r'(<nav class="nav-links">)', r'<div class="menu-toggle"><i class="fa-solid fa-bars"></i></div>\n      \1', content)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

print("Menu toggle added to all files")
