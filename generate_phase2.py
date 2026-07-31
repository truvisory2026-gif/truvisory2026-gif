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

# Function to adjust relative paths for subdirectory files
def adjust_paths_for_subdir(html_chunk):
    html_chunk = html_chunk.replace('"assets/', '"../assets/')
    html_chunk = re.sub(r'href="([^/"]+\.html)(#[^"]*)?"', r'href="../\1\2"', html_chunk)
    html_chunk = html_chunk.replace('href="#contact"', 'href="../index.html#contact"')
    return html_chunk

header_subdir = adjust_paths_for_subdir(base_header)
footer_subdir = adjust_paths_for_subdir(base_footer)

industries = [
    "Financial Services", "Healthcare", "Real Estate", "Technology", 
    "E-Commerce", "Manufacturing", "Energy", "Hospitality", 
    "Logistics", "Retail", "Aviation", "Education", 
    "Agriculture", "Media & Entertainment"
]

services = [
    "Company Incorporation", "Overseas Business Setup", "International Tax Planning", 
    "GST & VAT", "Corporate Tax", "Accounting & Bookkeeping", 
    "Payroll Services", "Compliance Management", "Virtual CFO", 
    "Business Advisory", "Franchise Expansion", "Business Structuring", 
    "Legal & Compliance"
]

def slugify(text):
    text = text.lower().replace('&', 'and')
    return re.sub(r'[^a-z0-9]+', '-', text).strip('-')

pages = []

for ind in industries:
    slug = slugify(ind)
    pages.append({
        "filepath": f"industries/{slug}.html",
        "title": f"{ind} Industry - Truvisory",
        "meta": f"Expert financial, tax, and compliance services for the {ind} industry.",
        "breadcrumb": f"Home / Industries / {ind}",
        "hero_title": ind,
        "hero_subtitle": f"Tailored solutions for the {ind} sector.",
        "content": f'''
        <div class="container" style="padding: 4rem 0;">
            <h2>Navigating the {ind} Landscape</h2>
            <p style="margin-bottom: 2rem;">The {ind} industry presents unique regulatory, financial, and operational challenges. At Truvisory, we bring deep domain expertise to help you optimize tax structures, ensure robust compliance, and scale your operations globally.</p>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
                <div class="glass-card" style="padding: 2rem;">
                    <h3 style="color: var(--primary);">Regulatory Compliance</h3>
                    <p>Stay ahead of industry-specific regulations and mitigate risk across all jurisdictions you operate in.</p>
                </div>
                <div class="glass-card" style="padding: 2rem;">
                    <h3 style="color: var(--primary);">Tax Optimization</h3>
                    <p>Leverage specialized tax incentives and efficient cross-border structuring designed for {ind} enterprises.</p>
                </div>
                <div class="glass-card" style="padding: 2rem;">
                    <h3 style="color: var(--primary);">Growth Advisory</h3>
                    <p>Strategic M&A support, capital raising advisory, and market entry strategies tailored for your sector.</p>
                </div>
            </div>
            
            <div style="margin-top: 4rem; text-align: center;">
                <h2>Speak to our {ind} Experts</h2>
                <a href="../contact.html" class="btn btn-primary" style="margin-top: 1rem;">Book a Consultation</a>
            </div>
        </div>
        '''
    })

for srv in services:
    slug = slugify(srv)
    pages.append({
        "filepath": f"services/{slug}.html",
        "title": f"{srv} - Truvisory Services",
        "meta": f"Professional {srv} solutions to help you expand and manage your business effectively.",
        "breadcrumb": f"Home / Services / {srv}",
        "hero_title": srv,
        "hero_subtitle": "Expert guidance and seamless execution.",
        "content": f'''
        <div class="container" style="padding: 4rem 0;">
            <h2>Comprehensive {srv} Solutions</h2>
            <p style="margin-bottom: 3rem;">We provide end-to-end support for {srv}, ensuring accuracy, compliance, and strategic alignment with your overarching business goals.</p>
            
            <div style="display: flex; flex-direction: column; gap: 2rem; max-width: 900px; margin: 0 auto;">
                <div class="glass-card" style="padding: 2rem; display: flex; gap: 2rem; align-items: flex-start;">
                    <div style="font-size: 3rem; color: var(--primary);"><i class="fa-solid fa-check-circle"></i></div>
                    <div>
                        <h3>Strategic Approach</h3>
                        <p>Our {srv} team doesn't just process transactions; we look at the bigger picture to identify cost-saving opportunities and efficiency improvements.</p>
                    </div>
                </div>
                <div class="glass-card" style="padding: 2rem; display: flex; gap: 2rem; align-items: flex-start;">
                    <div style="font-size: 3rem; color: var(--primary);"><i class="fa-solid fa-globe"></i></div>
                    <div>
                        <h3>Global Capabilities</h3>
                        <p>Whether you are operating locally or expanding across continents, our global network ensures your {srv} needs are met seamlessly across borders.</p>
                    </div>
                </div>
                <div class="glass-card" style="padding: 2rem; display: flex; gap: 2rem; align-items: flex-start;">
                    <div style="font-size: 3rem; color: var(--primary);"><i class="fa-solid fa-shield-halved"></i></div>
                    <div>
                        <h3>Risk Mitigation</h3>
                        <p>We implement robust frameworks to ensure 100% compliance, protecting your business from penalties and legal exposure.</p>
                    </div>
                </div>
            </div>
            
            <div style="margin-top: 4rem; text-align: center;">
                <h2>Ready to streamline your operations?</h2>
                <a href="../contact.html" class="btn btn-primary" style="margin-top: 1rem;">Get a Custom Proposal</a>
            </div>
        </div>
        '''
    })

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

print("Phase 2 & 3 Generation Complete.")
