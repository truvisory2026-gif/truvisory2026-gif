import os
import re

root_nav = '''<nav class="nav-links">
        <a href="index.html">Home</a>
        <a href="about.html">About Us</a>
        <a href="services.html">Services</a>
        <a href="why-truvisory.html">Why Us</a>
        <a href="testimonials.html">Testimonials</a>
        <a href="contact.html">Contact Us</a>
      </nav>'''

sub_nav = '''<nav class="nav-links">
        <a href="../index.html">Home</a>
        <a href="../about.html">About Us</a>
        <a href="../services.html">Services</a>
        <a href="../why-truvisory.html">Why Us</a>
        <a href="../testimonials.html">Testimonials</a>
        <a href="../contact.html">Contact Us</a>
      </nav>'''

root_logo = '''<a href="index.html" class="logo">
        <img src="assets/images/logo.png" alt="Truvisory Logo" style="height: 40px; width: auto; object-fit: contain;">
      </a>'''

sub_logo = '''<a href="../index.html" class="logo">
        <img src="../assets/images/logo.png" alt="Truvisory Logo" style="height: 40px; width: auto; object-fit: contain;">
      </a>'''

for file in os.listdir('.'):
    if file.endswith('.html'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = re.sub(r'<nav class="nav-links">.*?</nav>', root_nav, content, flags=re.DOTALL)
        content = re.sub(r'<a href="index\.html" class="logo">.*?</a>', root_logo, content, flags=re.DOTALL)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

for d in ['countries', 'seo-landing-pages']:
    for file in os.listdir(d):
        if file.endswith('.html'):
            filepath = os.path.join(d, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            content = re.sub(r'<nav class="nav-links">.*?</nav>', sub_nav, content, flags=re.DOTALL)
            content = re.sub(r'<a href="\.\./index\.html" class="logo">.*?</a>', sub_logo, content, flags=re.DOTALL)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Update complete")
