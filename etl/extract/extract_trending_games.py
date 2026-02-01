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

    soup = BeautifulSoup(response.text, "html.parser")

    return soup

def extract_trending_games_table(soup: BeautifulSoup | None) -> dict[str, list]:
    """
    Extract top 5 trending games table from the Steam Charts website.
    """
    result = {
        "app_id": [],
        "name": [],
        "24_hour_change": [],
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
    
        anchor_tag: Tag = list_of_all_table_data_tags[0].find("a")
        app_id = anchor_tag["href"]
        app_id = str(app_id)
        
        name = anchor_tag.get_text()
        name = str(name)

        twenty_four_hour_change = list_of_all_table_data_tags[1]
        twenty_four_hour_change = twenty_four_hour_change.get_text()
        twenty_four_hour_change = str(twenty_four_hour_change)

        current_players = list_of_all_table_data_tags[3]
        current_players = current_players.get_text()
        current_players = str(current_players)

        result["app_id"].append(app_id)
        result["name"].append(name)
        result["24_hour_change"].append(twenty_four_hour_change)
        result["current_players"].append(current_players)

    return result

def extract_player_concurrency_data(soup: BeautifulSoup | None) -> dict[str, dict]:
    """
    Extract the player concurrency data of the number 1 trending game from Steam Charts website.
    """
    result = {
        "app_title": "",
        "current_concurrent_players": {},
        "peak_concurrent_players": {"24_hour_peak": ""},
        "all_time_peak": {}
    }

    if soup is None:
        return result

    body_tag: Tag = soup.find('body')
    div_tag_with_content_wrapper_id: Tag = body_tag.find("div", attrs={"id": "content-wrapper"})
    
    app_title_tag: Tag = div_tag_with_content_wrapper_id.find("h1", attrs={"id": "app-title"})
    app_title = app_title_tag.get_text()
    app_title = str(app_title)
    result["app_title"] = app_title

    div_tag_with_app_heading_id: Tag = div_tag_with_content_wrapper_id.find("div", attrs={"id": "app-heading"})
    list_of_all_div_tag_with_app_stat_classes: ResultSet[Tag] = div_tag_with_app_heading_id.find_all("div", attrs={"class": "app-stat"})

    for cell_number, div_tag_with_app_stat_class in enumerate(list_of_all_div_tag_with_app_stat_classes):
        cell_number += 1

        if cell_number == 1:
            header = div_tag_with_app_stat_class.get_text()
            abbr_tag: Tag = div_tag_with_app_stat_class.find("abbr")
            header = header + abbr_tag.get_text()
            header = str(header)

            current_concurrent_players = div_tag_with_app_stat_class.find("span", attrs={"class": "num"}).get_text()
            current_concurrent_players = int(current_concurrent_players)

            result["current_concurrent_players"][header] = current_concurrent_players
            continue

        else:
            br_tag: Tag = div_tag_with_app_stat_class.find("br")
            header = br_tag.get_text()
            header = str(header)

            concurrent_players_tag: Tag = div_tag_with_app_stat_class.find("span", attrs={"class": "num"})
            concurrent_players = concurrent_players_tag.get_text()
            concurrent_players = int(concurrent_players)

        if cell_number == 2:
            result["peak_concurrent_players"][header] = concurrent_players

        else:
            result["peak_concurrent_players"][header] = concurrent_players

    return result