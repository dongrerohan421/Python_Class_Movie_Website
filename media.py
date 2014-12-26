class Movie() :		# define class movie
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):		# creates and initializes space in memory
		self.title = movie_title	# initialize movie variables
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
