import os
import re

services = {
    "company-incorporation": {
        "title": "Company Incorporation",
        "description": "Expert assistance in setting up your business entity locally and globally.",
        "content": "Our Company Incorporation services streamline the legal and administrative complexities of starting a business. From choosing the right corporate structure (LLC, Corporation, Partnership) to registering with local authorities, we handle everything. We ensure that your business is built on a solid foundation, compliant with all regulations, and ready for growth."
    },
    "overseas-business-setup": {
        "title": "Overseas Business Setup",
        "description": "Expand your operations across international borders effortlessly.",
        "content": "Taking your business global is a major step. We provide end-to-end overseas business setup services in premier jurisdictions like the UAE, Singapore, Hong Kong, and the USA. We assist with entity selection, foreign ownership laws, local sponsorships, and cross-border banking setup."
    },
    "international-tax-planning": {
        "title": "International Tax Planning",
        "description": "Optimize your global tax structure while remaining fully compliant.",
        "content": "Navigating international tax laws requires deep expertise. Our tax planning services help multinational businesses minimize tax liabilities through strategic structuring, transfer pricing analysis, and leveraging double taxation avoidance agreements (DTAAs). We keep you compliant with OECD guidelines and local tax authorities."
    },
    "gst-vat": {
        "title": "GST & VAT Services",
        "description": "Comprehensive Indirect Tax Registration and Return Filing.",
        "content": "Whether it is GST in Singapore or VAT in the UAE, indirect taxes can severely impact cash flow if not managed correctly. We assist businesses with VAT/GST registration, accurate tax calculation, timely return filings, and compliance with constantly evolving indirect tax legislation."
    },
    "corporate-tax": {
        "title": "Corporate Tax",
        "description": "Strategic corporate tax advisory and compliance management.",
        "content": "We offer robust corporate tax services that go beyond mere compliance. We help you understand the implications of new tax regimes (like the UAE Corporate Tax), manage your tax provisions, file annual tax returns, and represent your firm during tax audits."
    },
    "accounting-bookkeeping": {
        "title": "Accounting & Bookkeeping",
        "description": "Accurate, timely, and compliant financial record keeping.",
        "content": "Outsource your financial tracking to our experts. We provide comprehensive accounting and bookkeeping services utilizing modern cloud-based software. From ledger maintenance and bank reconciliations to monthly financial reporting, we ensure your finances are always audit-ready."
    },
    "payroll": {
        "title": "Payroll Management",
        "description": "Seamless payroll processing and employee compliance.",
        "content": "Managing payroll across different jurisdictions involves complex labor laws and tax withholdings. Our payroll services ensure your employees are paid accurately and on time, while managing local statutory contributions, tax deductions, and year-end reporting."
    },
    "compliance-management": {
        "title": "Compliance Management",
        "description": "Stay ahead of regulatory changes and avoid penalties.",
        "content": "Regulatory non-compliance can lead to severe financial and reputational damage. We provide holistic compliance management services, including Economic Substance Regulations (ESR), Anti-Money Laundering (AML) reporting, and Ultimate Beneficial Owner (UBO) declarations."
    },
    "virtual-cfo": {
        "title": "Virtual CFO",
        "description": "Executive-level financial strategy without the full-time cost.",
        "content": "Scale your business with the strategic insights of a Chief Financial Officer. Our Virtual CFO services offer cash flow forecasting, budget management, financial modeling, KPI tracking, and board-level reporting to help you make informed, data-driven decisions."
    },
    "business-advisory": {
        "title": "Business Advisory",
        "description": "Strategic guidance to navigate challenges and accelerate growth.",
        "content": "From market entry strategies to mergers and acquisitions, our business advisory team provides actionable insights. We analyze market trends, assess operational inefficiencies, and develop comprehensive business plans tailored to your long-term objectives."
    },
    "franchise-expansion": {
        "title": "Franchise Expansion",
        "description": "Turn your successful business model into a global franchise.",
        "content": "Ready to franchise? We assist businesses in developing scalable franchise models, drafting franchise disclosure documents (FDD), establishing royalty structures, and protecting intellectual property across international borders."
    },
    "business-structuring": {
        "title": "Business Structuring",
        "description": "Optimal corporate structures for asset protection and efficiency.",
        "content": "The right corporate structure can protect your assets and enhance operational efficiency. We analyze your business goals and advise on the creation of holding companies, subsidiaries, and offshore entities to maximize legal protection and financial flexibility."
    }
}

template = '''<!DOCTYPE html>
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
<body>
    <!-- Header -->
    <header class="header">
        <div class="nav-container">
            <a href="../index.html" class="logo">
                <img src="../assets/images/logo.png" alt="Truvisory Logo" style="height: 65px; width: auto; object-fit: contain;">
            </a>
            <div class="menu-toggle"><i class="fa-solid fa-bars"></i></div>
            <nav class="nav-links">
                <a href="../index.html">Home</a>
                <a href="../about.html">About Us</a>
                <a href="../services.html">Services</a>
                <a href="../why-truvisory.html">Why Us</a>
                <a href="../testimonials.html">Testimonials</a>
                <a href="../contact.html">Contact Us</a>
            </nav>
            <a href="../contact.html" class="btn btn-primary" style="margin-left: auto;">Get Started</a>
        </div>
    </header>

    <!-- Page Header -->
    <section class="page-header" style="padding-top: 150px; text-align: center; margin-bottom: 50px;">
        <div class="container reveal">
            <h1 class="gradient-text">{title}</h1>
            <p style="color: var(--text-muted); font-size: 1.2rem; max-width: 800px; margin: 20px auto;">{description}</p>
        </div>
    </section>

    <!-- Main Content -->
    <section class="section" style="padding-top: 0;">
        <div class="container reveal">
            <div class="glass-card" style="padding: 40px; text-align: left; line-height: 1.8;">
                <h2 style="margin-bottom: 20px;">Overview</h2>
                <p style="color: var(--text-muted); font-size: 1.1rem; margin-bottom: 30px;">
                    {content}
                </p>
                <div class="cta-banner" style="margin-top: 40px; background: rgba(255, 255, 255, 0.05); padding: 30px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1); text-align: center;">
                    <h3 style="margin-bottom: 15px;">Ready to discuss {title}?</h3>
                    <p style="color: var(--text-muted); margin-bottom: 20px;">Contact our experts today for a customized consultation tailored to your specific business needs.</p>
                    <a href="../contact.html" class="btn btn-primary">Book a Free Consultation</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
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
</html>'''

os.makedirs('services', exist_ok=True)

for slug, data in services.items():
    html_content = template.format(
        title=data['title'],
        description=data['description'],
        content=data['content']
    )
    with open(f'services/{slug}.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

print("Generated 12 service pages successfully.")
