from PIL import Image

# Open the PNG file
image = Image.open('123.jpg')

# Convert the image to a matrix of RGB values
rgb_matrix = image.convert('RGB')

# Get the size of the image
width, height = image.size

# Open the output file for writing
with open('test.txt', 'w') as f:
    # Loop through each pixel in the image
    for x in range(width):
        for y in range(height):
            # Get the RGB value of the pixel
            r, g, b = rgb_matrix.getpixel((x, y))
            # Write the RGB value to the output file
            # f.write(f"Pixel ({x}, {y}): R={r}, G={g}, B={b}\n")
            f.write(f"{x} {y} {r} {g} {b}\n")
            (x,y) position of pixel 
            r,g,b value of pixel