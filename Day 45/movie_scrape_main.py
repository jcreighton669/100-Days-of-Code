import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")


def strip_enum(title):
    if not title[0].isdigit():
        return title
    return " ".join(title.split()[1:])


all_movies = [strip_enum(movie.getText()) for movie in soup.select("h3.title")[::-1]]

# print(movies)
with open(r"movies.txt", mode="w", encoding="ISO-8859-1") as file:
    for index, movie in enumerate(all_movies):
        file.write(f"{index + 1}) {movie}\n")
