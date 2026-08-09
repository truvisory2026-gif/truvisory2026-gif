css_path = r'C:\Users\roopc\OneDrive\Desktop\truvisory\style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

import re

# Remove the old trust-strip css
css = re.sub(r'/\* Trust Strip Formatting \*/.*?(?=\n/\*|\Z)', '', css, flags=re.DOTALL)

trust_strip_css = """
/* Trust Strip Formatting */
.trust-strip {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
}
@media (max-width: 768px) {
  .trust-strip {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
    background-color: #f8f9fa;
    border: 1px solid var(--border-medium);
    border-radius: 8px;
    padding: 16px;
    margin-top: 10px;
    width: 100%;
  }
  .trust-strip span {
    display: flex;
    align-items: center;
    width: 100%;
    border-bottom: 1px solid #eaeaea;
    padding-bottom: 8px;
  }
  .trust-strip span:last-child {
    border-bottom: none;
    padding-bottom: 0;
  }
}
"""

css += trust_strip_css

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css with boxed mobile alignment for trust strip.")
