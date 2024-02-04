import speech_recognition as sr
from RecordingTextFile import RecordingTextFile


def voice_prompt():
	r = sr.Recognizer()
	mic = sr.Microphone()
	# Listen to the user through the mic
	print("Now it is listening to your voice....")
	try:
		with mic as source:
			audio = r.listen(source)
		return r.recognize_google(audio)
	except sr.UnknownValueError:  # if the mic is not picking up any voice
		print("Speech Recognition could not understand audio")
	except Exception as e:
		print(f"An unexpected error occurred: {e}")


# Close the program via voice-controlled
while True:
	print("Say: Create file")
	# Listen to the user and store it in response
	response = voice_prompt()
	if response == 'create file':
		user_filename = input("Enter file name: ")
		# It will record the user voice convert into text and save it
		RecordingTextFile(user_filename, voice_prompt())
	else:
		# If the user said other than "create file"
		print(f"This is what you said: {response}")
	print("Say: 'close the program' in order to exit out from the program")
	if voice_prompt() == 'close the program':
		break
