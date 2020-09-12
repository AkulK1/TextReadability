
# -*- coding: utf-8 -*-
"""
This snipet is from Ken Jee's github'
"""

import requests 
import time

t0 = time.time()

URL = "https://ds-text-readability-20.herokuapp.com/fullpredict"
# https://ds-text-readability-20.herokuapp.com
articleURL = 'https://www.newyorker.com/books/flash-fiction/keys' 
headers = {"Content-Type": "application/json"}
data = {"article_url": articleURL, "info": 0}

r=requests.post(URL, headers = headers, json=data)


print( time.time()-t0 )
print (r.json() )


# URL = 'http://127.0.0.1:5000/textpred'
# textfile = """Flying cars are no longer a dream of the future. SkyDrive Inc., in Japan, announced on August 28 that a pilot had successfully flown one of its cars. There are more than 100 flying-car projects in the world, according to Tomohiro Fukuzawa. He leads the SkyDrive effort. But “only a handful has succeeded with a person on board,” he says. SkyDrive’s vehicle flew about six feet off the ground and can hover for up to 10 minutes.

# The company’s goal is to get flight time up to 30 minutes. Fukuzawa wants a flying car for sale by 2023. He thinks it will sell for at least $300,000. He says a less expensive vehicle could be ready by 2030. For now, testing will continue. “I hope many people will want to ride it and feel safe,” Fukuzawa says. """
# data= {'input': textfile, "info": 1}
# print( requests.post( URL, headers=headers, json=data).json()  )