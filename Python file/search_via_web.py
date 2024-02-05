from googlesearch import search
import webbrowser


class Information:
	def __init__(self, words):
		self.words = words

	def search_web(self):
		urls = []
		for url in search(self.words, stop=4):
			urls.append(url)
		print('\n'.join(urls))
		user_input = int(input("Specify the link via number: "))
		webbrowser.open(urls[user_input])

