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
def decrypt(ciphertext):
    """
    Decrypt the ciphertext using the Blowfish algorithm with the key read from the file.
    Returns the decrypted plaintext.
    """
    # Extract the IV from the ciphertext
    iv = ciphertext[:Blowfish.block_size]

    # Create the cipher object and decrypt the ciphertext
    cipher = Blowfish.new(read_key(), Blowfish.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext[Blowfish.block_size:]))

    # Return the decrypted plaintext
    return plaintext

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

image = Image.open(r'C:\Users\aimem\OneDrive\Desktop\CODE OF HONOUR\encoded_image.png')
ciphertext = lsb.reveal(image)
decrypted_plaintext = decrypt(ciphertext)
print(decrypted_plaintext.decode())
