import speech_recognition as sr
import os


# Create new directory and save the file name
def create_directory(directory_name):
	current_directory = os.getcwd()
	# One level up the current directory and create new directory
	directory_path = os.path.join(current_directory, '..', directory_name)
	if not os.path.exists(directory_path):  # if the directory does not exist, create it
		os.makedirs(directory_path)

	return directory_path


# Store the recording speech to text file
def STT_file(file_name, mic_recording):
	directory_name = "Speech to text"
	directory_path = create_directory(directory_name)
	file_path = os.path.join(directory_path, file_name)
	with open('{}.txt'.format(file_path), 'a') as text_file:  # Create new and save the file
		text_file.write(mic_recording)
	with open('{}.txt'.format(file_path), 'r') as read_text_file:  # Output the file that had just been saved
		print(read_text_file.read())


r = sr.Recognizer()
mic = sr.Microphone()
user_file_name = input("Enter the file name: ")
try:
	# Listen to the user through the mic
	print("Now it is listening to your voice....")
	with mic as source:
		audio = r.listen(source)
	# Save recording in text format file
	STT_file(user_file_name, r.recognize_google(audio))
except sr.UnknownValueError:  # if the mic is not picking up any voice
	print("Speech Recognition could not understand audio")
except Exception as e:
	print(f"An unexpected error occurred: {e}")
input("Press Enter to exit...")
