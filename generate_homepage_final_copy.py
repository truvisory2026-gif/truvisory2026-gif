import re

def update_index_html_final():
    file_path = 'c:\\Users\\roopc\\OneDrive\\Desktop\\truvisory\\index.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    header_end_idx = content.find('<!-- Section 1 - Hero Banner -->')
    if header_end_idx == -1:
        # Fallback to older comment
        header_end_idx = content.find('<!-- 01. Hero Section -->')
        
    footer_end_idx = content.find('<!-- Footer (Expanded) -->')
    if footer_end_idx == -1:
        footer_end_idx = content.find('<!-- Floating UI -->')

    header_part = content[:header_end_idx]
    
    # We will also manually append the floating UI at the end since we are replacing till footer
    floating_ui = content[content.find('<!-- Floating UI -->'):]

    new_content = """
  <!-- Section 1 - Hero Banner -->
  <section class="hero section-white" id="home">
    <div class="container">
      <div class="grid hero-grid">
        <div class="hero-content fade-up">
          <div class="badge-chip">Global Financial Advisory & Strategic Growth Partners</div>
          <h1 class="main-title text-navy">Navigating Complexity. Driving Corporate Growth.</h1>
          <p class="hero-subtext">Truvisory delivers elite financial strategy, uncompromising tax compliance, and visionary CFO advisory. We empower modern enterprises to scale seamlessly across global markets with absolute regulatory certainty.</p>
          <div class="hero-ctas mt-4">
            <a href="#schedule" class="btn btn-primary cta-btn mr-3">Request a Strategic Consultation</a>
            <a href="#services" class="btn btn-outline cta-btn">Explore Global Solutions</a>
          </div>
          <div class="trust-indicators mt-4">
            <span class="trust-item">✓ Over $500M in Client Revenue Optimized</span>
            <span class="trust-item">✓ 15+ Years Cross-Border Expertise</span>
            <span class="trust-item">✓ 100% Audit & Statutory Compliance Rate</span>
          </div>
          <!-- Hero Visual Recommendation: A high-resolution, modern corporate abstract (e.g., glass buildings interacting with subtle data visualizations) or a diverse team of executives in a premium boardroom setting. -->
        </div>
        <div class="hero-visual fade-left">
          <img src="https://placehold.co/800x600/F8FAFC/0F172A?text=Corporate+Boardroom+Strategy" alt="Premium Corporate Strategy and Financial Advisory" class="hero-image">
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
          <p class="mb-3">In an increasingly complex global economy, ambitious enterprises often find their growth stifled by fragmented regulatory frameworks and disjointed financial advice. We identified a critical gap: businesses needed a unified, top-tier partner capable of delivering both strategic foresight and meticulous compliance.</p>
          <h3 class="mb-3 mt-4">Our Genesis & The Truvisory Name</h3>
          <p class="mb-3">Founded by a coalition of veteran financial experts, Truvisory was established to bridge this gap. Our name is a synthesis of <strong>True</strong> and <strong>Advisory</strong>. It encapsulates our foundational pledge: to provide transparent, unvarnished truth paired with actionable, elite advisory services.</p>
          <h3 class="mb-3 mt-4">Mission, Vision & Core Values</h3>
          <p class="mb-3"><strong>Mission:</strong> To engineer financial architecture that empowers visionary companies to scale globally without friction.</p>
          <p class="mb-3"><strong>Vision:</strong> To be the undisputed global standard for integrated corporate financial and compliance advisory.</p>
          <p class="mb-3"><strong>Core Values:</strong> Uncompromising Integrity, Precision Execution, Strategic Foresight, and Client-Centric Innovation.</p>
        </div>
        <div class="quote-box-container fade-left">
          <div class="quote-box">
            <div class="quote-icon">"</div>
            <p class="quote-text">We do not simply interpret regulations; we architect financial strategies that turn compliance into a competitive advantage and data into exponential growth.</p>
            <p class="quote-author">- Leadership, Truvisory Financial Services</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 3 - Your Business Journey -->
  <section class="business-journey section-white section-padding" id="journey">
    <div class="container">
      <h2 class="section-title text-center fade-up">Your Business Journey, Architected for Success</h2>
      <p class="text-center mb-4 max-w-700 mx-auto fade-up">From the inception of an idea to formidable international expansion, Truvisory is the strategic constant in your corporate lifecycle.</p>
      
      <div class="timeline-container mt-4">
        <div class="timeline">
          
          <div class="timeline-item left fade-up">
            <div class="timeline-content">
              <h3>1. Business Idea & Planning</h3>
              <p>We rigorously stress-test your financial models and determine the most tax-efficient entity structure before you launch, mitigating early-stage risk.</p>
              <a href="#schedule" class="link-teal mt-2 d-block">Consult on Structuring &rarr;</a>
            </div>
          </div>
          
          <div class="timeline-item right fade-up">
            <div class="timeline-content">
              <h3>2. Company Formation & Registration</h3>
              <p>Flawless execution of Private Limited, LLP, or foreign subsidiary incorporation, establishing a rock-solid legal foundation for future capital raises.</p>
            </div>
          </div>
          
          <div class="timeline-item left fade-up">
            <div class="timeline-content">
              <h3>3. Accounting Setup</h3>
              <p>Implementation of enterprise-grade cloud accounting systems and internal controls, ensuring real-time visibility into your fiscal health.</p>
            </div>
          </div>
          
          <div class="timeline-item right fade-up">
            <div class="timeline-content">
              <h3>4. Tax Registration & Compliance</h3>
              <p>Comprehensive direct and indirect tax registrations (GST, Corporate Tax) engineered to prevent leakage and optimize your effective tax rate.</p>
            </div>
          </div>
          
          <div class="timeline-item left fade-up">
            <div class="timeline-content">
              <h3>5. Payroll Setup</h3>
              <p>Structuring executive and employee compensation packages that are highly tax-efficient and fully compliant with local labor laws.</p>
            </div>
          </div>
          
          <div class="timeline-item right fade-up">
            <div class="timeline-content">
              <h3>6. Trademark Protection</h3>
              <p>Securing your intellectual property assets globally, ensuring your brand equity is legally defensible as you capture market share.</p>
            </div>
          </div>

          <div class="timeline-item left fade-up">
            <div class="timeline-content">
              <h3>7. Financial Advisory (Virtual CFO)</h3>
              <p>Deploying our Virtual CFOs to architect board-level reporting, manage cash burn, and prepare your data rooms for Series A/B fundraising.</p>
            </div>
          </div>

          <div class="timeline-item right fade-up">
            <div class="timeline-content">
              <h3>8. International Growth</h3>
              <p>Masterminding cross-border expansion, managing transfer pricing, and establishing compliant foreign entities in lucrative new jurisdictions.</p>
              <a href="#countries" class="link-teal mt-2 d-block">Explore Global Expansion &rarr;</a>
            </div>
          </div>

        </div>
      </div>
      <p class="text-center mt-5 font-weight-500 fade-up">Wherever you are in this lifecycle, Truvisory transforms financial friction into operational momentum.</p>
    </div>
  </section>

  <!-- Section 4 - Countries We Serve -->
  <section class="countries section-dark section-padding text-center" id="countries">
    <div class="container">
      <h2 class="section-title text-white fade-up">Global Footprint. Local Precision.</h2>
      <p class="text-white mb-4 max-w-700 mx-auto fade-up">Expanding across borders requires mastery of disparate regulatory environments. Truvisory provides seamless, compliant market entry into the world's most critical economic hubs.</p>
      
      <div class="grid grid-3-col mt-5">
        <div class="country-card fade-up">
          <div class="flag-icon">🇮🇳</div>
          <h3>India</h3>
          <p>Navigate the complexities of FEMA, RBI regulations, and GST. We facilitate frictionless inbound investment, subsidiary setups, and aggressive domestic scaling for foreign and local entities.</p>
        </div>
        <div class="country-card fade-up">
          <div class="flag-icon">🇦🇪</div>
          <h3>United Arab Emirates</h3>
          <p>Capitalize on zero-tax environments and strategic global positioning. We engineer Mainland, Free Zone, and Offshore setups tailored to your specific commercial objectives in Dubai and Abu Dhabi.</p>
        </div>
        <div class="country-card fade-up">
          <div class="flag-icon">🇸🇬</div>
          <h3>Singapore</h3>
          <p>Establish your Asian headquarters in a premier financial hub. We manage ACRA compliance, optimize corporate tax incentives, and structure wealth management vehicles.</p>
        </div>
        <div class="country-card fade-up">
          <div class="flag-icon">🇬🇧</div>
          <h3>United Kingdom</h3>
          <p>Secure a foothold in the European and global markets. We oversee UK Company House registrations, VAT structuring, and seamless integration with your parent entity.</p>
        </div>
        <div class="country-card fade-up">
          <div class="flag-icon">🇭🇰</div>
          <h3>Hong Kong</h3>
          <p>Access the gateway to mainland China and beyond. Our experts handle the nuances of the Inland Revenue Department, ensuring maximum advantage of Hong Kong's territorial tax system.</p>
        </div>
        <div class="country-card fade-up">
          <div class="flag-icon">🇺🇸</div>
          <h3>United States</h3>
          <p>Penetrate the world's largest market with confidence. From Delaware C-Corp formations to complex IRS compliance and state-level nexus analysis, we manage your US footprint.</p>
        </div>
      </div>
      <a href="#schedule" class="btn btn-primary mt-5 fade-up">Plan Your International Expansion</a>
    </div>
  </section>

  <!-- Section 5 - Complete Business Solutions -->
  <section class="services section-light section-padding" id="services">
    <div class="container">
      <h2 class="section-title text-center fade-up">Complete Business Solutions</h2>
      <p class="text-center mb-5 max-w-700 mx-auto fade-up">A holistic suite of corporate services designed to protect your assets, optimize your tax position, and accelerate your growth trajectory.</p>
      
      <div class="grid grid-3-col mt-4">
        
        <div class="service-card fade-up">
          <div class="service-icon">🏢</div>
          <h4>Company Formation</h4>
          <p>Precision structuring for Private Limited Companies, LLPs, and Section 8 NGOs. We also secure Startup India and MSME (Udyam) registrations to unlock vital government incentives.</p>
          <a href="services.html#formation" class="link-teal mt-3 d-block font-weight-500">Discover Formation &rarr;</a>
        </div>
        
        <div class="service-card fade-up">
          <div class="service-icon">📊</div>
          <h4>Accounting & Bookkeeping</h4>
          <p>Transform raw data into strategic intelligence. We implement rigorous, GAAP/IFRS-compliant bookkeeping practices and deliver executive MIS reporting for absolute financial clarity.</p>
          <a href="services.html#accounting" class="link-teal mt-3 d-block font-weight-500">Discover Accounting &rarr;</a>
        </div>
        
        <div class="service-card fade-up">
          <div class="service-icon">⚖️</div>
          <h4>Tax Advisory</h4>
          <p>Aggressive yet fully compliant tax optimization. We handle intricate GST filings, corporate income tax structuring, and transfer pricing mechanisms to preserve your capital.</p>
          <a href="services.html#tax" class="link-teal mt-3 d-block font-weight-500">Discover Tax Advisory &rarr;</a>
        </div>
        
        <div class="service-card fade-up">
          <div class="service-icon">👥</div>
          <h4>Payroll Services</h4>
          <p>Confidential, automated, and compliant payroll processing. We manage TDS, Provident Fund, ESI, and complex executive compensation structuring with zero margin for error.</p>
          <a href="services.html#payroll" class="link-teal mt-3 d-block font-weight-500">Discover Payroll &rarr;</a>
        </div>
        
        <div class="service-card fade-up">
          <div class="service-icon">📜</div>
          <h4>ROC & Annual Compliance</h4>
          <p>Shield your directors from liabilities. We meticulously manage secretarial audits, annual filings, board resolutions, and continuous Ministry of Corporate Affairs compliance.</p>
          <a href="services.html#compliance" class="link-teal mt-3 d-block font-weight-500">Discover Compliance &rarr;</a>
        </div>
        
        <div class="service-card fade-up">
          <div class="service-icon">™️</div>
          <h4>Trademark & Patent</h4>
          <p>Fortify your intellectual property portfolio. From comprehensive trademark searches and objections to rigorous patent filings, we secure your commercial innovations globally.</p>
          <a href="services.html#ip" class="link-teal mt-3 d-block font-weight-500">Discover IP Protection &rarr;</a>
        </div>
        
        <div class="service-card fade-up">
          <div class="service-icon">📈</div>
          <h4>Virtual CFO</h4>
          <p>Elite financial leadership on demand. Benefit from sophisticated financial modeling, cash flow forecasting, and board-level strategic guidance without the overhead of a full-time executive.</p>
          <a href="services.html#cfo" class="link-teal mt-3 d-block font-weight-500">Discover Virtual CFO &rarr;</a>
        </div>

        <div class="service-card fade-up">
          <div class="service-icon">🤝</div>
          <h4>Business Advisory</h4>
          <p>Navigate complex corporate transitions. We provide specialized consulting for restructuring, joint ventures, ESOP formulation, and operational efficiency improvements.</p>
          <a href="services.html#advisory" class="link-teal mt-3 d-block font-weight-500">Discover Advisory &rarr;</a>
        </div>
        
        <div class="service-card fade-up">
          <div class="service-icon">🚀</div>
          <h4>Business Growth Solutions</h4>
          <p>Prepare for liquidity events. We orchestrate rigorous financial due diligence, precise enterprise valuations, and investor-readiness programs for M&A and Series funding rounds.</p>
          <a href="services.html#growth" class="link-teal mt-3 d-block font-weight-500">Discover Growth Solutions &rarr;</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 6 - Why Choose Truvisory -->
  <section class="why-choose section-white section-padding" id="why-choose">
    <div class="container">
      <h2 class="section-title text-center fade-up">The Truvisory Advantage</h2>
      <p class="text-center mb-5 max-w-700 mx-auto fade-up">We don’t just process numbers; we partner with founders and executives to build enduring, unassailable corporate structures.</p>
      
      <div class="grid grid-4-col mt-4">
        <div class="card fade-up">
          <h4 class="card-title text-teal">Expert, Multidisciplinary Team</h4>
          <p>Our roster includes veteran Chartered Accountants, legal experts, and former Big 4 consultants, bringing institutional-grade intelligence to your business.</p>
        </div>
        <div class="card fade-up">
          <h4 class="card-title text-teal">Technology-Driven Precision</h4>
          <p>We leverage cutting-edge financial tech and AI-driven compliance tools to eliminate manual errors, ensuring fast turnarounds and absolute data security.</p>
        </div>
        <div class="card fade-up">
          <h4 class="card-title text-teal">Transparent, Predictable Pricing</h4>
          <p>No hidden retainers or surprise billings. We operate on a model of absolute transparency, aligning our commercial success directly with your growth.</p>
        </div>
        <div class="card fade-up">
          <h4 class="card-title text-teal">End-to-End Accountability</h4>
          <p>From incorporating a foreign subsidiary to filing local payroll, we provide a single, dedicated point of contact for all global compliance and advisory needs.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 7 - Industries We Serve -->
  <section class="industries section-light section-padding" id="industries">
    <div class="container">
      <h2 class="section-title text-center fade-up">Sector-Specific Mastery</h2>
      <p class="text-center mb-5 max-w-700 mx-auto fade-up">Deep industry knowledge allows us to anticipate regulatory shifts and tailor financial strategies that solve sector-specific challenges.</p>
      
      <div class="grid grid-4-col mt-4">
        <div class="industry-card fade-up"><h4>High-Growth Startups</h4></div>
        <div class="industry-card fade-up"><h4>IT & SaaS</h4></div>
        <div class="industry-card fade-up"><h4>E-Commerce & Retail</h4></div>
        <div class="industry-card fade-up"><h4>Manufacturing</h4></div>
        <div class="industry-card fade-up"><h4>Healthcare & Pharma</h4></div>
        <div class="industry-card fade-up"><h4>Import & Export</h4></div>
        <div class="industry-card fade-up"><h4>Logistics & Supply Chain</h4></div>
        <div class="industry-card fade-up"><h4>Professional Services</h4></div>
        <div class="industry-card fade-up"><h4>Real Estate & PropTech</h4></div>
        <div class="industry-card fade-up"><h4>Education & EdTech</h4></div>
        <div class="industry-card fade-up"><h4>Hospitality</h4></div>
        <div class="industry-card fade-up"><h4>Construction</h4></div>
        <div class="industry-card fade-up"><h4>Financial Services & FinTech</h4></div>
        <div class="industry-card fade-up"><h4>NGOs & Non-Profits</h4></div>
      </div>
    </div>
  </section>

  <!-- Section 8 - Client Success Stories -->
  <section class="success-stories section-white section-padding" id="case-studies">
    <div class="container">
      <h2 class="section-title text-center fade-up">Proven Client Outcomes</h2>
      <div class="grid grid-3-col mt-5">
        
        <div class="case-study-card fade-up">
          <span class="badge badge-blue mb-2">SaaS & Technology</span>
          <h3>Preparing for a $12M Series B</h3>
          <p class="mb-3"><strong>Challenge:</strong> A rapidly scaling SaaS firm lacked the GAAP-compliant financials and MRR reconciliation required by top-tier venture capitalists.</p>
          <p class="mb-3"><strong>Solution:</strong> Truvisory deployed a Virtual CFO, overhauled their revenue recognition policies, and curated a flawless due-diligence data room.</p>
          <div class="business-outcomes mt-3">
            <strong>Metrics of Success:</strong>
            <ul>
              <li>Zero discrepancies found during VC audit</li>
              <li>Successfully closed $12M funding round</li>
            </ul>
          </div>
        </div>

        <div class="case-study-card fade-up">
          <span class="badge badge-green mb-2">Cross-Border / Manufacturing</span>
          <h3>UK Expansion for Precision Manufacturing</h3>
          <p class="mb-3"><strong>Challenge:</strong> An Indian manufacturer faced severe transfer pricing complexities and VAT registration hurdles while expanding into the UK.</p>
          <p class="mb-3"><strong>Solution:</strong> We structured a tax-efficient UK subsidiary, managed cross-border transfer pricing documentation, and established compliant local payroll.</p>
          <div class="business-outcomes mt-3">
            <strong>Metrics of Success:</strong>
            <ul>
              <li>UK entity operational in under 6 weeks</li>
              <li>22% reduction in projected effective tax rate</li>
            </ul>
          </div>
        </div>

        <div class="case-study-card fade-up">
          <span class="badge badge-blue mb-2">E-Commerce</span>
          <h3>Navigating Complex Multi-State GST</h3>
          <p class="mb-3"><strong>Challenge:</strong> A high-volume e-commerce brand was suffering from blocked working capital due to mismatched input tax credits across 12 state jurisdictions.</p>
          <p class="mb-3"><strong>Solution:</strong> Truvisory implemented automated GST reconciliation tools and conducted a forensic audit of historical filings to recover locked capital.</p>
          <div class="business-outcomes mt-3">
            <strong>Metrics of Success:</strong>
            <ul>
              <li>Recovered ₹3.5 Crore in blocked ITC</li>
              <li>Reduced monthly compliance time by 60%</li>
            </ul>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- Section 9 - Insights & Resources -->
  <section class="insights section-light section-padding" id="insights">
    <div class="container">
      <h2 class="section-title text-center fade-up">Intellectual Capital & Resources</h2>
      <p class="text-center mb-5 max-w-700 mx-auto fade-up">Access our repository of institutional knowledge. Stay ahead of regulatory curves with our expert guides, tax alerts, and business templates.</p>
      
      <div class="grid grid-3-col mt-4">
        <div class="card article-card fade-up">
          <span class="badge badge-blue">Whitepaper</span>
          <h3 class="article-title mt-3">The Anatomy of a Series A Data Room</h3>
          <p class="article-excerpt">Discover the critical financial and legal documents VCs scrutinize. A must-read checklist for founders preparing to raise institutional capital.</p>
          <a href="#" class="link-teal">Download Whitepaper &rarr;</a>
        </div>
        <div class="card article-card fade-up">
          <span class="badge badge-green">Tax & Compliance Alert</span>
          <h3 class="article-title mt-3">Navigating the New Corporate Tax Paradigm</h3>
          <p class="article-excerpt">A comprehensive breakdown of recent direct tax amendments and how they impact multinational subsidiaries operating in India.</p>
          <a href="#" class="link-teal">Read Briefing &rarr;</a>
        </div>
        <div class="card article-card fade-up">
          <span class="badge badge-blue">Country Guide</span>
          <h3 class="article-title mt-3">UAE Corporate Tax 2024: What You Must Know</h3>
          <p class="article-excerpt">An executive summary of the UAE's new 9% corporate tax regime, transfer pricing rules, and exemptions for Free Zone persons.</p>
          <a href="#" class="link-teal">Access Guide &rarr;</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 10 - Testimonials -->
  <section class="testimonials section-dark section-padding text-center" id="testimonials">
    <div class="container">
      <h2 class="section-title text-white fade-up">Trusted by Industry Leaders</h2>
      <p class="text-white mb-5 max-w-700 mx-auto fade-up">Our reputation is built on the rigorous success of our clients. Here is what leading founders and executives have to say about partnering with Truvisory.</p>
      
      <div class="testimonial-slider fade-up mt-4">
        <div class="testimonial-slide active">
          <p class="testimonial-text text-white">"Truvisory operates with the precision and depth of a Big 4 firm, but with the agility and personalized attention of a boutique advisory. Their structuring advice saved our Series A round."</p>
          <p class="testimonial-author text-white mt-3"><strong>- Marcus V.</strong>, CEO, FinTech Innovators</p>
          <div class="text-warning mt-2">★★★★★</div>
        </div>
        <div class="testimonial-slide">
          <p class="testimonial-text text-white">"Entering the Indian market seemed daunting due to the compliance landscape. Truvisory handled our entire subsidiary setup, FEMA compliance, and payroll seamlessly. Outstanding professionals."</p>
          <p class="testimonial-author text-white mt-3"><strong>- Elena R.</strong>, VP Expansion, Global Logistics Corp</p>
          <div class="text-warning mt-2">★★★★★</div>
        </div>
        <div class="testimonial-slide">
          <p class="testimonial-text text-white">"Our previous accountants missed crucial GST updates that cost us heavily. Since shifting to Truvisory, our compliance is at 100%, and our Virtual CFO provides insights that actually drive revenue."</p>
          <p class="testimonial-author text-white mt-3"><strong>- David K.</strong>, Founder, E-Comm Scale</p>
          <div class="text-warning mt-2">★★★★★</div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 11 - FAQs -->
  <section class="faq section-white section-padding" id="faq">
    <div class="container faq-container mx-auto">
      <h2 class="section-title text-center fade-up">Expert Answers to Critical Questions</h2>
      
      <div class="faq-tabs text-center mb-5 fade-up">
        <button class="faq-tab active" data-target="formation">Formation & Compliance</button>
        <button class="faq-tab" data-target="tax">Tax & Accounting</button>
        <button class="faq-tab" data-target="international">International Business</button>
      </div>

      <div class="accordion fade-up">
        <!-- Formation & Compliance -->
        <div class="accordion-item">
          <button class="accordion-header">What is the difference between an LLP and a Private Limited Company?</button>
          <div class="accordion-content">
            <p>A Private Limited Company allows for the issuance of equity shares and is the preferred structure if you plan to raise venture capital. An LLP (Limited Liability Partnership) offers limited liability protection but is managed via a partnership agreement, making it suitable for closely-held professional firms not seeking external equity funding.</p>
          </div>
        </div>
        <div class="accordion-item">
          <button class="accordion-header">How long does it take to register a trademark?</button>
          <div class="accordion-content">
            <p>Filing the application takes 1-3 days, granting you the right to use the "TM" symbol. However, the complete registration process by the Registry, assuming no objections, typically takes 6 to 12 months before you receive the final certification and can use the "®" symbol.</p>
          </div>
        </div>
        <div class="accordion-item">
          <button class="accordion-header">What does a Virtual CFO actually do for my startup?</button>
          <div class="accordion-content">
            <p>A Virtual CFO goes beyond basic bookkeeping. We provide high-level financial strategy, cash flow forecasting, budget vs. actuals variance analysis, unit economics optimization, and we prepare and present financial decks for board meetings and potential investors.</p>
          </div>
        </div>
        <div class="accordion-item">
          <button class="accordion-header">What are the mandatory annual compliances for a Pvt Ltd company?</button>
          <div class="accordion-content">
            <p>Mandatory compliances include conducting minimum 4 Board Meetings, 1 Annual General Meeting (AGM), filing form AOC-4 (Financial Statements) and MGT-7 (Annual Return) with the ROC, statutory audit by a CA, and filing of Income Tax Returns (ITR-6).</p>
          </div>
        </div>

        <!-- Tax & Accounting -->
        <div class="accordion-item">
          <button class="accordion-header">When is GST Registration mandatory?</button>
          <div class="accordion-content">
            <p>GST registration is mandatory for businesses supplying goods whose turnover exceeds ₹40 Lakhs (₹20 Lakhs in special category states), or businesses supplying services exceeding ₹20 Lakhs (₹10 Lakhs in special states). It is also mandatory for all e-commerce sellers and entities involved in inter-state supply, regardless of turnover.</p>
          </div>
        </div>
        <div class="accordion-item">
          <button class="accordion-header">How can we optimize our Corporate Tax liability?</button>
          <div class="accordion-content">
            <p>Optimization involves adopting the concessional tax regimes (like Section 115BAA in India offering a 22% base rate), restructuring executive compensation, maximizing R&D depreciation benefits, and ensuring robust transfer pricing policies for inter-company transactions.</p>
          </div>
        </div>
        
        <!-- International -->
        <div class="accordion-item">
          <button class="accordion-header">What is FEMA compliance for foreign subsidiaries in India?</button>
          <div class="accordion-content">
            <p>The Foreign Exchange Management Act (FEMA) regulates foreign direct investment (FDI). If you inject capital into an Indian subsidiary from abroad, you must file the Advance Remittance Form (ARF) within 30 days and the FC-GPR form within 30 days of allotting shares to the foreign parent.</p>
          </div>
        </div>
        <div class="accordion-item">
          <button class="accordion-header">Which UAE jurisdiction is best: Free Zone or Mainland?</button>
          <div class="accordion-content">
            <p>Free Zones are ideal for businesses intending to trade internationally or provide services outside the UAE, offering 100% foreign ownership and easier setups. Mainland companies are necessary if you intend to trade directly with the local UAE market or participate in government tenders.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 12 - Final CTA -->
  <section class="bottom-cta section-light section-padding text-center border-top-light" id="schedule">
    <div class="container cta-container fade-up">
      <h2 class="main-title text-navy mb-3">Secure Your Financial Future. Scale with Certainty.</h2>
      <p class="cta-subtext mb-4">Partner with Truvisory to eliminate compliance risk and unlock strategic financial insights. Let our experts architect the foundation for your next phase of growth.</p>
      <div class="cta-actions">
        <a href="contact.html" class="btn btn-primary cta-btn">Book Your Free Strategic Consultation</a>
        <a href="mailto:expert@truvisory.com" class="link-navy mt-3 d-block font-weight-500">Or email us directly to request a custom quote &rarr;</a>
      </div>
    </div>
  </section>

  <!-- Footer (Expanded) -->
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col">
          <a href="index.html" class="logo footer-logo mb-3">
            <img src="assets/images/logo.png" alt="Truvisory Services" class="logo-img" style="height: 60px;">
          </a>
          <p class="footer-desc mt-3">Truvisory Financial Services Pvt. Ltd. delivers elite, end-to-end corporate advisory, international structuring, and stringent tax compliance for the world's most ambitious enterprises.</p>
        </div>
        
        <div class="footer-col">
          <h4>Corporate Services</h4>
          <ul>
            <li><a href="services.html#setup">Entity Formation</a></li>
            <li><a href="services.html#accounting">Audit & Assurance</a></li>
            <li><a href="services.html#tax">Corporate Tax Advisory</a></li>
            <li><a href="services.html#cfo">Virtual CFO Services</a></li>
            <li><a href="services.html#compliance">Regulatory Compliance</a></li>
            <li><a href="services.html#trademark">Intellectual Property</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Global Desks</h4>
          <ul>
            <li><a href="countries.html#india">India Entry Strategy</a></li>
            <li><a href="countries.html#uae">UAE Free Zones</a></li>
            <li><a href="countries.html#singapore">Singapore Hub</a></li>
            <li><a href="countries.html#uk">UK & Europe</a></li>
            <li><a href="countries.html#us">United States</a></li>
          </ul>
        </div>
        
        <div class="footer-col">
          <h4>Insights & Support</h4>
          <ul>
            <li><a href="about.html">Our Leadership</a></li>
            <li><a href="insights.html">Tax & Regulatory Updates</a></li>
            <li><a href="resources.html">Whitepapers & Guides</a></li>
            <li><a href="#faq">Knowledge Base / FAQs</a></li>
            <li><a href="careers.html">Careers at Truvisory</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Contact & Legal</h4>
          <ul>
            <li><strong>Email:</strong> advisory@truvisory.com</li>
            <li><strong>Phone:</strong> +91 (22) 4567 8900</li>
            <li><strong>HQ:</strong> BKC, Mumbai, India</li>
            <li><strong>Hours:</strong> Mon - Fri, 9 AM - 6 PM</li>
            <li class="mt-3"><a href="privacy.html" class="text-slate" style="font-size:0.8rem;">Privacy Policy</a></li>
            <li><a href="terms.html" class="text-slate" style="font-size:0.8rem;">Terms & Conditions</a></li>
            <li><a href="refund.html" class="text-slate" style="font-size:0.8rem;">Refund Policy</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom mt-4">
        <p>&copy; 2026 Truvisory Financial Services Pvt. Ltd. All rights reserved.</p>
        <div class="footer-network">
          <a href="#">LinkedIn</a>
          <a href="#">Twitter/X</a>
          <a href="#">YouTube</a>
        </div>
      </div>
    </div>
  </footer>
"""

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(header_part + new_content + floating_ui)
        
    print("Updated index.html successfully with final premium copy.")

if __name__ == "__main__":
    update_index_html_final()
