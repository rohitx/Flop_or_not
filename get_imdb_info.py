# This program gets all of the movie info from the IMDb website.
# The program scraps the information from the website based on the movie
# code. The code is received from a pandas dataframe.
#
# The information procured is the movie cast (15 max), movie budget,
# and the 1 week gross, and screens on opening weekend.
#
# Created May 31, 2015
# Author: Rohit Deshpande
#-------------------------------------------
#
# Import statement
import pandas as pd
from pattern import web
import requests

# Get movie cast
inception = "tt1375666"
avengers = "tt0848228"
movie_cast = []
url_movie = "http://www.imdb.com/title/"+inception+"/"
movie_html = requests.get(url_movie)
dom = web.Element(movie_html.text)
for cast in dom.by_tag('td.itemprop'):
    the_cast = cast.by_tag('a')[0]
    movie_cast.append(the_cast.by_tag('span.itemprop')[0].content)

# Get budget and opening weekend
url_business = url_movie = "http://www.imdb.com/title/"+avengers+"/business"
business_html = requests.get(url_business)
dom = web.Element(business_html.text)
