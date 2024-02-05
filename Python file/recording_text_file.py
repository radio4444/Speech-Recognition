import os


class RecordingTextFile:

	# Constructor method
	# def __init__(self, directory_name='speech to text'):
	# 	self.directory_name = directory_name
	# Use this, if: let the user create new file and then end the program

	def __init__(self, file_name, mic_recording, directory_name='speech to text'):
		self.directory_name = directory_name
		self.stt_file(file_name, mic_recording)

	# Create new directory

	def create_directory(self):
		current_directory = os.getcwd()
		# One level up the current directory and create new directory
		directory_path = os.path.join(current_directory, '..', self.directory_name)
		if not os.path.exists(directory_path):  # if the directory does not exist, create it
			os.makedirs(directory_path)

		return directory_path

	# Store the recording speech to text file and save it
	def stt_file(self, file_name, mic_recording):
		directory_path = self.create_directory()
		file_path = os.path.join(directory_path, file_name)
		with open('{}.txt'.format(file_path), 'a') as text_file:  # Create new and save the file
			text_file.write(mic_recording)
		with open('{}.txt'.format(file_path), 'r') as read_text_file:  # Output the file that had just been saved
			print(read_text_file.read())
