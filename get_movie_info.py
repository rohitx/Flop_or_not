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
movie_file = io.open("Movie_listings_2014.csv", "w", encoding='utf8')

def encode(text):
    return text.encode('utf-8')

count = 0
#for movie_name in movies:
for i in range(13,14):
    movie_name = movies[i]
    count += 1
    print "Doing movie no: ", count, "Movie: ", movie_name


    # Create a URL to query:
    response = urllib2.Request("http://www.omdbapi.com/?t="+movie_name+"&y="+movie_year+"&plot=short&r=json")
    opener = urllib2.build_opener()
    f = opener.open(response)
    movie_json = simplejson.load(f)
    print movie_json

    # Write the movie information to file
    title = movie_json["Title"]
    year = movie_json["Year"]
    released = movie_json["Released"].split(" ")[1]
    language = movie_json["Language"]
    rated = movie_json["Rated"]
    #imdb_rating = movie_json["imdbRating"]
    runtime = movie_json["Runtime"]
    writer = movie_json["Writer"].split(",")[0]
    #director = movie_json["Director"]
    #awards = movie_json["Awards"]
    imdb_ID = movie_json["imdbID"]
    #imdbVotes = movie_json["imdbVotes"]

    movie_file.write("{title:s}, {year:s}, {released:s}, {language:s}, {rated:s}, {runtime:s},\
             "
             .format(title=title, year=year, released = released, language=language,
                     rated=rated, runtime=runtime))
    # Set up random wait:
    wait_time = random.randint(1,10)
    print "Waiting for...", wait_time
    time.sleep(wait_time)

movie_file.close()


















