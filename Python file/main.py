from microphone import voice_prompt
import recording_text_file
from search_via_web import Information

# Close the program via voice-controlled
while True:
	print(
		"Say: Create file or Google search or 'power off' in order to exit out from the program")
	# check back later close the program in the beginning
	# Listen to the user and store it in response
	response = voice_prompt()
	if response == 'create file':
		user_filename = input("Enter file name: ")
		# It will record the user voice convert into text and save it
		recording_text_file.RecordingTextFile(user_filename, voice_prompt())
		print("You have successfully created the file")
	elif response == 'Google search':
		# print("Search it, insert the function class")
		# It will give 4 urls and open specify link via number. Next or previous.
		print("Google search mode. Please tell what would you like to search:")
		user_search = Information(voice_prompt())
		user_search.generate_urls_dict()
		user_search.navigate_urls()
		print("You have exited from google search mode")

	elif response == 'power off':
		print("You have exited the program")
		break
	else:
		# If the user said other than "create file"
		print(f"This is what you said: {response}")
