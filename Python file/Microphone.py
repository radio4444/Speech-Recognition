import speech_recognition as sr


# Read and save the audio file function
# Maybe later we can let the user specify the file name
def speech_to_text_file(mic_recording):
	text_file = open("Testing 1", 'a')
	text_file.write(mic_recording)
	text_file.close()

	read_text_file = open('Testing 1', 'r')
	print(read_text_file.read())


r = sr.Recognizer()
mic = sr.Microphone()

try:
	with mic as source:
		# r.adjust_for_ambient_noise(source)
		audio = r.listen(source)

	# print(r.recognize_google(audio))  # Sentence is fine but not when it comes to name
	speech_to_text_file(r.recognize_google(audio))
except sr.UnknownValueError:
	print("Speech Recognition could not understand audio")
except Exception as e:
	print(f"An unexpected error occurred: {e}")

# pretty much have r.recognize.goggle(audio) be store in the file.
# so first need to figure out how to use file. Create a function instead of write out
