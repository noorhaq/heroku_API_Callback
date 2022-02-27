from flask import Flask
from PIL import Image
import requests

app = Flask(__name__)

@app.route("/")
def index():
    # Read Image
    # while True:
    img = Image.open(requests.get('https://image.thum.io/get/auth/8123-imagecolorpicker/png/fullpage/noanimate/wait/3/https://global-mind.org/gcpdot/gcp.html', stream=True).raw)
    # print(img)
    # img = Image.open(im)

    # Convert Image into RGB
    img = img.convert('RGB')

    # call function
    common_color = most_common_used_color(img)

    return common_color

def most_common_used_color(img):
    # Get width and height of Image
    width, height = img.size
 
    # Initialize Variable
    r_total = 0
    g_total = 0
    b_total = 0
 
    count = 0
 
    # Iterate through each pixel
    for x in range(0, width):
        for y in range(0, height):
            # r,g,b value of pixel
            r, g, b = img.getpixel((x, y))
 
            r_total += r
            g_total += g
            b_total += b
            count += 1
 
    return round(r_total/count), round(g_total/count), round(b_total/count),
 