import speech_recognition as sr
from RecordingTextFile import RecordingTextFile


def rstt():
	user_file_name = input("Enter the file name: ")
	# Listen to the user through the mic
	print("Now it is listening to your voice....")
	try:
		with mic as source:
			audio = r.listen(source)
		# Save recording in text format file
		RecordingTextFile(user_file_name, r.recognize_google(audio))
	except sr.UnknownValueError:  # if the mic is not picking up any voice
		print("Speech Recognition could not understand audio")
	except Exception as e:
		print(f"An unexpected error occurred: {e}")


r = sr.Recognizer()
mic = sr.Microphone()

user_option = input("Enter your choice: 1. Record my speech and store it: ")
if user_option == '1':
	rstt()
input("Press Enter to exit...")
