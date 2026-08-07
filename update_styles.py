import os

def append_styles():
    file_path = 'c:\\Users\\roopc\\OneDrive\\Desktop\\truvisory\\style.css'
    
    new_css = """
/* ==========================================================================
   VOLUME 1 CONTENT BIBLE - NEW COMPONENT STYLES
   ========================================================================== */

/* Typography Helpers */
.max-w-700 { max-width: 700px; }
.mr-3 { margin-right: 1rem; }
.align-center { align-items: center; }

/* Buttons */
.btn-outline {
  background-color: transparent;
  border: 2px solid var(--text-dark);
  color: var(--text-dark);
}

.btn-outline:hover {
  background-color: var(--text-dark);
  color: #FFFFFF;
}

/* Animations */
.fade-up {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.8s ease, transform 0.8s ease;
}

.fade-up.visible {
  opacity: 1;
  transform: translateY(0);
}

.fade-left {
  opacity: 0;
  transform: translateX(30px);
  transition: opacity 0.8s ease, transform 0.8s ease;
}

.fade-left.visible {
  opacity: 1;
  transform: translateX(0);
}

/* Hero Section Enhancements */
.hero-ctas {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
}

.trust-indicators {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  font-size: 0.875rem;
  color: var(--text-slate);
  font-weight: 500;
}

.trust-item {
  display: flex;
  align-items: center;
}

/* Quote Box */
.quote-box-container {
  padding: 24px;
}

.quote-box {
  background: var(--card-bg);
  padding: 40px;
  border-radius: var(--border-radius-card);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
  position: relative;
  border-left: 4px solid var(--cta-gold);
}

.quote-icon {
  font-family: var(--font-serif);
  font-size: 4rem;
  color: var(--cta-gold);
  line-height: 1;
  position: absolute;
  top: 10px;
  left: 20px;
  opacity: 0.3;
}

.quote-text {
  font-size: 1.25rem;
  font-style: italic;
  font-family: var(--font-serif);
  color: var(--text-dark);
  margin-bottom: 16px;
  position: relative;
  z-index: 1;
}

.quote-author {
  font-weight: 600;
  color: var(--link-teal);
}

/* Vertical Timeline */
.timeline-container {
  position: relative;
  max-width: 800px;
  margin: 0 auto;
}

.timeline::after {
  content: '';
  position: absolute;
  width: 4px;
  background-color: var(--card-border);
  top: 0;
  bottom: 0;
  left: 50%;
  margin-left: -2px;
  border-radius: 4px;
}

.timeline-item {
  padding: 10px 40px;
  position: relative;
  background-color: inherit;
  width: 50%;
}

.timeline-item::after {
  content: '';
  position: absolute;
  width: 20px;
  height: 20px;
  right: -10px;
  background-color: white;
  border: 4px solid var(--cta-gold);
  top: 25px;
  border-radius: 50%;
  z-index: 1;
  box-shadow: 0 0 0 4px rgba(245, 158, 11, 0.2);
}

.left {
  left: 0;
}

.right {
  left: 50%;
}

.left::after {
  right: -10px;
}

.right::after {
  left: -10px;
}

.timeline-content {
  padding: 24px;
  background-color: white;
  position: relative;
  border-radius: var(--border-radius-card);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  border: 1px solid var(--card-border);
  transition: transform 0.3s ease;
}

.timeline-item:hover .timeline-content {
  transform: translateY(-5px);
  border-color: var(--link-teal);
}

.timeline-content h3 {
  font-family: var(--font-sans);
  font-size: 1.125rem;
  margin-bottom: 8px;
  color: var(--link-teal);
}

/* Country Cards */
.country-card {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: var(--border-radius-card);
  padding: 32px;
  transition: all 0.3s ease;
}

.country-card:hover {
  background: rgba(255, 255, 255, 0.1);
  transform: translateY(-5px);
}

.country-card h3 {
  color: white;
  margin-bottom: 8px;
}

.flag-icon {
  font-size: 3rem;
  margin-bottom: 16px;
}

/* Service Cards */
.service-card {
  background-color: var(--card-bg);
  border: 1px solid var(--card-border);
  border-radius: var(--border-radius-card);
  padding: 32px 24px;
  transition: all 0.3s ease;
}

.service-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.08);
  border-color: var(--link-teal);
}

.service-icon {
  font-size: 2.5rem;
  margin-bottom: 16px;
}

.service-card h4 {
  font-family: var(--font-sans);
  font-size: 1.125rem;
  margin-bottom: 12px;
}

/* Industry Cards */
.industry-card {
  background-color: var(--card-bg);
  border: 1px solid var(--card-border);
  border-radius: 8px;
  padding: 24px;
  text-align: center;
  transition: all 0.3s ease;
}

.industry-card:hover {
  background-color: var(--link-teal);
  color: white;
}

.industry-card:hover h4 {
  color: white;
}

.industry-card h4 {
  font-family: var(--font-sans);
  font-size: 1rem;
  margin-bottom: 0;
  transition: color 0.3s ease;
}

/* Case Study Cards */
.case-study-card {
  background-color: var(--bg-light);
  border: 1px solid var(--card-border);
  border-radius: var(--border-radius-card);
  padding: 40px;
  transition: all 0.3s ease;
}

.case-study-card:hover {
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
}

.case-study-card h3 {
  font-family: var(--font-serif);
  font-size: 1.5rem;
  margin: 16px 0;
}

.business-outcomes {
  background: white;
  padding: 16px;
  border-radius: 8px;
  border-left: 4px solid var(--cta-gold);
}

.business-outcomes ul {
  margin-top: 8px;
  padding-left: 20px;
}

/* Testimonial Slider */
.testimonial-slider {
  max-width: 800px;
  margin: 0 auto;
  position: relative;
}

.testimonial-slide {
  display: none;
  padding: 20px;
}

.testimonial-slide.active {
  display: block;
  animation: fadeIn 0.5s;
}

.testimonial-text {
  font-size: 1.5rem;
  font-style: italic;
  font-family: var(--font-serif);
  line-height: 1.8;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* FAQ Tabs */
.faq-tabs {
  display: flex;
  justify-content: center;
  gap: 12px;
  flex-wrap: wrap;
}

.faq-tab {
  background: var(--bg-light);
  border: 1px solid var(--card-border);
  padding: 10px 24px;
  border-radius: 30px;
  font-family: var(--font-sans);
  font-weight: 600;
  color: var(--text-slate);
  cursor: pointer;
  transition: all 0.3s ease;
}

.faq-tab.active, .faq-tab:hover {
  background: var(--link-teal);
  color: white;
  border-color: var(--link-teal);
}

/* Expanded Footer */
.footer-grid {
  grid-template-columns: 2fr 1fr 1fr 1fr 1fr;
}

@media screen and (max-width: 1024px) {
  .footer-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

/* Responsive Timeline */
@media screen and (max-width: 768px) {
  .timeline::after {
    left: 31px;
  }
  
  .timeline-item {
    width: 100%;
    padding-left: 70px;
    padding-right: 25px;
  }
  
  .timeline-item::after {
    left: 21px;
  }
  
  .right {
    left: 0%;
  }
}
"""
    
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(new_css)
        
    print("Appended styles successfully.")

if __name__ == "__main__":
    append_styles()
