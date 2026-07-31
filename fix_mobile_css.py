import re

filename = 'assets/css/styles.css'
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix html overflow
if 'overflow-x: hidden;' not in content[:200]:
    content = content.replace('html {\n  scroll-behavior: smooth;', 'html {\n  overflow-x: hidden;\n  scroll-behavior: smooth;')

# Add strong mobile logo and general container fixes
mobile_fixes = """
/* --- Strict Mobile Fixes --- */
html, body {
    overflow-x: hidden !important;
    width: 100%;
    max-width: 100vw;
    margin: 0;
    padding: 0;
}

img, video, canvas, svg {
    max-width: 100%;
    height: auto;
}

.container {
    max-width: 100%;
    overflow-x: hidden;
    padding: 0 1rem;
}

@media (max-width: 768px) {
    .logo img {
        max-width: 180px !important;
        height: auto !important;
    }
    .nav-container {
        height: auto !important;
        padding: 10px 0;
    }
    .hero-headline {
        font-size: 2rem !important;
    }
    .section {
        padding: 3rem 0;
    }
    .grid-2, .grid-3, .grid-4, .services-grid {
        grid-template-columns: 1fr !important;
    }
    .auth-container, .glass-card {
        width: 100% !important;
        padding: 1.5rem !important;
        margin: 0 !important;
        box-sizing: border-box !important;
    }
    .process-step {
        flex-direction: column !important;
        text-align: center;
    }
}
"""

if '/* --- Strict Mobile Fixes --- */' not in content:
    content += "\n" + mobile_fixes

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Updated {filename}")
