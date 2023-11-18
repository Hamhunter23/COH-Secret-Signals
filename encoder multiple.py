from Crypto.Cipher import Blowfish
from Crypto import Random
import struct
from PIL import Image
import stegano.lsb as lsb

def read_key():
    """
    Read the key from the file called key.txt
    """
    with open('key.txt', 'rb') as f:
        key = f.read()
    return key

def encrypt(plaintext):
    """
    Encrypt the plaintext using the Blowfish algorithm with the key read from the file.
    Returns the encrypted ciphertext.
    """
    # Generate a random initialization vector
    iv = Random.new().read(Blowfish.block_size)

    # Create the cipher object and encrypt the plaintext
    cipher = Blowfish.new(read_key(), Blowfish.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext))

    # Return the IV and ciphertext as a single byte string
    return iv + ciphertext

def pad(s):
    """
    Pad the given string s with zeros to a multiple of the block size.
    """
    if isinstance(s, str):
        s = s.encode()
    return s + (Blowfish.block_size - len(s) % Blowfish.block_size) * bytes([0])

def unpad(s):
    """
    Remove the zero padding from the given string s.
    """
    return s.rstrip(bytes([0]))

image = Image.open(r'C:\Users\aimem\OneDrive\Desktop\CODE OF HONOUR\download.jpeg')
key = Random.get_random_bytes(16)
with open('key.txt', 'wb') as f:
    f.write(key)

plaintext = input("Enter the text to be encrypted: ").encode()
ciphertext = encrypt(plaintext)
print(ciphertext)
encoded_image = lsb.hide(image, ciphertext)
encoded_image.save("encoded_image.png")
