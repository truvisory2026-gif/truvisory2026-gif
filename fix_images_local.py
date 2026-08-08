import re
import os

filepath = 'C:/Users/roopc/.gemini/antigravity/brain/c93a1649-f9d8-443c-9da6-d0a3b3a80bd0/scratch/rebuild_ui.py'
with open(filepath, 'r', encoding='utf-8') as f:
    c = f.read()

# Current Unsplash IDs in the file mapped to the new local image filenames
mapping = {
    # Countries
    "1512453979436-5a5369ce9e1f": "country_uae_1786206222662.png",
    "1525625293386-3f8f99389edd": "country_singapore_1786206240342.png",
    "1513635269975-59663e0ac1ad": "country_uk_1786206252492.png",
    "1506927802816-6466f2043e06": "country_hk_1786206267336.png",
    "1496442226666-8d4d0e62e6e9": "country_usa_1786206280836.png",
    "1524492412937-b28074a5d7da": "country_india_1786206295041.png",
    
    # Industries
    "1556761175-4b46a572b786": "ind_startups_1786206318113.png",
    "1460925895917-afdab827c52f": "ind_it_saas_1786206333027.png",
    "1556742049-0cfed4f6a45d": "ind_ecommerce_1786206345476.png",
    "1565514120008-8e833441865e": "ind_manufacturing_1786206358131.png",
    "1538108149393-fbbd81895907": "ind_healthcare_1786206372993.png",
    "1586528116311-ad8ed7c15b54": "ind_logistics_1786206385016.png",
    
    # Insights (Fallback to blogs image if specific one wasn't generated)
    "1434626881859-194d67b2b86f": "insight_blogs_1786206408849.png", # Insights hero
    "1455390582262-044cdead27d8": "insight_blogs_1786206408849.png", # Blogs
    "1454165804606-c3d57bc86b40": "insight_blogs_1786206408849.png", # Business Guides
    "1554224155-6726b3ff858f": "insight_blogs_1786206408849.png", # Tax Updates
    "1506784365847-bbad939e9335": "insight_blogs_1786206408849.png", # Compliance Calendar
    "1516321318423-f06f85e504b3": "insight_blogs_1786206408849.png", # FAQs
    
    # Other generic replacements
    "1486406146926-c627a92ad1ab": "insight_blogs_1786206408849.png",
    "1573164713988-8665fc963095": "insight_blogs_1786206408849.png",
    "1573497019940-1c28c88b4f3e": "insight_blogs_1786206408849.png",
    "1600880292203-757bb62b4baf": "insight_blogs_1786206408849.png",
    "1589561253811-30040e94bbbf": "insight_blogs_1786206408849.png",
    "1553877522-43269d4ea984": "country_singapore_1786206240342.png"
}

def repl(m):
    unsplash_id = m.group(1)
    if unsplash_id in mapping:
        return f"{{prefix}}assets/images/{mapping[unsplash_id]}"
    return m.group(0)

# Replace all https://images.unsplash.com/photo-{id}?w=800 with {prefix}assets/images/filename.png
c = re.sub(r'https://images\.unsplash\.com/photo-([a-zA-Z0-9\-]+)\?w=800', repl, c)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(c)

print("Local images mapped!")
