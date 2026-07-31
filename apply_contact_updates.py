import os
import re

css_file = 'assets/css/styles.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Fix future-expansion visibility
css_content = re.sub(
    r'\.future-expansion\s*\{[^}]*\}',
    '.future-expansion {\n  margin: 3rem auto 0;\n  text-align: center;\n  padding: 1.5rem;\n  background: var(--glass-bg);\n  border: 1px solid var(--glass-border);\n  border-radius: 50px;\n  display: block;\n  max-width: fit-content;\n}',
    css_content
)
with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_content)
print("Updated styles.css")

html_files = []
for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Phone Numbers and WhatsApp links
    content = content.replace('wa.me/919876543210', 'wa.me/919930426774')
    content = content.replace('+91 98765 43210', '+91 99304 26774')
    content = content.replace('+919876543210', '+919930426774')

    # Update Contact Form (only in contact.html usually)
    if 'contact.html' in file_path or 'Inquiry Form' in content:
        # Update form tag
        content = content.replace('<form class="contact-form">', '<form class="contact-form" action="https://formsubmit.co/truvisoryfinance@gmail.com" method="POST">')
        # Add name attributes
        content = content.replace('<input type="text" placeholder="Your Name" required>', '<input type="text" name="name" placeholder="Your Name" required>')
        content = content.replace('<input type="email" placeholder="Your Email" required>', '<input type="email" name="email" placeholder="Your Email" required>')
        content = content.replace('<input type="tel" placeholder="Your Phone">', '<input type="tel" name="phone" placeholder="Your Phone">')
        content = content.replace('<textarea placeholder="How can we help you?" required></textarea>', '<textarea name="message" placeholder="How can we help you?" required></textarea>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
print("Updated all HTML files.")
