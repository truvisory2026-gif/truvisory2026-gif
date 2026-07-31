import re

service_map = {
    "Company Incorporation": "company-incorporation.html",
    "Overseas Business Setup": "overseas-business-setup.html",
    "International Tax Planning": "international-tax-planning.html",
    "GST & VAT": "gst-vat.html",
    "Corporate Tax": "corporate-tax.html",
    "Accounting & Bookkeeping": "accounting-bookkeeping.html",
    "Payroll": "payroll.html",
    "Compliance Management": "compliance-management.html",
    "Virtual CFO": "virtual-cfo.html",
    "Business Advisory": "business-advisory.html",
    "Franchise Expansion": "franchise-expansion.html",
    "Business Structuring": "business-structuring.html"
}

with open("services.html", "r", encoding="utf-8") as f:
    content = f.read()

for title, slug in service_map.items():
    old = f'<h3 class="card-title">{title}</h3>'
    new = f'<h3 class="card-title"><a href="services/{slug}" style="color: inherit; text-decoration: none;">{title}</a></h3>'
    content = content.replace(old, new)
    
    # Also fix it if there is &amp;
    if "&" in title:
        old_amp = f'<h3 class="card-title">{title.replace("&", "&amp;")}</h3>'
        new_amp = f'<h3 class="card-title"><a href="services/{slug}" style="color: inherit; text-decoration: none;">{title.replace("&", "&amp;")}</a></h3>'
        content = content.replace(old_amp, new_amp)

with open("services.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated services.html links")
