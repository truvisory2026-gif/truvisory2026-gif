import os

def append_script():
    file_path = 'c:\\Users\\roopc\\OneDrive\\Desktop\\truvisory\\script.js'
    
    new_js = """
  // ==========================================
  // VOLUME 1 - NEW COMPONENT LOGIC
  // ==========================================

  // Intersection Observer for scroll animations (fade-up, fade-left)
  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.15
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target); // Only animate once
      }
    });
  }, observerOptions);

  const animatedElements = document.querySelectorAll('.fade-up, .fade-left');
  animatedElements.forEach(el => observer.observe(el));

  // FAQ Tabs Logic
  const faqTabs = document.querySelectorAll('.faq-tab');
  if (faqTabs.length > 0) {
    faqTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        // Remove active class from all tabs
        faqTabs.forEach(t => t.classList.remove('active'));
        // Add active class to clicked tab
        tab.classList.add('active');
        
        // Example: In a real implementation, you would filter the FAQ items based on the data-target
        // const target = tab.getAttribute('data-target');
        // filterFaqs(target);
      });
    });
  }

  // Simple Testimonial Carousel (Example for future dynamic behavior)
  const slides = document.querySelectorAll('.testimonial-slide');
  if (slides.length > 1) {
    let currentSlide = 0;
    setInterval(() => {
      slides[currentSlide].classList.remove('active');
      currentSlide = (currentSlide + 1) % slides.length;
      slides[currentSlide].classList.add('active');
    }, 5000);
  }
});
"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the final "});" of the DOMContentLoaded event listener
    # To properly append inside the DOMContentLoaded block
    content = content.replace("});\n", new_js)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Appended JS successfully.")

if __name__ == "__main__":
    append_script()
