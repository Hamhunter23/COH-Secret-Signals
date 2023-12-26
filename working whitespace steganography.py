def encode(message, filename):
    
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    
    with open(filename, 'w') as f:
        for bit in binary_message:
            if bit == '0':
                f.write(' ')
            else:
                f.write('\t')

def decode(filename):
    with open(filename, 'r') as f:
        binary_message = ''
        for char in f.read():
            if char == ' ':
                binary_message += '0'
            elif char == '\t':
                binary_message += '1'
        
        message = ''
        for i in range(0, len(binary_message), 8):
            byte = binary_message[i:i+8]
            message += chr(int(byte, 2))
        return message

while True:
    choice = input("Enter 'e' to encode or 'd' to decode: ")
    if choice == 'e':
        message = input("Enter the message to encode: ")
        filename = input("Enter the filename to save the encoded message: ")
        encode(message, filename)
        print("Message encoded and saved to file.")
        break
    elif choice == 'd':
        filename = input("Enter the filename to decode: ")
        message = decode(filename)
        print("Decoded message: ", message)
        break
    else:
        print("Invalid choice. Please enter 'e' or 'd'.")
