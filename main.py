import requests

api = "107cce3cce76461394397f2967cb0180"
url = ("https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey="
       "107cce3cce76461394397f2967cb0180")

#make a request
request = requests.get(url)
content = request.json()

#Access to title and descripcion
for article in content["articles"]:
    print(article["title"])
    print(article["description"])