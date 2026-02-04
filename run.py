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

# Number one trending game
number_one_trending_game_path = trending_games["app_id"][0]
number_one_trending_game_path = str(number_one_trending_game_path).replace("/app", "app")
number_one_trending_game_url = base_url + number_one_trending_game_path
number_one_trending_game_soup = extract_and_parse_soup(number_one_trending_game_url)
number_one_concurrency_data = extract_player_concurrency_data(number_one_trending_game_soup)
etl_pipeline_logs("EXTRACT", "Extract number two trending game from Steam Charts website.")

# Number two trending game
number_two_trending_game_path = trending_games["app_id"][1]
number_two_trending_game_path = str(number_two_trending_game_path).replace("/app", "app")
number_two_trending_game_url = base_url + number_two_trending_game_path
number_two_trending_game_soup = extract_and_parse_soup(number_two_trending_game_url)
number_two_concurrency_data  = extract_player_concurrency_data(number_two_trending_game_soup)
etl_pipeline_logs("EXTRACT", "Extract number two trending game from Steam Charts website.")

# Number three trending game
number_three_trending_game_path = trending_games["app_id"][1]
number_three_trending_game_path = str(number_three_trending_game_path).replace("/app", "app")
number_three_trending_game_url = base_url + number_three_trending_game_path
number_three_trending_game_soup = extract_and_parse_soup(number_three_trending_game_url)
number_three_concurrency_data  = extract_player_concurrency_data(number_three_trending_game_soup)
etl_pipeline_logs("EXTRACT", "Extract number three trending game from Steam Charts website.")

# Number four trending game
number_four_trending_game_path = trending_games["app_id"][1]
number_four_trending_game_path = str(number_four_trending_game_path).replace("/app", "app")
number_four_trending_game_url = base_url + number_four_trending_game_path
number_four_trending_game_soup = extract_and_parse_soup(number_four_trending_game_url)
number_four_concurrency_data  = extract_player_concurrency_data(number_four_trending_game_soup)
etl_pipeline_logs("EXTRACT", "Extract number four trending game from Steam Charts website.")