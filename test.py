import urllib2
import simplejson
import random
import time
import io
movie_json = {'Plot': "A chronicle of one woman's 1,100-mile solo hike undertaken as a way to recover from a recent catastrophe.", 'Rated': 'R', 'Response': 'True', 'Language': 'English', 'Title': 'Wild', 'Country': 'USA', 'Writer': 'Nick Hornby, Cheryl Strayed (memoir "Wild: From Lost to Found on the Pacific Crest Trail")', 'Metascore': '76', 'imdbRating': '7.2', 'Director': u'Jean-Marc Vall\xe9e', 'Released': '19 Dec 2014', 'Actors': 'Reese Witherspoon, Laura Dern, Thomas Sadoski, Keene McRae', 'Year': '2014', 'Genre': 'Biography, Drama', 'Awards': 'Nominated for 2 Oscars. Another 8 wins & 48 nominations.', 'Runtime': '115 min', 'Type': 'movie', 'Poster': 'http://ia.media-imdb.com/images/M/MV5BMTczNzI2MDc1Ml5BMl5BanBnXkFtZTgwOTU5NTYxMjE@._V1_SX300.jpg', 'imdbVotes': '41294', 'imdbID': 'tt2305051'}

movie_file = open("Movie_listings_2014.csv", "w")

def encode(text):
    return text.encode('utf-8')

# Write the movie information to file
title = movie_json["Title"]
year = movie_json["Year"]
released = movie_json["Released"].split(" ")[1]
language = movie_json["Language"]
rated = movie_json["Rated"]
#imdb_rating = movie_json["imdbRating"]
runtime = movie_json["Runtime"]
#writer = movie_json["Writer"].split(",")[0]
director = movie_json["Director"]
#awards = movie_json["Awards"]
imdb_ID = movie_json["imdbID"]
#imdbVotes = movie_json["imdbVotes"]

movie_file.write(title+",")
movie_file.write(year+",")
movie_file.write(encode(director)+",")

movie_file.close()