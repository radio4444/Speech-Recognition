import speech_recognition as sr
from RecordingTextFile import RecordingTextFile

r = sr.Recognizer()
mic = sr.Microphone()

user_file_name = input("Enter the file name: ")
try:
	# Listen to the user through the mic
	print("Now it is listening to your voice....")
	with mic as source:
		audio = r.listen(source)
	# Save recording in text format file
	recording_file_object = RecordingTextFile(user_file_name, r.recognize_google(audio))
except sr.UnknownValueError:  # if the mic is not picking up any voice
	print("Speech Recognition could not understand audio")
except Exception as e:
	print(f"An unexpected error occurred: {e}")
input("Press Enter to exit...")
