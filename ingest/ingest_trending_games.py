"""
Ingest top 5 trending games from the steam from the url 'https://steamcharts.com'
"""
from ssl import CHANNEL_BINDING_TYPES
import requests
from bs4 import BeautifulSoup, Tag, ResultSet

def ingest_raw_trending_games_table(url: str) -> BeautifulSoup | None:
    """
    Ingest function to ingest the top 5 trending games from the Steam Charts.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0"
    }
    response = requests.get(url=url, headers=headers)

    if response.status_code != 200:
        return None

    soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')

    result = {
        "name": [],
        "24-hour_change": [],
        "current_players": []
    }

    trending_games_tag: Tag = soup.find('div', attrs={"class": "content"})
    tbody_tag: Tag = trending_games_tag.find('tbody')
    list_of_all_table_row_tags: ResultSet[Tag] = tbody_tag.find_all('tr')

    for table_row_tag in list_of_all_table_row_tags:
        list_of_all_table_data_tags: ResultSet[Tag] = table_row_tag.find_all('td')

        list_of_all_cell_datas = []

        for index, table_data_tag in enumerate(list_of_all_table_data_tags):
            index += 1

            if index != 3:
                cell_data = table_data_tag.get_text()
                cell_data = str(cell_data)
                list_of_all_cell_datas.append(cell_data)

        name = list_of_all_cell_datas[0]
        result["name"].append(name)

        twentyfour_hour_change = list_of_all_cell_datas[1]
        result["24-hour_change"].append(twentyfour_hour_change)

        current_players = list_of_all_cell_datas[1]
        result["current_players"].append(current_players)

    return result