import os
import re

for dirpath, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith('.html'):
            filepath = os.path.join(dirpath, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            content = content.replace('style="height: 40px;', 'style="height: 65px;')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Logo size updated")
