import os
import re

def slugify(text):
    text = text.lower().replace('&', 'and')
    return re.sub(r'[^a-z0-9]+', '-', text).strip('-')

pages = {
    # Careers
    "Our Culture": "careers/our-culture.html",
    "Employee Benefits": "careers/employee-benefits.html",
    "Open Positions": "careers/open-positions.html",
    "Recruitment Process": "careers/recruitment-process.html",
    "Internship Opportunities": "careers/internships.html",
    "Career FAQs": "careers/faqs.html",
    "Apply Now": "careers/apply.html",
    
    # Resources
    "Business Guides": "resources/business-guides.html",
    "Tax Calendar": "resources/tax-calendar.html",
    "Compliance Calendar": "resources/compliance-calendar.html",
    "Download Brochures": "resources/brochures.html",
    "Success Stories": "resources/success-stories.html",
    "Resource FAQs": "resources/faqs.html",
    
    # Industries
    "Financial Services": "industries/financial-services.html",
    "Healthcare": "industries/healthcare.html",
    "Real Estate": "industries/real-estate.html",
    "Technology": "industries/technology.html",
    "E-Commerce": "industries/e-commerce.html",
    "Manufacturing": "industries/manufacturing.html",
    "Energy": "industries/energy.html",
    "Hospitality": "industries/hospitality.html",
    "Logistics": "industries/logistics.html",
    "Retail": "industries/retail.html",
    "Aviation": "industries/aviation.html",
    "Education": "industries/education.html",
    "Agriculture": "industries/agriculture.html",
    "Media & Entertainment": "industries/media-and-entertainment.html",
    
    # Services
    "Company Incorporation": "services/company-incorporation.html",
    "Overseas Business Setup": "services/overseas-business-setup.html",
    "International Tax Planning": "services/international-tax-planning.html",
    "GST & VAT": "services/gst-and-vat.html",
    "Corporate Tax": "services/corporate-tax.html",
    "Accounting & Bookkeeping": "services/accounting-and-bookkeeping.html",
    "Payroll Services": "services/payroll-services.html",
    "Compliance Management": "services/compliance-management.html",
    "Virtual CFO": "services/virtual-cfo.html",
    "Business Advisory": "services/business-advisory.html",
    "Franchise Expansion": "services/franchise-expansion.html",
    "Business Structuring": "services/business-structuring.html",
    "Legal & Compliance": "services/legal-and-compliance.html"
}

html_files = []
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

for filepath in html_files:
    # Determine depth to compute relative path
    depth = filepath.count(os.sep) - 1 # because of './'
    if filepath.startswith('.\\'):
        depth = filepath.count('\\') - 1
        
    prefix = "../" * depth if depth > 0 else ""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original_content = content
    
    for name, path in pages.items():
        # The links are typically like <a href="#">Name</a>
        # Find all occurrences of href="#" or href="" before >Name<
        # We can use a regex to replace href="..." where the text is exactly `name`
        
        # Regex explanation:
        # href="[^"]*" matches href attribute
        # ([^>]*>) matches any other attributes and the closing >
        # \s* matches optional whitespace
        # re.escape(name) matches the exact name
        # \s*</a> matches the closing tag
        
        pattern = r'href="([^"]*)"([^>]*)>\s*' + re.escape(name) + r'\s*</a>'
        
        def replacer(match):
            old_href = match.group(1)
            other_attrs = match.group(2)
            # Only replace if old_href is '#' or '' or a wrong link
            # Or always replace to ensure correctness
            new_href = prefix + path
            return f'href="{new_href}"{other_attrs}>{name}</a>'
            
        content = re.sub(pattern, replacer, content, flags=re.IGNORECASE)
        
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated links in {filepath}")

print("Link fixing complete.")
