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
# Listen to user and do the prompt the user tell to do
try:
	print("Say: Create file")
	with mic as voice:
		response = r.listen(voice)
	response_recognize = r.recognize_google(response)
	if response_recognize == 'create file':
		rstt()
except sr.UnknownValueError:
	print("The mic is picking up your voice")
except Exception as a:
	print(f"This is an unexpected error {a}")

input("Press Enter to exit...")
