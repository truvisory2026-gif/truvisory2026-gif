with open('seo-landing-pages.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('seo-landing-pages/dubai-company-registration.html', 'seo-landing-pages/company-registration-in-dubai.html')
content = content.replace('seo-landing-pages/uae-business-setup.html', 'seo-landing-pages/business-setup-in-uae.html')
content = content.replace('seo-landing-pages/uae-vat-registration.html', 'seo-landing-pages/vat-registration-uae.html')

with open('seo-landing-pages.html', 'w', encoding='utf-8') as f:
    f.write(content)
