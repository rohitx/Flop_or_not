# This program gets all of the movie info from the OMDb api website.
#
# Created May 19, 2015
# Author: Rohit Deshpande
#-------------------------------------------
#
# Import statement

import urllib2
import simplejson
import random
import time
import io

# Read in the file with movie names:

myfile = open("Movies_2014.txt", "r")
a = myfile.readlines()

movies = []
for i in range(len(a)):
    if not a[i] == '\n':
        a[i] = (a[i]).strip()
        movies.append(a[i].replace(" ", "+"))

movie_year = '2014'
movie_file = open("Movie_listings_2014.csv", "w")

def encode(text):
    return text.encode('utf-8')

count = 0
#for movie_name in movies:
for i in range(15,16):
    movie_name = movies[i]
    count += 1
    print "Doing movie no: ", count, "Movie: ", movie_name


    # Create a URL to query:
    response = urllib2.Request("http://www.omdbapi.com/?t="+movie_name+"&y="+movie_year+"&plot=short&r=json")
    opener = urllib2.build_opener()
    f = opener.open(response)
    movie_json = simplejson.load(f)
    #print movie_json

    # Write the movie information to file
    title = encode(movie_json["Title"])
    year = movie_json["Year"]
    released = movie_json["Released"]
    language = (movie_json["Language"].split(","))[0]
    rated = movie_json["Rated"]
    imdb_rating = movie_json["imdbRating"]
    runtime = (movie_json["Runtime"].split(" "))[0]
    writer = encode(movie_json["Writer"].split(",")[0])
    director = encode(movie_json["Director"])
    awards = movie_json["Awards"]
    imdb_ID = movie_json["imdbID"]
    imdbVotes = movie_json["imdbVotes"]
    genre = movie_json["Genre"].replace(",", " ")

    movie_file.write("{title:s}, {yr:s}, {mn:s}, {lang:s}, {time:s}, {writ:s}, {dir:s}, {rate:s}, {rated:s}, {id:s}, {vote:s}, {gen:s}, {awrds:s}\n"
        .format(title=title, yr=year, mn=released, lang=language, time=runtime, writ=writer,
                dir=director, rate=imdb_rating, rated = rated, id=imdb_ID, vote=imdbVotes, awrds=awards, gen=genre))
    # Set up random wait:
    wait_time = random.randint(1,5)
    print "Waiting for...", wait_time
    time.sleep(wait_time)

movie_file.close()


















