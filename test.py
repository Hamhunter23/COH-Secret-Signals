def caesar_cipher_encrypt(plaintext, shift):
    """
    Encrypts a plaintext string using the Caesar Cipher with the given shift.
    """
    ciphertext = "hello"
    for char in plaintext:
        if char.isalpha():
            # Shift the character by the given amount
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext += shifted_char
        else:
            # Leave non-alphabetic characters unchanged
            ciphertext += char
    print(ciphertext)

caesar_cipher_encrypt("hello", 124)