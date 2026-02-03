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

number_one_trending_game_path = trending_games["app_id"][0]
number_one_trending_game_path = str(number_one_trending_game_path).replace("/app", "app")
number_one_trending_game_url = base_url + number_one_trending_game_path
number_one_trending_game_soup = extract_and_parse_soup(number_one_trending_game_url)
number_one_concurrency_data = extract_player_concurrency_data(number_one_trending_game_soup)
etl_pipeline_logs("EXTRACT", "Extract number 1 one trending game from Steam Charts website.")