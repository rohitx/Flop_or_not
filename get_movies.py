import urllib2
from bs4 import BeautifulSoup
import random
import time
import re

# Define a function to use UTF-8 encoding for movie names:

def encode(text):
    return text.encode('utf-8')


# Let's write the program to collect data for the first 10 pages for a give year
years = ['2001', '2000']

for year in years:
    # Open the file to write out the movies
    myFile = open("Movies_"+year+".txt", "w")

    # Run it for 9 pages. The pages are in decreasing order of popularity:
    for i in range(0,10):
        response = urllib2.urlopen("http://movieweb.com/movies/"+year+"/0/?page="+str(i))
        html_page = response.read()
        this_page = BeautifulSoup(html_page)

        # Get the names of the movies on the page:
        for a in this_page.find_all('a', {'href': re.compile(r'^http://movieweb.com/movie/.*')}):
            myFile.write(encode(a.text))
            myFile.write("\n")

        print "Done with page..."+str(i)

        # Set up random wait:
        wait_time = random.randint(1,10)
        print "Waiting for...", wait_time
        time.sleep(wait_time)

    myFile.close()
    print "Done with ...", year
    print "*" * 80