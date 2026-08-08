import re
import os

filepath = 'C:/Users/roopc/.gemini/antigravity/brain/c93a1649-f9d8-443c-9da6-d0a3b3a80bd0/scratch/rebuild_ui.py'
with open(filepath, 'r', encoding='utf-8') as f:
    c = f.read()

mapping = {
    "truvisory1": "1486406146926-c627a92ad1ab",
    "truvisory2": "1573164713988-8665fc963095",
    "truvisory3": "1573497019940-1c28c88b4f3e",
    "truvisory4": "1600880292203-757bb62b4baf",
    "truvisory5": "1589561253811-30040e94bbbf",
    "truvisory6": "1512453979436-5a5369ce9e1f",
    "truvisory7": "1525625293386-3f8f99389edd",
    "truvisory8": "1513635269975-59663e0ac1ad",
    "truvisory9": "1506927802816-6466f2043e06",
    "truvisory10": "1496442226666-8d4d0e62e6e9",
    "truvisory11": "1524492412937-b28074a5d7da",
    "truvisory12": "1556761175-4b46a572b786",
    "truvisory13": "1460925895917-afdab827c52f",
    "truvisory14": "1556742049-0cfed4f6a45d",
    "truvisory15": "1565514120008-8e833441865e",
    "truvisory16": "1538108149393-fbbd81895907",
    "truvisory17": "1586528116311-ad8ed7c15b54",
    "truvisory18": "1434626881859-194d67b2b86f",
    "truvisory19": "1455390582262-044cdead27d8",
    "truvisory20": "1454165804606-c3d57bc86b40",
    "truvisory21": "1554224155-6726b3ff858f",
    "truvisory22": "1506784365847-bbad939e9335",
    "truvisory23": "1516321318423-f06f85e504b3",
    "truvisory24": "1553877522-43269d4ea984"
}

def repl(m):
    key = m.group(1)
    if key in mapping:
        return f"https://images.unsplash.com/photo-{mapping[key]}?w=800"
    return m.group(0)

c = re.sub(r'https://picsum\.photos/seed/([^/]+)/800/500', repl, c)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(c)

print("Images fixed!")
