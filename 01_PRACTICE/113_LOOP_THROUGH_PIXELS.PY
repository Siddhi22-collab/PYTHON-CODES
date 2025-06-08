from PIL import Image

# Open image
img = Image.open('your_image.jpg')

# Convert image to RGB
img = img.convert('RGB')

# Get width and height
width, height = img.size

# Access each pixel
for x in range(width):
    for y in range(height):
        r, g, b = img.getpixel((x, y))
        print(f"Pixel at ({x},{y}) - R: {r}, G: {g}, B: {b}")
        # Example: Make all pixels red
        img.putpixel((x, y), (255, 0, 0))

# Save the red image
img.save('red_image.jpg')
img.show()
