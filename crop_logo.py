from PIL import Image

logo_path = 'C:/Users/roopc/OneDrive/Desktop/truvisory/assets/images/logo.png'

try:
    img = Image.open(logo_path).convert("RGBA")
    
    # Get bounding box of non-transparent pixels
    bbox = img.getbbox()
    if bbox:
        cropped_img = img.crop(bbox)
        cropped_img.save(logo_path)
        print("Logo successfully cropped to visible bounds.")
    else:
        print("Image is entirely transparent or empty.")
except Exception as e:
    print(f"Error cropping logo: {e}")
