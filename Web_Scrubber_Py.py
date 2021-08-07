#LIMITATIONS:
#   does not test for proper formatting aside from http, just runs and throws exception if needed
#   regexp only searches for links that begin with http/https
#   does not use the libcurl library as the c++ version does, 
#	so given that the webcode will be fetched and handled differently, different blocks of HTML may be included or left out

import urllib.request
from urllib.parse import urlparse
import re
import sys

#if there are arguments use those as urls
if len(sys.argv) > 1:
    urls = sys.argv
    del urls[0]
#else fetch urls from user
else:        
    urls = input("Url to be scrubbed: ").split()

for page in urls:
    #put in proper format for urllib
    if not urlparse(page).scheme:
        page = 'http://' + page

    #regular expression to find urls
    regex = "https?:\\/\\/(www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b([-a-zA-Z0-9()@:%_\\+.~#?&//=]*)"

    #send urllib request for given url store as "the_page"
    req = urllib.request.Request(page)
    try: 
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
#run regexp on "the_page" store as match object "m"
        m = re.findall(regex,str(the_page))
#print length of match object "m"
        print(page + " " + str(len(m)) + "\n")

    except urllib.error.URLError as e:
        print(e.reason)

