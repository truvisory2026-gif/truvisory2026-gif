# -*- coding: utf-8 -*-
import os
import re

# 1. Update Global Navigation in all HTML files
html_files = []
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    prefix = ""
    depth = filepath.count(os.sep) - 1
    if depth > 0:
        prefix = "../" * depth
        
    old_nav = r'<div class="nav-actions">.*?<a href="[^"]*contact\.html" class="btn btn-primary">Book Consultation</a>.*?</div>'
    new_nav = f'''<div class="nav-actions" style="display: flex; gap: 15px; align-items: center;">
                <a href="{prefix}login.html" class="btn btn-outline" style="padding: 10px 20px; font-weight: 500; border-color: rgba(255,255,255,0.2);">Login / Sign Up</a>
                <a href="{prefix}contact.html" class="btn btn-primary">Book Consultation</a>
            </div>'''
            
    if 'Login / Sign Up' not in content:
        new_content = re.sub(old_nav, new_nav, content, flags=re.DOTALL)
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated Navigation in {filepath}")

# 2. Rewrite Why Us
why_us_main = '''
  <main>
    <section class="page-header" style="padding-top: 150px; text-align: center; margin-bottom: 50px;">
        <div class="container reveal">
            <h1 class="gradient-text">Why Choose Truvisory?</h1>
            <h3 style="color: white; margin-top: 10px;">Your Trusted Partner for Growth</h3>
        </div>
    </section>

    <section style="padding-bottom: 80px;">
        <div class="container">
            <div class="grid-3">
                <div class="glass-card reveal card-hover" style="text-align: center; padding: 40px 30px;">
                    <div class="card-icon" style="color: var(--primary); font-size: 2.5rem; margin-bottom: 20px;"><i class="fa-solid fa-earth-americas"></i></div>
                    <h3 style="color: #fff; margin-bottom: 15px;">Global Business Expertise</h3>
                    <p style="color: var(--text-muted); line-height: 1.6;">We have extensive experience in setting up and scaling businesses across multiple international jurisdictions including the US, UAE, Singapore, and UK.</p>
                </div>
                <div class="glass-card reveal card-hover delay-1" style="text-align: center; padding: 40px 30px;">
                    <div class="card-icon" style="color: var(--primary); font-size: 2.5rem; margin-bottom: 20px;"><i class="fa-solid fa-shield-check"></i></div>
                    <h3 style="color: #fff; margin-bottom: 15px;">End-to-End Compliance</h3>
                    <p style="color: var(--text-muted); line-height: 1.6;">From initial incorporation to monthly tax filings and annual audits, we handle 100% of your regulatory compliance so you can focus on growth.</p>
                </div>
                <div class="glass-card reveal card-hover delay-2" style="text-align: center; padding: 40px 30px;">
                    <div class="card-icon" style="color: var(--primary); font-size: 2.5rem; margin-bottom: 20px;"><i class="fa-solid fa-users"></i></div>
                    <h3 style="color: #fff; margin-bottom: 15px;">Dedicated Financial Advisors</h3>
                    <p style="color: var(--text-muted); line-height: 1.6;">Every client is assigned a dedicated relationship manager and a team of Chartered Accountants who act as a true extension of your business.</p>
                </div>
                <div class="glass-card reveal card-hover" style="text-align: center; padding: 40px 30px;">
                    <div class="card-icon" style="color: var(--primary); font-size: 2.5rem; margin-bottom: 20px;"><i class="fa-solid fa-scale-balanced"></i></div>
                    <h3 style="color: #fff; margin-bottom: 15px;">Transparent Pricing</h3>
                    <p style="color: var(--text-muted); line-height: 1.6;">No hidden fees. We believe in complete transparency, providing clear cost structures before we begin any engagement.</p>
                </div>
                <div class="glass-card reveal card-hover delay-1" style="text-align: center; padding: 40px 30px;">
                    <div class="card-icon" style="color: var(--primary); font-size: 2.5rem; margin-bottom: 20px;"><i class="fa-solid fa-medal"></i></div>
                    <h3 style="color: #fff; margin-bottom: 15px;">15+ Years of Experience</h3>
                    <p style="color: var(--text-muted); line-height: 1.6;">Led by seasoned industry professionals, our team brings decades of combined experience in taxation, law, and corporate finance.</p>
                </div>
                <div class="glass-card reveal card-hover delay-2" style="text-align: center; padding: 40px 30px;">
                    <div class="card-icon" style="color: var(--primary); font-size: 2.5rem; margin-bottom: 20px;"><i class="fa-solid fa-handshake-angle"></i></div>
                    <h3 style="color: #fff; margin-bottom: 15px;">500+ Businesses Served</h3>
                    <p style="color: var(--text-muted); line-height: 1.6;">Join a growing community of successful entrepreneurs, startups, and large enterprises who trust Truvisory with their financial foundations.</p>
                </div>
            </div>
        </div>
    </section>
  </main>
'''

with open('why-truvisory.html', 'r', encoding='utf-8') as f:
    content = f.read()
new_content = re.sub(r'<main>.*?</main>', why_us_main, content, flags=re.DOTALL)
with open('why-truvisory.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated why-truvisory.html")

# 3. Rewrite Testimonials
testimonials_main = '''
  <main>
    <section class="page-header" style="padding-top: 150px; text-align: center; margin-bottom: 50px;">
        <div class="container reveal">
            <h1 class="gradient-text">Client Testimonials</h1>
            <h3 style="color: white; margin-top: 10px;">Hear From Businesses We've Helped Grow</h3>
        </div>
    </section>

    <section style="padding-bottom: 80px;">
        <div class="container">
            <div class="grid-2">
                
                <div class="glass-card reveal" style="padding: 40px;">
                    <div style="color: #FFD700; font-size: 1.2rem; margin-bottom: 20px;">
                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                    </div>
                    <p style="color: #fff; font-size: 1.1rem; line-height: 1.8; margin-bottom: 30px; font-style: italic;">
                        "Truvisory made our expansion into the UAE incredibly seamless. What seemed like a daunting maze of regulatory requirements was handled with absolute precision. Their team took care of the incorporation, tax structuring, and compliance, allowing us to focus purely on business strategy. Truly exceptional service."
                    </p>
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="width: 50px; height: 50px; background: var(--primary); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; color: #fff; font-size: 1.2rem;">R</div>
                        <div>
                            <h4 style="color: #fff; margin: 0;">Rajesh Kumar</h4>
                            <p style="color: var(--text-muted); margin: 0; font-size: 0.9rem;">CEO, TechVentures Logistics</p>
                        </div>
                    </div>
                </div>

                <div class="glass-card reveal delay-1" style="padding: 40px;">
                    <div style="color: #FFD700; font-size: 1.2rem; margin-bottom: 20px;">
                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                    </div>
                    <p style="color: #fff; font-size: 1.1rem; line-height: 1.8; margin-bottom: 30px; font-style: italic;">
                        "As a rapidly growing SaaS startup, we needed a robust Virtual CFO to manage our burn rate and fundraising audits. Truvisory stepped in and completely transformed our financial reporting. Their CA team is highly responsive, deeply knowledgeable, and operates just like an internal finance team."
                    </p>
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="width: 50px; height: 50px; background: var(--primary); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; color: #fff; font-size: 1.2rem;">S</div>
                        <div>
                            <h4 style="color: #fff; margin: 0;">Sarah Jenkins</h4>
                            <p style="color: var(--text-muted); margin: 0; font-size: 0.9rem;">Founder, CloudSync Solutions</p>
                        </div>
                    </div>
                </div>

                <div class="glass-card reveal" style="padding: 40px;">
                    <div style="color: #FFD700; font-size: 1.2rem; margin-bottom: 20px;">
                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                    </div>
                    <p style="color: #fff; font-size: 1.1rem; line-height: 1.8; margin-bottom: 30px; font-style: italic;">
                        "We transitioned our entire payroll and GST compliance to Truvisory two years ago, and we have never looked back. Their dedication to accuracy and transparent pricing is refreshing. We never miss a deadline, and their advisory on corporate tax has saved us a significant amount of capital."
                    </p>
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="width: 50px; height: 50px; background: var(--primary); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; color: #fff; font-size: 1.2rem;">A</div>
                        <div>
                            <h4 style="color: #fff; margin: 0;">Amit Desai</h4>
                            <p style="color: var(--text-muted); margin: 0; font-size: 0.9rem;">Director, Desai Manufacturing Group</p>
                        </div>
                    </div>
                </div>

                <div class="glass-card reveal delay-1" style="padding: 40px;">
                    <div style="color: #FFD700; font-size: 1.2rem; margin-bottom: 20px;">
                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                    </div>
                    <p style="color: #fff; font-size: 1.1rem; line-height: 1.8; margin-bottom: 30px; font-style: italic;">
                        "The international tax planning provided by Truvisory was a game-changer for our e-commerce business. They helped us establish a highly efficient holding structure in Singapore while maintaining full compliance in India. Highly recommended for any business looking to cross borders."
                    </p>
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="width: 50px; height: 50px; background: var(--primary); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; color: #fff; font-size: 1.2rem;">E</div>
                        <div>
                            <h4 style="color: #fff; margin: 0;">Elena Rostova</h4>
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
new_content = re.sub(r'<main>.*?</main>', testimonials_main, content, flags=re.DOTALL)
with open('testimonials.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated testimonials.html")


# 4. Create Login and Signup Pages
# First, extract top_nav and mega_footer from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

top_part = idx_content.split('<main>')[0]
bottom_part = idx_content.split('</main>')[1]

auth_css = '''
<style>
.auth-container {
    max-width: 500px;
    margin: 0 auto;
    padding: 50px;
}
.auth-title {
    text-align: center;
    margin-bottom: 30px;
}
.auth-form .form-group {
    margin-bottom: 20px;
}
.auth-form label {
    display: block;
    color: #fff;
    margin-bottom: 8px;
    font-size: 0.9rem;
}
.auth-form input {
    width: 100%;
    background: rgba(0,0,0,0.5);
    border: 1px solid rgba(255,255,255,0.1);
    padding: 12px 15px;
    border-radius: 8px;
    color: #fff;
    font-family: inherit;
    transition: border-color 0.3s;
}
.auth-form input:focus {
    outline: none;
    border-color: var(--primary);
}
.auth-btn {
    width: 100%;
    padding: 12px;
    background: var(--primary);
    color: #fff;
    border: none;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    margin-top: 10px;
    transition: background 0.3s;
}
.auth-btn:hover {
    background: #0056b3;
}
.auth-links {
    text-align: center;
    margin-top: 25px;
    font-size: 0.9rem;
}
.auth-links a {
    color: var(--primary);
    text-decoration: none;
    font-weight: 500;
}
.auth-links a:hover {
    text-decoration: underline;
}
</style>
'''

login_main = f'''
  <main style="padding-top: 150px; padding-bottom: 80px; min-height: 80vh; display: flex; align-items: center;">
    {auth_css}
    <div class="container">
        <div class="glass-card auth-container reveal">
            <h2 class="auth-title gradient-text">Welcome Back</h2>
            <p style="text-align: center; color: var(--text-muted); margin-bottom: 30px;">Login to access your client portal</p>
            
            <form class="auth-form" action="#" method="POST">
                <div class="form-group">
                    <label>Email Address</label>
                    <input type="email" placeholder="name@company.com" required>
                </div>
                <div class="form-group">
                    <label style="display: flex; justify-content: space-between;">
                        <span>Password</span>
                        <a href="#" style="color: var(--primary); text-decoration: none;">Forgot?</a>
                    </label>
                    <input type="password" placeholder="Enter your password" required>
                </div>
                <button type="submit" class="auth-btn">Login</button>
            </form>
            
            <div class="auth-links">
                <p style="color: var(--text-muted);">Don't have an account? <a href="signup.html">Sign Up</a></p>
            </div>
        </div>
    </div>
  </main>
'''

signup_main = f'''
  <main style="padding-top: 150px; padding-bottom: 80px; min-height: 80vh; display: flex; align-items: center;">
    {auth_css}
    <div class="container">
        <div class="glass-card auth-container reveal" style="max-width: 600px;">
            <h2 class="auth-title gradient-text">Create an Account</h2>
            <p style="text-align: center; color: var(--text-muted); margin-bottom: 30px;">Join Truvisory to manage your compliance seamlessly</p>
            
            <form class="auth-form" action="#" method="POST">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                    <div class="form-group">
                        <label>First Name</label>
                        <input type="text" placeholder="John" required>
                    </div>
                    <div class="form-group">
                        <label>Last Name</label>
                        <input type="text" placeholder="Doe" required>
                    </div>
                </div>
                <div class="form-group">
                    <label>Company Name (Optional)</label>
                    <input type="text" placeholder="e.g. Acme Corp">
                </div>
                <div class="form-group">
                    <label>Email Address</label>
                    <input type="email" placeholder="name@company.com" required>
                </div>
                <div class="form-group">
                    <label>Phone Number</label>
                    <input type="tel" placeholder="+91 98765 43210" required>
                </div>
                <div class="form-group">
                    <label>Password</label>
                    <input type="password" placeholder="Create a strong password" required>
                </div>
                <button type="submit" class="auth-btn" style="margin-top: 20px;">Create Account</button>
            </form>
            
            <div class="auth-links">
                <p style="color: var(--text-muted);">Already have an account? <a href="login.html">Login</a></p>
            </div>
        </div>
    </div>
  </main>
'''

with open('login.html', 'w', encoding='utf-8') as f:
    f.write(top_part + login_main + bottom_part)
print("Created login.html")

with open('signup.html', 'w', encoding='utf-8') as f:
    f.write(top_part + signup_main + bottom_part)
print("Created signup.html")
