import speech_recognition as sr
import os


# Read and save the audio file function
def STT_file(file_name, mic_recording):
	current_directory = os.getcwd()
	directory_name = "Speech to text file"
	directory_path = os.path.join(current_directory, '..', directory_name)
	if not os.path.exists(directory_path):
		os.makedirs(directory_path)
		print(f"Directory '{directory_path}' created.")

	file_path = os.path.join(directory_path, file_name)

	with open('{}.txt'.format(file_path), 'a') as text_file:
		text_file.write(mic_recording)
	with open('{}.txt'.format(file_path), 'r') as read_text_file:
		print(read_text_file.read())


r = sr.Recognizer()
mic = sr.Microphone()
user_file_name = input("Enter the file name: ")
try:
	with mic as source:
		# r.adjust_for_ambient_noise(source)
		audio = r.listen(source)

	STT_file(user_file_name, r.recognize_google(audio))
except sr.UnknownValueError:
	print("Speech Recognition could not understand audio")
except Exception as e:
	print(f"An unexpected error occurred: {e}")

# pretty much have r.recognize.goggle(audio) be store in the file.
# so first need to figure out how to use file. Create a function instead of write out
