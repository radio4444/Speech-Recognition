from googlesearch import search
import webbrowser


class Information:
	def __init__(self, words):
		self.words = words

	def search_web(self):
		urls = []
		for url in enumerate(search(self.words, stop=4), 1):
			urls.append(url)
		return urls

