# -*- coding: utf-8 -*-
import glob
import re

# 1. Fix CSS
css_path = 'assets/css/styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Increase font size of nav links (from 0.95rem to 1.15rem)
css = re.sub(r'(\.nav-links a\s*\{[^\}]+?font-size:\s*)0\.95rem', r'\g<1>1.15rem', css)
# Increase gap
css = re.sub(r'(\.nav-links\s*\{[^\}]+?gap:\s*)1\.5rem', r'\g<1>2.2rem', css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Fix HTML Header Structure
html_files = glob.glob('**/*.html', recursive=True)

new_header = '''  <header class="glass-nav" id="navbar">
    <div class="container nav-container" style="display: flex; justify-content: space-between; align-items: center; width: 100%;">
      
      <!-- Left: Navigation Links -->
      <nav class="nav-links" style="display: flex; align-items: center;">
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

      <!-- Center-Right: Buttons -->
      <div class="nav-actions" style="display: flex; gap: 15px; align-items: center; margin-left: auto; margin-right: 40px;">
        <a href="login.html" class="btn btn-outline" style="padding: 10px 20px; font-weight: 500; border-color: rgba(255,255,255,0.2);">Login / Sign Up</a>
        <a href="contact.html" class="btn btn-primary">Book Consultation</a>
      </div>

      <!-- Far Right: Logo -->
      <a href="index.html" class="logo" style="margin-left: 0;">
        <img src="assets/images/logo.png" alt="Truvisory Logo" style="height: 120px; width: auto; object-fit: contain;">
      </a>
      
      <div class="menu-toggle"><i class="fa-solid fa-bars"></i></div>
    </div>
  </header>'''

for filepath in html_files:
    if 'node_modules' in filepath or 'venv' in filepath:
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the old header with the new one
    # Note: Regex to grab everything from <header class="glass-nav" to </header>
    updated_content = re.sub(r'<header class="glass-nav"[^>]*>.*?</header>', new_header, content, flags=re.DOTALL)
    
    # Check if the page is 'index.html' so we fix the Book Consultation hash link
    if 'index.html' in filepath:
        updated_content = updated_content.replace('href="contact.html" class="btn btn-primary"', 'href="#contact" class="btn btn-primary"')

    if content != updated_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)

print("Header restructured and resized successfully.")
