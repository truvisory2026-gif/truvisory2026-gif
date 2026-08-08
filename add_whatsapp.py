import re

ui_path = 'C:/Users/roopc/.gemini/antigravity/brain/c93a1649-f9d8-443c-9da6-d0a3b3a80bd0/scratch/rebuild_ui.py'
with open(ui_path, 'r', encoding='utf-8') as f:
    c = f.read()

whatsapp_html = """
  <!-- WhatsApp Floating Button -->
  <a href="https://wa.me/919999999999" class="whatsapp-float" target="_blank" rel="noopener noreferrer">
    <i class="fa-brands fa-whatsapp"></i>
  </a>
  
  <script>"""

# We can replace the existing `<script>` that I added earlier for the mobile nav with `whatsapp_html` which includes `<script>`
c = c.replace('  <script>', whatsapp_html)

with open(ui_path, 'w', encoding='utf-8') as f:
    f.write(c)

css_path = 'C:/Users/roopc/OneDrive/Desktop/truvisory/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

whatsapp_css = """
/* WhatsApp Floating Button */
.whatsapp-float {
  position: fixed;
  width: 60px;
  height: 60px;
  bottom: 40px;
  right: 40px;
  background-color: #25d366;
  color: #FFF;
  border-radius: 50px;
  text-align: center;
  font-size: 30px;
  box-shadow: 2px 2px 3px #999;
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  text-decoration: none;
}

.whatsapp-float:hover {
  background-color: #128C7E;
  transform: translateY(-3px);
  color: #FFF;
}

@media (max-width: 768px) {
  .whatsapp-float {
    width: 50px;
    height: 50px;
    bottom: 20px;
    right: 20px;
    font-size: 26px;
  }
}
"""

if '/* WhatsApp Floating Button */' not in css:
    css += whatsapp_css
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)

print("WhatsApp button added.")
