import os

for dirpath, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith('.html'):
            filepath = os.path.join(dirpath, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            content = content.replace('style="height: 65px;', 'style="height: 100px; transform: scale(1.2); transform-origin: left center;"')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Logo made much larger")
