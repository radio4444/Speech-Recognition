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
			# maybe be turn this into function
			for url in search(self.words, start=new_results, stop=4):
				urls.append(url)  # store 4 urls via search method
			print('\n'.join(urls))  # show the 4 url
			user_input = input("Specify the link via number 0-3 or refresh: ")
			new_results = new_results + 4
			if user_input != 'refresh':
				# Open the url, the user has specified
				webbrowser.open(urls[int(user_input)])
				break
