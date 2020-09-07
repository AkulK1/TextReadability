
# -*- coding: utf-8 -*-
"""
This snipet is from Ken Jee's github'
"""

import requests 

URL = 'http://127.0.0.1:5000//textpred'
textfile = """“Mother Bear, Mother Bear, Where are you?” calls Little Bear. “Oh, dear, Mother Bear is not here, and today is my birthday. “I think my friends will come, but I do not see a birthday cake. My goodness – no birthday cake. What can I do? The pot is by the fire. The water in the pot is hot. If I put something in the water, I can make Birthday Soup. All my friends like soup. Let me see what we have. We have carrots and potatoes, peas and tomatoes; I can make soup with carrots, potatoes, peas and tomatoes.” So Little Bear begins to make soup in the big black pot. First, Hen comes in. “Happy Birthday, Little Bear,” she says. “Thank you, Hen,” says Little Bear. Hen says, “My! Something smells good here. Is it in the big black pot?” “Yes,” says Little Bear, “I am making Birthday Soup. Will you stay and have some?” “Oh, yes, thank you,” says Hen. And she sits down to wait. Next, Duck comes in. “Happy Birthday, Little bear,” says Duck. “My, something smells good. Is it in the big black pot?” “Thank you, Duck,” says Little Bear. “Yes, I am making Birthday Soup. Will you stay and have some with us?” “Thank you, yes, thank you,” says Duck. And she sits down to wait. Next, Cat comes in. “Happy Birthday, Little Bear,” he says. “Thank you, Cat,” says Little Bear. “I hope you like Birthday Soup. I am making Birthday Soup. Cat says, “Can you really cook? If you can really make it, I will eat it.” “Good,” says Little Bear. “The Birthday Soup is hot, so we must eat it now. We cannot wait for Mother Bear. I do not know where she is.” “Now, here is some soup for you, Hen,” says Little Bear. “And here is some soup for you, Duck, and here is some soup for you, Cat, and here is some soup for me. Now we can all have some Birthday Soup.” Cat sees Mother Bear at the door, and says, “Wait, Little Bear. Do not eat yet. Shut your eyes, and say one, two, three.” Little Bear shuts his eyes and says, “One, two, three.” Mother Bear comes in with a big cake. “Now, look,” says Cat. “Oh, Mother Bear,” says Little Bear, “what a big beautiful Birthday Cake! Birthday Soup is good to eat, but not as good as Birthday Cake. I am so happy you did not forget.” “Yes, Happy Birthday, Little Bear!” says Mother Bear. “This Birthday Cake is a surprise for you. I never did forget your birthday, and I never will.”"""
print( textfile )
headers = {"Content-Type": "application/json"}
data = {"input": textfile, "info": 0}

r=requests.post(URL, headers = headers, json=data)

print (r.json() )
