import requests
import json
query=input("enter the type of news you are intrested in ?")
url=f"https://newsapi.org/v2/everything?q={query}&from=2024-09-19&sortBy=publishedAt&apiKey=f5c3d73810064b3289cec7a99a4b93ce"

res = requests.get(url)
news = json.loads(res.text)

for article in news["articles"]:
    print(article["title"])
    print("\n")
    print(article["description"])
    print("\n\n\n")
