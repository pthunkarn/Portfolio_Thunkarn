## import function
from gazpacho import Soup
import requests
import pandas as pd

url = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc"
html = requests.get(url)
imdb = Soup(html.text)

titles = imdb.find("h3", {"class": "lister-item-header"})
clean_titles = [title.strip()[3:-7] for title in titles]

years = imdb.find("span", {"class": "lister-item-year"})
clean_years = [year.strip()[1:-1] for year in years]

movie_rank = pd.DataFrame(data = {
    "title": clean_titles,
    "years": clean_years
})
        
movie_rank.head(5)
