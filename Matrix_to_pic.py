from PIL import Image

# Read the RGB values from the output file
# with open('teatime2.txt', 'r') as f:
#     rgb_values = f.readlines()


width = 2000 
height = 2001
# Create a new image with the same dimensions as the original image
image = Image.new('RGB', (width, height))

# Set the RGB value of each pixel in the new image
# for x in range(width):
#     for y in range(height):
#         # Get the RGB value of the pixel
#         r, g, b = map(int, rgb_values.split())
#         # Set the RGB value of the pixel in the new image
#         # print(x,y,r,g,b)
#         image.putpixel((x, y), (r, g, b))

with open('test.txt', 'r') as f:
    for line in f:
        x,y,r,g,b = map(int, line.strip().split())
        # print(x, y, z)
        image.putpixel((x, y), (r, g, b))

# Save the new image as a JPEG file
image.save('new_image3.jpg')