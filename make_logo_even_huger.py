import os

with open("assets/css/styles.css", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("height: 80px;", "height: 120px;")

with open("assets/css/styles.css", "w", encoding="utf-8") as f:
    f.write(content)

for dirpath, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith('.html'):
            filepath = os.path.join(dirpath, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            html_content = html_content.replace('style="height: 100px; transform: scale(1.2); transform-origin: left center;"', 'style="height: 120px; transform: scale(1.5); transform-origin: left center;"')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html_content)

print("CSS updated for larger logo")
