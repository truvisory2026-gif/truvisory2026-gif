import re

def rewrite_index_html():
    file_path = 'c:\\Users\\roopc\\OneDrive\\Desktop\\truvisory\\index.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # We will preserve the <head> block
    head_end = content.find('</head>') + len('</head>')
    head_part = content[:head_end]

    # Include Calendly and Script at bottom
    scripts_start = content.find('<!-- Calendly widget scripts -->')
    if scripts_start != -1:
        scripts_part = content[scripts_start:]
    else:
        scripts_part = """
  <!-- Calendly widget scripts -->
  <link href="https://assets.calendly.com/assets/external/widget.css" rel="stylesheet">
  <script src="https://assets.calendly.com/assets/external/widget.js" type="text/javascript" async></script>
  <script src="script.js"></script>
</body>
</html>
"""

    new_body = """
<body>
  <!-- Header -->
  <header class="header">
    <div class="container header-container">
      <a href="index.html" class="logo">
        <img src="assets/images/logo.png" alt="Truvisory Services" class="logo-img" style="height: 60px;">
      </a>
      
      <!-- Desktop Nav -->
      <nav class="desktop-nav">
        <a href="#home">Home</a>
        <a href="#about">About Us</a>
        <a href="#services">Services</a>
        <a href="#why-us">Why Truvisory</a>
        <a href="#testimonials">Testimonials</a>
        <a href="#contact">Contact Us</a>
        <a href="#contact" class="nav-cta">Book a Free Consultation</a>
      </nav>

      <!-- Mobile Menu Toggle -->
      <button class="mobile-menu-toggle" aria-label="Toggle Menu" id="menu-toggle">
        <span class="hamburger"></span>
      </button>
    </div>
  </header>

  <!-- Mobile Drawer -->
  <div class="mobile-drawer" id="mobile-drawer">
    <div class="drawer-header">
      <a href="index.html" class="logo">
        <img src="assets/images/logo.png" alt="Truvisory Services" class="logo-img" style="height: 50px;">
      </a>
      <button class="close-menu" id="close-menu">&times;</button>
    </div>
    <div class="drawer-content">
      <div class="drawer-links">
        <a href="#home" class="drawer-link">Home</a>
        <a href="#about" class="drawer-link">About Us</a>
        <a href="#services" class="drawer-link">Services</a>
        <a href="#why-us" class="drawer-link">Why Truvisory</a>
        <a href="#testimonials" class="drawer-link">Testimonials</a>
        <a href="#contact" class="drawer-link">Contact Us</a>
        <a href="#contact" class="btn btn-primary w-100 text-center mt-4">Book a Free Consultation</a>
      </div>
      <div class="drawer-subcategories text-center mt-4">
        <p class="font-weight-500 mb-2">Contact Us:</p>
        <a href="tel:+919930426774" class="link-navy d-block">📞 +91 99304 26774</a>
        <a href="mailto:truvisoryfinance@gmail.com" class="link-navy d-block mt-2">✉ truvisoryfinance@gmail.com</a>
        <a href="https://wa.me/919930426774?text=Hello%20Truvisory%20Financial%20Services,%20I%20would%20like%20to%20know%20more%20about%20your%20business%20advisory%20and%20financial%20services." class="btn btn-outline w-100 text-center mt-3" target="_blank">Chat on WhatsApp</a>
      </div>
    </div>
  </div>

  <!-- Hero Section -->
  <section class="hero section-white" id="home">
    <div class="container">
      <div class="grid hero-grid align-center">
        <div class="hero-content fade-up">
          <h1 class="main-title text-navy">Your Growth. Our Expertise.</h1>
          <h3 class="category-tagline mb-3" style="color: var(--text-slate); font-family: var(--font-sans); text-transform: none; letter-spacing: normal;">Financial and Advisory Solutions for New Businesses, SMEs and Global Expansions</h3>
          <p class="hero-subtext">Truvisory Financial Services is a Mumbai-based advisory firm built for entrepreneurs, startups and growing businesses. From company incorporation to taxation, compliance, payroll and accounting, our dedicated team of Chartered Accountants and financial experts helps you build on a solid foundation — in India and across the globe.</p>
          <p class="hero-subtext">We currently support clients across India, the USA, UAE, Singapore and Hong Kong, offering one consistent standard of service no matter where you operate.</p>
          <div class="hero-ctas mt-4">
            <a href="#contact" class="btn btn-primary cta-btn mr-3">Get a Free Consultation</a>
            <a href="https://wa.me/919930426774?text=Hello%20Truvisory%20Financial%20Services,%20I%20would%20like%20to%20know%20more%20about%20your%20business%20advisory%20and%20financial%20services." target="_blank" class="btn btn-outline cta-btn">WhatsApp an Expert</a>
          </div>
          <div class="trust-indicators mt-4">
            <span class="trust-item mb-2 d-block">✓ Business Incorporation — India, UAE and global</span>
            <span class="trust-item mb-2 d-block">✓ Taxation — Direct Tax, Indirect Tax, VAT & Corporate Tax</span>
            <span class="trust-item mb-2 d-block">✓ Compliances — ROC and Regulatory Filings</span>
            <span class="trust-item mb-2 d-block">✓ Accounting and Bookkeeping</span>
            <span class="trust-item mb-2 d-block">✓ Staff and Payroll Management</span>
            <span class="trust-item mb-2 d-block">✓ Legal Formalities and Advisory</span>
            <span class="trust-item mb-2 d-block">✓ Marketing Support for Growing Businesses</span>
          </div>
        </div>
        <div class="hero-visual fade-left">
          <img src="https://placehold.co/800x800/FFFFFF/0F172A?text=Global+Financial+Consulting" alt="Global Financial Consulting and Advisory" class="hero-image" style="border: 1px solid var(--card-border);">
        </div>
      </div>
    </div>
  </section>

  <!-- About Us -->
  <section class="about section-gray section-padding" id="about">
    <div class="container">
      <div class="text-center fade-up mb-5">
        <h2 class="section-title mb-2">About Truvisory</h2>
        <h3 class="mb-4 text-navy">Truvisory — Introduction</h3>
        <div class="max-w-700 mx-auto">
          <p class="mb-3">Truvisory Financial Services was founded with a simple purpose: to give new businesses and SMEs access to the same quality of financial, legal and advisory guidance that large corporations take for granted.</p>
          <p class="mb-3">Headquartered in Mumbai, we work with founders and enterprises across India and internationally, guiding them through incorporation, taxation, compliance and everyday financial operations.</p>
          <p class="mb-3">Our name reflects our promise — <strong>True Advisory</strong>.</p>
          <p>We combine deep technical expertise with a genuine understanding of each client's business, so every recommendation we make is practical, compliant and built for long-term growth.</p>
        </div>
      </div>
      
      <!-- Vision & Mission Cards -->
      <div class="grid grid-2-col mt-5 max-w-900 mx-auto">
        <div class="card text-center fade-up">
          <div class="card-icon text-teal">👁️</div>
          <h3 class="card-title text-navy">Our Vision</h3>
          <p>To be the most trusted financial and advisory partner for businesses expanding across India and the world.</p>
        </div>
        <div class="card fade-up">
          <div class="card-icon text-center text-teal">🎯</div>
          <h3 class="card-title text-center text-navy">Our Mission</h3>
          <ul class="pricing-features text-left">
            <li>Simplify incorporation, taxation and compliance for new and growing businesses.</li>
            <li>Deliver expert, transparent advice at every stage of a client's journey.</li>
            <li>Support businesses expanding from India to the world, and into India from abroad.</li>
            <li>Build long-term relationships based on trust, accuracy and accountability.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- Our Team -->
  <section class="team section-white section-padding" id="team">
    <div class="container">
      <h2 class="section-title text-center fade-up">Our Team</h2>
      <div class="grid grid-2-col mt-4 max-w-900 mx-auto">
        
        <div class="card profile-card fade-up">
          <h3 class="card-title text-navy">Nivya Jain</h3>
          <span class="badge badge-blue mb-3">Founder</span>
          <p class="mb-2 font-weight-500">Master's Degree in Marketing and Finance</p>
          <p class="mb-2">Leads Truvisory's vision, client strategy and business growth.</p>
          <p>Her approach blends financial discipline with a strong understanding of branding and market positioning, helping clients grow not just compliantly, but competitively.</p>
        </div>
        
        <div class="card profile-card fade-up">
          <h3 class="card-title text-navy">CA Manish Parasmal Jain</h3>
          <span class="badge badge-green mb-3">Chartered Accountant</span>
          <p class="mb-2 font-weight-500">Heads taxation, accounting and compliance practice</p>
          <p>With deep expertise across Indian and international tax frameworks, he ensures every client engagement is technically sound, fully compliant and efficiently executed.</p>
        </div>
        
      </div>
      <p class="text-center mt-5 max-w-700 mx-auto fade-up">Behind Nivya and Manish stands a dedicated team of Chartered Accountants, tax specialists and compliance professionals who work as an extension of every client's own team.</p>
    </div>
  </section>

  <!-- Why Choose Truvisory -->
  <section class="why-choose section-gray section-padding" id="why-us">
    <div class="container">
      <h2 class="section-title text-center fade-up">Why Businesses Choose Truvisory</h2>
      
      <div class="grid grid-3-col mt-5">
        <div class="card fade-up">
          <div class="card-icon text-teal">🌍</div>
          <h4 class="card-title text-navy">Global Expertise, Local Understanding</h4>
          <p>With operations spanning India, the USA, UAE, Singapore and Hong Kong, we understand the regulatory and tax landscape of multiple jurisdictions, giving businesses a single point of contact for global expansion.</p>
        </div>
        <div class="card fade-up">
          <div class="card-icon text-teal">🔄</div>
          <h4 class="card-title text-navy">A Holistic Approach</h4>
          <p>We don't just file returns or process paperwork. Our holistic approach connects taxation, compliance, accounting, payroll and legal advisory into one coordinated strategy, ensuring every aspect of your business works together.</p>
        </div>
        <div class="card fade-up">
          <div class="card-icon text-teal">🤝</div>
          <h4 class="card-title text-navy">Our Commitment</h4>
          <p>Every client works directly with experienced Chartered Accountants and advisors committed to accuracy, confidentiality and timely delivery.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Services -->
  <section class="services section-white section-padding" id="services">
    <div class="container">
      <h2 class="section-title text-center fade-up">End-to-End Financial, Legal & Business Advisory Services</h2>
      
      <div class="grid grid-3-col mt-5">
        
        <div class="service-card fade-up">
          <div class="service-icon">⚖️</div>
          <h4>Tax Consultation</h4>
          <p class="font-weight-500 mb-2">India:</p>
          <ul class="mb-3" style="padding-left: 20px; font-size: 0.9rem;">
            <li>Direct Tax & Income Tax Planning</li>
            <li>GST Registration & Filing</li>
            <li>Corporate Tax Planning & Compliance</li>
          </ul>
          <p class="font-weight-500 mb-2">UAE:</p>
          <ul class="mb-3" style="padding-left: 20px; font-size: 0.9rem;">
            <li>VAT Registration & Filing</li>
            <li>Corporate Tax Planning</li>
          </ul>
          <p class="font-weight-500 mb-2">Other Countries:</p>
          <ul class="mb-3" style="padding-left: 20px; font-size: 0.9rem;">
            <li>International Tax Support</li>
          </ul>
          <a href="#contact" class="link-teal mt-2 d-block">Learn More &rarr;</a>
        </div>
        
        <div class="service-card fade-up">
          <div class="service-icon">💳</div>
          <h4>VAT Services</h4>
          <p>End-to-end VAT registration, return filing and advisory.</p>
          <a href="#contact" class="link-teal mt-2 d-block">Learn More &rarr;</a>
        </div>
        
        <div class="service-card fade-up">
          <div class="service-icon">📜</div>
          <h4>Compliance</h4>
          <p>ROC Filings, Annual Compliance, and Regulatory Compliance.</p>
          <a href="#contact" class="link-teal mt-2 d-block">Learn More &rarr;</a>
        </div>
        
        <div class="service-card fade-up">
          <div class="service-icon">👥</div>
          <h4>Staff & Payroll</h4>
          <p>Payroll Processing, Statutory Compliance, and Employee Management Support.</p>
          <a href="#contact" class="link-teal mt-2 d-block">Learn More &rarr;</a>
        </div>
        
        <div class="service-card fade-up">
          <div class="service-icon">📊</div>
          <h4>Accounting & Bookkeeping</h4>
          <p>Bookkeeping, Financial Reporting, Bank Reconciliation, and Management Reporting.</p>
          <a href="#contact" class="link-teal mt-2 d-block">Learn More &rarr;</a>
        </div>
        
        <div class="service-card fade-up">
          <div class="service-icon">🏢</div>
          <h4>Business Incorporation</h4>
          <p>India Incorporation, UAE Incorporation, USA Incorporation, Singapore Incorporation, Hong Kong Incorporation, Global Business Setup.</p>
          <a href="#contact" class="link-teal mt-2 d-block">Learn More &rarr;</a>
        </div>
        
        <div class="service-card fade-up">
          <div class="service-icon">📝</div>
          <h4>Legal Formalities</h4>
          <p>Business Documentation, Legal Advisory, and Regulatory Documentation.</p>
          <a href="#contact" class="link-teal mt-2 d-block">Learn More &rarr;</a>
        </div>
        
        <div class="service-card fade-up">
          <div class="service-icon">📈</div>
          <h4>Marketing Support</h4>
          <p>Business Branding, Growth Strategy, and Marketing Guidance.</p>
          <a href="#contact" class="link-teal mt-2 d-block">Learn More &rarr;</a>
        </div>
        
      </div>
    </div>
  </section>

  <!-- Testimonials -->
  <section class="testimonials section-gray section-padding text-center" id="testimonials">
    <div class="container">
      <h2 class="section-title text-navy fade-up">What Our Clients Say</h2>
      
      <div class="grid grid-3-col mt-5">
        <div class="card text-left fade-up">
          <p class="testimonial-text mb-4">"Truvisory made our UAE incorporation seamless — responsive, knowledgeable and always available."</p>
          <p class="font-weight-500 text-navy mb-0">Rakesh Sharma</p>
          <p class="text-slate text-sm">Managing Director</p>
          <div class="text-warning mt-2">★★★★★</div>
        </div>
        <div class="card text-left fade-up">
          <p class="testimonial-text mb-4">"A reliable partner for our accounting and compliance needs across India."</p>
          <p class="font-weight-500 text-navy mb-0">Priya Patel</p>
          <p class="text-slate text-sm">Founder</p>
          <div class="text-warning mt-2">★★★★★</div>
        </div>
        <div class="card text-left fade-up">
          <p class="testimonial-text mb-4">"Their team simplified our tax planning across two countries. Highly recommended."</p>
          <p class="font-weight-500 text-navy mb-0">Vikram Singh</p>
          <p class="text-slate text-sm">Operations Head</p>
          <div class="text-warning mt-2">★★★★★</div>
        </div>
      </div>
      <p class="text-slate mt-4 fade-up" style="font-size: 0.8rem;">*Replace the above testimonials with verified client reviews before publishing.</p>
    </div>
  </section>

  <!-- Contact Us -->
  <section class="contact section-white section-padding" id="contact">
    <div class="container">
      <div class="grid grid-2-col">
        <div class="contact-info fade-up">
          <h2 class="section-title mb-4">Let's Build Your Business, Together</h2>
          
          <div class="mb-4">
            <h4 class="mb-2 text-navy">Office</h4>
            <p>📍 Mumbai, India</p>
          </div>
          
          <div class="mb-4">
            <h4 class="mb-2 text-navy">Operations</h4>
            <p>🌍 India • USA • UAE • Singapore • Hong Kong</p>
          </div>
          
          <div class="mb-4">
            <h4 class="mb-2 text-navy">Contact</h4>
            <p class="mb-2">✉ <a href="mailto:truvisoryfinance@gmail.com" class="link-teal font-weight-500">truvisoryfinance@gmail.com</a></p>
            <p>📞 <a href="tel:+919930426774" class="link-teal font-weight-500">+91 99304 26774</a></p>
          </div>
          
          <div class="mt-4">
            <a href="https://wa.me/919930426774?text=Hello%20Truvisory%20Financial%20Services,%20I%20would%20like%20to%20know%20more%20about%20your%20business%20advisory%20and%20financial%20services." target="_blank" class="btn btn-outline mr-2 mb-2">Chat on WhatsApp</a>
            <a href="tel:+919930426774" class="btn btn-outline mr-2 mb-2">Call Now</a>
          </div>
        </div>
        
        <div class="contact-form-container fade-left">
          <div class="card form-card">
            <h3 class="mb-4 text-navy">Book a Free Consultation</h3>
            
            <!-- Using Formspree as standard reliable static form handler -->
            <form action="https://formspree.io/f/xknkoyvd" method="POST" id="contactForm">
              
              <div class="form-group mb-3">
                <label for="name" class="font-weight-500 mb-1 d-block">Name *</label>
                <input type="text" id="name" name="Name" class="form-control" required style="width: 100%; padding: 12px; border: 1px solid var(--card-border); border-radius: 8px;">
              </div>
              
              <div class="grid grid-2-col" style="gap: 16px;">
                <div class="form-group mb-3">
                  <label for="email" class="font-weight-500 mb-1 d-block">Email *</label>
                  <input type="email" id="email" name="Email" class="form-control" required style="width: 100%; padding: 12px; border: 1px solid var(--card-border); border-radius: 8px;">
                </div>
                <div class="form-group mb-3">
                  <label for="phone" class="font-weight-500 mb-1 d-block">Phone *</label>
                  <input type="tel" id="phone" name="Phone" class="form-control" required style="width: 100%; padding: 12px; border: 1px solid var(--card-border); border-radius: 8px;">
                </div>
              </div>
              
              <div class="grid grid-2-col" style="gap: 16px;">
                <div class="form-group mb-3">
                  <label for="company" class="font-weight-500 mb-1 d-block">Company</label>
                  <input type="text" id="company" name="Company" class="form-control" style="width: 100%; padding: 12px; border: 1px solid var(--card-border); border-radius: 8px;">
                </div>
                <div class="form-group mb-3">
                  <label for="country" class="font-weight-500 mb-1 d-block">Country</label>
                  <input type="text" id="country" name="Country" class="form-control" style="width: 100%; padding: 12px; border: 1px solid var(--card-border); border-radius: 8px;">
                </div>
              </div>

              <div class="form-group mb-3">
                <label for="service" class="font-weight-500 mb-1 d-block">Service Required</label>
                <select id="service" name="Service Required" class="form-control" style="width: 100%; padding: 12px; border: 1px solid var(--card-border); border-radius: 8px; background: white;">
                  <option value="General Inquiry">General Inquiry</option>
                  <option value="Business Incorporation">Business Incorporation</option>
                  <option value="Tax Consultation">Tax Consultation</option>
                  <option value="Accounting & Bookkeeping">Accounting & Bookkeeping</option>
                  <option value="Compliance">Compliance</option>
                  <option value="Staff & Payroll">Staff & Payroll</option>
                </select>
              </div>
              
              <div class="form-group mb-4">
                <label for="message" class="font-weight-500 mb-1 d-block">Message *</label>
                <textarea id="message" name="Message" rows="4" class="form-control" required style="width: 100%; padding: 12px; border: 1px solid var(--card-border); border-radius: 8px;"></textarea>
              </div>
              
              <!-- Hidden field to specify email subject -->
              <input type="hidden" name="_subject" value="New Website Enquiry from Truvisory Form">
              
              <button type="submit" class="btn btn-primary w-100 text-center">Submit Enquiry</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Privacy Policy Note -->
  <section class="privacy section-gray section-padding" id="privacy">
    <div class="container text-center fade-up">
      <h3 class="text-navy mb-3">Privacy Policy</h3>
      <p class="max-w-700 mx-auto mb-3">Truvisory Financial Services is committed to protecting the privacy and confidentiality of client information shared with us.</p>
      <p class="max-w-700 mx-auto mb-4">Any personal, financial or business data submitted through this website or during our engagement is used solely for the purpose of delivering our services and is not shared with third parties without consent, except as required by law.</p>
      <div class="alert alert-warning d-inline-block px-4 py-3" style="background: #FFFBEB; border: 1px solid #FEF3C7; border-radius: 8px; font-size: 0.9rem;">
        <strong>Note:</strong> This Privacy Policy is placeholder content. We recommend having a qualified legal professional review and finalize the complete Privacy Policy before publishing.
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer section-white border-top-light" style="padding-top: 60px; padding-bottom: 30px;">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col">
          <a href="index.html" class="logo footer-logo mb-3">
            <img src="assets/images/logo.png" alt="Truvisory Services" class="logo-img" style="height: 60px;">
          </a>
          <p class="footer-desc mt-3">Truvisory Financial Services Pvt. Ltd.</p>
        </div>
        
        <div class="footer-col">
          <h4 class="text-navy">Quick Links</h4>
          <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#about">About Us</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#why-us">Why Truvisory</a></li>
            <li><a href="#contact">Contact Us</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4 class="text-navy">Global Presence</h4>
          <ul>
            <li>India</li>
            <li>USA</li>
            <li>UAE</li>
            <li>Singapore</li>
            <li>Hong Kong</li>
          </ul>
        </div>

        <div class="footer-col">
          <h4 class="text-navy">Contact Info</h4>
          <ul>
            <li class="mb-2">📍 Mumbai, India</li>
            <li class="mb-2">📞 <a href="tel:+919930426774" class="link-teal">+91 99304 26774</a></li>
            <li class="mb-2">✉ <a href="mailto:truvisoryfinance@gmail.com" class="link-teal">truvisoryfinance@gmail.com</a></li>
          </ul>
          <div class="footer-network mt-3">
            <a href="https://wa.me/919930426774?text=Hello%20Truvisory%20Financial%20Services,%20I%20would%20like%20to%20know%20more%20about%20your%20business%20advisory%20and%20financial%20services." target="_blank" style="font-size: 1.5rem; text-decoration: none;" title="WhatsApp">📱</a>
            <a href="mailto:truvisoryfinance@gmail.com" style="font-size: 1.5rem; text-decoration: none; margin-left: 10px;" title="Email">✉</a>
            <a href="tel:+919930426774" style="font-size: 1.5rem; text-decoration: none; margin-left: 10px;" title="Phone">📞</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom mt-5 text-center" style="border-top: 1px solid var(--card-border); padding-top: 20px;">
        <p class="text-slate">&copy; 2026 Truvisory Financial Services Pvt. Ltd. All rights reserved.</p>
      </div>
    </div>
  </footer>

  <!-- Floating WhatsApp Button -->
  <a href="https://wa.me/919930426774?text=Hello%20Truvisory%20Financial%20Services,%20I%20would%20like%20to%20know%20more%20about%20your%20business%20advisory%20and%20financial%20services." class="floating-whatsapp" aria-label="Chat on WhatsApp" target="_blank" style="background-color: #25D366; color: white; border-radius: 50%; width: 60px; height: 60px; display: flex; justify-content: center; align-items: center; position: fixed; bottom: 30px; right: 30px; z-index: 1000; box-shadow: 0 4px 10px rgba(0,0,0,0.2); transition: transform 0.3s;">
    <svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor">
      <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/>
    </svg>
  </a>
"""

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(head_part + new_body + scripts_part)
        
    print("Updated index.html with new premium corporate content.")

if __name__ == "__main__":
    rewrite_index_html()
