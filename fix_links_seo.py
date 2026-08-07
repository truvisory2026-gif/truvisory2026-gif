import glob

# Fix links in seo-landing-pages/*.html
for filepath in glob.glob('seo-landing-pages/*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace('href="seo-landing-pages.html"', 'href="../seo-landing-pages.html"')
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Fixed links in SEO pages")
