from PIL import Image
import os

imgs = [os.path.join("images", file) for file in os.listdir("images")]

print("Image Resizer")
width = int(input("width >>> "))
height = int(input("height >>> "))

for img in imgs:
    im1 = Image.open(img)
    im2 = im1.resize((width, height))
    im2.save(img)
