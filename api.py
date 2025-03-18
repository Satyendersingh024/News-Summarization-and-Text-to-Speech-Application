import requests

API_URL = "https://newsapi.org/v2/everything"
API_KEY = "df0f1798a59e459989ef80fea179c2de"

def fetch_news(company):
    params = {"q": company, "apiKey": API_KEY, "language": "en"}
    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        return response.json().get("articles", [])
    return []
