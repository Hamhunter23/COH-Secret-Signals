from PIL import Image
import random

# Open the image file
image = Image.open("path/to/image.jpg")

# Get the dimensions of the image
width, height = image.size

# Create a new image to store the encrypted pixels
encrypted_image = Image.new("RGB", (width, height))

# Create a list of all the pixel coordinates
pixel_coordinates = [(x, y) for x in range(width) for y in range(height)]

# Shuffle the pixel coordinates
random.shuffle(pixel_coordinates)

# Loop through each pixel coordinate and encrypt the pixel
for x, y in pixel_coordinates:
    # Get the original pixel value
    original_pixel = image.getpixel((x, y))

    # Encrypt the pixel value
    encrypted_pixel = (
        (original_pixel[0] ^ x) % 256,
        (original_pixel[1] ^ y) % 256,
        (original_pixel[2] ^ (x + y)) % 256,
    )

    # Set the encrypted pixel in the new image
    encrypted_image.putpixel((x, y), encrypted_pixel)

# Save the encrypted image
encrypted_image.save("path/to/encrypted_image.jpg")
