from PIL import Image
def decode_image(encoded_image_path, output_path):
    encoded_image = Image.open(encoded_image_path)

    encoded_pixels = encoded_image.load()

    width, height = encoded_image.size

    decoded_image = Image.new('RGB', encoded_image.size)

    for i in range(width):
        for j in range(height):
            encoded_pixel = encoded_pixels[i, j]

            new_pixel = ((encoded_pixel[0] & 0x01) << 7,
                         (encoded_pixel[1] & 0x01) << 7,
                         (encoded_pixel[2] & 0x01) << 7)

            decoded_image.putpixel((i, j), new_pixel)

    decoded_image.save(output_path)

decode_image('encoded.png', 'decoded.png')
