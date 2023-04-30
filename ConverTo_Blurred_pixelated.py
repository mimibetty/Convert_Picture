from PIL import Image, ImageFilter

# Open the image
image = Image.open('123.jpg')

# Use the GaussianBlur filter to blur the image
blurred_image = image.filter(ImageFilter.GaussianBlur(radius=10))

# Use the Pixelate filter to pixelate the image
pixelated_image = image.resize((50, 50), resample=Image.BOX).resize(image.size, resample=Image.NEAREST)

# Save the blurred and pixelated images to files
blurred_image.save('blurred_image.jpg')
pixelated_image.save('pixelated_image.jpg')