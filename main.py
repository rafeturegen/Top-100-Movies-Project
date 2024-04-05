import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
all_titles = soup.find_all(name="h3", class_="title")
for title in reversed(all_titles):
    movie = title.getText()
    with open("movies.txt", "a", encoding="utf-8") as data:
        data.writelines(f"{movie}\n")
