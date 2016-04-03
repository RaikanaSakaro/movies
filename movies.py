#Define variables for lists of info
movie_names = ['The Boy','Steve Jobs','Mean Girls','Terminator Genisys','Prisoners']
movie_ratings = ['PG-13','R','PG-13','PG-13','R']
movie_bechdel = ['3','3','3','0','3']
movie_stars = ['6.2','7.3','7.0','7.0','8.1']
movie_genres = ['Horror/Thriller','Biography/Drama','Comedy','Action/Adventure/Sci-fi','Mystery/Crime/Drama/Thriller']

#Create a master list of all the variables
movies_info = zip(movie_names, movie_ratings, movie_bechdel, movie_stars, movie_genres)

#Print out the information for each movie in the list
for movie in movies_info:
#	print movie (Too much punctuation)
#Print the info with just commas. Information from stackoverflow.com.
#http://stackoverflow.com/questions/11858159/displaying-python-2d-list-without-commas-brackets-etc-and-newline-after-every
	print ", ".join(map(str,movie))
