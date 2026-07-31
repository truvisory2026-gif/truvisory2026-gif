# -*- coding: utf-8 -*-
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)

# New header structure:
# Nav Links (left) + Nav Actions (left-ish) + auto-margin + Logo (extreme right)
new_header = '''  <header class="glass-nav" id="navbar">
    <div class="container nav-container" style="display: flex; justify-content: flex-start; align-items: center; width: 100%;">
      
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

      <!-- Center-Left: Buttons (right next to Nav Links) -->
      <div class="nav-actions" style="display: flex; gap: 15px; align-items: center; margin-left: 30px;">
        <a href="login.html" class="btn btn-outline" style="padding: 12px 24px; font-weight: 500; border-color: rgba(255,255,255,0.2);">Login / Sign Up</a>
        <a href="contact.html" class="btn btn-primary" style="padding: 12px 24px;">Book Consultation</a>
      </div>

      <!-- Extreme Right: Logo -->
      <!-- We use margin-left: auto to push it as far right as possible. -->
      <!-- We increase height significantly (200px) for visibility. -->
      <a href="index.html" class="logo" style="margin-left: auto; display: flex; align-items: center;">
        <img src="assets/images/logo.png" alt="Truvisory Logo" style="height: 180px; width: auto; object-fit: contain; transform: scale(1.3);">
      </a>
      
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

print("Applied exact extreme-right logo layout with increased logo dimensions.")
