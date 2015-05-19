import urllib2
from bs4 import BeautifulSoup
import random
import time
import re

# Let's write the program to collect data for the first 10 pages for a give year
year = ['2014']

# Open the file to write out the movies
myFile = open("Movies_2014.txt", "w")

# Run it for 9 pages. The pages are in decreasing order of popularity:
for i in range(0,5):
    response = urllib2.urlopen("http://movieweb.com/movies/2014/0/?page="+str(i))
    html_page = response.read()
    this_page = BeautifulSoup(html_page)
    print this_page.find_all('a')
    print "*" * 80

    # Get the names of the movies on the page:
    for a in this_page.find_all('a', {'href': re.compile(r'^http://movieweb.com/movie/.*')}):
        myFile.write(a.text)
        myFile.write("\n")
    print "Done with page..."+str(i)

    # Set up random wait:
    wait_time = random.randint(1,10)
    print "Waiting for...", wait_time
    time.sleep(wait_time)

myFile.close()