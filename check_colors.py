from PIL import Image
import os

images = {
    "leharin.jpg": "C:\\Users\\Leharin\\.gemini\\antigravity\\scratch\\ghosttrack\\leharin.jpg",
    "rajamaran.jpg": "C:\\Users\\Leharin\\.gemini\\antigravity\\scratch\\ghosttrack\\rajamaran.jpg",
    "sumith.jpg": "C:\\Users\\Leharin\\.gemini\\antigravity\\scratch\\ghosttrack\\sumith.jpg"
}

for name, path in images.items():
    if os.path.exists(path):
        img = Image.open(path)
        img = img.resize((1, 1))
        color = img.getpixel((0, 0))
        print(f"{name}: average color = {color}")
    else:
        print(f"{name} does not exist!")
