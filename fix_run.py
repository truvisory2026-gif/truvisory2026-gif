import os
import re

# Read template
with open('index.html', 'r', encoding='utf-8') as f:
    template_content = f.read()

# Extract header and footer
header_match = re.search(r'<header class="glass-nav".*?</header>', template_content, re.DOTALL)
footer_match = re.search(r'<footer class="mega-footer".*?</footer>', template_content, re.DOTALL)

if not header_match or not footer_match:
    print("Could not find header or footer in index.html")
    exit(1)

base_header = header_match.group(0)
base_footer = footer_match.group(0)

# Function to adjust relative paths for subdirectory files (e.g., adding ../)
def adjust_paths_for_subdir(html_chunk):
    # Adjust asset paths
    html_chunk = html_chunk.replace('"assets/', '"../assets/')
    # Adjust root html links (assuming they all sit in root)
    html_chunk = re.sub(r'href="([^/"]+\.html)(#[^"]*)?"', r'href="../\1\2"', html_chunk)
    # Fix the hash link for contact if it's currently href="#contact"
    html_chunk = html_chunk.replace('href="#contact"', 'href="../index.html#contact"')
    return html_chunk

header_subdir = adjust_paths_for_subdir(base_header)
footer_subdir = adjust_paths_for_subdir(base_footer)

with open('generate_phase1.py', 'r', encoding='utf-8') as f:
    code = f.read()

import ast
# We need to extract the 'pages' variable from the file.
# Easier to just replace the rendering logic in the file and re-run.
new_logic = '''
for page in pages:
    filepath = page['filepath']
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    html = html_template.replace('{title}', page['title'])
    html = html.replace('{meta}', page['meta'])
    html = html.replace('{breadcrumb}', page['breadcrumb'])
    html = html.replace('{hero_title}', page['hero_title'])
    html = html.replace('{hero_subtitle}', page['hero_subtitle'])
    html = html.replace('{content}', page['content'])
    html = html.replace('{header}', header_subdir)
    html = html.replace('{footer}', footer_subdir)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {filepath}")

print("Phase 1 Generation Complete.")
'''
code = code.split('for page in pages:')[0] + new_logic
with open('generate_phase1.py', 'w', encoding='utf-8') as f:
    f.write(code)

import subprocess
subprocess.run(["python", "generate_phase1.py"])
