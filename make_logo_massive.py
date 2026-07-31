import os

with open("assets/css/styles.css", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("height: 120px;", "height: 150px;")

with open("assets/css/styles.css", "w", encoding="utf-8") as f:
    f.write(content)

for dirpath, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith('.html'):
            filepath = os.path.join(dirpath, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            html_content = html_content.replace('style="height: 120px; transform: scale(1.5); transform-origin: left center;"', 'style="height: 150px; transform: scale(2.0); transform-origin: left center;"')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html_content)

print("CSS updated for even larger logo")
