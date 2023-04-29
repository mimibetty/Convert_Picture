from PIL import Image

# Open the PNG file
image = Image.open('tea.jpg')

# Convert the image to a matrix of RGB values
rgb_matrix = image.convert('RGB')

# Get the size of the image
width, height = image.size

print(width, height)
# Create a new image with the same size as the input image
output_image = Image.new('RGB', (width, height))

# Loop through each pixel in the image
for x in range(width):
    for y in range(height):
        # Get the RGB value of the pixel
        r, g, b = rgb_matrix.getpixel((x, y))
        # Set the RGB value of the corresponding pixel in the output image
        output_image.putpixel((x, y), (r, g, b))

# Save the output image in JPEG format
output_image.save('output.jpg', 'JPEG')