import requests
import pandas as pd

def fbref_call(url, fbref_section):
    """Helper function that calls fbref.com

    Args:
        url (_type_): _description_
        fbref_section (_type_): _description_

    Returns:
        _type_: _description_
    """
    data = requests.get(url, timeout=)
    
    df = pd.read_html(data.text,
                      match=fbref_section)
    return df