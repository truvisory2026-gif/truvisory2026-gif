import os
import re

for dirpath, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith('.html'):
            filepath = os.path.join(dirpath, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # replace the inline style to add margin-right
            new_content = content.replace('style="height: 150px; transform: scale(2.0); transform-origin: left center;"', 'style="height: 150px; transform: scale(2.0); transform-origin: left center; margin-right: 120px;"')
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)

print("Added margin to fix overlap")
