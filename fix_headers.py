import os

new_nav_links = '''<nav class="nav-links">
        <a href="{prefix}index.html">Home</a>
        <a href="{prefix}about.html">About Us</a>
        <a href="{prefix}services.html">Services</a>
        <a href="{prefix}countries.html">Countries</a>
        <a href="{prefix}industries.html">Industries</a>
        <a href="{prefix}resources.html">Resources</a>
        <a href="{prefix}why-truvisory.html">Why Us</a>
        <a href="{prefix}testimonials.html">Testimonials</a>
        <a href="{prefix}contact.html">Contact Us</a>
      </nav>'''

# 1. First, fix testimonials.html and why-truvisory.html headers manually
def replace_old_header(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<header class="navbar"' in content:
        # Need to replace it with glass-nav header
        start_idx = content.find('<header class="navbar"')
        end_idx = content.find('</header>') + 9
        
        glass_header = '''<header class="glass-nav" id="navbar">
    <div class="container nav-container">
      <a href="index.html" class="logo">
        <img src="assets/images/logo.png" alt="Truvisory Logo" style="height: 150px; transform: scale(2.0); transform-origin: left center;" width="auto" style="object-fit: contain;">
      </a>
      <div class="menu-toggle"><i class="fa-solid fa-bars"></i></div>
      <nav class="nav-links">
        <a href="index.html">Home</a>
        <a href="about.html">About Us</a>
        <a href="services.html">Services</a>
        <a href="countries.html">Countries</a>
        <a href="industries.html">Industries</a>
        <a href="resources.html">Resources</a>
        <a href="why-truvisory.html">Why Us</a>
        <a href="testimonials.html">Testimonials</a>
        <a href="contact.html">Contact Us</a>
      </nav>
      <div class="nav-actions">
        <a href="contact.html" class="btn btn-primary">Book Consultation</a>
      </div>
    </div>
  </header>'''
        
        content = content[:start_idx] + glass_header + content[end_idx:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

replace_old_header('testimonials.html')
replace_old_header('why-truvisory.html')

# 2. Update nav-links everywhere else
import re

for dirpath, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith('.html'):
            filepath = os.path.join(dirpath, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Determine if this file is in a subdirectory (like services/ or countries/)
            prefix = ""
            if dirpath != '.':
                depth = dirpath.count(os.sep)
                prefix = "../" * depth
            
            nav_html = new_nav_links.format(prefix=prefix)
            
            # Use regex to find and replace <nav class="nav-links">...</nav>
            new_content = re.sub(r'<nav class="nav-links">.*?</nav>', nav_html, content, flags=re.DOTALL)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)

print("Headers fixed and nav updated")
