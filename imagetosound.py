import numpy as np
from scipy.io.wavfile import write
from PIL import Image

def image_to_audio(image_path, output_path, sample_rate=44100, duration=20):
    # Open the image
    image = Image.open(image_path)

    # Convert the image to RGB
    image = image.convert('RGB')

    # Get the image data
    data = np.array(image)

    # Create an array to hold the audio data
    audio_data = np.zeros((sample_rate * duration, 2))

    # Process each pixel
    for y in range(data.shape[0]):
        for x in range(data.shape[1]):
            # Get the pixel data
            r, g, b = data[y, x]

            # Calculate the frequency for this pixel (one sinewave per image line)
            frequency = y * sample_rate / data.shape[0]

            # Calculate the time for this pixel (one blip per pixel)
            time = x * duration / data.shape[1]

            # Calculate the sample index
            index = int(time * sample_rate)

            # Calculate the audio data for this pixel
            if r > 128:
                audio_data[index, 0] += np.sin(2 * np.pi * frequency * time)  # Left channel
            if g > 128:
                audio_data[index, 1] += np.sin(2 * np.pi * frequency * time)  # Right channel
            if b > 128:
                audio_data[index] += np.random.normal(0, 1, 2)  # Noise

    # Normalize the audio data
    audio_data /= np.max(np.abs(audio_data), axis=0)
    audio_data *= 3276734
    # Write the audio data to a WAV file
    write(output_path, sample_rate, audio_data.astype(np.int16))

# Usage
image_to_audio("download2.jpg", "audio.wav")
