"""
ETL Pipeline executor by running and orchestrating different pipeline jobs.
"""
from etl.extract.extract_trending_games import extract_and_parse_soup
from etl.extract.extract_trending_games import extract_trending_games_table
from logs.etl_pipeline_logs import etl_pipeline_logs

soup = extract_and_parse_soup('https://steamcharts.com/')
trending_games = extract_trending_games_table(soup)
etl_pipeline_logs("EXTRACT", "Extract top 5 trending games from Steam Charts website.")