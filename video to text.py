import cv2

# Function to extract and decrypt text from video frames
def extract_and_decrypt_text_from_video(video_path):
    video_capture = cv2.VideoCapture(video_path)
    extracted_text = []

    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if not ret:
            break

        char_code = frame[0][0][0]
        char = chr(char_code)
        extracted_text.append(char)

    return "".join(extracted_text)

# Function to decrypt text using a simple Caesar cipher
def decrypt_text(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Example usage for decryption
video_file = "encrypted_video.mp4"
decryption_key = 3
encrypted_text = extract_and_decrypt_text_from_video(video_file)
decrypted_text = decrypt_text(encrypted_text, decryption_key)
print("Decrypted Text:", decrypted_text)
