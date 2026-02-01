"""
Extract trending games raw data from Steam Charts.
"""
from requests import request
import requests
from bs4 import BeautifulSoup

def extract_and_parse_soup(url: str) -> BeautifulSoup | None:
    """
    Extract and parse BeautifulSoup from the Steam Charts website.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0"
    }
    response = requests.get(url=url, headers=headers)

    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    return soup

def extract_trending_games_table(soup: BeautifulSoup | None) -> dict[str, list]:
    """
    Extract top 5 trending games table from the Steam Charts website.
    """