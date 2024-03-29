from googlesearch import search
import webbrowser
from microphone import voice_prompt


class Information:
	def __init__(self, words):
		self.words = words
		self.new_results = 0
		self.order = ['first', 'second', 'third', 'fourth']
		self.urls_dict = {}

	def generate_urls_dict(self):
		self.urls_dict = {}
		# generate 4 urls
		urls_generator = search(self.words, start=self.new_results, stop=4)
		# urls are assigned to keys and store in dictionary
		self.urls_dict = dict(zip(self.order, urls_generator))
		return self.urls_dict

	def __str__(self):
		return '\n'.join(self.urls_dict)

	# Either generate new or go back to 4 urls. Or exit out. Or open up the link by indicating number.
	def navigate_urls(self):

		# Keep looping until the user input number for the url
		while True:
			# printout the urls with keys
			for key, value in self.urls_dict.items():
				print(f'{key} : {value}')

			print("Specify the link via first-fourth or next or previous or exit: ")
			user_input = voice_prompt()

			try:
				# give new 4 urls
				if user_input == 'next':
					# increment start value in search function by 4
					self.new_results += 4
					# calling this method updated start value
					self.generate_urls_dict()
				# show previous 4 urls
				elif user_input == 'previous':
					# decrement start value in search function by 4
					self.new_results -= 4
					if self.new_results < 0:
						print(
							"You cannot go back anymore. These are the first 4 urls")  # maybe remove the extra statement
					# calling this method updated start value
					self.generate_urls_dict()
				elif user_input == 'exit':
					break
				else:
					# Open the url, the user has specified
					webbrowser.open(self.urls_dict[user_input])
					break
			except Exception as e:
				print("Invalid input. Please choose the correct response")
