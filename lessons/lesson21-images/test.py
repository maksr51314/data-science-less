from PIL import Image, ImageFilter

img = Image.open('test.jpeg')
img.show()

# im2 = img.filter(ImageFilter.BLUR)
# im2.show()

print(ImageFilter.BLUR)

im3 = img.filter(ImageFilter.Kernel((3, 3), (-1, -2, -1, 0, 0, 0, 1, 2, 1)))
im3.show()
