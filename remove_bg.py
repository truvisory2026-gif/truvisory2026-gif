from PIL import Image
import sys

def remove_white_bg(input_path, output_path):
    img = Image.open(input_path)
    img = img.convert('RGBA')
    datas = img.getdata()

    newData = []
    for item in datas:
        # Change all white (also shades of whites)
        # to transparent
        if item[0] > 200 and item[1] > 200 and item[2] > 200:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(output_path, 'PNG')
    print('Logo background removed successfully.')

remove_white_bg(r'C:\Users\roopc\.gemini\antigravity\brain\dbc733fb-2e5f-4f17-9890-0613db826560\media__1785223040456.png', r'c:\Users\roopc\OneDrive\Desktop\truvisory\assets\images\logo.png')
