from PIL import Image, ImageFilter

# Open an image
img = Image.open("example.jpg")

# Resize the image
resized_img = img.resize((200, 200))
resized_img.save("resized.jpg")

# Convert to grayscale
gray_img = img.convert("L")
gray_img.save("gray.jpg")

# Apply a blur filter
blurred_img = img.filter(ImageFilter.BLUR)
blurred_img.save("blurred.jpg")

print("Image processing done using Pillow!")
