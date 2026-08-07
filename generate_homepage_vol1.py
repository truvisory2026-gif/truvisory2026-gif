import re

def update_index_html():
    file_path = 'c:\\Users\\roopc\\OneDrive\\Desktop\\truvisory\\index.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the end of the mobile drawer (which is just before Section 1)
    # Looking for: <!-- 01. Hero Section -->
    header_end_idx = content.find('<!-- 01. Hero Section -->')
    if header_end_idx == -1:
        print("Could not find start of Hero Section")
        return
        
    # Find the start of the Floating UI
    # Looking for: <!-- Floating UI -->
    footer_end_idx = content.find('<!-- Floating UI -->')
    if footer_end_idx == -1:
        print("Could not find start of Floating UI")
        return

    header_part = content[:header_end_idx]
    footer_part = content[footer_end_idx:]

    new_content = """
  <!-- Section 1 - Hero Banner -->
  <section class="hero section-white" id="home">
    <div class="container">
      <div class="grid hero-grid">
        <div class="hero-content fade-up">
          <div class="badge-chip">Trusted Financial Advisory • Strategic Growth Partners</div>
          <h1 class="main-title text-navy">Comprehensive financial strategy, tax compliance, and growth advisory for modern businesses.</h1>
          <p class="hero-subtext">Corporate structuring, tax compliance, or strategic CFO advisory — we handle it end to end. Build your business on solid foundations with our expert team.</p>
          <div class="hero-ctas mt-4">
            <a href="#schedule" class="btn btn-primary cta-btn mr-3">Schedule a Strategy Call</a>
            <a href="#services" class="btn btn-outline cta-btn">Explore Our Solutions</a>
          </div>
          <div class="trust-indicators mt-4">
            <span class="trust-item">✓ 500+ Clients Guided</span>
            <span class="trust-item">✓ 15+ Years Expertise</span>
            <span class="trust-item">✓ 100% Statutory Compliance</span>
          </div>
          <!-- Developer Note: Placeholders for Hero Visual and Trust Indicators are included above and below -->
        </div>
        <div class="hero-visual fade-left">
          <img src="https://placehold.co/600x400/F8FAFC/0F172A?text=Corporate+Growth+Visual" alt="Corporate Growth and Financial Advisory Visual" class="hero-image">
        </div>
      </div>
    </div>
  </section>

  <!-- Section 2 - Why Truvisory Exists -->
  <section class="why-truvisory section-light section-padding" id="why-truvisory">
    <div class="container">
      <div class="grid grid-2-col align-center">
        <div class="story-content fade-up">
          <h2 class="section-title">Why Truvisory Exists</h2>
          <h3 class="mb-3">The Truvisory Story</h3>
          <p class="mb-3">We saw a gap in the market where ambitious businesses were held back by fragmented advisory services. Truvisory was founded to provide a cohesive, end-to-end financial partnership.</p>
          <h3 class="mb-3 mt-4">Why the Name "Truvisory"?</h3>
          <p class="mb-3">Our name is a blend of <strong>True</strong> and <strong>Advisory</strong>. It reflects our commitment to transparent, honest, and impactful guidance.</p>
          <h3 class="mb-3 mt-4">Our Brand Philosophy</h3>
          <p>We believe that sound financial strategy should act as an accelerator for growth, not just a compliance checkbox.</p>
        </div>
        <div class="quote-box-container fade-left">
          <div class="quote-box">
            <div class="quote-icon">"</div>
            <p class="quote-text">Our mission is to simplify complex financial landscapes so that founders can focus on what they do best: building great companies.</p>
            <p class="quote-author">- The Truvisory Team</p>
          </div>
          <!-- Developer Note: Added Quote Box as requested -->
        </div>
      </div>
    </div>
  </section>

  <!-- Section 3 - Your Business Journey -->
  <section class="business-journey section-white section-padding" id="journey">
    <div class="container">
      <h2 class="section-title text-center fade-up">Your Business Journey</h2>
      <p class="text-center mb-4 max-w-700 mx-auto fade-up">From an initial idea to global expansion, Truvisory partners with you at every stage of your business lifecycle.</p>
      
      <div class="timeline-container mt-4">
        <div class="timeline">
          <!-- Timeline Items -->
          <div class="timeline-item left fade-up">
            <div class="timeline-content">
              <h3>1. Business Idea & Planning</h3>
              <p>Structuring the right entity and validating financial models before launch.</p>
            </div>
          </div>
          <div class="timeline-item right fade-up">
            <div class="timeline-content">
              <h3>2. Company Incorporation</h3>
              <p>Seamless registration of your Pvt Ltd, LLP, or foreign subsidiary.</p>
            </div>
          </div>
          <div class="timeline-item left fade-up">
            <div class="timeline-content">
              <h3>3. Accounting & Taxation</h3>
              <p>Establishing robust bookkeeping and tax compliance frameworks.</p>
            </div>
          </div>
          <div class="timeline-item right fade-up">
            <div class="timeline-content">
              <h3>4. Payroll & Compliance</h3>
              <p>Managing employee taxation, PF, and statutory labor filings.</p>
            </div>
          </div>
          <div class="timeline-item left fade-up">
            <div class="timeline-content">
              <h3>5. Trademark & Legal</h3>
              <p>Protecting your intellectual property and establishing legal contracts.</p>
            </div>
          </div>
          <div class="timeline-item right fade-up">
            <div class="timeline-content">
              <h3>6. Branding & Digital Presence</h3>
              <p>Aligning your corporate identity with your growth ambitions.</p>
            </div>
          </div>
          <div class="timeline-item left fade-up">
            <div class="timeline-content">
              <h3>7. Business Expansion</h3>
              <p>Scaling operations across borders with strategic entry plans.</p>
            </div>
          </div>
          <div class="timeline-item right fade-up">
            <div class="timeline-content">
              <h3>8. Long-Term Advisory</h3>
              <p>Fractional CFO services for fundraising, M&A, and exit strategies.</p>
            </div>
          </div>
        </div>
      </div>
      <p class="text-center mt-4 font-weight-500 fade-up">Wherever you are on this journey, we have a solution to propel you forward.</p>
    </div>
  </section>

  <!-- Section 4 - Countries We Serve -->
  <section class="countries section-dark section-padding text-center" id="countries">
    <div class="container">
      <h2 class="section-title text-white fade-up">Global Presence</h2>
      <p class="text-white mb-4 max-w-700 mx-auto fade-up">We help businesses establish and scale their operations across key global markets.</p>
      
      <div class="grid grid-3-col mt-4">
        <div class="country-card fade-up">
          <div class="flag-icon">🇮🇳</div>
          <h3>India</h3>
          <p>Complete entry and compliance for the Indian market.</p>
        </div>
        <div class="country-card fade-up">
          <div class="flag-icon">🇦🇪</div>
          <h3>UAE</h3>
          <p>Setup in Dubai Free Zones and Mainland.</p>
        </div>
        <div class="country-card fade-up">
          <div class="flag-icon">🇸🇬</div>
          <h3>Singapore</h3>
          <p>Gateway to Southeast Asian expansion.</p>
        </div>
        <div class="country-card fade-up">
          <div class="flag-icon">🇬🇧</div>
          <h3>UK</h3>
          <p>Strategic European market entry.</p>
        </div>
        <div class="country-card fade-up">
          <div class="flag-icon">🇭🇰</div>
          <h3>Hong Kong</h3>
          <p>Premier financial hub structuring.</p>
        </div>
        <div class="country-card fade-up">
          <div class="flag-icon">🇺🇸</div>
          <h3>USA</h3>
          <p>Delaware C-Corp setups and compliance.</p>
        </div>
      </div>
      <a href="countries.html" class="btn btn-primary mt-4 fade-up">Explore Our Global Reach</a>
    </div>
  </section>

  <!-- Section 5 - Complete Business Solutions -->
  <section class="services section-light section-padding" id="services">
    <div class="container">
      <h2 class="section-title text-center fade-up">Complete Business Solutions</h2>
      
      <div class="grid grid-4-col mt-4">
        <!-- Service Cards -->
        <div class="service-card fade-up">
          <div class="service-icon">🏢</div>
          <h4>Business Setup</h4>
          <p>Entity formation, licensing, and registrations.</p>
          <a href="services.html#setup" class="link-teal mt-2 d-block">Learn More &rarr;</a>
        </div>
        <div class="service-card fade-up">
          <div class="service-icon">📊</div>
          <h4>Accounting & Bookkeeping</h4>
          <p>Accurate financial records and MIS reporting.</p>
          <a href="services.html#accounting" class="link-teal mt-2 d-block">Learn More &rarr;</a>
        </div>
        <div class="service-card fade-up">
          <div class="service-icon">💰</div>
          <h4>Taxation</h4>
          <p>GST, Direct Tax, and international tax advisory.</p>
          <a href="services.html#tax" class="link-teal mt-2 d-block">Learn More &rarr;</a>
        </div>
        <div class="service-card fade-up">
          <div class="service-icon">👥</div>
          <h4>Payroll</h4>
          <p>End-to-end employee payroll and PF management.</p>
          <a href="services.html#payroll" class="link-teal mt-2 d-block">Learn More &rarr;</a>
        </div>
        <div class="service-card fade-up">
          <div class="service-icon">📜</div>
          <h4>Compliance</h4>
          <p>Annual ROC filings, FEMA, and secretarial services.</p>
          <a href="services.html#compliance" class="link-teal mt-2 d-block">Learn More &rarr;</a>
        </div>
        <div class="service-card fade-up">
          <div class="service-icon">™️</div>
          <h4>Trademark</h4>
          <p>Brand protection and intellectual property registration.</p>
          <a href="services.html#trademark" class="link-teal mt-2 d-block">Learn More &rarr;</a>
        </div>
        <div class="service-card fade-up">
          <div class="service-icon">💡</div>
          <h4>Patent</h4>
          <p>Securing your innovations and unique methodologies.</p>
          <a href="services.html#patent" class="link-teal mt-2 d-block">Learn More &rarr;</a>
        </div>
        <div class="service-card fade-up">
          <div class="service-icon">🤝</div>
          <h4>Business Advisory</h4>
          <p>Strategic consulting for scaling and restructuring.</p>
          <a href="services.html#advisory" class="link-teal mt-2 d-block">Learn More &rarr;</a>
        </div>
        <div class="service-card fade-up">
          <div class="service-icon">📈</div>
          <h4>Virtual CFO</h4>
          <p>Expert financial leadership without the full-time cost.</p>
          <a href="services.html#cfo" class="link-teal mt-2 d-block">Learn More &rarr;</a>
        </div>
        <div class="service-card fade-up">
          <div class="service-icon">🚀</div>
          <h4>Business Growth Solutions</h4>
          <p>Fundraising readiness, valuations, and M&A support.</p>
          <a href="services.html#growth" class="link-teal mt-2 d-block">Learn More &rarr;</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 6 - Why Choose Truvisory -->
  <section class="why-choose section-white section-padding" id="why-choose">
    <div class="container">
      <h2 class="section-title text-center fade-up">Why Choose Truvisory</h2>
      
      <div class="grid grid-3-col mt-4">
        <div class="card fade-up">
          <div class="card-icon text-teal">🎯</div>
          <h4 class="card-title">Key Differentiators</h4>
          <p>We combine deep regulatory expertise with modern technology to deliver faster, more accurate results.</p>
        </div>
        <div class="card fade-up">
          <div class="card-icon text-teal">🤝</div>
          <h4 class="card-title">Why Clients Trust Us</h4>
          <p>A proven track record of maintaining 100% compliance for over 500+ growing enterprises globally.</p>
        </div>
        <div class="card fade-up">
          <div class="card-icon text-teal">💎</div>
          <h4 class="card-title">Value Proposition</h4>
          <p>A single point of contact for all your financial, legal, and compliance needs, saving you time and money.</p>
        </div>
      </div>
      <div class="text-center mt-4">
        <a href="about.html" class="btn btn-outline fade-up">Discover Our Approach</a>
      </div>
    </div>
  </section>

  <!-- Section 7 - Industries We Serve -->
  <section class="industries section-light section-padding" id="industries">
    <div class="container">
      <h2 class="section-title text-center fade-up">Industries We Serve</h2>
      <div class="grid grid-4-col mt-4">
        <div class="industry-card fade-up">
          <h4>Startups</h4>
        </div>
        <div class="industry-card fade-up">
          <h4>Manufacturing</h4>
        </div>
        <div class="industry-card fade-up">
          <h4>Healthcare</h4>
        </div>
        <div class="industry-card fade-up">
          <h4>IT & SaaS</h4>
        </div>
        <div class="industry-card fade-up">
          <h4>Import & Export</h4>
        </div>
        <div class="industry-card fade-up">
          <h4>Retail & E-commerce</h4>
        </div>
        <div class="industry-card fade-up">
          <h4>Logistics</h4>
        </div>
        <div class="industry-card fade-up">
          <h4>Professional Services</h4>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 8 - Client Success Stories -->
  <section class="success-stories section-white section-padding" id="case-studies">
    <div class="container">
      <h2 class="section-title text-center fade-up">Client Success Stories</h2>
      <div class="grid grid-2-col mt-4">
        <div class="case-study-card fade-up">
          <span class="badge badge-blue mb-2">IT & SaaS</span>
          <h3>Scaling a SaaS Startup to Series A</h3>
          <p>Implemented robust financial models and virtual CFO services, resulting in a successful $5M funding round.</p>
          <div class="business-outcomes mt-3">
            <strong>Outcomes:</strong>
            <ul>
              <li>100% Due Diligence Readiness</li>
              <li>Optimized Cash Flow</li>
            </ul>
          </div>
        </div>
        <div class="case-study-card fade-up">
          <span class="badge badge-green mb-2">Cross-Border</span>
          <h3>Seamless India Entry for US Tech Firm</h3>
          <p>Managed end-to-end subsidiary incorporation, FEMA compliance, and initial payroll setup within 4 weeks.</p>
          <div class="business-outcomes mt-3">
            <strong>Outcomes:</strong>
            <ul>
              <li>Zero Compliance Delays</li>
              <li>Streamlined Transfer Pricing</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 9 - Insights & Resources -->
  <section class="insights section-light section-padding" id="insights">
    <div class="container">
      <h2 class="section-title text-center fade-up">Insights & Resources</h2>
      
      <div class="grid grid-3-col mt-4">
        <!-- Resource Card 1 -->
        <div class="card article-card fade-up">
          <span class="badge badge-blue">Business Guide</span>
          <h3 class="article-title mt-3">The Ultimate Guide to India Entry</h3>
          <p class="article-excerpt">A comprehensive roadmap for foreign companies looking to establish a presence in India.</p>
          <a href="#" class="link-teal">Download Guide &rarr;</a>
        </div>
        <!-- Resource Card 2 -->
        <div class="card article-card fade-up">
          <span class="badge badge-green">Compliance Updates</span>
          <h3 class="article-title mt-3">New GST Regulations for 2027</h3>
          <p class="article-excerpt">Stay ahead of the curve with our breakdown of the upcoming changes to GST filings.</p>
          <a href="#" class="link-teal">Read Article &rarr;</a>
        </div>
        <!-- Resource Card 3 -->
        <div class="card article-card fade-up">
          <span class="badge badge-blue">Country Guide</span>
          <h3 class="article-title mt-3">Setting up in UAE Free Zones</h3>
          <p class="article-excerpt">Compare the top Free Zones in the UAE and find the right fit for your business model.</p>
          <a href="#" class="link-teal">Read Guide &rarr;</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 10 - Testimonials -->
  <section class="testimonials section-dark section-padding text-center" id="testimonials">
    <div class="container">
      <h2 class="section-title text-white fade-up">What Our Clients Say</h2>
      
      <div class="testimonial-slider fade-up mt-4">
        <div class="testimonial-slide active">
          <p class="testimonial-text text-white">"Truvisory completely transformed our financial operations. Their Virtual CFO service feels like having an in-house expert, but at a fraction of the cost."</p>
          <p class="testimonial-author text-white mt-3"><strong>- Sarah J.</strong>, Tech Founder</p>
        </div>
        <!-- Note: Slider functionality to be handled by JS -->
      </div>
    </div>
  </section>

  <!-- Section 11 - FAQs -->
  <section class="faq section-white section-padding" id="faq">
    <div class="container faq-container mx-auto">
      <h2 class="section-title text-center fade-up">Frequently Asked Questions</h2>
      
      <div class="faq-tabs text-center mb-4 fade-up">
        <button class="faq-tab active" data-target="general">General</button>
        <button class="faq-tab" data-target="country">Country FAQs</button>
        <button class="faq-tab" data-target="service">Service FAQs</button>
      </div>

      <div class="accordion fade-up" id="general-faqs">
        <div class="accordion-item">
          <button class="accordion-header">What does end-to-end advisory mean?</button>
          <div class="accordion-content">
            <p>It means we handle everything from your initial company registration to ongoing tax compliance, payroll, and strategic financial planning (CFO services) as you grow.</p>
          </div>
        </div>
        <div class="accordion-item">
          <button class="accordion-header">How quickly can we get started?</button>
          <div class="accordion-content">
            <p>After our initial free consultation, we provide an engagement proposal within 24 hours. Once approved, onboarding takes less than 2 days.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 12 - Final CTA -->
  <section class="bottom-cta section-light section-padding text-center border-top-light" id="schedule">
    <div class="container cta-container fade-up">
      <h2 class="main-title text-navy mb-3">Ready to Build Your Business on Solid Foundations?</h2>
      <p class="cta-subtext mb-4">Book a free 30-minute consultation with our advisory team.</p>
      <div class="cta-actions">
        <a href="#" class="btn btn-primary cta-btn">Book Consultation Now</a>
        <a href="contact.html" class="link-navy mt-3 d-block font-weight-500">Contact Options &rarr;</a>
      </div>
    </div>
  </section>

  <!-- Footer (Expanded) -->
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col">
          <a href="index.html" class="logo footer-logo mb-3">
            <img src="assets/images/logo.png" alt="Truvisory Services" class="logo-img">
          </a>
          <p class="footer-desc">End-to-end financial advisory and regulatory compliance for ambitious businesses worldwide.</p>
        </div>
        
        <div class="footer-col">
          <h4>Services</h4>
          <ul>
            <li><a href="services.html#setup">Business Setup</a></li>
            <li><a href="services.html#accounting">Accounting & Tax</a></li>
            <li><a href="services.html#cfo">Virtual CFO</a></li>
            <li><a href="services.html#compliance">Compliance</a></li>
            <li><a href="services.html#trademark">IP & Trademark</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Countries</h4>
          <ul>
            <li><a href="countries.html#india">India</a></li>
            <li><a href="countries.html#uae">UAE</a></li>
            <li><a href="countries.html#singapore">Singapore</a></li>
            <li><a href="countries.html#uk">UK</a></li>
            <li><a href="countries.html#us">USA</a></li>
          </ul>
        </div>
        
        <div class="footer-col">
          <h4>Resources</h4>
          <ul>
            <li><a href="about.html">About Us</a></li>
            <li><a href="insights.html">Blog & Insights</a></li>
            <li><a href="resources.html">Guides & Downloads</a></li>
            <li><a href="#faq">FAQs</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Contact & Legal</h4>
          <ul>
            <li>hello@truvisory.com</li>
            <li>+91 98765 43210</li>
            <li>Mumbai, India</li>
            <li class="mt-2"><a href="privacy.html">Privacy Policy</a></li>
            <li><a href="terms.html">Terms of Service</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 Truvisory Service. All rights reserved.</p>
        <div class="footer-network">
          <a href="#">LinkedIn</a>
          <a href="#">Twitter</a>
          <a href="#">Facebook</a>
        </div>
      </div>
    </div>
  </footer>
"""

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(header_part + new_content + footer_part)
        
    print("Updated index.html successfully.")

if __name__ == "__main__":
    update_index_html()
