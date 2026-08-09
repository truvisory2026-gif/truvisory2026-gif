import re

ui_path = r'C:\Users\roopc\.gemini\antigravity\brain\c93a1649-f9d8-443c-9da6-d0a3b3a80bd0\scratch\rebuild_ui.py'
with open(ui_path, 'r', encoding='utf-8') as f:
    ui = f.read()

index_html = """
<main>
  <!-- Hero Section -->
  <section class="hero">
    <div class="container hero-grid">
      <div class="hero-content">
        <h1>Helping Businesses Build, Grow &amp; Expand Beyond Borders</h1>
        <p>Truvisory Financial Services Pvt. Ltd. is a business consulting and financial advisory firm that helps entrepreneurs, startups, SMEs and established businesses set up, manage and grow with confidence. We bring incorporation, accounting, taxation, compliance, payroll and business advisory together under one roof, backed by a team of Chartered Accountants and experienced business professionals. From your first company registration to your expansion into international markets such as the UAE, Singapore, UK, Hong Kong and the USA, we work as a single, accountable partner rather than a fragmented set of vendors.<br><br>Founded in 2024, Truvisory is built on the belief that every business deserves advice that is honest, practical and genuinely suited to its goals.</p>
        <div class="hero-ctas">
          <a href="https://calendly.com/truvisory2026/30min" class="btn btn-gold" target="_blank">Book a Free Business Consultation</a>
          <a href="services.html" class="btn btn-outline">Explore Our Services</a>
        </div>
      </div>
      <div class="hero-image-container">
        <img src="assets/images/insight_blogs_1786206408849.png" alt="Global Expansion">
      </div>
    </div>
  </section>
  
  <!-- Trust & Credibility Strip -->
  <div style="background-color: var(--bg-white); padding: 16px 0; border-top: 1px solid var(--border-medium); border-bottom: 1px solid var(--border-medium);">
    <div class="container" style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; font-size: 0.875rem; color: var(--text-main); font-weight: 500;">
      <span><i class="fa-solid fa-check" style="color: var(--accent-gold); margin-right: 8px;"></i> Chartered Accountant-Led Advisory Team</span>
      <span><i class="fa-solid fa-check" style="color: var(--accent-gold); margin-right: 8px;"></i> Founded in 2024</span>
      <span><i class="fa-solid fa-check" style="color: var(--accent-gold); margin-right: 8px;"></i> Active Presence Across 6 Countries</span>
      <span><i class="fa-solid fa-check" style="color: var(--accent-gold); margin-right: 8px;"></i> End-to-End Support</span>
      <span><i class="fa-solid fa-check" style="color: var(--accent-gold); margin-right: 8px;"></i> Direct Access to Your Advisor</span>
    </div>
  </div>

  <!-- Countries We Serve -->
  <section class="section">
    <div class="container text-center mb-6">
      <h2 class="mb-2">Countries We Serve</h2>
      <p style="color: var(--text-muted); max-width: 800px; margin: 0 auto 24px;">India | UAE | Singapore | United Kingdom | Hong Kong | United States<br><br>Whether you are establishing a local business or planning global expansion, our advisors help you evaluate the right jurisdiction, understand regulatory requirements and ensure a smooth business setup process.</p>
      <a href="countries.html" class="btn btn-outline">Compare Jurisdictions &rarr;</a>
    </div>
  </section>

  <!-- Service Categories -->
  <section class="section section-white">
    <div class="container">
      <div class="text-center mb-6">
        <h2 class="mb-2">Service Categories</h2>
      </div>
      <div class="grid-3">
        <div class="service-card"><div class="card-icon"><i class="fa-solid fa-building"></i></div><h3>Business Setup</h3><p>Company incorporation in India and abroad, entity structuring, licensing.</p><a href="services.html" style="margin-top: 16px; font-weight: 600; font-size: 0.875rem;">Learn More &rarr;</a></div>
        <div class="service-card"><div class="card-icon"><i class="fa-solid fa-calculator"></i></div><h3>Accounting &amp; Bookkeeping</h3><p>Day-to-day financial record-keeping and MIS reporting.</p><a href="services.html" style="margin-top: 16px; font-weight: 600; font-size: 0.875rem;">Learn More &rarr;</a></div>
        <div class="service-card"><div class="card-icon"><i class="fa-solid fa-file-invoice"></i></div><h3>Taxation</h3><p>Direct tax, GST/VAT, international tax planning.</p><a href="services.html" style="margin-top: 16px; font-weight: 600; font-size: 0.875rem;">Learn More &rarr;</a></div>
        <div class="service-card"><div class="card-icon"><i class="fa-solid fa-clipboard-check"></i></div><h3>Compliance &amp; Payroll</h3><p>Statutory filings, ROC compliance, payroll processing.</p><a href="services.html" style="margin-top: 16px; font-weight: 600; font-size: 0.875rem;">Learn More &rarr;</a></div>
        <div class="service-card"><div class="card-icon"><i class="fa-solid fa-chart-line"></i></div><h3>Virtual CFO &amp; Business Advisory</h3><p>Strategic financial guidance without a full-time hire.</p><a href="services.html" style="margin-top: 16px; font-weight: 600; font-size: 0.875rem;">Learn More &rarr;</a></div>
        <div class="service-card"><div class="card-icon"><i class="fa-solid fa-file-contract"></i></div><h3>Trademark, Patent &amp; Legal Documentation</h3><p>Protecting your brand and intellectual property.</p><a href="services.html" style="margin-top: 16px; font-weight: 600; font-size: 0.875rem;">Learn More &rarr;</a></div>
        <div class="service-card"><div class="card-icon"><i class="fa-solid fa-rocket"></i></div><h3>Business Growth Solutions</h3><p>Branding, website development, SEO and digital marketing.</p><a href="services.html" style="margin-top: 16px; font-weight: 600; font-size: 0.875rem;">Learn More &rarr;</a></div>
      </div>
    </div>
  </section>
  
  <!-- Business Journey -->
  <section class="section" style="background-color: var(--bg-cream);">
    <div class="container mb-6">
      <h2 class="mb-3 text-center">Business Journey</h2>
      <p class="text-center" style="max-width: 800px; margin: 0 auto 32px; color: var(--text-muted);">A step-by-step timeline showing how Truvisory partners with a client from idea to expansion.</p>
      <div class="grid-2" style="max-width: 800px; margin: 0 auto;">
        <ul style="list-style: none; padding: 0;">
          <li style="margin-bottom: 24px;"><strong>1. Free Consultation</strong><br><span style="color: var(--text-muted);">Understanding your business goals and current stage</span></li>
          <li style="margin-bottom: 24px;"><strong>2. Planning &amp; Structuring</strong><br><span style="color: var(--text-muted);">Recommending the right entity type and jurisdiction</span></li>
          <li style="margin-bottom: 24px;"><strong>3. Documentation &amp; Incorporation</strong><br><span style="color: var(--text-muted);">Managing paperwork, filings and registrations</span></li>
        </ul>
        <ul style="list-style: none; padding: 0;">
          <li style="margin-bottom: 24px;"><strong>4. Banking &amp; Tax Setup</strong><br><span style="color: var(--text-muted);">Bank account facilitation and tax registrations</span></li>
          <li style="margin-bottom: 24px;"><strong>5. Ongoing Compliance &amp; Accounting</strong><br><span style="color: var(--text-muted);">Keeping the business audit-ready year-round</span></li>
          <li style="margin-bottom: 24px;"><strong>6. Growth &amp; Expansion</strong><br><span style="color: var(--text-muted);">Branding, digital presence and entry into new markets</span></li>
        </ul>
      </div>
    </div>
  </section>

  <!-- Why Truvisory & Why Choose Truvisory -->
  <section class="section section-white">
    <div class="container mb-6">
      <h2 class="mb-3 text-center">Why Truvisory</h2>
      <p class="text-center" style="max-width: 800px; margin: 0 auto 32px; color: var(--text-muted);">The name Truvisory is inspired by one simple belief — every business deserves true advisory.<br><br>We are committed to providing honest, transparent and practical guidance that helps entrepreneurs make informed business decisions. Rather than offering isolated services, we understand your business objectives and recommend integrated solutions that support long-term growth.<br><br>Whether you are launching your first startup, restructuring an existing business or expanding internationally, Truvisory becomes your long-term business partner.</p>
      
      <h3 class="mb-4 text-center" style="margin-top: 48px;">Why Choose Truvisory?</h3>
      <div class="grid-3" style="max-width: 1000px; margin: 0 auto;">
          <div class="service-card" style="box-shadow: 0 4px 12px rgba(0,0,0,0.05); padding: 24px;">
              <h4 style="margin-bottom: 8px;">End-to-End Business Solutions</h4>
              <p style="font-size: 0.875rem;">From incorporation and accounting to taxation, compliance, payroll, trademark, branding, website development and digital marketing, everything is available under one roof.</p>
          </div>
          <div class="service-card" style="box-shadow: 0 4px 12px rgba(0,0,0,0.05); padding: 24px;">
              <h4 style="margin-bottom: 8px;">Business Expansion Experts</h4>
              <p style="font-size: 0.875rem;">We assist businesses planning to establish operations across India, UAE, Singapore, UK, Hong Kong and the USA.</p>
          </div>
          <div class="service-card" style="box-shadow: 0 4px 12px rgba(0,0,0,0.05); padding: 24px;">
              <h4 style="margin-bottom: 8px;">Chartered Accountant-Led Team</h4>
              <p style="font-size: 0.875rem;">Our experienced professionals combine financial expertise with strategic business consulting.</p>
          </div>
          <div class="service-card" style="box-shadow: 0 4px 12px rgba(0,0,0,0.05); padding: 24px;">
              <h4 style="margin-bottom: 8px;">A Founder Who Understands Business, Not Just Numbers</h4>
              <p style="font-size: 0.875rem;">Truvisory was founded by Nivya Jain, who brings hands-on corporate marketing experience from her time with organisations including Thomas Cook and Citibank. That perspective shapes how we advise clients — with equal attention to compliance and to commercial growth.</p>
          </div>
          <div class="service-card" style="box-shadow: 0 4px 12px rgba(0,0,0,0.05); padding: 24px;">
              <h4 style="margin-bottom: 8px;">Client-First Approach</h4>
              <p style="font-size: 0.875rem;">Every recommendation is based on your business goals, not a one-size-fits-all approach.</p>
          </div>
          <div class="service-card" style="box-shadow: 0 4px 12px rgba(0,0,0,0.05); padding: 24px;">
              <h4 style="margin-bottom: 8px;">Long-Term Partnership</h4>
              <p style="font-size: 0.875rem;">We aim to build lasting relationships and become the trusted advisor businesses recommend to others.</p>
          </div>
      </div>
    </div>
  </section>

  <!-- Industries We Work With -->
  <section class="section" style="background-color: var(--bg-cream);">
    <div class="container text-center">
      <h2 class="mb-4">Industries We Work With</h2>
      <div style="display: flex; justify-content: center; gap: 16px; flex-wrap: wrap; font-weight: 500;">
        <span style="padding: 10px 20px; background-color: white; border: 1px solid var(--border-medium); border-radius: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">Startups</span>
        <span style="padding: 10px 20px; background-color: white; border: 1px solid var(--border-medium); border-radius: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">Manufacturing</span>
        <span style="padding: 10px 20px; background-color: white; border: 1px solid var(--border-medium); border-radius: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">Healthcare</span>
        <span style="padding: 10px 20px; background-color: white; border: 1px solid var(--border-medium); border-radius: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">IT &amp; SaaS</span>
        <span style="padding: 10px 20px; background-color: white; border: 1px solid var(--border-medium); border-radius: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">Import &amp; Export</span>
        <span style="padding: 10px 20px; background-color: white; border: 1px solid var(--border-medium); border-radius: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">Logistics</span>
        <span style="padding: 10px 20px; background-color: white; border: 1px solid var(--border-medium); border-radius: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">Retail &amp; E-commerce</span>
        <span style="padding: 10px 20px; background-color: white; border: 1px solid var(--border-medium); border-radius: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">Professional Services</span>
      </div>
    </div>
  </section>

  <!-- Success Stories -->
  <section class="section section-white">
    <div class="container mb-6">
      <h2 class="mb-4 text-center">Success Stories</h2>
      <div class="grid-3">
        <div class="service-card" style="box-shadow: 0 10px 30px rgba(0,0,0,0.05); padding: 32px;">
          <h3 class="mb-3">A Delhi-based D2C Brand Expands to the UAE</h3>
          <p>Truvisory managed company formation, VAT registration and initial compliance, enabling the brand to launch in Dubai within eight weeks.</p>
        </div>
        <div class="service-card" style="box-shadow: 0 10px 30px rgba(0,0,0,0.05); padding: 32px;">
          <h3 class="mb-3">A Bengaluru SaaS Startup Enters Singapore</h3>
          <p>We streamlined entity setup, nominee director requirements, and cross-border tax structuring so the founders could focus entirely on product growth.</p>
        </div>
        <div class="service-card" style="box-shadow: 0 10px 30px rgba(0,0,0,0.05); padding: 32px;">
          <h3 class="mb-3">A UK Consultancy Launches in India</h3>
          <p>Navigating FDI regulations and local compliances, Truvisory seamlessly established their wholly-owned subsidiary in Mumbai within record time.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Insights -->
  <section class="section" style="background-color: var(--bg-cream);">
    <div class="container text-center mb-6">
      <h2 class="mb-4">Insights &amp; Resources</h2>
      <div class="grid-3 text-left">
        <div class="service-card" style="padding: 24px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
          <h4 style="margin-bottom: 8px;">Choosing the Right Business Structure</h4>
          <p>A comprehensive guide to understanding Private Limited, LLP, and Sole Proprietorship.</p>
          <a href="insights.html" style="margin-top: 16px; font-weight: 600; font-size: 0.875rem;">Read More &rarr;</a>
        </div>
        <div class="service-card" style="padding: 24px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
          <h4 style="margin-bottom: 8px;">A Founder's Guide to UAE Expansion</h4>
          <p>Key considerations when deciding between Free Zone and Mainland setup.</p>
          <a href="insights.html" style="margin-top: 16px; font-weight: 600; font-size: 0.875rem;">Read More &rarr;</a>
        </div>
        <div class="service-card" style="padding: 24px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
          <h4 style="margin-bottom: 8px;">Corporate Tax and VAT Updates</h4>
          <p>Latest changes and mandatory compliance updates for businesses across jurisdictions.</p>
          <a href="insights.html" style="margin-top: 16px; font-weight: 600; font-size: 0.875rem;">Read More &rarr;</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Testimonials & FAQs -->
  <section class="section section-white">
    <div class="container mb-6 text-center">
      <h2 class="mb-4">Testimonials</h2>
      <div class="grid-2">
        <div class="service-card" style="box-shadow: 0 10px 30px rgba(0,0,0,0.05); padding: 40px;">
          <p style="font-size: 1.125rem; font-style: italic; color: var(--text-muted); margin-bottom: 24px;">"Truvisory completely removed the stress of incorporating our company in the UK. Their team was professional, transparent about costs, and guided us every step of the way."</p>
          <h4 style="margin-bottom: 4px;">Rahul Sharma</h4>
          <p style="font-size: 0.875rem; color: var(--text-light);">Founder &amp; CEO, Tech Innovations</p>
        </div>
        <div class="service-card" style="box-shadow: 0 10px 30px rgba(0,0,0,0.05); padding: 40px;">
          <p style="font-size: 1.125rem; font-style: italic; color: var(--text-muted); margin-bottom: 24px;">"Setting up in Dubai seemed daunting until we met Truvisory. They handled our mainland registration, licensing, and VAT setup with absolute efficiency."</p>
          <h4 style="margin-bottom: 4px;">Priya Menon</h4>
          <p style="font-size: 0.875rem; color: var(--text-light);">Director, Global Trade FZC</p>
        </div>
      </div>
    </div>

    <div class="container mb-6" style="margin-top: 60px;">
      <h2 class="mb-4 text-center">FAQs</h2>
      <div class="grid-2" style="max-width: 1000px; margin: 0 auto;">
          <div class="service-card" style="box-shadow: 0 4px 12px rgba(0,0,0,0.05); padding: 24px; text-align: left;">
              <h4 style="margin-bottom: 8px;">What services does Truvisory offer?</h4>
              <p>We provide end-to-end business setup, accounting, taxation, payroll, compliance, and growth solutions (like trademarking and digital marketing).</p>
          </div>
          <div class="service-card" style="box-shadow: 0 4px 12px rgba(0,0,0,0.05); padding: 24px; text-align: left;">
              <h4 style="margin-bottom: 8px;">Can Truvisory help me set up a business outside India?</h4>
              <p>Yes, we specialize in international expansion and business setup in the UAE, Singapore, United Kingdom, Hong Kong, and the United States.</p>
          </div>
          <div class="service-card" style="box-shadow: 0 4px 12px rgba(0,0,0,0.05); padding: 24px; text-align: left;">
              <h4 style="margin-bottom: 8px;">Do I need to visit your office, or can everything be done remotely?</h4>
              <p>Most of our services, including cross-border company incorporation, can be facilitated entirely remotely with digital documentation.</p>
          </div>
          <div class="service-card" style="box-shadow: 0 4px 12px rgba(0,0,0,0.05); padding: 24px; text-align: left;">
              <h4 style="margin-bottom: 8px;">How is Truvisory different from a regular CA firm?</h4>
              <p>We combine Chartered Accountant expertise with commercial growth advisory, acting as your single partner for everything from compliance to branding.</p>
          </div>
          <div class="service-card" style="box-shadow: 0 4px 12px rgba(0,0,0,0.05); padding: 24px; grid-column: 1 / -1; text-align: left;">
              <h4 style="margin-bottom: 8px;">How do I get started?</h4>
              <p>Simply book a free consultation through our Calendly link. We'll understand your goals and map out a practical action plan.</p>
          </div>
      </div>
    </div>
  </section>

  <!-- Final Call to Action -->
  <section class="section" style="background-color: var(--bg-cream); text-align: center;">
    <div class="container text-center">
      <h2 class="mb-3">Let's Build Your Business, Together.</h2>
      <p class="mb-4" style="color: var(--text-muted); max-width: 800px; margin: 0 auto 32px; font-size: 1.125rem;">From your first registration to your next international market — Truvisory is with you at every step.</p>
      <a href="https://calendly.com/truvisory2026/30min" class="btn btn-gold" target="_blank">Book a Free Business Consultation</a>
    </div>
  </section>
</main>
"""

# Replace index_main
ui = re.sub(r'index_main = """\n<main>.*?</main>\n"""', f'index_main = """\n{index_html}\n"""', ui, flags=re.DOTALL)

with open(ui_path, 'w', encoding='utf-8') as f:
    f.write(ui)

print("Home page errors removed and highly polished.")
