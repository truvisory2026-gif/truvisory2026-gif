import re
import os

ui_path = 'C:/Users/roopc/.gemini/antigravity/brain/c93a1649-f9d8-443c-9da6-d0a3b3a80bd0/scratch/rebuild_ui.py'
with open(ui_path, 'r', encoding='utf-8') as f:
    c = f.read()

# Add mobile menu button to header
header_replace = """      <a href="{prefix}contact.html" class="btn btn-gold desktop-only">Book Consultation</a>
      <button class="mobile-menu-btn"><i class="fa-solid fa-bars"></i></button>"""
c = c.replace('<a href="{prefix}contact.html" class="btn btn-gold">Book Consultation</a>', header_replace)

# Add mobile nav drawer and script before </body>
mobile_nav = """
  <!-- Mobile Navigation Drawer -->
  <div class="mobile-nav" id="mobileNav">
    <div class="mobile-nav-header">
      <img src="{prefix}assets/images/logo.png" alt="Truvisory Services" style="height: 40px;">
      <button class="close-mobile-btn" id="closeBtn"><i class="fa-solid fa-xmark"></i></button>
    </div>
    <div class="mobile-nav-links">
        <a href="{prefix}index.html" class="{'active' if 'index.html' in filepath else ''}">Home</a>
        <a href="{prefix}about.html" class="{'active' if 'about.html' in filepath else ''}">About Us</a>
        <a href="{prefix}services.html" class="{'active' if 'services.html' in filepath else ''}">Services</a>
        <a href="{prefix}countries.html" class="{'active' if 'countries.html' in filepath else ''}">Countries</a>
        <a href="{prefix}industries.html" class="{'active' if 'industries.html' in filepath else ''}">Industries</a>
        <a href="{prefix}insights.html" class="{'active' if 'insights.html' in filepath else ''}">Insights</a>
        <a href="{prefix}success-stories.html" class="{'active' if 'success-stories.html' in filepath else ''}">Success Stories</a>
        <a href="{prefix}contact.html" class="{'active' if 'contact.html' in filepath else ''}">Contact</a>
        <a href="{prefix}seo-landing-pages.html" class="{'active' if 'seo-landing-pages.html' in filepath else ''}">SEO Landing Pages</a>
    </div>
  </div>
  
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const menuBtn = document.querySelector('.mobile-menu-btn');
      const closeBtn = document.getElementById('closeBtn');
      const mobileNav = document.getElementById('mobileNav');
      
      if (menuBtn && mobileNav && closeBtn) {
        menuBtn.addEventListener('click', () => {
          mobileNav.classList.add('active');
        });
        
        closeBtn.addEventListener('click', () => {
          mobileNav.classList.remove('active');
        });
      }
    });
  </script>
</body>"""
c = c.replace('</body>', mobile_nav)

# Fix Services image
# We know Services main starts with Services hero, and since both About and Services got mapped to ind_startups_1786206318113.png
# Let's target the exact one in services_main. 
services_start = c.find('services_main =')
services_end = c.find('create_html(\'services.html\'', services_start)
services_section = c[services_start:services_end]
services_section = services_section.replace('assets/images/ind_startups_1786206318113.png', 'assets/images/ind_manufacturing_1786206358131.png', 1)
c = c[:services_start] + services_section + c[services_end:]

with open(ui_path, 'w', encoding='utf-8') as f:
    f.write(c)

css_path = 'C:/Users/roopc/OneDrive/Desktop/truvisory/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

mobile_css = """

/* Mobile Navigation Styles */
.mobile-menu-btn {
  display: none;
  background: none;
  border: none;
  font-size: 1.5rem;
  color: var(--text-main);
  cursor: pointer;
}

.desktop-only {
  display: inline-block;
}

.mobile-nav {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  background-color: var(--bg-white);
  z-index: 1000;
  padding: 24px;
  transform: translateX(-100%);
  transition: transform 0.3s ease;
  overflow-y: auto;
}

.mobile-nav.active {
  transform: translateX(0);
}

.mobile-nav-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 32px;
}

.close-mobile-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  color: var(--text-main);
  cursor: pointer;
}

.mobile-nav-links {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.mobile-nav-links a {
  color: var(--text-main);
  font-weight: 500;
  font-size: 1.125rem;
  text-decoration: none;
  border-bottom: 1px solid var(--border-medium);
  padding-bottom: 12px;
}

.mobile-nav-links a.active {
  color: var(--accent-gold);
}

@media (max-width: 991px) {
  .desktop-nav, .desktop-only {
    display: none !important;
  }
  .mobile-menu-btn {
    display: block;
  }
}
"""

if '/* Mobile Navigation Styles */' not in css:
    css += mobile_css
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)

print("Mobile nav added and services image changed.")
