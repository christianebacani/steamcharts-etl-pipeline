"""
ETL Pipeline executor by running and orchestrating different pipeline jobs.
"""
from etl.extract.extract_trending_games import extract_and_parse_soup
from etl.extract.extract_trending_games import extract_trending_games_table
from etl.extract.extract_trending_games import extract_player_concurrency_data
from logs.etl_pipeline_logs import etl_pipeline_logs

base_url = "https://steamcharts.com/"

trending_games_soup = extract_and_parse_soup(base_url)
trending_games = extract_trending_games_table(trending_games_soup)
etl_pipeline_logs("EXTRACT", "Extract top 5 trending games from Steam Charts website.")

trending_games_concurrency_data = []

for number in range(5):
    path = trending_games["app_id"][number]
    path = str(path).replace("/app", "app")
    url = base_url + path

    soup = extract_and_parse_soup(url)
    player_concurrency_data = extract_player_concurrency_data(soup)
    trending_games_concurrency_data.append(player_concurrency_data)
    etl_pipeline_logs("EXTRACT", f"Extract the player concurrency data of the top {number + 1} game from Steam Charts.")