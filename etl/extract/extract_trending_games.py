"""
Extract trending games raw data from Steam Charts.
"""
import requests
from bs4 import BeautifulSoup, Tag, ResultSet

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

    soup = BeautifulSoup(response.text, "html.parser')

    return soup

def extract_trending_games_table(soup: BeautifulSoup | None) -> dict[str, list]:
    """
    Extract top 5 trending games table from the Steam Charts website.
    """
    result = {
        "name": [],
        "24-hour_change": [],
        "current_players": []
    }

    if soup is None:
        return result

    body_tag: Tag = soup.find("body")
    div_tag_with_content_wrapper_id: Tag = body_tag.find("div", attrs={"id": "content-wrapper"})
    div_tag_with_content_class: Tag = div_tag_with_content_wrapper_id.find("div", attrs={"class": "content"})
    trending_games_table: Tag = div_tag_with_content_class.find("table", attrs={"id": "trending-recent"})
    tbody_tag: Tag = trending_games_table.find("tbody")
    list_of_all_table_row_tags: ResultSet[Tag] = tbody_tag.find_all("tr")

    for table_row_tag in list_of_all_table_row_tags:
        list_of_all_table_data_tags = table_row_tag.find_all("td")

        name = list_of_all_table_data_tags[0]
        name = name.get_text()
        name = str(name)

        twenty_four_hour_change = list_of_all_table_data_tags[1]
        twenty_four_hour_change = twenty_four_hour_change.get_text()
        twenty_four_hour_change = str(twenty_four_hour_change)

        current_players = list_of_all_table_data_tags[3]
        current_players = current_players.get_text()
        current_players = str(current_players)

        result["name"].append(name)
        result["24-hour_change"].append(twenty_four_hour_change)
        result["current_players"].append(current_players)

    return result