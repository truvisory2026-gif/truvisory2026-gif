# -*- coding: utf-8 -*-
import os

top_nav = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Truvisory Services</title>
    <link rel="stylesheet" href="../assets/css/styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body class="dark-theme">
    <!-- Header -->
    <header class="glass-nav" id="navbar">
        <div class="container nav-container">
            <a href="../index.html" class="logo">
                <img src="../assets/images/logo.png" alt="Truvisory Logo" style="height: 150px; transform: scale(2.0); transform-origin: left center; margin-right: 120px;" width="auto" style="object-fit: contain;">
            </a>
            <div class="menu-toggle"><i class="fa-solid fa-bars"></i></div>
            <nav class="nav-links">
                <a href="../index.html">Home</a>
                <a href="../about.html">About Us</a>
                <a href="../services.html">Services</a>
                <a href="../countries.html">Countries</a>
                <a href="../industries.html">Industries</a>
                <a href="../resources.html">Resources</a>
                <a href="../why-truvisory.html">Why Us</a>
                <a href="../testimonials.html">Testimonials</a>
                <a href="../contact.html">Contact Us</a>
            </nav>
            <div class="nav-actions">
                <a href="../contact.html" class="btn btn-primary">Book Consultation</a>
            </div>
        </div>
    </header>
'''

footer = '''    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 40px;">
                <div class="footer-about">
                    <a href="../index.html" class="logo" style="margin-bottom: 20px; display: block;">
                        <img src="../assets/images/logo.png" alt="Truvisory Logo" style="height: 50px; width: auto; object-fit: contain;">
                    </a>
                    <p style="color: var(--text-muted);">Your trusted partner for Global Business Setup and Advisory.</p>
                </div>
                <div class="footer-links">
                    <h4 style="color: white; margin-bottom: 20px;">Quick Links</h4>
                    <ul style="list-style: none;">
                        <li><a href="../about.html" style="color: var(--text-muted); text-decoration: none;">About Us</a></li>
                        <li><a href="../services.html" style="color: var(--text-muted); text-decoration: none;">Services</a></li>
                        <li><a href="../contact.html" style="color: var(--text-muted); text-decoration: none;">Contact Us</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom" style="margin-top: 40px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.1); text-align: center; color: var(--text-muted);">
                <p>&copy; 2026 Truvisory Financial Services. All rights reserved.</p>
            </div>
        </div>
    </footer>
    <script src="../assets/js/main.js"></script>
</body>
</html>
'''

pages_data = [
    {
        "filename": "company-incorporation.html",
        "title": "Company Incorporation",
        "hero_subtitle": "Start Your Business with Confidence.",
        "hero_desc": "We simplify the process of company registration and legal incorporation across multiple jurisdictions. Whether you're launching a startup, expanding internationally, or restructuring your business, Truvisory provides end-to-end incorporation services.",
        "overview": "Establishing a company involves much more than registering a name. Choosing the right legal structure, understanding regulatory obligations, obtaining tax registrations, and ensuring compliance are critical to building a successful business. Our experienced consultants manage the entire incorporation process while ensuring your business complies with local laws from day one.",
        "services": ["Private Limited Company Registration", "LLP Registration", "Sole Proprietorship", "Partnership Firm Registration", "Branch Office Registration", "Representative Office Setup", "Foreign Company Registration", "Government Approvals", "PAN & TAN Registration", "Digital Signature Certificates", "Business Licenses", "Startup Registration"],
        "why_choose_us": ["Fast Registration", "Legal Compliance", "Transparent Pricing", "Expert Consultation", "End-to-End Documentation", "Dedicated Relationship Manager"],
        "process": ["Consultation", "Documentation", "Registration", "Government Approval", "Tax Registration", "Business Ready"],
        "industries": ["IT", "Manufacturing", "Healthcare", "Retail", "Logistics", "Construction", "Education", "Hospitality"],
        "faq": {"How long does incorporation take?": "Typically 5-15 business days depending on the jurisdiction."}
    },
    {
        "filename": "overseas-business-setup.html",
        "title": "Overseas Business Setup",
        "hero_subtitle": "Expand Your Business Beyond Borders",
        "hero_desc": "Launch your business in global markets with complete support for incorporation, licensing, banking, taxation, and compliance.",
        "overview": "We Help You Set Up In: UAE, USA, UK, Singapore, Canada, Australia, Saudi Arabia, Oman, Qatar, Bahrain.",
        "services": ["Company Formation", "Trade License", "Corporate Bank Account Assistance", "Visa Assistance", "Tax Registration", "Accounting Setup", "Compliance", "Business License Renewals"],
        "why_choose_us": ["100% Foreign Ownership (where applicable)", "Tax Advantages", "International Banking", "Global Expansion", "Investment Opportunities"],
        "process": ["Market Consultation", "Country Selection", "Company Formation", "Licensing", "Bank Account", "Business Launch"],
        "industries": [],
        "faq": {}
    },
    {
        "filename": "international-tax-planning.html",
        "title": "International Tax Planning",
        "hero_subtitle": "Reduce Global Tax Risks with Smart Planning",
        "hero_desc": "International taxation requires strategic planning to minimize liabilities while maintaining compliance across multiple jurisdictions.",
        "overview": "",
        "services": ["Double Taxation Avoidance", "Transfer Pricing", "Cross-Border Tax Planning", "Permanent Establishment Advisory", "International Structuring", "Foreign Tax Credits", "Global Tax Compliance", "BEPS Advisory"],
        "why_choose_us": ["Reduce Tax Burden", "Prevent Double Taxation", "Regulatory Compliance", "Efficient Business Structures"],
        "process": [],
        "industries": [],
        "faq": {}
    },
    {
        "filename": "gst-vat.html",
        "title": "GST & VAT",
        "hero_subtitle": "Comprehensive GST & VAT Compliance",
        "hero_desc": "Our tax experts help businesses manage GST and VAT registrations, filings, audits, and advisory services efficiently.",
        "overview": "",
        "services": ["GST Registration", "VAT Registration", "GST Returns", "VAT Returns", "Input Tax Credit", "GST Audit Support", "GST Litigation", "Tax Planning"],
        "why_choose_us": [],
        "process": [],
        "industries": ["All Business Sectors"],
        "faq": {}
    },
    {
        "filename": "corporate-tax.html",
        "title": "Corporate Tax",
        "hero_subtitle": "Corporate Tax Solutions for Modern Businesses",
        "hero_desc": "We provide complete corporate tax planning, filing, assessments, and advisory services to help businesses remain compliant while optimizing tax efficiency.",
        "overview": "",
        "services": ["Corporate Tax Registration", "Tax Returns", "Advance Tax Planning", "Tax Assessments", "Appeals", "International Tax", "Corporate Restructuring", "Tax Advisory"],
        "why_choose_us": [],
        "process": [],
        "industries": [],
        "faq": {}
    },
    {
        "filename": "accounting-bookkeeping.html",
        "title": "Accounting & Bookkeeping",
        "hero_subtitle": "Accurate Financial Records. Better Business Decisions.",
        "hero_desc": "Professional bookkeeping and accounting services that keep your finances organized, compliant, and audit-ready.",
        "overview": "Software: QuickBooks, Xero, Zoho Books, Tally, Sage, ERP Systems.",
        "services": ["Daily Bookkeeping", "Financial Statements", "Bank Reconciliation", "Accounts Payable", "Accounts Receivable", "Inventory Accounting", "Fixed Asset Management", "MIS Reports"],
        "why_choose_us": [],
        "process": [],
        "industries": [],
        "faq": {}
    },
    {
        "filename": "payroll.html",
        "title": "Payroll",
        "hero_subtitle": "End-to-End Payroll Management",
        "hero_desc": "Automate payroll processing while ensuring complete compliance with labor laws and statutory regulations.",
        "overview": "",
        "services": ["Payroll Processing", "Salary Structure", "Payslips", "Employee Benefits", "Tax Deduction", "Leave Management", "HR Payroll Support", "Payroll Reports"],
        "why_choose_us": [],
        "process": [],
        "industries": [],
        "faq": {}
    },
    {
        "filename": "compliance-management.html",
        "title": "Compliance Management",
        "hero_subtitle": "Never Miss Another Compliance Deadline",
        "hero_desc": "Stay compliant with statutory regulations through proactive compliance management.",
        "overview": "",
        "services": ["Annual Compliance", "ROC Filings", "Secretarial Compliance", "Regulatory Reporting", "Compliance Calendar", "Licensing", "Corporate Governance", "Internal Compliance Reviews"],
        "why_choose_us": [],
        "process": [],
        "industries": [],
        "faq": {}
    },
    {
        "filename": "virtual-cfo.html",
        "title": "Virtual CFO",
        "hero_subtitle": "Executive Financial Leadership Without Full-Time Cost",
        "hero_desc": "Gain access to experienced CFOs who help drive strategic financial decisions, improve profitability, and support business growth.",
        "overview": "",
        "services": ["Financial Planning", "Budgeting", "Forecasting", "Investor Reporting", "Cash Flow Management", "Fundraising Support", "KPI Dashboard", "Strategic Advisory"],
        "why_choose_us": [],
        "process": [],
        "industries": [],
        "faq": {}
    },
    {
        "filename": "business-advisory.html",
        "title": "Business Advisory",
        "hero_subtitle": "Strategic Advice for Sustainable Growth",
        "hero_desc": "We work closely with entrepreneurs and organizations to identify opportunities, solve challenges, and build long-term success.",
        "overview": "",
        "services": ["Business Strategy", "Growth Planning", "Financial Analysis", "Risk Assessment", "Market Entry", "Digital Transformation", "Operational Excellence", "Performance Improvement"],
        "why_choose_us": [],
        "process": [],
        "industries": [],
        "faq": {}
    },
    {
        "filename": "franchise-expansion.html",
        "title": "Franchise Expansion",
        "hero_subtitle": "Expand Your Brand Through Franchising",
        "hero_desc": "Build scalable franchise systems that help your business grow into new markets while maintaining consistency and profitability.",
        "overview": "",
        "services": ["Franchise Model Development", "Franchise Documentation", "Financial Planning", "Territory Planning", "Franchise Recruitment", "Operations Manual", "Legal Agreements", "Expansion Strategy"],
        "why_choose_us": [],
        "process": [],
        "industries": [],
        "faq": {}
    },
    {
        "filename": "business-structuring.html",
        "title": "Business Structuring",
        "hero_subtitle": "Build the Right Business Structure for Long-Term Success",
        "hero_desc": "Choosing the right legal and operational structure can improve tax efficiency, protect assets, attract investors, and support sustainable growth.",
        "overview": "",
        "services": ["Business Restructuring", "Holding Company Structures", "Group Company Planning", "Family Business Structuring", "Investment Structuring", "Partnership Structuring", "Corporate Governance", "Exit Strategy Planning"],
        "why_choose_us": ["Improved Tax Efficiency", "Better Risk Management", "Enhanced Investor Confidence", "Easier Business Expansion", "Optimized Ownership Structure"],
        "process": [],
        "industries": [],
        "faq": {}
    }
]

def generate_page(data):
    html = top_nav.replace('{title}', data['title'])
    
    html += f'''
    <!-- Page Header -->
    <section class="page-header" style="padding-top: 150px; text-align: center; margin-bottom: 50px;">
        <div class="container reveal">
            <h1 class="gradient-text">{data['title']}</h1>
            <h3 style="color: white; margin-top: 10px;">{data['hero_subtitle']}</h3>
            <p style="color: var(--text-muted); font-size: 1.2rem; max-width: 800px; margin: 20px auto;">{data['hero_desc']}</p>
            <a href="../contact.html" class="btn btn-primary" style="margin-top: 20px;">Book Free Consultation</a>
        </div>
    </section>
    
    <main style="padding-bottom: 80px;">
        <div class="container">
'''
    
    if data['overview']:
        html += f'''
            <div class="glass-card reveal" style="padding: 40px; text-align: left; line-height: 1.8; margin-bottom: 40px;">
                <h2 style="margin-bottom: 20px; color: var(--primary);">Overview</h2>
                <p style="color: var(--text-muted); font-size: 1.1rem;">{data['overview']}</p>
            </div>
'''
            
    if data['services']:
        html += '''
            <h2 class="reveal" style="text-align: center; margin-bottom: 30px; margin-top: 50px;">Our Services</h2>
            <div class="grid-4 reveal" style="margin-bottom: 50px;">
'''
        for s in data['services']:
            html += f'''
                <div class="glass-card card-hover" style="text-align: center; padding: 20px;">
                    <div class="card-icon" style="margin-bottom: 10px;"><i class="fa-solid fa-check"></i></div>
                    <h4 class="card-title" style="font-size: 1.1rem;">{s}</h4>
                </div>
'''
        html += '</div>'

    if data['why_choose_us']:
        title = "Benefits" if data['title'] != 'Company Incorporation' else "Why Choose Truvisory"
        html += f'''
            <h2 class="reveal" style="text-align: center; margin-bottom: 30px; margin-top: 50px;">{title}</h2>
            <div class="grid-4 reveal" style="margin-bottom: 50px;">
'''
        for w in data['why_choose_us']:
            w = w.replace('✓ ', '')
            html += f'''
                <div class="glass-card card-hover" style="text-align: center; padding: 20px;">
                    <div class="card-icon" style="margin-bottom: 10px; color: var(--primary);"><i class="fa-solid fa-star"></i></div>
                    <h4 class="card-title" style="font-size: 1.1rem;">{w}</h4>
                </div>
'''
        html += '</div>'

    if data['industries']:
        html += '''
            <h2 class="reveal" style="text-align: center; margin-bottom: 30px; margin-top: 50px;">Industries We Serve</h2>
            <div class="grid-4 reveal" style="margin-bottom: 50px;">
'''
        for i in data['industries']:
            html += f'''
                <div class="glass-card card-hover" style="text-align: center; padding: 20px;">
                    <div class="card-icon" style="margin-bottom: 10px;"><i class="fa-solid fa-building"></i></div>
                    <h4 class="card-title" style="font-size: 1.1rem;">{i}</h4>
                </div>
'''
        html += '</div>'
        
    if data['process']:
        html += '''
            <h2 class="reveal" style="text-align: center; margin-bottom: 30px; margin-top: 50px;">Process</h2>
            <div class="reveal" style="display: flex; justify-content: center; align-items: center; gap: 15px; flex-wrap: wrap; margin-bottom: 50px;">
'''
        for idx, p in enumerate(data['process']):
            html += f'''
                <div class="glass-card" style="padding: 15px 25px; text-align: center; font-weight: bold;">{p}</div>
'''
            if idx < len(data['process']) - 1:
                html += '''<div style="color: var(--primary); font-size: 1.5rem;"><i class="fa-solid fa-arrow-right"></i></div>'''
        html += '</div>'

    if data['faq']:
        html += '''
            <h2 class="reveal" style="text-align: center; margin-bottom: 30px; margin-top: 50px;">FAQ</h2>
            <div class="reveal" style="max-width: 800px; margin: 0 auto; margin-bottom: 50px;">
'''
        for q, a in data['faq'].items():
            html += f'''
                <div class="glass-card" style="margin-bottom: 20px; padding: 20px;">
                    <h4 style="color: var(--primary); margin-bottom: 10px;">Q: {q}</h4>
                    <p style="color: var(--text-muted);">A: {a}</p>
                </div>
'''
        html += '</div>'

    html += '''
        </div>
    </main>
'''
    html += footer
    
    with open(f"services/{data['filename']}", 'w', encoding='utf-8') as f:
        f.write(html)

os.makedirs('services', exist_ok=True)
for pd in pages_data:
    generate_page(pd)

print("Generated all 12 service pages!")
