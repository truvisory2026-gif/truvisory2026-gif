# -*- coding: utf-8 -*-
import os
import re

why_us_main = '''
  <main id="main-content">
    <section class="page-header" style="padding-top: 150px; text-align: center; margin-bottom: 50px;">
        <div class="container reveal">
            <h1 class="gradient-text">Why Choose Truvisory?</h1>
            <h3 style="color: white; margin-top: 10px;">Your Trusted Partner for Growth</h3>
        </div>
    </section>

    <section style="padding-bottom: 80px;">
        <div class="container">
            <div class="grid-3" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
                <div class="glass-card reveal card-hover" style="text-align: center; padding: 40px 30px; border-top: 4px solid var(--primary);">
                    <div class="card-icon" style="color: var(--primary); font-size: 2.5rem; margin-bottom: 20px;"><i class="fa-solid fa-earth-americas"></i></div>
                    <h3 style="color: #fff; margin-bottom: 15px; font-size: 1.3rem;">Global Business Expertise</h3>
                    <p style="color: var(--text-muted); line-height: 1.6;">We have extensive experience in setting up and scaling businesses across multiple international jurisdictions including the US, UAE, Singapore, and UK.</p>
                </div>
                <div class="glass-card reveal card-hover delay-1" style="text-align: center; padding: 40px 30px; border-top: 4px solid var(--primary);">
                    <div class="card-icon" style="color: var(--primary); font-size: 2.5rem; margin-bottom: 20px;"><i class="fa-solid fa-shield-halved"></i></div>
                    <h3 style="color: #fff; margin-bottom: 15px; font-size: 1.3rem;">End-to-End Compliance</h3>
                    <p style="color: var(--text-muted); line-height: 1.6;">From initial incorporation to monthly tax filings and annual audits, we handle 100% of your regulatory compliance so you can focus on growth.</p>
                </div>
                <div class="glass-card reveal card-hover delay-2" style="text-align: center; padding: 40px 30px; border-top: 4px solid var(--primary);">
                    <div class="card-icon" style="color: var(--primary); font-size: 2.5rem; margin-bottom: 20px;"><i class="fa-solid fa-users"></i></div>
                    <h3 style="color: #fff; margin-bottom: 15px; font-size: 1.3rem;">Dedicated Financial Advisors</h3>
                    <p style="color: var(--text-muted); line-height: 1.6;">Every client is assigned a dedicated relationship manager and a team of Chartered Accountants who act as a true extension of your business.</p>
                </div>
                <div class="glass-card reveal card-hover" style="text-align: center; padding: 40px 30px; border-top: 4px solid var(--primary);">
                    <div class="card-icon" style="color: var(--primary); font-size: 2.5rem; margin-bottom: 20px;"><i class="fa-solid fa-scale-balanced"></i></div>
                    <h3 style="color: #fff; margin-bottom: 15px; font-size: 1.3rem;">Transparent Pricing</h3>
                    <p style="color: var(--text-muted); line-height: 1.6;">No hidden fees. We believe in complete transparency, providing clear cost structures before we begin any engagement.</p>
                </div>
                <div class="glass-card reveal card-hover delay-1" style="text-align: center; padding: 40px 30px; border-top: 4px solid var(--primary);">
                    <div class="card-icon" style="color: var(--primary); font-size: 2.5rem; margin-bottom: 20px;"><i class="fa-solid fa-medal"></i></div>
                    <h3 style="color: #fff; margin-bottom: 15px; font-size: 1.3rem;">15+ Years of Experience</h3>
                    <p style="color: var(--text-muted); line-height: 1.6;">Led by seasoned industry professionals, our team brings decades of combined experience in taxation, law, and corporate finance.</p>
                </div>
                <div class="glass-card reveal card-hover delay-2" style="text-align: center; padding: 40px 30px; border-top: 4px solid var(--primary);">
                    <div class="card-icon" style="color: var(--primary); font-size: 2.5rem; margin-bottom: 20px;"><i class="fa-solid fa-handshake-angle"></i></div>
                    <h3 style="color: #fff; margin-bottom: 15px; font-size: 1.3rem;">500+ Businesses Served</h3>
                    <p style="color: var(--text-muted); line-height: 1.6;">Join a growing community of successful entrepreneurs, startups, and large enterprises who trust Truvisory with their financial foundations.</p>
                </div>
            </div>
        </div>
    </section>
  </main>
'''

with open('why-truvisory.html', 'r', encoding='utf-8') as f:
    content = f.read()
new_content = re.sub(r'<main.*?</main>', why_us_main, content, flags=re.DOTALL)
with open('why-truvisory.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated why-truvisory.html")

testimonials_main = '''
  <main id="main-content">
    <section class="page-header" style="padding-top: 150px; text-align: center; margin-bottom: 50px;">
        <div class="container reveal">
            <h1 class="gradient-text">Client Testimonials</h1>
            <h3 style="color: white; margin-top: 10px;">Hear From Businesses We've Helped Grow</h3>
        </div>
    </section>

    <section style="padding-bottom: 80px;">
        <div class="container">
            <div class="grid-2" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 40px;">
                
                <div class="glass-card reveal card-hover" style="padding: 40px; border-top: 4px solid var(--primary);">
                    <div style="color: #FFD700; font-size: 1.2rem; margin-bottom: 20px;">
                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                    </div>
                    <p style="color: #fff; font-size: 1.1rem; line-height: 1.8; margin-bottom: 30px; font-style: italic;">
                        "Truvisory made our expansion into the UAE incredibly seamless. What seemed like a daunting maze of regulatory requirements was handled with absolute precision. Their team took care of the incorporation, tax structuring, and compliance, allowing us to focus purely on business strategy. Truly exceptional service."
                    </p>
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="width: 50px; height: 50px; background: var(--primary); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; color: #fff; font-size: 1.2rem;">R</div>
                        <div>
                            <h4 style="color: #fff; margin: 0; font-size: 1.1rem;">Rajesh Kumar</h4>
                            <p style="color: var(--text-muted); margin: 0; font-size: 0.9rem;">CEO, TechVentures Logistics</p>
                        </div>
                    </div>
                </div>

                <div class="glass-card reveal card-hover delay-1" style="padding: 40px; border-top: 4px solid var(--primary);">
                    <div style="color: #FFD700; font-size: 1.2rem; margin-bottom: 20px;">
                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                    </div>
                    <p style="color: #fff; font-size: 1.1rem; line-height: 1.8; margin-bottom: 30px; font-style: italic;">
                        "As a rapidly growing SaaS startup, we needed a robust Virtual CFO to manage our burn rate and fundraising audits. Truvisory stepped in and completely transformed our financial reporting. Their CA team is highly responsive, deeply knowledgeable, and operates just like an internal finance team."
                    </p>
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="width: 50px; height: 50px; background: var(--primary); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; color: #fff; font-size: 1.2rem;">S</div>
                        <div>
                            <h4 style="color: #fff; margin: 0; font-size: 1.1rem;">Sarah Jenkins</h4>
                            <p style="color: var(--text-muted); margin: 0; font-size: 0.9rem;">Founder, CloudSync Solutions</p>
                        </div>
                    </div>
                </div>

                <div class="glass-card reveal card-hover" style="padding: 40px; border-top: 4px solid var(--primary);">
                    <div style="color: #FFD700; font-size: 1.2rem; margin-bottom: 20px;">
                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                    </div>
                    <p style="color: #fff; font-size: 1.1rem; line-height: 1.8; margin-bottom: 30px; font-style: italic;">
                        "We transitioned our entire payroll and GST compliance to Truvisory two years ago, and we have never looked back. Their dedication to accuracy and transparent pricing is refreshing. We never miss a deadline, and their advisory on corporate tax has saved us a significant amount of capital."
                    </p>
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="width: 50px; height: 50px; background: var(--primary); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; color: #fff; font-size: 1.2rem;">A</div>
                        <div>
                            <h4 style="color: #fff; margin: 0; font-size: 1.1rem;">Amit Desai</h4>
                            <p style="color: var(--text-muted); margin: 0; font-size: 0.9rem;">Director, Desai Manufacturing Group</p>
                        </div>
                    </div>
                </div>

                <div class="glass-card reveal card-hover delay-1" style="padding: 40px; border-top: 4px solid var(--primary);">
                    <div style="color: #FFD700; font-size: 1.2rem; margin-bottom: 20px;">
                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                    </div>
                    <p style="color: #fff; font-size: 1.1rem; line-height: 1.8; margin-bottom: 30px; font-style: italic;">
                        "The international tax planning provided by Truvisory was a game-changer for our e-commerce business. They helped us establish a highly efficient holding structure in Singapore while maintaining full compliance in India. Highly recommended for any business looking to cross borders."
                    </p>
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="width: 50px; height: 50px; background: var(--primary); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; color: #fff; font-size: 1.2rem;">E</div>
                        <div>
                            <h4 style="color: #fff; margin: 0; font-size: 1.1rem;">Elena Rostova</h4>
                            <p style="color: var(--text-muted); margin: 0; font-size: 0.9rem;">Co-Founder, GlobalGoods Retail</p>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>
  </main>
'''

with open('testimonials.html', 'r', encoding='utf-8') as f:
    content = f.read()
new_content = re.sub(r'<main.*?</main>', testimonials_main, content, flags=re.DOTALL)
with open('testimonials.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated testimonials.html")
