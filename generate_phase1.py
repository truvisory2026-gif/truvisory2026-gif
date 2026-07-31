import os
import re

# Read template
with open('index.html', 'r', encoding='utf-8') as f:
    template_content = f.read()

# Extract header and footer
header_match = re.search(r'<header class="glass-nav".*?</header>', template_content, re.DOTALL)
footer_match = re.search(r'<footer class="mega-footer".*?</footer>', template_content, re.DOTALL)

if not header_match or not footer_match:
    print("Could not find header or footer in index.html")
    exit(1)

base_header = header_match.group(0)
base_footer = footer_match.group(0)

# Function to adjust relative paths for subdirectory files (e.g., adding ../)
def adjust_paths_for_subdir(html_chunk):
    # Adjust asset paths
    html_chunk = html_chunk.replace('"assets/', '"../assets/')
    # Adjust root html links (assuming they all sit in root)
    html_chunk = re.sub(r'href="([^/"]+\.html)(#[^"]*)?"', r'href="../\1\2"', html_chunk)
    # Fix the hash link for contact if it's currently href="#contact"
    html_chunk = html_chunk.replace('href="#contact"', 'href="../index.html#contact"')
    return html_chunk

header_subdir = adjust_paths_for_subdir(base_header)
footer_subdir = adjust_paths_for_subdir(base_footer)

pages = [
    {
        "filepath": "careers/our-culture.html",
        "title": "Our Culture - Truvisory Careers",
        "meta": "Discover the vibrant, inclusive, and growth-oriented culture at Truvisory. We believe in empowering our employees to achieve excellence.",
        "breadcrumb": "Home / Careers / Our Culture",
        "hero_title": "Our Culture",
        "hero_subtitle": "Fostering Innovation, Integrity, and Excellence.",
        "content": '''
        <div class="container" style="padding: 4rem 0;">
            <h2>Who We Are</h2>
            <p>At Truvisory, our culture is the bedrock of our success. We operate as a unified ecosystem of professionals dedicated to solving complex financial challenges. We celebrate diversity of thought, encourage continuous learning, and reward proactive problem-solving.</p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-top: 3rem;">
                <div class="glass-card" style="padding: 2rem;">
                    <h3><i class="fa-solid fa-users" style="color: var(--primary);"></i> Collaborative Environment</h3>
                    <p>No silos. We believe the best solutions come from cross-functional collaboration and open communication at all levels.</p>
                </div>
                <div class="glass-card" style="padding: 2rem;">
                    <h3><i class="fa-solid fa-arrow-trend-up" style="color: var(--primary);"></i> Continuous Growth</h3>
                    <p>We invest heavily in the professional development of our team members through certifications, workshops, and mentorship.</p>
                </div>
                <div class="glass-card" style="padding: 2rem;">
                    <h3><i class="fa-solid fa-scale-balanced" style="color: var(--primary);"></i> Work-Life Balance</h3>
                    <p>Excellence doesn't mean burnout. We support flexible arrangements to ensure our team remains healthy, focused, and motivated.</p>
                </div>
            </div>
            <div style="margin-top: 4rem; text-align: center;">
                <h2>Join Our Team</h2>
                <p style="margin-bottom: 2rem;">Ready to make an impact? Explore our current openings and take the next step in your career.</p>
                <a href="open-positions.html" class="btn btn-primary">View Open Positions</a>
            </div>
        </div>
        '''
    },
    {
        "filepath": "careers/employee-benefits.html",
        "title": "Employee Benefits - Truvisory",
        "meta": "Explore the comprehensive benefits package at Truvisory, including health coverage, retirement planning, and wellness programs.",
        "breadcrumb": "Home / Careers / Employee Benefits",
        "hero_title": "Employee Benefits",
        "hero_subtitle": "Comprehensive care for you and your family.",
        "content": '''
        <div class="container" style="padding: 4rem 0;">
            <h2>Investing in Our People</h2>
            <p>We understand that to attract and retain top talent, we must provide a holistic benefits package that addresses health, wealth, and wellbeing.</p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-top: 3rem;">
                <div class="glass-card" style="padding: 2rem;">
                    <h3>Healthcare & Wellness</h3>
                    <ul>
                        <li>Premium Medical, Dental, and Vision Insurance</li>
                        <li>Annual Executive Health Checkups</li>
                        <li>Mental Health Support & Therapy Allowances</li>
                        <li>Gym Memberships & Wellness Stipends</li>
                    </ul>
                </div>
                <div class="glass-card" style="padding: 2rem;">
                    <h3>Financial & Retirement</h3>
                    <ul>
                        <li>Competitive Base Salary & Performance Bonuses</li>
                        <li>Company-Matched Retirement Plans (401k/Equivalent)</li>
                        <li>Employee Stock Ownership Plan (ESOP) for eligible roles</li>
                        <li>Financial Planning Assistance</li>
                    </ul>
                </div>
                <div class="glass-card" style="padding: 2rem;">
                    <h3>Lifestyle & Time Off</h3>
                    <ul>
                        <li>Generous Paid Time Off (PTO) & Public Holidays</li>
                        <li>Comprehensive Maternity & Paternity Leave</li>
                        <li>Hybrid & Remote Work Options</li>
                        <li>Paid Sabbaticals for long-tenured employees</li>
                    </ul>
                </div>
            </div>
            <div style="margin-top: 4rem; text-align: center;">
                <h2>Experience the Difference</h2>
                <a href="apply.html" class="btn btn-primary">Apply Now</a>
            </div>
        </div>
        '''
    },
    {
        "filepath": "careers/open-positions.html",
        "title": "Open Positions - Truvisory",
        "meta": "Browse current job openings at Truvisory across our global offices. Apply today to join a world-class financial advisory firm.",
        "breadcrumb": "Home / Careers / Open Positions",
        "hero_title": "Open Positions",
        "hero_subtitle": "Find your next great opportunity.",
        "content": '''
        <div class="container" style="padding: 4rem 0;">
            <h2>Current Opportunities</h2>
            <p style="margin-bottom: 3rem;">Filter by department or location to find the perfect role for your skills.</p>
            
            <div style="display: flex; flex-direction: column; gap: 1.5rem;">
                <div class="glass-card" style="padding: 2rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                    <div>
                        <h3 style="margin-bottom: 0.5rem; color: var(--primary);">Senior Corporate Tax Advisor</h3>
                        <p style="margin-bottom: 0;">Department: Tax & Compliance | Location: Dubai, UAE | Type: Full-Time</p>
                    </div>
                    <a href="apply.html" class="btn btn-outline">Apply Now</a>
                </div>
                
                <div class="glass-card" style="padding: 2rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                    <div>
                        <h3 style="margin-bottom: 0.5rem; color: var(--primary);">Virtual CFO</h3>
                        <p style="margin-bottom: 0;">Department: Financial Advisory | Location: Remote/Singapore | Type: Full-Time</p>
                    </div>
                    <a href="apply.html" class="btn btn-outline">Apply Now</a>
                </div>

                <div class="glass-card" style="padding: 2rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                    <div>
                        <h3 style="margin-bottom: 0.5rem; color: var(--primary);">Business Setup Consultant</h3>
                        <p style="margin-bottom: 0;">Department: Incorporation | Location: Hong Kong | Type: Full-Time</p>
                    </div>
                    <a href="apply.html" class="btn btn-outline">Apply Now</a>
                </div>
            </div>
            
            <div style="margin-top: 4rem; text-align: center;">
                <h3>Don't see a fit?</h3>
                <p>We are always looking for exceptional talent. Submit your resume for future opportunities.</p>
                <a href="apply.html" class="btn btn-primary" style="margin-top: 1rem;">Submit General Application</a>
            </div>
        </div>
        '''
    },
    {
        "filepath": "careers/recruitment-process.html",
        "title": "Recruitment Process - Truvisory",
        "meta": "Learn about the transparent, multi-stage recruitment process at Truvisory designed to find the best fit for both you and us.",
        "breadcrumb": "Home / Careers / Recruitment Process",
        "hero_title": "Our Recruitment Process",
        "hero_subtitle": "Transparent, rigorous, and candidate-centric.",
        "content": '''
        <div class="container" style="padding: 4rem 0;">
            <h2>How We Hire</h2>
            <p>Our hiring process is designed to be a two-way street. We assess your skills and cultural fit, while giving you the opportunity to evaluate if Truvisory is the right home for your career.</p>
            
            <div class="process-timeline" style="margin-top: 3rem; display: flex; flex-direction: column; gap: 2rem;">
                <div class="glass-card" style="padding: 2rem; display: flex; gap: 2rem; align-items: flex-start;">
                    <div style="font-size: 3rem; color: var(--primary); font-weight: bold;">01</div>
                    <div>
                        <h3>Application & Resume Review</h3>
                        <p>Submit your application via our portal. Our Talent Acquisition team reviews every resume manually against the core competencies required for the role.</p>
                    </div>
                </div>
                <div class="glass-card" style="padding: 2rem; display: flex; gap: 2rem; align-items: flex-start;">
                    <div style="font-size: 3rem; color: var(--primary); font-weight: bold;">02</div>
                    <div>
                        <h3>Initial Screening Call</h3>
                        <p>A 30-minute introductory call with a recruiter to discuss your background, career aspirations, and basic alignment with our culture.</p>
                    </div>
                </div>
                <div class="glass-card" style="padding: 2rem; display: flex; gap: 2rem; align-items: flex-start;">
                    <div style="font-size: 3rem; color: var(--primary); font-weight: bold;">03</div>
                    <div>
                        <h3>Technical Assessment / Case Study</h3>
                        <p>Depending on the role, you may be asked to complete a technical test or present a business case study to demonstrate your practical expertise.</p>
                    </div>
                </div>
                <div class="glass-card" style="padding: 2rem; display: flex; gap: 2rem; align-items: flex-start;">
                    <div style="font-size: 3rem; color: var(--primary); font-weight: bold;">04</div>
                    <div>
                        <h3>Panel Interview</h3>
                        <p>A comprehensive interview with future team members and cross-functional stakeholders focusing on behavioral and situational questions.</p>
                    </div>
                </div>
                <div class="glass-card" style="padding: 2rem; display: flex; gap: 2rem; align-items: flex-start;">
                    <div style="font-size: 3rem; color: var(--primary); font-weight: bold;">05</div>
                    <div>
                        <h3>Final Interview & Offer</h3>
                        <p>A final conversation with a Partner or Director, followed by an official offer extension if there is a mutual fit.</p>
                    </div>
                </div>
            </div>
            
            <div style="margin-top: 4rem; text-align: center;">
                <h2>Ready to start the journey?</h2>
                <a href="open-positions.html" class="btn btn-primary">View Open Positions</a>
            </div>
        </div>
        '''
    },
    {
        "filepath": "careers/internships.html",
        "title": "Internship Opportunities - Truvisory",
        "meta": "Kickstart your career with Truvisory's global internship programs. Gain real-world experience in finance, taxation, and consulting.",
        "breadcrumb": "Home / Careers / Internships",
        "hero_title": "Internship Opportunities",
        "hero_subtitle": "Shape your future with hands-on experience.",
        "content": '''
        <div class="container" style="padding: 4rem 0;">
            <h2>Launch Your Career</h2>
            <p>Our internship programs are not about getting coffee. They are immersive, 10-week experiences where you will work on real client deliverables alongside seasoned industry experts.</p>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-top: 3rem;">
                <div class="glass-card" style="padding: 2rem;">
                    <h3>Summer Analyst Program</h3>
                    <p>A rigorous program for university juniors and seniors. Rotate through our core advisory, tax, and incorporation departments.</p>
                    <ul style="margin-top: 1rem;">
                        <li>Duration: 10-12 Weeks (Summer)</li>
                        <li>Mentorship from Senior Partners</li>
                        <li>Pathway to Full-Time Analyst Offer</li>
                    </ul>
                </div>
                <div class="glass-card" style="padding: 2rem;">
                    <h3>Off-Cycle Internships</h3>
                    <p>Designed for recent graduates or masters students requiring flexible, part-time, or off-season intensive experience.</p>
                    <ul style="margin-top: 1rem;">
                        <li>Duration: 3-6 Months</li>
                        <li>Deep dive into specialized departments</li>
                        <li>Performance-based permanent placement</li>
                    </ul>
                </div>
            </div>

            <div style="margin-top: 4rem;">
                <h3>What We Look For</h3>
                <ul style="line-height: 1.8;">
                    <li>Strong academic record in Finance, Accounting, Economics, or Law.</li>
                    <li>Demonstrated leadership through extracurricular activities.</li>
                    <li>Exceptional analytical and problem-solving skills.</li>
                    <li>A proactive, "self-starter" mentality.</li>
                </ul>
            </div>
            
            <div style="margin-top: 4rem; text-align: center;">
                <h2>Apply for our next cohort</h2>
                <a href="apply.html" class="btn btn-primary">Apply for Internship</a>
            </div>
        </div>
        '''
    },
    {
        "filepath": "careers/faqs.html",
        "title": "Career FAQs - Truvisory",
        "meta": "Frequently asked questions about working at Truvisory. Learn about our hiring process, visa sponsorships, and remote work policies.",
        "breadcrumb": "Home / Careers / FAQs",
        "hero_title": "Career FAQs",
        "hero_subtitle": "Everything you need to know about joining us.",
        "content": '''
        <div class="container" style="padding: 4rem 0;">
            <div style="max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; gap: 1.5rem;">
                
                <div class="glass-card" style="padding: 2rem;">
                    <h3 style="color: var(--primary); margin-bottom: 1rem;">Do you offer remote work options?</h3>
                    <p>Yes. While certain client-facing roles require physical presence in our regional hubs (Dubai, Singapore, etc.), we offer flexible hybrid models and fully remote positions for specific advisory and backend roles.</p>
                </div>
                
                <div class="glass-card" style="padding: 2rem;">
                    <h3 style="color: var(--primary); margin-bottom: 1rem;">Does Truvisory sponsor work visas?</h3>
                    <p>Yes, for highly qualified candidates, we provide comprehensive relocation assistance and work visa sponsorship for our global offices.</p>
                </div>
                
                <div class="glass-card" style="padding: 2rem;">
                    <h3 style="color: var(--primary); margin-bottom: 1rem;">How long does the recruitment process take?</h3>
                    <p>Typically, the process from initial application to final offer takes between 3 to 5 weeks, depending on the seniority of the role and scheduling logistics.</p>
                </div>
                
                <div class="glass-card" style="padding: 2rem;">
                    <h3 style="color: var(--primary); margin-bottom: 1rem;">Can I apply for multiple roles simultaneously?</h3>
                    <p>We recommend applying only to the 1 or 2 roles that best match your skill set. Our talent team will route your profile to other departments if they believe there is a better fit elsewhere.</p>
                </div>

            </div>
            
            <div style="margin-top: 4rem; text-align: center;">
                <h2>Still have questions?</h2>
                <a href="../contact.html" class="btn btn-primary">Contact HR Team</a>
            </div>
        </div>
        '''
    },
    {
        "filepath": "careers/apply.html",
        "title": "Apply Now - Truvisory Careers",
        "meta": "Submit your application to Truvisory. Join our team of global financial experts and consultants.",
        "breadcrumb": "Home / Careers / Apply Now",
        "hero_title": "Apply Now",
        "hero_subtitle": "Take the first step towards a rewarding career.",
        "content": '''
        <div class="container" style="padding: 4rem 0; max-width: 800px;">
            <div class="glass-card" style="padding: 3rem;">
                <h2 style="margin-bottom: 2rem; text-align: center;">Application Portal</h2>
                <form action="#" method="POST" style="display: flex; flex-direction: column; gap: 1.5rem;">
                    
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;">
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-light);">First Name *</label>
                            <input type="text" required style="width: 100%; padding: 12px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 4px; color: #fff;">
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-light);">Last Name *</label>
                            <input type="text" required style="width: 100%; padding: 12px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 4px; color: #fff;">
                        </div>
                    </div>

                    <div>
                        <label style="display: block; margin-bottom: 0.5rem; color: var(--text-light);">Email Address *</label>
                        <input type="email" required style="width: 100%; padding: 12px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 4px; color: #fff;">
                    </div>

                    <div>
                        <label style="display: block; margin-bottom: 0.5rem; color: var(--text-light);">Position Applying For *</label>
                        <select required style="width: 100%; padding: 12px; background: rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.1); border-radius: 4px; color: #fff;">
                            <option value="">Select a position...</option>
                            <option value="tax">Senior Corporate Tax Advisor</option>
                            <option value="cfo">Virtual CFO</option>
                            <option value="setup">Business Setup Consultant</option>
                            <option value="intern">Summer Internship</option>
                            <option value="general">General Application</option>
                        </select>
                    </div>

                    <div>
                        <label style="display: block; margin-bottom: 0.5rem; color: var(--text-light);">LinkedIn Profile URL</label>
                        <input type="url" style="width: 100%; padding: 12px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 4px; color: #fff;">
                    </div>

                    <div>
                        <label style="display: block; margin-bottom: 0.5rem; color: var(--text-light);">Upload Resume/CV (PDF) *</label>
                        <input type="file" accept=".pdf" required style="width: 100%; padding: 12px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 4px; color: #fff;">
                    </div>

                    <div>
                        <label style="display: block; margin-bottom: 0.5rem; color: var(--text-light);">Cover Letter (Optional)</label>
                        <textarea rows="4" style="width: 100%; padding: 12px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 4px; color: #fff;"></textarea>
                    </div>

                    <button type="submit" class="btn btn-primary" style="padding: 15px; font-size: 1.1rem; width: 100%; margin-top: 1rem;">Submit Application</button>
                </form>
            </div>
        </div>
        '''
    },
    {
        "filepath": "resources/business-guides.html",
        "title": "Business Guides - Truvisory Resources",
        "meta": "Download comprehensive guides on business incorporation, tax planning, and compliance for international markets.",
        "breadcrumb": "Home / Resources / Business Guides",
        "hero_title": "Business Guides",
        "hero_subtitle": "In-depth insights to navigate global markets.",
        "content": '''
        <div class="container" style="padding: 4rem 0;">
            <h2>Expert Manuals & Whitepapers</h2>
            <p style="margin-bottom: 3rem;">Authored by our senior partners, these guides provide actionable intelligence on structuring and expanding your enterprise.</p>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
                <div class="glass-card" style="padding: 2rem;">
                    <div style="height: 150px; background: rgba(255,255,255,0.05); border-radius: 8px; margin-bottom: 1.5rem; display: flex; align-items: center; justify-content: center;">
                        <i class="fa-solid fa-file-pdf" style="font-size: 4rem; color: var(--primary);"></i>
                    </div>
                    <h3>The UAE Corporate Tax Handbook</h3>
                    <p>A complete 40-page guide detailing the recent UAE corporate tax implementation, exemptions, and compliance requirements.</p>
                    <a href="#" class="btn btn-outline" style="margin-top: 1rem;">Download PDF</a>
                </div>
                
                <div class="glass-card" style="padding: 2rem;">
                    <div style="height: 150px; background: rgba(255,255,255,0.05); border-radius: 8px; margin-bottom: 1.5rem; display: flex; align-items: center; justify-content: center;">
                        <i class="fa-solid fa-file-pdf" style="font-size: 4rem; color: var(--primary);"></i>
                    </div>
                    <h3>Singapore vs. Hong Kong Structuring</h3>
                    <p>A comparative analysis of the legal frameworks, taxation, and banking environments of Asia's premier financial hubs.</p>
                    <a href="#" class="btn btn-outline" style="margin-top: 1rem;">Download PDF</a>
                </div>

                <div class="glass-card" style="padding: 2rem;">
                    <div style="height: 150px; background: rgba(255,255,255,0.05); border-radius: 8px; margin-bottom: 1.5rem; display: flex; align-items: center; justify-content: center;">
                        <i class="fa-solid fa-file-pdf" style="font-size: 4rem; color: var(--primary);"></i>
                    </div>
                    <h3>Holding Company Structures</h3>
                    <p>Advanced strategies for utilizing Free Zones, offshore jurisdictions, and holding companies to maximize asset protection.</p>
                    <a href="#" class="btn btn-outline" style="margin-top: 1rem;">Download PDF</a>
                </div>
            </div>
            
            <div style="margin-top: 4rem; text-align: center;">
                <h2>Need Custom Advice?</h2>
                <p>These guides provide general information. For tailored strategies, speak directly with our advisory team.</p>
                <a href="../contact.html" class="btn btn-primary" style="margin-top: 1rem;">Book a Free Consultation</a>
            </div>
        </div>
        '''
    },
    {
        "filepath": "resources/tax-calendar.html",
        "title": "Global Tax Calendar - Truvisory",
        "meta": "Stay compliant with our global tax calendar. Important deadlines for corporate tax, VAT, and financial filings across UAE, US, and Asia.",
        "breadcrumb": "Home / Resources / Tax Calendar",
        "hero_title": "Global Tax Calendar",
        "hero_subtitle": "Never miss a crucial filing deadline.",
        "content": '''
        <div class="container" style="padding: 4rem 0;">
            <h2>Upcoming Tax Deadlines</h2>
            <p style="margin-bottom: 3rem;">A consolidated view of major corporate filing deadlines across our key operating jurisdictions.</p>
            
            <div class="glass-card" style="padding: 2rem; overflow-x: auto;">
                <table style="width: 100%; border-collapse: collapse; text-align: left;">
                    <thead>
                        <tr style="border-bottom: 2px solid var(--primary);">
                            <th style="padding: 1rem;">Date</th>
                            <th style="padding: 1rem;">Jurisdiction</th>
                            <th style="padding: 1rem;">Filing Type</th>
                            <th style="padding: 1rem;">Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
                            <td style="padding: 1rem; color: #ff6b6b;">Jan 31</td>
                            <td style="padding: 1rem;">UAE</td>
                            <td style="padding: 1rem;">VAT Return</td>
                            <td style="padding: 1rem;">Q4 VAT Filing & Payment Deadline</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
                            <td style="padding: 1rem; color: #ff6b6b;">Mar 15</td>
                            <td style="padding: 1rem;">USA</td>
                            <td style="padding: 1rem;">Corporate Tax</td>
                            <td style="padding: 1rem;">Form 1120/1120S Deadline for Calendar Year Entities</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
                            <td style="padding: 1rem; color: #ff6b6b;">Apr 15</td>
                            <td style="padding: 1rem;">Hong Kong</td>
                            <td style="padding: 1rem;">Profits Tax</td>
                            <td style="padding: 1rem;">Issuance of Profits Tax Returns (PTR)</td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
                            <td style="padding: 1rem; color: #ff6b6b;">Nov 30</td>
                            <td style="padding: 1rem;">Singapore</td>
                            <td style="padding: 1rem;">Corporate Tax</td>
                            <td style="padding: 1rem;">Form C-S / Form C E-Filing Deadline</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            
            <div style="margin-top: 4rem; text-align: center;">
                <h2>Let us handle the deadlines.</h2>
                <a href="../contact.html" class="btn btn-primary">Outsource Your Compliance</a>
            </div>
        </div>
        '''
    },
    {
        "filepath": "resources/compliance-calendar.html",
        "title": "Compliance Calendar - Truvisory",
        "meta": "Track annual corporate compliance, license renewals, and statutory audit deadlines with Truvisory's compliance calendar.",
        "breadcrumb": "Home / Resources / Compliance Calendar",
        "hero_title": "Compliance Calendar",
        "hero_subtitle": "Statutory requirements and license renewals.",
        "content": '''
        <div class="container" style="padding: 4rem 0;">
            <h2>Corporate Maintenance Schedule</h2>
            <p style="margin-bottom: 3rem;">Beyond taxation, maintaining a corporate entity requires strict adherence to statutory deadlines to avoid penalties or deregistration.</p>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
                <div class="glass-card" style="padding: 2rem;">
                    <h3 style="color: var(--primary);">Annual General Meetings (AGM)</h3>
                    <p><strong>Singapore:</strong> Must be held within 6 months from the Financial Year End (FYE).<br>
                    <strong>Hong Kong:</strong> First AGM within 18 months of incorporation, subsequently every 15 months.</p>
                </div>
                <div class="glass-card" style="padding: 2rem;">
                    <h3 style="color: var(--primary);">License Renewals</h3>
                    <p><strong>UAE Free Zones:</strong> Trade licenses must be renewed annually, generally requiring submission of a valid lease agreement and updated KYC 30 days prior to expiry.</p>
                </div>
                <div class="glass-card" style="padding: 2rem;">
                    <h3 style="color: var(--primary);">Economic Substance (ESR)</h3>
                    <p><strong>UAE & Offshore:</strong> ESR Notifications usually due 6 months after the end of the financial year. Full ESR Report due 12 months after FYE.</p>
                </div>
                <div class="glass-card" style="padding: 2rem;">
                    <h3 style="color: var(--primary);">Beneficial Ownership (UBO)</h3>
                    <p>Registers of Ultimate Beneficial Owners must be updated continually. Annual declarations are required in most jurisdictions within 14 days of any structural change.</p>
                </div>
            </div>
            
            <div style="margin-top: 4rem; text-align: center;">
                <h2>Talk to Our Experts</h2>
                <a href="../contact.html" class="btn btn-primary">Book a Free Consultation</a>
            </div>
        </div>
        '''
    },
    {
        "filepath": "resources/brochures.html",
        "title": "Download Brochures - Truvisory",
        "meta": "Download comprehensive company brochures detailing Truvisory's corporate, tax, and advisory services.",
        "breadcrumb": "Home / Resources / Brochures",
        "hero_title": "Corporate Brochures",
        "hero_subtitle": "Everything about our services in one place.",
        "content": '''
        <div class="container" style="padding: 4rem 0;">
            <h2>Service Catalogs & Firm Profiles</h2>
            <p style="margin-bottom: 3rem;">Download our official brochures to share with your board of directors or executive team.</p>
            
            <div style="display: flex; flex-direction: column; gap: 2rem; max-width: 800px; margin: 0 auto;">
                <div class="glass-card" style="padding: 2rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                    <div style="display: flex; align-items: center; gap: 1.5rem;">
                        <i class="fa-solid fa-file-pdf" style="font-size: 3rem; color: var(--primary);"></i>
                        <div>
                            <h3 style="margin-bottom: 0.5rem;">Truvisory Corporate Overview (2025)</h3>
                            <p style="margin-bottom: 0;">Our complete firm profile, global footprint, and core service offerings.</p>
                        </div>
                    </div>
                    <a href="#" class="btn btn-outline">Download</a>
                </div>

                <div class="glass-card" style="padding: 2rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                    <div style="display: flex; align-items: center; gap: 1.5rem;">
                        <i class="fa-solid fa-file-pdf" style="font-size: 3rem; color: var(--primary);"></i>
                        <div>
                            <h3 style="margin-bottom: 0.5rem;">UAE Setup & Tax Guide</h3>
                            <p style="margin-bottom: 0;">Detailed breakdown of Mainland vs Free Zone structures and Corporate Tax mechanics.</p>
                        </div>
                    </div>
                    <a href="#" class="btn btn-outline">Download</a>
                </div>
                
                <div class="glass-card" style="padding: 2rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                    <div style="display: flex; align-items: center; gap: 1.5rem;">
                        <i class="fa-solid fa-file-pdf" style="font-size: 3rem; color: var(--primary);"></i>
                        <div>
                            <h3 style="margin-bottom: 0.5rem;">Virtual CFO Service Brochure</h3>
                            <p style="margin-bottom: 0;">How our outsourced financial controllers can scale your business efficiently.</p>
                        </div>
                    </div>
                    <a href="#" class="btn btn-outline">Download</a>
                </div>
            </div>
            
            <div style="margin-top: 4rem; text-align: center;">
                <h2>Require a Custom Proposal?</h2>
                <a href="../contact.html" class="btn btn-primary">Contact Us</a>
            </div>
        </div>
        '''
    },
    {
        "filepath": "resources/success-stories.html",
        "title": "Success Stories & Case Studies - Truvisory",
        "meta": "Read real success stories of how Truvisory helped enterprises scale globally, optimize tax structures, and resolve complex compliance challenges.",
        "breadcrumb": "Home / Resources / Success Stories",
        "hero_title": "Success Stories",
        "hero_subtitle": "Real challenges. Real solutions. Real results.",
        "content": '''
        <div class="container" style="padding: 4rem 0;">
            <h2>Client Case Studies</h2>
            <p style="margin-bottom: 3rem;">Discover how we have partnered with businesses across various sectors to drive growth, ensure compliance, and maximize efficiency.</p>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 2rem;">
                <div class="glass-card" style="padding: 2rem;">
                    <span style="display: inline-block; padding: 5px 12px; background: rgba(255,255,255,0.1); border-radius: 20px; font-size: 0.85rem; margin-bottom: 1rem;">E-Commerce / Retail</span>
                    <h3 style="color: var(--primary);">Cross-Border Tax Optimization for a Global E-tailer</h3>
                    <p><strong>The Challenge:</strong> A European e-commerce brand was losing 28% of net margins due to inefficient warehousing setups and double taxation across Asian markets.</p>
                    <p><strong>The Solution:</strong> We restructured their operations via a Hong Kong holding company with a Singapore operational subsidiary, leveraging specific tax treaties.</p>
                    <p><strong>The Result:</strong> Net margins improved by 14%, and cross-border compliance risk was completely mitigated.</p>
                </div>
                
                <div class="glass-card" style="padding: 2rem;">
                    <span style="display: inline-block; padding: 5px 12px; background: rgba(255,255,255,0.1); border-radius: 20px; font-size: 0.85rem; margin-bottom: 1rem;">Technology / SaaS</span>
                    <h3 style="color: var(--primary);">Rapid Middle East Expansion for a SaaS Unicorn</h3>
                    <p><strong>The Challenge:</strong> A fast-growing US software company needed to establish a MENA headquarters in Dubai within 45 days to secure a major government contract.</p>
                    <p><strong>The Solution:</strong> Truvisory expedited a DIFC incorporation, secured specialized tech licenses, and handled all employment visas for the executive landing team.</p>
                    <p><strong>The Result:</strong> Entity incorporated in 18 days, contract secured, and banking facilities opened ahead of schedule.</p>
                </div>
            </div>
            
            <div style="margin-top: 4rem; text-align: center;">
                <h2>Be our next success story.</h2>
                <a href="../contact.html" class="btn btn-primary">Talk to Our Experts</a>
            </div>
        </div>
        '''
    },
    {
        "filepath": "resources/faqs.html",
        "title": "Resource FAQs - Truvisory",
        "meta": "Frequently asked questions regarding our business guides, downloads, and compliance tools.",
        "breadcrumb": "Home / Resources / FAQs",
        "hero_title": "Resource FAQs",
        "hero_subtitle": "Answers to your common queries.",
        "content": '''
        <div class="container" style="padding: 4rem 0;">
            <div style="max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; gap: 1.5rem;">
                
                <div class="glass-card" style="padding: 2rem;">
                    <h3 style="color: var(--primary); margin-bottom: 1rem;">Are the business guides completely free?</h3>
                    <p>Yes, all publicly available whitepapers and brochures on this portal are free to download and share. We believe in educating our clients to make informed decisions.</p>
                </div>
                
                <div class="glass-card" style="padding: 2rem;">
                    <h3 style="color: var(--primary); margin-bottom: 1rem;">How often is the tax calendar updated?</h3>
                    <p>Our tax and compliance calendars are reviewed quarterly by our compliance directors to ensure any legislative changes are immediately reflected.</p>
                </div>
                
                <div class="glass-card" style="padding: 2rem;">
                    <h3 style="color: var(--primary); margin-bottom: 1rem;">Can I republish your guides on my website?</h3>
                    <p>All materials are copyrighted by Truvisory. However, you may quote excerpts or summarize our content provided you include a direct backlink and attribute the source to Truvisory.</p>
                </div>

            </div>
            
            <div style="margin-top: 4rem; text-align: center;">
                <h2>Have a specific technical question?</h2>
                <a href="../contact.html" class="btn btn-primary">Book a Free Consultation</a>
            </div>
        </div>
        '''
    }
]

html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{meta}">
  <link rel="stylesheet" href="../assets/css/styles.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body class="dark-theme">
  {header}

  <main>
    <section class="hero" style="min-height: 40vh; display: flex; align-items: center; justify-content: center; text-align: center; padding-top: 150px;">
      <div class="hero-bg-shapes">
        <div class="shape shape-1"></div>
        <div class="shape shape-2"></div>
      </div>
      <div class="container" style="position: relative; z-index: 2;">
        <p style="color: var(--primary); margin-bottom: 1rem; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 2px;">{breadcrumb}</p>
        <h1 style="font-size: 3.5rem; margin-bottom: 1rem;">{hero_title}</h1>
        <p style="font-size: 1.2rem; color: var(--text-light);">{hero_subtitle}</p>
      </div>
    </section>

    {content}
  </main>

  {footer}

  <script>
    // Simple script to handle menu toggle if needed
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-left-group');
    if(menuToggle && navLinks) {
        menuToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }
  </script>
</body>
</html>'''


for page in pages:
    filepath = page['filepath']
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    html = html_template.replace('{title}', page['title'])
    html = html.replace('{meta}', page['meta'])
    html = html.replace('{breadcrumb}', page['breadcrumb'])
    html = html.replace('{hero_title}', page['hero_title'])
    html = html.replace('{hero_subtitle}', page['hero_subtitle'])
    html = html.replace('{content}', page['content'])
    html = html.replace('{header}', header_subdir)
    html = html.replace('{footer}', footer_subdir)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {filepath}")

print("Phase 1 Generation Complete.")
