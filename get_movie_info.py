# This program gets all of the movie info from the OMDb api website.
#
# Created May 19, 2015
# Author: Rohit Deshpande
#-------------------------------------------
#
# Import statement

import urllib2
import simplejson



# Read in the file with movie names:

myfile = open("Movies_2014.txt", "r")
a = myfile.readlines()

movies = []
for i in range(len(a)):
    if not a[i] == '\n':
        movies.append((a[i]).strip())

movie_name = movies[1]
movie_year = '2014'

# Create a URL to query:
response = urllib2.Request("http://www.omdbapi.com/?t="+movie_name+"&y="+movie_year+"&plot=short&r=json")
opener = urllib2.build_opener()
f = opener.open(response)
movie_json = simplejson.load(f)
print movie_json