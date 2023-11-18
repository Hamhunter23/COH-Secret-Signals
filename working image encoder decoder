from Crypto.Cipher import Blowfish
from Crypto import Random
import stegano.lsb as lsb
from PIL import Image

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

def decrypt(ciphertext):
    """
    Decrypt the ciphertext using the Blowfish algorithm with the key read from the file.
    Returns the decrypted plaintext.
    """
    # Extract the IV from the ciphertext
    iv = ciphertext[:Blowfish.block_size]

    # Create the cipher object and decrypt the ciphertext
    cipher = Blowfish.new(read_key(), Blowfish.MODE_CBC, iv.encode())
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

# Generate a new key and write it to a file
key = Random.get_random_bytes(16)
with open('key.txt', 'wb') as f:
    f.write(key)

while True:
    print("Select an option:")
    print("1. Encode")
    print("2. Decode")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == '1':
        path = input("Enter the path of the image: ")
        image = Image.open(path)
        plaintext = input("Enter the text to be encrypted: ")
        #key = Random.get_random_bytes(16)
        # with open('key.txt', 'wb') as f:
        #    f.write(key)
        #ciphertext = encrypt(plaintext)
        encoded_image = lsb.hide(image, plaintext)
        encoded_image.save("encoded_image.png")
    elif choice == '2':
        path = input("Enter the path of the image: ")
        image = Image.open(path)
        plaintext = lsb.reveal(image)
        #decrypted_plaintext = decrypt(ciphertext)
        # keypath = input("Enter the path of the key: ")
        print("Decrypted text:", plaintext)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

