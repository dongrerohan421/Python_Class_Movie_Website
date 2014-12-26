import media	# imports media package i.e all class, functions and objects

toy_story = media.Movie("Toy Story",
			"A story of boy and his toys that come to life",
			"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
			"https://www.youtube.com/watch?v=0q1rxc96m2w")	# calling class Movie from media.py and assign to variable toy_story

print (toy_story.storyline)
