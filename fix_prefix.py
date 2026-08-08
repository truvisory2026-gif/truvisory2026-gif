import re

filepath = 'C:/Users/roopc/.gemini/antigravity/brain/c93a1649-f9d8-443c-9da6-d0a3b3a80bd0/scratch/rebuild_ui.py'
with open(filepath, 'r', encoding='utf-8') as f:
    c = f.read()

# Replace literal {prefix} for the images since the strings aren't f-strings in these blocks
c = c.replace('{prefix}assets/images/ind_', 'assets/images/ind_')
c = c.replace('{prefix}assets/images/country_', 'assets/images/country_')
c = c.replace('{prefix}assets/images/insight_', 'assets/images/insight_')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(c)

print("Fixed literal prefix tags.")
