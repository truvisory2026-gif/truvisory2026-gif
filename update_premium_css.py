import re

def update_css():
    file_path = 'c:\\Users\\roopc\\OneDrive\\Desktop\\truvisory\\style.css'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update variables
    content = content.replace('--bg-light: #F8FAFC;', '--bg-light: #FFFFFF;\n  --bg-gray: #F8FAFC;')

    # Add missing classes for the new theme
    additional_css = """

/* Additional Classes for Premium White Theme */
.section-white {
  background-color: #FFFFFF;
}

.section-gray {
  background-color: var(--bg-gray);
}

.text-navy {
  color: var(--bg-dark-end);
}

.link-navy {
  color: var(--bg-dark-end);
  text-decoration: none;
}
.link-navy:hover {
  text-decoration: underline;
}

.link-teal {
  color: var(--link-teal);
  text-decoration: none;
  font-weight: 500;
}
.link-teal:hover {
  text-decoration: underline;
}

.floating-whatsapp:hover {
  transform: scale(1.1);
}

/* Form Styles */
.form-card {
  padding: 40px;
  background: white;
  border-radius: var(--border-radius-card);
  box-shadow: 0 10px 40px rgba(0,0,0,0.05);
}
.form-control:focus {
  outline: none;
  border-color: var(--link-teal) !important;
  box-shadow: 0 0 0 3px rgba(13,148,136,0.1);
}
"""

    if ".section-white" not in content:
        content += additional_css

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Updated CSS for white theme.")

if __name__ == "__main__":
    update_css()
