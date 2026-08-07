document.addEventListener('DOMContentLoaded', () => {
  // Mobile Menu Toggle
  const menuToggle = document.getElementById('menu-toggle');
  const closeMenu = document.getElementById('close-menu');
  const mobileDrawer = document.getElementById('mobile-drawer');
  
  const toggleMenu = () => {
    if (mobileDrawer) {
      mobileDrawer.classList.toggle('active');
      document.body.style.overflow = mobileDrawer.classList.contains('active') ? 'hidden' : '';
    }
  };

  if (menuToggle) menuToggle.addEventListener('click', toggleMenu);
  if (closeMenu) closeMenu.addEventListener('click', toggleMenu);
  
  // Close menu when clicking a link
  const drawerLinks = document.querySelectorAll('.drawer-link, .drawer-sub-section a:not(.mobile-accordion-btn)');
  drawerLinks.forEach(link => {
    link.addEventListener('click', () => {
      if (mobileDrawer) mobileDrawer.classList.remove('active');
      document.body.style.overflow = '';
    });
  });

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
        faqTabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
      });
    });
  }

  // Accordion Functionality
  const accordionItems = document.querySelectorAll('.accordion-item');
  accordionItems.forEach(item => {
    const header = item.querySelector('.accordion-header');
    if (header) {
      header.addEventListener('click', () => {
        // Close others
        accordionItems.forEach(otherItem => {
          if (otherItem !== item) {
            otherItem.classList.remove('active');
          }
        });
        // Toggle current
        item.classList.toggle('active');
      });
    }
  });

  // Simple Testimonial Carousel
  const slides = document.querySelectorAll('.testimonial-slide');
  if (slides.length > 1) {
    let currentSlide = 0;
    setInterval(() => {
      slides[currentSlide].classList.remove('active');
      currentSlide = (currentSlide + 1) % slides.length;
      slides[currentSlide].classList.add('active');
    }, 5000);
  }

  // Mobile Mega Menu Accordion
  const accordionBtns = document.querySelectorAll('.mobile-accordion-btn');
  accordionBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      const accordion = e.currentTarget.closest('.mobile-accordion');
      if (accordion) {
        accordion.classList.toggle('active');
        const expanded = accordion.classList.contains('active');
        btn.setAttribute('aria-expanded', expanded);
      }
    });
  });

  // Back to Top Button
  const backToTopBtn = document.getElementById('back-to-top');
  if (backToTopBtn) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 500) {
        backToTopBtn.classList.add('visible');
      } else {
        backToTopBtn.classList.remove('visible');
      }
    });

    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }
});
