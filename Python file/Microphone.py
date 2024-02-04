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


print("Say: Create file")
response = voice_prompt()
if response == 'create file':
	user_filename = input("Enter file name: ")
	# Save recording in text format file
	RecordingTextFile(user_filename, voice_prompt())
else:
	print(f"This is what you said: {response}")
input("Press Enter to exit...")
