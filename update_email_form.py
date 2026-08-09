import re

ui_path = r'C:\Users\roopc\.gemini\antigravity\brain\c93a1649-f9d8-443c-9da6-d0a3b3a80bd0\scratch\rebuild_ui.py'
with open(ui_path, 'r', encoding='utf-8') as f:
    ui = f.read()

# Replace all old email occurrences
ui = ui.replace('inquiries@truvisory.com', 'nivyajain@truvisoryfspl.com')
ui = ui.replace('info@truvisory.com', 'nivyajain@truvisoryfspl.com')

# Make the form functional
old_form_start = '<form style="display: flex; flex-direction: column; gap: 16px;">'
new_form_start = '<form action="https://formsubmit.co/nivyajain@truvisoryfspl.com" method="POST" style="display: flex; flex-direction: column; gap: 16px;">'

# Add name attributes to inputs
ui = ui.replace(old_form_start, new_form_start)
ui = ui.replace('<input type="text" placeholder="Full Name *"', '<input type="text" name="name" placeholder="Full Name *"')
ui = ui.replace('<input type="email" placeholder="Email Address *"', '<input type="email" name="email" placeholder="Email Address *"')
ui = ui.replace('<select style="', '<select name="country" style="')
ui = ui.replace('<textarea placeholder="Message / Requirements *"', '<textarea name="message" placeholder="Message / Requirements *"')

with open(ui_path, 'w', encoding='utf-8') as f:
    f.write(ui)

print("Email and form updated.")
