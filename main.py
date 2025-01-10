import requests
from pyexpat.errors import messages

from Send_Email import Send_email
topic = "videogames"
api = "107cce3cce76461394397f2967cb0180"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "sortBy=publishedAt&"
       "apiKey=107cce3cce76461394397f2967cb0180&"
       "language=es")

#make a request
request = requests.get(url)
content = request.json()
message = "\n"
#Access to title and descripcion
for article in content["articles"][:20]:
    if article["title"] is not None:
        message = ("Subject: Today's News" + message + article["title"] + "\n" + article["description"]
                   + "\n"+ article["url"] +2*"\n")

message = message.encode("utf-8")
Send_email(message)