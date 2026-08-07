# -*- coding: utf-8 -*-
import os
import re

pages_data = [
    {
        "filename": "company-registration-in-dubai.html",
        "title": "Company Registration in Dubai | Truvisory Financial Services",
        "desc": "Register your company in Dubai with Truvisory. End-to-end support for Mainland and Free Zone incorporation, licensing and bank account setup.",
        "h1": "Company Registration in Dubai — Fast, Compliant, Fully Managed",
        "intro": "Setting up a company in Dubai involves choosing between Mainland and Free Zone jurisdictions, securing the right trade licence and completing visa and banking formalities. Truvisory manages the entire process end-to-end, so you can focus on launching, not paperwork."
    },
    {
        "filename": "business-setup-in-uae.html",
        "title": "Business Setup in UAE | Truvisory Financial Services",
        "desc": "Truvisory helps entrepreneurs set up businesses across the UAE — Mainland, Free Zone and Offshore — with full documentation and licensing support.",
        "h1": "Business Setup in the UAE Made Simple",
        "intro": "From choosing the right emirate and jurisdiction to securing licences and opening a corporate bank account, our advisors guide you through every stage of establishing your UAE business."
    },
    {
        "filename": "singapore-company-incorporation.html",
        "title": "Singapore Company Incorporation | Truvisory Financial Services",
        "desc": "Incorporate your company in Singapore with Truvisory. Fast Pte. Ltd. registration, nominee director support and first-year compliance.",
        "h1": "Singapore Company Incorporation — Done Right, Done Fast",
        "intro": "Singapore's pro-business environment makes it a top choice for international expansion. We handle incorporation, statutory compliance and nominee director arrangements so your Singapore entity is operational within days."
    },
    {
        "filename": "hong-kong-company-formation.html",
        "title": "Hong Kong Company Formation | Truvisory Financial Services",
        "desc": "Form your Hong Kong company with Truvisory — incorporation, company secretary services and compliance, fully managed.",
        "h1": "Hong Kong Company Formation for Global Businesses",
        "intro": "Hong Kong's simple tax regime and strategic access to China make it a preferred base for regional expansion. We manage incorporation, mandatory company secretary appointment and ongoing compliance."
    },
    {
        "filename": "usa-company-registration.html",
        "title": "USA Company Registration | Truvisory Financial Services",
        "desc": "Register your LLC or Corporation in the USA with Truvisory — state selection, EIN application and compliance support.",
        "h1": "USA Company Registration for Founders Worldwide",
        "intro": "Whether you're forming an LLC or a C-Corporation, choosing the right state and structure matters. Truvisory guides you through registration, EIN application and ongoing US compliance obligations."
    },
    {
        "filename": "vat-registration-uae.html",
        "title": "VAT Registration UAE | Truvisory Financial Services",
        "desc": "Get VAT-registered in the UAE with Truvisory's tax specialists — registration, filing and ongoing VAT compliance support.",
        "h1": "UAE VAT Registration & Compliance",
        "intro": "If your UAE business crosses the mandatory VAT threshold, timely registration and accurate filing are essential. Our tax team manages registration, return filing and VAT advisory to keep you compliant."
    },
    {
        "filename": "international-tax-planning.html",
        "title": "International Tax Planning | Truvisory Financial Services",
        "desc": "Plan your cross-border tax strategy with Truvisory — DTAA advisory, transfer pricing and multi-jurisdiction tax structuring.",
        "h1": "International Tax Planning for Growing Businesses",
        "intro": "Operating across borders brings tax complexity — from double taxation risk to transfer pricing rules. We help structure your affairs efficiently while staying compliant in every jurisdiction you operate in."
    },
    {
        "filename": "accounting-services.html",
        "title": "Accounting Services | Truvisory Financial Services",
        "desc": "Outsource your accounting and bookkeeping to Truvisory — accurate, timely and always audit-ready.",
        "h1": "Professional Accounting & Bookkeeping Services",
        "intro": "Reliable financials are the backbone of every good business decision. Our accounting team manages your books on cloud platforms, so you always have an accurate, real-time view of your finances."
    },
    {
        "filename": "compliance-services.html",
        "title": "Compliance Services | Truvisory Financial Services",
        "desc": "Stay fully compliant with Truvisory's compliance management services — ROC filings, statutory audits, FEMA and more.",
        "h1": "End-to-End Compliance Management Services",
        "intro": "Missed statutory deadlines can mean penalties and reputational risk. We manage your full compliance calendar — ROC filings, audits, secretarial compliance and cross-border regulatory requirements — so nothing slips through."
    }
]

def generate_full_pages():
    with open('index.html', 'r', encoding='utf-8') as f:
        template = f.read()

    parts = template.split('<section class="hero')
    header_part = parts[0]
    rest_of_page = '<section class="why-truvisory' + parts[1].split('<section class="why-truvisory')[1]

    header_part = header_part.replace('href="assets/', 'href="../assets/')
    header_part = header_part.replace('href="style.css"', 'href="../style.css"')
    header_part = header_part.replace('src="assets/', 'src="../assets/')
    header_part = header_part.replace('href="index.html"', 'href="../index.html"')
    header_part = header_part.replace('href="about.html"', 'href="../about.html"')
    header_part = header_part.replace('href="services.html"', 'href="../services.html"')
    header_part = header_part.replace('href="countries.html"', 'href="../countries.html"')
    header_part = header_part.replace('href="industries.html"', 'href="../industries.html"')
    header_part = header_part.replace('href="resources.html"', 'href="../resources.html"')
    header_part = header_part.replace('href="testimonials.html"', 'href="../testimonials.html"')
    header_part = header_part.replace('href="contact.html"', 'href="../contact.html"')
    header_part = header_part.replace('href="seo-landing-pages.html"', 'href="../seo-landing-pages.html"')

    rest_of_page = rest_of_page.replace('href="assets/', 'href="../assets/')
    rest_of_page = rest_of_page.replace('src="assets/', 'src="../assets/')
    rest_of_page = rest_of_page.replace('href="index.html"', 'href="../index.html"')
    rest_of_page = rest_of_page.replace('href="about.html"', 'href="../about.html"')
    rest_of_page = rest_of_page.replace('href="services.html"', 'href="../services.html"')
    rest_of_page = rest_of_page.replace('href="countries.html"', 'href="../countries.html"')
    rest_of_page = rest_of_page.replace('href="contact.html"', 'href="../contact.html"')
    rest_of_page = rest_of_page.replace('src="script.js"', 'src="../script.js"')

    os.makedirs('seo-landing-pages', exist_ok=True)
    
    for page in pages_data:
        custom_header = re.sub(r'<title>.*?</title>', f'<title>{page["title"]}</title>', header_part, flags=re.DOTALL)
        if '<meta name="description"' in custom_header:
            custom_header = re.sub(r'<meta name="description".*?>', f'<meta name="description" content="{page["desc"]}">', custom_header)
        else:
            custom_header = custom_header.replace('<title>', f'<meta name="description" content="{page["desc"]}">\n  <title>')
            
        hero_section = f'''
  <section class="hero section-white" style="padding-top: 150px; padding-bottom: 80px;">
    <div class="container text-center">
      <h1 class="main-title text-navy">{page['h1']}</h1>
      <p class="mb-5 max-w-700 mx-auto" style="font-size: 1.1rem; line-height: 1.8;">{page['intro']}</p>
      <a href="../contact.html" class="btn btn-primary">Book a Free Consultation &rarr;</a>
    </div>
  </section>
'''
        full_html = custom_header + hero_section + rest_of_page
        
        with open(os.path.join('seo-landing-pages', page["filename"]), 'w', encoding='utf-8') as f:
            f.write(full_html)
            
    print("SEO Full Pages Generated.")

generate_full_pages()
