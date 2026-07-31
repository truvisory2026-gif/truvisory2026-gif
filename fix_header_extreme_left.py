# -*- coding: utf-8 -*-
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)

# New header structure:
# Extreme Left: Logo -> Center/Right: Nav Links -> Far Right: Buttons
new_header = '''  <header class="glass-nav" id="navbar">
    <div class="container nav-container" style="display: flex; justify-content: space-between; align-items: center; width: 100%;">
      
      <!-- Extreme Left: Logo -->
      <a href="index.html" class="logo" style="display: flex; align-items: center; margin-right: 40px;">
        <img src="assets/images/logo.png" alt="Truvisory Logo" style="height: 180px; width: auto; object-fit: contain; transform: scale(1.3); transform-origin: left center;">
      </a>

      <!-- Center-Right: Navigation Links -->
      <nav class="nav-links" style="display: flex; align-items: center; margin-left: auto;">
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

      <!-- Far Right: Buttons -->
      <div class="nav-actions" style="display: flex; gap: 15px; align-items: center; margin-left: 40px;">
        <a href="login.html" class="btn btn-outline" style="padding: 12px 24px; font-weight: 500; border-color: rgba(255,255,255,0.2);">Login / Sign Up</a>
        <a href="contact.html" class="btn btn-primary" style="padding: 12px 24px;">Book Consultation</a>
      </div>
      
      <div class="menu-toggle" style="margin-left: 20px;"><i class="fa-solid fa-bars"></i></div>
    </div>
  </header>'''

for filepath in html_files:
    if 'node_modules' in filepath or 'venv' in filepath:
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    updated_content = re.sub(r'<header class="glass-nav"[^>]*>.*?</header>', new_header, content, flags=re.DOTALL)
    
    if 'index.html' in filepath:
        updated_content = updated_content.replace('href="contact.html" class="btn btn-primary"', 'href="#contact" class="btn btn-primary"')

    if content != updated_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)

print("Applied exact extreme-left logo layout.")
