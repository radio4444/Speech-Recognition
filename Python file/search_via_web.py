from googlesearch import search
import webbrowser


class Information:
	def __init__(self, words):
		self.words = words
		self.new_results = 0
		self.urls = []

	# Generate 4 new urls using the user phrase
	def generate_urls(self):
		self.urls = []
		for url in search(self.words, start=self.new_results, stop=4):
			self.urls.append(url)  # store 4 urls via search method
		return self.urls  # show the 4 url

	# Either generate new or go back to 4 urls. Or exit out. Or open up the link by indicating number.
	def navigate_urls(self):

		# Keep looping until the user input number for the url
		while True:
			# print 4 new urls
			print('\n'.join(self.urls))
			print("Specify the link via number 1-4 or next or previous or exit: ")
			user_input = input()  # change to response

			try:
				# give new 4 urls
				if user_input == 'next':
					# increment start value in search function by 4
					self.new_results += 4
					# calling this method updated start value
					self.generate_urls()
				# show previous 4 urls
				elif user_input == 'previous':
					# decrement start value in search function by 4
					self.new_results -= 4
					if self.new_results < 0:
						print(
							"You cannot go back anymore. These are the first 4 urls")  # maybe remove the extra statement
					# calling this method updated start value
					self.generate_urls()
				elif user_input == 'exit':
					break
				else:
					# Open the url, the user has specified
					webbrowser.open(self.urls[int(user_input) - 1])
					break
			except Exception as e:
				print("Invalid input. Please choose the correct response")
