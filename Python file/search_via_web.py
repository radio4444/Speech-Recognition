from googlesearch import search
import webbrowser


class Information:
	def __init__(self, words):
		self.words = words

	def search_web(self):
		new_results = 0
		# Keep looping until the user input number for the url
		while True:
			urls = []
			for url in search(self.words, start=new_results, stop=4):
				urls.append(url)  # store 4 urls via search method
			print('\n'.join(urls))  # show the 4 url
			user_input = input("Specify the link via number 0-3 or next or previous or exit: ")
			try:
				# give new 4 urls
				if user_input == 'next':
					new_results = new_results + 4  # increment start value in search function by 4
				# show previous 4 urls
				elif user_input == 'previous':
					new_results = new_results - 4  # decrement start value in search function by 4
					if new_results < 0:
						print(
							"You cannot go back anymore. These are the first 4 urls")  # maybe remove the extra statement
				elif user_input == 'exit':
					break
				else:
					# Open the url, the user has specified
					webbrowser.open(urls[int(user_input)])
					break
			except Exception as e:
				print("Invalid input. Please choose the correct response")
