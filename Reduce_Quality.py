from PIL import Image

# Open the image
image = Image.open('tea.jpg')


# # Resize the image to a smaller size
width, height = image.size
resized_image = image.resize((width, height))

# Save the resized image to a file with reduced quality
resized_image.save('compressed_image.jpg', quality=50)