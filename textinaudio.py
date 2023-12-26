import wave

def case(a):
	if a == 1:
		encode()
	elif a == 2:
		decode()
	elif a == 3:
		quit()
	else:
		print("\nEnter valid Choice!")

def encode():
    print("\nEncoding Starts..")
    audio = wave.open("sampleStego.wav", mode="rb")
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes()))) #reads all the audio frames from the opened audio file and converts them into a list of bytes
    string = input("enter text: ")
    print(string)
    string = string + int((len(frame_bytes) - (len(string) * 8 * 8)) / 8) * '#' #calculates the number of '#' characters needed based on the length of the audio frames and the length of the message
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in string])))#converts the characters in the text message to binary and creates a list of bits
    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit #254 is used for lsb=0
    frame_modified = bytes(frame_bytes)  # Convert back to bytes
    for i in range(0, 10):
        print(frame_bytes[i]) #prints the first 10 bytes of the modified frame
    newAudio = wave.open('sampleStego.wav', 'wb') #opens a new WAV audio file in write binary mode
    newAudio.setparams(audio.getparams())#sets the parameters of the new audio file to match the original audio file.
    newAudio.writeframes(frame_modified)
    newAudio.close()
    audio.close()
    print(" |---->successfully encoded inside sampleStego.wav")

def decode():
	print("\nDecoding Starts..")
	audio = wave.open("sampleStego.wav", mode='rb')
	frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
	extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
	string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
	decoded = string.split("###")[0]
	print("Sucessfully decoded: "+decoded)
	audio.close()	

while(1):
	print("\nSelect an option: \n1)Encode\n2)Decode\n3)exit")
	val = int(input("\nChoice:"))
	case(val)