
"""
`pynwa.BasicDataFetch` allows for a pull of readily
available Liverpool data including match results and player stats. PREMIER LEAGUE DATA ONLY.
Unlike `pynwa.AdvDataFetch`, this module does not contain any information
around position of the ball and players relative to it at any given timestamp.

This module is meant to grab high level information.
"""

import requests
import pandas as pd
import yaml

with open('pynwa/config.yml', 'r', encoding='utf-8') as file:
    CONFIG = yaml.safe_load(file)


def get_standard_player_stats(output_pandas=True):
    """Function that gets the latest Standard Stats from fbref.com
    Metrics related to Playing Time, Performance, Expected, Progression and Per 90 Minutes
    can be found here. Results aggregate data from Premier League matches only.
    

    Args:
        output_pandas (bool, optional): Determines if the resulting data structure is Pandas DataFrame (True) or JSON. Defaults to True.

    Returns:
        result (pd.Dataframe or JSON): Data output containing standard statistics (ex: Position, Playing Time, Performance, etc.)
    """
    _url = CONFIG.get('URL_BASIC_LIVERPOOL_STATS')
    _standard_stats_header = CONFIG.get('STANDARD_STATISTICS')
    
    data = requests.get(_url, timeout=10)
    
    match_list = pd.read_html(data.text,
                      match=_standard_stats_header)
    
    df = match_list[0]
    
    if output_pandas:
        result = df
    else:
        result = df.to_json(orient='records')
    
    return result


def get_scores_and_fixtures(output_pandas=True):
    """Function that gets the latest Scores and Fixtures (Match Log) from fbref.com.
    Contains time (home team venue local timezone), along with Round, Opponent, Attendance, and other metrics.
    

    Args:
        output_pandas (bool, optional): Determines if the resulting data structure is Pandas DataFrame (True) or JSON. Defaults to True.

    Returns:
        result (pd.Dataframe or JSON): Data output containing standard statistics (ex: Position, Playing Time, Performance, etc.)
    """
    _url = CONFIG.get('URL_BASIC_LIVERPOOL_STATS')
    _scores_and_fixtures = CONFIG.get('SCORES_AND_FIXTURES')
    
    data = requests.get(_url, timeout=10)
    
    match_list = pd.read_html(data.text,
                              match=_scores_and_fixtures)
    
    df = match_list[0]
    
    if output_pandas:
        result = df
    else:
        result = df.to_json(orient='records')
    
    return result


def get_shooting_stats(output_pandas=True):
    """Function that gets the latest shooting stats from fbref.com (ex: Goals scored or allowed. Results are aggregated
    over Premier League games only. Contains metrics such as Goals scored or allowed.
    

    Args:
        output_pandas (bool, optional): Determines if the resulting data structure is Pandas DataFrame (True) or JSON. Defaults to True.

    Returns:
        result (pd.Dataframe or JSON): Data output containing standard statistics (ex: Goals scored or allowed, Expected Goals, etc.)
    """
    _url = CONFIG.get('URL_BASIC_LIVERPOOL_STATS')
    _shooting_stats = CONFIG.get('SHOOTING_STATS')
    
    data = requests.get(_url, timeout=10)
    
    match_list = pd.read_html(data.text,
                              match=_shooting_stats)
    
    df = match_list[0]
    
    if output_pandas:
        result = df
    else:
        result = df.to_json(orient='records')
    
    return result


def get_goal_and_shot_creation_stats(output_pandas=True):
    """Function that gets the latest goal and shot creation data from fbref.com. 
    Results are aggregated only over Premier League matches.Includes metrics such as
    Shot Creating Actions and Goal Creating Actions.
    

    Args:
        output_pandas (bool, optional): Determines if the resulting data structure is Pandas DataFrame (True) or JSON. Defaults to True.

    Returns:
        result (pd.Dataframe or JSON): Data output containing standard statistics (ex: Shot Creating Actions, Live Ball passes that led to goals, etc.)
    """
    _url = CONFIG.get('URL_BASIC_LIVERPOOL_STATS')
    _goal_and_shot_creation = CONFIG.get('GOAL_SHOT_CREATION')
    data = requests.get(_url, timeout=10)
    
    match_list = pd.read_html(data.text,
                              match=_goal_and_shot_creation)
    
    df = match_list[0]
    
    if output_pandas:
        result = df
    else:
        result = df.to_json(orient='records')
    
    return result