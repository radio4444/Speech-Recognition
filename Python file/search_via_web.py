from googlesearch import search


class Information:
	def __init__(self, words):
		self.words = words
		self.search_web()

	def search_web(self):
		for url in search(self.words, stop=4):
			print(url)
			# If I say, show more, then it will show 4 more
