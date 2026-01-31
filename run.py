"""
Run/Execute module to run functions from different packages to perform ETL operation
"""
from ingest.ingest_trending_games import ingest_raw_trending_games_data

ingest_raw_trending_games_data('https://steamcharts.com/')