import webbrowser

class Movie() :		# define class movie
	""" This class provides a way to store movie related information"""

	VALID_RATINGS = ["G","PG","PG-13","R","G"]
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):		# creates and initializes space in memory
		self.title = movie_title	# initialize movie variables
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self) : 
		webbrowser.open(self.trailer_youtube_url)	# open webbrowser
