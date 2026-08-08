import re
filepath = 'C:/Users/roopc/.gemini/antigravity/brain/c93a1649-f9d8-443c-9da6-d0a3b3a80bd0/scratch/rebuild_ui.py'
with open(filepath, 'r', encoding='utf-8') as f:
    c = f.read()
# Replace all unsplash links with picsum links
# To avoid browser caching all the same image, let's append a unique index
def repl(m):
    repl.counter += 1
    return f"https://picsum.photos/seed/truvisory{repl.counter}/800/500"
repl.counter = 0

c = re.sub(r'https://images\.unsplash\.com/photo-[^"]+', repl, c)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(c)
print("Replaced Unsplash links with Picsum links")
