"""
ETL Pipeline executor by running and orchestrating different pipeline jobs.
"""
from etl.extract.extract_trending_games import extract_and_parse_soup
from logs.etl_pipeline_logs import etl_pipeline_logs

extract_and_parse_soup('https://steamcharts.com/')
etl_pipeline_logs('EXTRACT', 'Extract and parse BeautifulSoup object from the Steam Charts website.')