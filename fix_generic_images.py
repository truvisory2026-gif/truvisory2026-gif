import re

ui_path = 'C:/Users/roopc/.gemini/antigravity/brain/c93a1649-f9d8-443c-9da6-d0a3b3a80bd0/scratch/rebuild_ui.py'
with open(ui_path, 'r', encoding='utf-8') as f:
    c = f.read()

# Replace About Us Hero
c = c.replace(
    '<img src="assets/images/insight_blogs_1786206408849.png" alt="Meeting">',
    '<img src="assets/images/ind_startups_1786206318113.png" alt="Business Advisory">'
)

# Replace Services Hero (same alt="Meeting", so it will catch both if they are identical, but let's be careful)
# Actually, the above replace will replace all instances of alt="Meeting".
# Let's check alt="Nivya Jain"
c = c.replace(
    '<img src="assets/images/insight_blogs_1786206408849.png" style="width: 100%; height: 250px; object-fit: cover;" alt="Nivya Jain">',
    '<img src="assets/images/logo.png" style="width: 100%; height: 250px; object-fit: contain; padding: 20px; background: #fff;" alt="Nivya Jain">'
)

# Replace Countries Hero
c = c.replace(
    '<img src="assets/images/insight_blogs_1786206408849.png" alt="World Map">',
    '<img src="assets/images/country_uae_1786206222662.png" alt="World Map">'
)

# Replace Insights Hero
c = c.replace(
    '<img src="assets/images/insight_blogs_1786206408849.png" alt="Insights">',
    '<img src="assets/images/ind_manufacturing_1786206358131.png" alt="Insights">'
)

# Replace Insights Cards
c = c.replace(
    '<img src="assets/images/insight_blogs_1786206408849.png" style="width: 100%; height: 200px; object-fit: cover;" alt="Blogs">',
    '<img src="assets/images/ind_it_saas_1786206333027.png" style="width: 100%; height: 200px; object-fit: cover;" alt="Blogs">'
)
c = c.replace(
    '<img src="assets/images/insight_blogs_1786206408849.png" style="width: 100%; height: 200px; object-fit: cover;" alt="Business Guides">',
    '<img src="assets/images/ind_logistics_1786206385016.png" style="width: 100%; height: 200px; object-fit: cover;" alt="Business Guides">'
)
c = c.replace(
    '<img src="assets/images/insight_blogs_1786206408849.png" style="width: 100%; height: 200px; object-fit: cover;" alt="Tax Updates">',
    '<img src="assets/images/ind_ecommerce_1786206345476.png" style="width: 100%; height: 200px; object-fit: cover;" alt="Tax Updates">'
)
c = c.replace(
    '<img src="assets/images/insight_blogs_1786206408849.png" style="width: 100%; height: 200px; object-fit: cover;" alt="Compliance Calendar">',
    '<img src="assets/images/ind_healthcare_1786206372993.png" style="width: 100%; height: 200px; object-fit: cover;" alt="Compliance Calendar">'
)
c = c.replace(
    '<img src="assets/images/insight_blogs_1786206408849.png" style="width: 100%; height: 200px; object-fit: cover;" alt="FAQs">',
    '<img src="assets/images/country_usa_1786206280836.png" style="width: 100%; height: 200px; object-fit: cover;" alt="FAQs">'
)


with open(ui_path, 'w', encoding='utf-8') as f:
    f.write(c)

print("Fixed generic images!")
