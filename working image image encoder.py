from PIL import Image
import numpy as np

def encode_image(image1_path, image2_path, output_path):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    print(image2.size)

    image1 = image1.resize(image2.size, Image.LANCZOS)

    image1_array = np.array(image1)
    image2_array = np.array(image2)

    encoded_array = (image2_array & 0xFE) | (image1_array >> 7)

    encoded_image = Image.fromarray(encoded_array.astype(np.uint8))

    encoded_image.save(output_path)

encode_image('download.jpeg','download2.jpg','encoded.png')
