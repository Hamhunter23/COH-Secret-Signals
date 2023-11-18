
from stegano import lsb
from PIL import Image

# Open the cover image
cover_image = Image.open('cover_image.png')

# Define the message to be encoded
message = "This is a secret message."

# Encode the message into the cover image using LSB steganography
encoded_image = lsb.hide(cover_image, message)

# Save the encoded image
encoded_image.save('encoded_image.png')

