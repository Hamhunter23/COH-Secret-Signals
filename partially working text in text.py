
def text_to_binary(text):
    binary = ""
    for char in text:
        binary += format(ord(char), '08b')
    return binary

def binary_to_text(binary):
    text = ""
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        text += chr(int(byte, 2))
    return text

def embed_secret_message(carrier_text, secret_message):
    binary_secret_message = text_to_binary(secret_message)
    modified_carrier_text = ""
    for i, char in enumerate(carrier_text):
        binary_char = format(ord(char), '08b')
        if i < len(binary_secret_message):
            modified_char = binary_char[:-1] + binary_secret_message[i]
        else:
            modified_char = binary_char
        modified_carrier_text += chr(int(modified_char, 2))
    return modified_carrier_text

def extract_secret_message(modified_carrier_text):
    binary_secret_message = ""
    for char in modified_carrier_text:
        binary_char = format(ord(char), '08b')
        binary_secret_message += binary_char[-1]
    secret_message = binary_to_text(binary_secret_message)
    return secret_message

carrier_text = "The quick brown fox jumps over the lazy dog."
secret_message = "helllllllllllo i am garv haldia and i am thirsty"
modified_carrier_text = embed_secret_message(carrier_text, secret_message)
with open('modified_carrier_text.txt', 'w') as f:
    f.write(modified_carrier_text)

