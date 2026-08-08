import re

ui_path = 'C:/Users/roopc/.gemini/antigravity/brain/c93a1649-f9d8-443c-9da6-d0a3b3a80bd0/scratch/rebuild_ui.py'
with open(ui_path, 'r', encoding='utf-8') as f:
    c = f.read()

missing_about = """
    <div class="container mb-6">
      <h2 class="mb-3 text-center">Why Truvisory</h2>
      <p class="text-center" style="max-width: 800px; margin: 0 auto 32px; color: var(--text-muted);">We don't sell services in isolation. Before recommending a solution, we take the time to understand your business stage, goals and constraints — and build a plan around that.</p>
      <div class="grid-2" style="max-width: 800px; margin: 0 auto;">
        <ul style="list-style: none; padding: 0;">
          <li style="margin-bottom: 12px; display: flex;"><i class="fa-solid fa-check" style="color: var(--accent-gold); margin-right: 12px; margin-top: 4px;"></i> One firm for incorporation, accounting, tax, compliance, IP and growth services</li>
          <li style="margin-bottom: 12px; display: flex;"><i class="fa-solid fa-check" style="color: var(--accent-gold); margin-right: 12px; margin-top: 4px;"></i> Direct access to Chartered Accountants, not just relationship managers</li>
        </ul>
        <ul style="list-style: none; padding: 0;">
          <li style="margin-bottom: 12px; display: flex;"><i class="fa-solid fa-check" style="color: var(--accent-gold); margin-right: 12px; margin-top: 4px;"></i> Advisory grounded in real jurisdiction knowledge across six countries</li>
          <li style="margin-bottom: 12px; display: flex;"><i class="fa-solid fa-check" style="color: var(--accent-gold); margin-right: 12px; margin-top: 4px;"></i> A long-term advisory relationship, not a transactional service</li>
        </ul>
      </div>
    </div>

    <div class="container text-center mb-6">
      <h2 class="mb-3">Global Presence</h2>
      <p style="max-width: 800px; margin: 0 auto; color: var(--text-muted);">Truvisory supports business establishment and ongoing compliance across India, UAE, Singapore, United Kingdom, Hong Kong and the United States — through a combination of in-house expertise and trusted local partners in each jurisdiction, helping clients get accurate, on-ground guidance wherever they choose to grow.</p>
    </div>
"""

# Insert missing about section right before the end of the section-white in about_main
c = c.replace('  </section>\n</main>\n"""', missing_about + '  </section>\n</main>\n"""', 1)

with open(ui_path, 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated rebuild_ui.py with missing about content")
