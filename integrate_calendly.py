import re

ui_path = 'C:/Users/roopc/.gemini/antigravity/brain/c93a1649-f9d8-443c-9da6-d0a3b3a80bd0/scratch/rebuild_ui.py'
with open(ui_path, 'r', encoding='utf-8') as f:
    c = f.read()

# Replace header button
c = c.replace(
    '<a href="{prefix}contact.html" class="btn btn-gold desktop-only">Book Consultation</a>',
    '<a href="https://calendly.com/truvisory2026/30min" class="btn btn-gold desktop-only" target="_blank">Book Consultation</a>'
)

# Replace other book buttons
c = c.replace(
    '<a href="contact.html" class="btn btn-gold">Book a Free Business Consultation</a>',
    '<a href="https://calendly.com/truvisory2026/30min" class="btn btn-gold" target="_blank">Book a Free Business Consultation</a>'
)
c = c.replace(
    '<a href="contact.html" class="btn btn-gold">Book a Free Consultation</a>',
    '<a href="https://calendly.com/truvisory2026/30min" class="btn btn-gold" target="_blank">Book a Free Consultation</a>'
)
c = c.replace(
    '<a href="../contact.html" class="btn btn-gold">Book a Free Consultation &rarr;</a>',
    '<a href="https://calendly.com/truvisory2026/30min" class="btn btn-gold" target="_blank">Book a Free Consultation &rarr;</a>'
)
c = c.replace(
    '<a href="contact.html" class="btn btn-gold">Talk to Our Advisory Team</a>',
    '<a href="https://calendly.com/truvisory2026/30min" class="btn btn-gold" target="_blank">Talk to Our Advisory Team</a>'
)

# Embed Calendly in contact.html
contact_form_start = c.find('<div class="contact-form">')
contact_form_end = c.find('</div>\n      </div>\n    </div>\n  </section>\n</main>')

if contact_form_start != -1 and contact_form_end != -1:
    old_contact_block = c[contact_form_start:contact_form_end]
    
    calendly_embed = """<div class="contact-form" style="padding: 0; background: transparent; box-shadow: none;">
          <h2 class="mb-3 text-center">Schedule a Meeting</h2>
          <!-- Calendly inline widget begin -->
          <div class="calendly-inline-widget" data-url="https://calendly.com/truvisory2026/30min?hide_event_type_details=1&hide_gdpr_banner=1" style="min-width:320px;height:700px;"></div>
          <script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>
          <!-- Calendly inline widget end -->"""
          
    c = c[:contact_form_start] + calendly_embed + c[contact_form_end:]

with open(ui_path, 'w', encoding='utf-8') as f:
    f.write(c)

print("Calendly integrated.")
