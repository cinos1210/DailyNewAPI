import requests
from pyexpat.errors import messages

from Send_Email import Send_email

api = "107cce3cce76461394397f2967cb0180"
url = ("https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey="
       "107cce3cce76461394397f2967cb0180")

#make a request
request = requests.get(url)
content = request.json()
message = ""
#Access to title and descripcion
for article in content["articles"]:
    if article["title"] is not None:
        message = article["title"] + "/n" + article["description"] + "/n/n"

message = message.encode("utf-8")
Send_email(message)