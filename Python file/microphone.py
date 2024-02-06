import speech_recognition as sr


def voice_prompt():
	r = sr.Recognizer()
	mic = sr.Microphone()
	# Listen to the user through the mic
	print("Now it is listening to your voice....")
	# keep looping till it can return.
	while True:
		try:
			with mic as source:
				audio = r.listen(source)
			return r.recognize_google(audio)  # act as break for while loop
		except sr.UnknownValueError:  # if the mic is not picking up any voice
			print("Speech Recognition could not understand. Try saying it again")
		except Exception as e:
			print(f"An unexpected error occurred: {e}")
