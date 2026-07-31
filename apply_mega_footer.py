# -*- coding: utf-8 -*-
import os
import re

css_additions = '''
/* --- MEGA FOOTER --- */
.mega-footer {
    background: #06110f;
    color: var(--text-muted);
    padding: 80px 0 30px;
    border-top: 1px solid rgba(255,255,255,0.05);
    font-size: 0.95rem;
    position: relative;
    z-index: 10;
}

.mega-footer a {
    color: var(--text-muted);
    text-decoration: none;
    transition: color 0.3s ease;
}

.mega-footer a:hover {
    color: var(--primary);
}

.footer-top {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr 1fr;
    gap: 40px;
    margin-bottom: 50px;
}

.footer-col h4 {
    color: #fff;
    font-size: 1.2rem;
    margin-bottom: 25px;
    font-weight: 600;
}

.footer-col ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.footer-col ul li {
    margin-bottom: 12px;
}

/* Column 1 */
.footer-brand {
    margin-bottom: 25px;
}
.footer-contact-list {
    margin: 25px 0;
}
.footer-contact-list li {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    margin-bottom: 15px;
}
.footer-contact-list i {
    color: var(--primary);
    margin-top: 5px;
}
.newsletter-box {
    margin-top: 30px;
    background: rgba(255,255,255,0.03);
    padding: 20px;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.05);
}
.newsletter-box h5 {
    color: #fff;
    margin-bottom: 10px;
    font-size: 1rem;
}
.newsletter-form {
    display: flex;
    gap: 10px;
    margin-top: 15px;
}
.newsletter-form input {
    flex: 1;
    background: rgba(0,0,0,0.5);
    border: 1px solid rgba(255,255,255,0.1);
    color: #fff;
    padding: 10px 15px;
    border-radius: 6px;
    outline: none;
}
.newsletter-form button {
    background: var(--primary);
    color: #fff;
    border: none;
    padding: 10px 20px;
    border-radius: 6px;
    cursor: pointer;
    font-weight: 600;
}
.social-icons {
    display: flex;
    gap: 15px;
    margin-top: 25px;
}
.social-icons a {
    width: 40px;
    height: 40px;
    background: rgba(255,255,255,0.05);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
    color: #fff;
    transition: all 0.3s ease;
}
.social-icons a:hover {
    background: var(--primary);
    transform: translateY(-3px);
}

/* Badges Row */
.footer-badges {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    gap: 20px;
    padding: 30px 0;
    border-top: 1px solid rgba(255,255,255,0.05);
    border-bottom: 1px solid rgba(255,255,255,0.05);
    margin-bottom: 30px;
}
.badge-item {
    display: flex;
    align-items: center;
    gap: 10px;
    background: rgba(255,255,255,0.03);
    padding: 10px 20px;
    border-radius: 30px;
    font-size: 0.9rem;
}
.badge-item i {
    color: var(--primary);
}

/* Footer Bottom */
.footer-bottom-mega {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 20px;
}
.legal-links {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
}

/* Responsive */
@media (max-width: 992px) {
    .footer-top {
        grid-template-columns: 1fr 1fr;
    }
}
@media (max-width: 576px) {
    .footer-top {
        grid-template-columns: 1fr;
    }
    .footer-bottom-mega {
        flex-direction: column;
        text-align: center;
    }
    .legal-links {
        justify-content: center;
    }
}

/* FLOATING WIDGETS */
.floating-whatsapp {
    position: fixed;
    bottom: 30px;
    right: 30px;
    background: #25D366;
    color: white !important;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 35px;
    box-shadow: 0 4px 15px rgba(37, 211, 102, 0.4);
    z-index: 999;
    transition: transform 0.3s ease;
}
.floating-whatsapp:hover {
    transform: scale(1.1);
}

.back-to-top {
    position: fixed;
    bottom: 30px;
    right: 110px;
    background: rgba(255,255,255,0.1);
    color: white !important;
    width: 45px;
    height: 45px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    z-index: 999;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.2);
    transition: all 0.3s ease;
    opacity: 0;
    pointer-events: none;
}
.back-to-top.visible {
    opacity: 1;
    pointer-events: auto;
}
.back-to-top:hover {
    background: var(--primary);
    border-color: var(--primary);
}
'''

# Append CSS if not exists
with open('assets/css/styles.css', 'r', encoding='utf-8') as f:
    css_content = f.read()
if 'MEGA FOOTER' not in css_content:
    with open('assets/css/styles.css', 'a', encoding='utf-8') as f:
        f.write("\n" + css_additions)
        print("Mega footer CSS added.")


# ----------------------------------------------------
# Mega Footer HTML Generator
# ----------------------------------------------------

def generate_mega_footer(prefix):
    return f'''
    <!-- MEGA FOOTER -->
    <footer class="mega-footer">
        <div class="container">
            <div class="footer-top">
                <!-- Column 1 -->
                <div class="footer-col">
                    <div class="footer-brand">
                        <a href="{prefix}index.html">
                            <img src="{prefix}assets/images/logo.png" alt="Truvisory Financial Services" style="height: 100px; transform: scale(1.5); transform-origin: left center;" width="auto" style="object-fit: contain;">
                        </a>
                        <p style="margin-top: 15px;">Your trusted partner for Global Business Setup, Company Incorporation, Taxation, Accounting, Compliance, Payroll, and Business Advisory.</p>
                    </div>
                    <ul class="footer-contact-list">
                        <li>
                            <i class="fa-solid fa-location-dot"></i>
                            <span>Corporate Office, Mumbai, India</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-phone"></i>
                            <span>+91 98765 43210</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-envelope"></i>
                            <span>truvisoryfinance@gmail.com</span>
                        </li>
                    </ul>
                    
                    <div class="newsletter-box">
                        <h5>Stay Updated</h5>
                        <p style="font-size: 0.85rem;">Tax Changes & Compliance Alerts</p>
                        <div class="newsletter-form">
                            <input type="email" placeholder="Email Address">
                            <button type="button">Subscribe</button>
                        </div>
                    </div>
                    
                    <div class="social-icons">
                        <a href="#"><i class="fa-brands fa-linkedin-in"></i></a>
                        <a href="#"><i class="fa-brands fa-facebook-f"></i></a>
                        <a href="#"><i class="fa-brands fa-instagram"></i></a>
                        <a href="#"><i class="fa-brands fa-x-twitter"></i></a>
                        <a href="#"><i class="fa-brands fa-youtube"></i></a>
                    </div>
                </div>
                
                <!-- Column 2 -->
                <div class="footer-col">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="{prefix}index.html">Home</a></li>
                        <li><a href="{prefix}about.html">About Us</a></li>
                        <li><a href="{prefix}services.html">Services</a></li>
                        <li><a href="{prefix}industries.html">Industries</a></li>
                        <li><a href="{prefix}countries.html">Global Presence</a></li>
                        <li><a href="{prefix}resources.html">Resources</a></li>
                        <li><a href="{prefix}why-truvisory.html">Why Us</a></li>
                        <li><a href="{prefix}testimonials.html">Testimonials</a></li>
                        <li><a href="{prefix}contact.html">Contact Us</a></li>
                        <li><a href="{prefix}contact.html">Careers</a></li>
                    </ul>
                    
                    <h4 style="margin-top: 30px;">Resources</h4>
                    <ul>
                        <li><a href="{prefix}resources.html">Business Guides</a></li>
                        <li><a href="{prefix}resources.html">Tax Calendar</a></li>
                        <li><a href="{prefix}resources.html">Compliance Calendar</a></li>
                        <li><a href="{prefix}resources.html">Download Brochures</a></li>
                        <li><a href="{prefix}resources.html">Success Stories</a></li>
                    </ul>
                </div>
                
                <!-- Column 3 -->
                <div class="footer-col">
                    <h4>Our Services</h4>
                    <ul>
                        <li><a href="{prefix}services/company-incorporation.html">Company Incorporation</a></li>
                        <li><a href="{prefix}services/overseas-business-setup.html">Overseas Business Setup</a></li>
                        <li><a href="{prefix}services/international-tax-planning.html">International Tax Planning</a></li>
                        <li><a href="{prefix}services/gst-vat.html">GST & VAT</a></li>
                        <li><a href="{prefix}services/corporate-tax.html">Corporate Tax</a></li>
                        <li><a href="{prefix}services/accounting-bookkeeping.html">Accounting & Bookkeeping</a></li>
                        <li><a href="{prefix}services/payroll.html">Payroll Services</a></li>
                        <li><a href="{prefix}services/compliance-management.html">Compliance Management</a></li>
                        <li><a href="{prefix}services/virtual-cfo.html">Virtual CFO</a></li>
                        <li><a href="{prefix}services/business-advisory.html">Business Advisory</a></li>
                        <li><a href="{prefix}services/franchise-expansion.html">Franchise Expansion</a></li>
                        <li><a href="{prefix}services/business-structuring.html">Business Structuring</a></li>
                    </ul>
                </div>
                
                <!-- Column 4 -->
                <div class="footer-col">
                    <h4>Industries We Serve</h4>
                    <ul>
                        <li><a href="{prefix}industries.html">Startups & SMEs</a></li>
                        <li><a href="{prefix}industries.html">Large Enterprises</a></li>
                        <li><a href="{prefix}industries.html">Manufacturing</a></li>
                        <li><a href="{prefix}industries.html">Healthcare</a></li>
                        <li><a href="{prefix}industries.html">Retail & E-commerce</a></li>
                        <li><a href="{prefix}industries.html">Technology</a></li>
                        <li><a href="{prefix}industries.html">Hospitality</a></li>
                        <li><a href="{prefix}industries.html">Logistics</a></li>
                        <li><a href="{prefix}industries.html">Construction & Real Estate</a></li>
                        <li><a href="{prefix}industries.html">Financial Services</a></li>
                    </ul>
                    
                    <h4 style="margin-top: 30px;">Countries We Support</h4>
                    <div style="display: flex; flex-wrap: wrap; gap: 10px;">
                        <a href="{prefix}countries.html" class="badge-item" style="border: 1px solid rgba(255,255,255,0.1); padding: 5px 12px; border-radius: 4px; font-size: 0.8rem;">India</a>
                        <a href="{prefix}countries/uae.html" class="badge-item" style="border: 1px solid rgba(255,255,255,0.1); padding: 5px 12px; border-radius: 4px; font-size: 0.8rem;">UAE</a>
                        <a href="{prefix}countries/usa.html" class="badge-item" style="border: 1px solid rgba(255,255,255,0.1); padding: 5px 12px; border-radius: 4px; font-size: 0.8rem;">USA</a>
                        <a href="{prefix}countries/singapore.html" class="badge-item" style="border: 1px solid rgba(255,255,255,0.1); padding: 5px 12px; border-radius: 4px; font-size: 0.8rem;">Singapore</a>
                        <a href="{prefix}countries/hong-kong.html" class="badge-item" style="border: 1px solid rgba(255,255,255,0.1); padding: 5px 12px; border-radius: 4px; font-size: 0.8rem;">Hong Kong</a>
                        <a href="{prefix}countries.html" class="badge-item" style="border: 1px solid rgba(255,255,255,0.1); padding: 5px 12px; border-radius: 4px; font-size: 0.8rem;">UK</a>
                        <a href="{prefix}countries.html" class="badge-item" style="border: 1px solid rgba(255,255,255,0.1); padding: 5px 12px; border-radius: 4px; font-size: 0.8rem;">Canada</a>
                        <a href="{prefix}countries.html" class="badge-item" style="border: 1px solid rgba(255,255,255,0.1); padding: 5px 12px; border-radius: 4px; font-size: 0.8rem;">Australia</a>
                        <a href="{prefix}countries.html" class="badge-item" style="border: 1px solid rgba(255,255,255,0.1); padding: 5px 12px; border-radius: 4px; font-size: 0.8rem;">Saudi Arabia</a>
                    </div>
                </div>
            </div>
            
            <div class="footer-badges">
                <div class="badge-item"><i class="fa-solid fa-certificate"></i> ISO Certified</div>
                <div class="badge-item"><i class="fa-solid fa-shield-halved"></i> Data Privacy Compliance</div>
                <div class="badge-item"><i class="fa-solid fa-lock"></i> Secure Payments</div>
                <div class="badge-item"><i class="fa-solid fa-landmark"></i> Government Registered</div>
                <div class="badge-item"><i class="fa-solid fa-building-circle-check"></i> MSME/Udyam Registered</div>
            </div>
            
            <div class="footer-bottom-mega">
                <div>&copy; 2026 Truvisory Financial Services. All Rights Reserved.</div>
                <div class="legal-links">
                    <a href="#">Privacy Policy</a>
                    <a href="#">Terms & Conditions</a>
                    <a href="#">Cookie Policy</a>
                    <a href="#">Disclaimer</a>
                    <a href="#">Sitemap</a>
                </div>
            </div>
        </div>
    </footer>
    
    <!-- Floating Widgets -->
    <a href="https://wa.me/919876543210" target="_blank" class="floating-whatsapp" aria-label="Chat on WhatsApp">
        <i class="fa-brands fa-whatsapp"></i>
    </a>
    <a href="#" class="back-to-top" id="backToTopMega" aria-label="Back to top">
        <i class="fa-solid fa-arrow-up"></i>
    </a>
    
    <script>
        // Back to top behavior
        window.addEventListener('scroll', function() {{
            var btn = document.getElementById('backToTopMega');
            if(btn) {{
                if (window.scrollY > 300) {{
                    btn.classList.add('visible');
                }} else {{
                    btn.classList.remove('visible');
                }}
            }}
        }});
        document.getElementById('backToTopMega')?.addEventListener('click', function(e) {{
            e.preventDefault();
            window.scrollTo({{top: 0, behavior: 'smooth'}});
        }});
    </script>
'''

html_files = []
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

# We will replace <footer class="footer">...</footer> with mega footer
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    prefix = ""
    depth = filepath.count(os.sep) - 1 # os.path.join gives .\index.html, depth=0
    if depth > 0:
        prefix = "../" * depth
        
    mega = generate_mega_footer(prefix)
    
    # We replace from <footer class="footer"> to </footer>
    if '<footer class="footer">' in content:
        import re
        new_content = re.sub(r'<footer class="footer">.*?</footer>', mega, content, flags=re.DOTALL)
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
