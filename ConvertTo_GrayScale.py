from PIL import Image

# Open the image
image = Image.open('tea.jpg')

# Convert the image to grayscale
grayscale_image = image.convert('L')

# Save the modified image
grayscale_image.save('hidden_image.jpg')