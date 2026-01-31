"""
Ingest top 5 trending games from the steam from the url 'https://steamcharts.com'
"""
import requests
from bs4 import BeautifulSoup, Tag, ResultSet

def ingest_raw_trending_games_data(url: str) -> BeautifulSoup | None:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0"
    }
    response = requests.get(url=url, headers=headers)

    if response.status_code != 200:
        return None

    soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
    trending_games_tag: Tag | None = soup.find('div', attrs={"class": "content"})

    if trending_games_tag is None:
        return {}

    tbody_tag: Tag | None = trending_games_tag.find('tbody')