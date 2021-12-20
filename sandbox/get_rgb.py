from PIL import Image

filename = "sandbox/pic.jpg"
img = Image.open(filename)
colors = img.getpixel((320,240))
print(colors[1])