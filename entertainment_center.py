import fresh_tomatoes
import media	# imports media package i.e all class, functions and objects

toy_story = media.Movie("Toy Story",
			"A story of boy and his toys that come to life",
			"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
			"https://www.youtube.com/watch?v=0q1rxc96m2w")	# calling class Movie from media.py and assign to variable toy_story
#print (toy_story.storyline)

avatar = media.Movie("Avatar",
			"A marine on an alien planet",
			"http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
			"https://www.youtube.com/watch?v=cRdxXPV9GNQ")	# creates instance of avatar
#print (avatar.storyline)

blackhat = media.Movie ("Blackhat",
			"A man is released from prison to help American and Chinese authorities pursue a mysterious cyber criminal. The dangerous search leads them from Chicago to Hong Kong",
			"http://upload.wikimedia.org/wikipedia/en/5/58/Blackhat_poster.jpg",
			"https://www.youtube.com/watch?v=jZ1ZDlLImF8")	# creates instance of blackhat
#blackhat.show_trailer()

furious_7 = media.Movie("Furious 7",
			"Deckard Shaw seeks revenge against Dominic Toretto and his family for the death of his brother.",
			"http://upload.wikimedia.org/wikipedia/en/b/b8/Furious_7_poster.jpg",
			"www.youtube.com/watch?v=Skpu5HaVkOc")	# creates instance of furious_7
pain_n_gain = media.Movie("Pain & Gain",
			   "Three high-school buddies (Bug Hall, Kevin M. Horton) use a legendary sex manual to lose their virginity.",
			   "http://upload.wikimedia.org/wikipedia/en/4/49/Pain_%26_Gain_film_poster.jpg",
			   "www.youtube.com/watch?v=SEQ8jyvmYtw") 

movies = [toy_story, avatar, blackhat, furious_7, pain_n_gain]	# array which contains list of movies
fresh_tomatoes.open_movies_page(movies)	# calling function
