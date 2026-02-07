"""
ETL Pipeline executor by running and orchestrating different pipeline jobs.
"""
from etl.extract.extract_trending_games import extract_and_parse_soup
from etl.extract.extract_trending_games import extract_trending_games_table
from etl.extract.extract_trending_games import extract_player_concurrency_data
from etl.extract.extract_trending_games import extract_historical_player_data
from logs.etl_pipeline_logs import etl_pipeline_logs

base_url = "https://steamcharts.com/"

# Extract trending games table
trending_games_soup = extract_and_parse_soup(base_url)
trending_games = extract_trending_games_table(trending_games_soup)
etl_pipeline_logs("EXTRACT", "Extract top 5 trending games from Steam Charts website.")

trending_games_concurrency_data = []
trending_games_historical_player_data = []

# Use for-loop that iterates 5 times to get all the 5 application id of trending games and extract their data
for number in range(5):
    app_id = trending_games["app_id"][number]
    app_name = trending_games["app_name"][number]

    # Extract and parse the BeautifulSoup object
    path = app_id
    path = str(path).replace("/app", "app")
    url = base_url + path
    soup = extract_and_parse_soup(url)

    # Extract player concurency data
    player_concurrency_data = extract_player_concurrency_data(soup)
    trending_games_concurrency_data.append(
        {
            app_name: player_concurrency_data
        }
    )
    etl_pipeline_logs("EXTRACT", f"Extract the player concurrency data of the number {number + 1} trending game from Steam Charts.")

    # Extract historical player data
    historical_player_data = extract_historical_player_data(soup)
    trending_games_historical_player_data.append(
        {
            app_name: historical_player_data
        }
    )
    etl_pipeline_logs("EXTRACT", f"Extract the historical player data of the number {number + 1} trending game from Steam Charts.")