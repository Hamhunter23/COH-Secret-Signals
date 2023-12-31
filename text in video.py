import cv2

# Function to embed encrypted text into video frames
def embed_encrypted_text_in_video(video_path, encrypted_text, output_path):
    video_capture = cv2.VideoCapture(video_path)
    frame_width = int(video_capture.get(3))
    frame_height = int(video_capture.get(4))
    frame_rate = int(video_capture.get(5))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, frame_rate, (frame_width, frame_height))

    text_index = 0

    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if not ret:
            break

        if text_index < len(encrypted_text):
            # Embed the encrypted text character into the pixel values of the frame
            char = encrypted_text[text_index]
            char_code = ord(char)
            frame[0][0] = (char_code, frame[0][0][1], frame[0][0][2])  # Only modify the red channel
            text_index += 1

        out.write(frame)

    video_capture.release()
    out.release()

# Example usage for encryption
video_file = "input.mp4"
encrypted_text_to_embed = "this is a simple text"
output_video_file = "encrypted_video.mp4"
embed_encrypted_text_in_video(video_file, encrypted_text_to_embed, output_video_file)
