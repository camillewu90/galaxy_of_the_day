import requests
from datetime import date


def download_info():
    today = str(date.today())

    url = "https://api.nasa.gov/planetary/apod?"\
          "api_key=Cm8ziv93pgI9e9GStR7fBmrmEaOWLjwQbWpD6y0E&"\
          f"date={today}"

    response = requests.get(url)
    content = response.json()
    image_url = content["url"]
    title = content['title']
    explanation = content['explanation']
    return title,image_url,explanation


if __name__ == "__main__":
    title, url, expl = download_info()
    print(title)
    print(url)
    print(expl)
