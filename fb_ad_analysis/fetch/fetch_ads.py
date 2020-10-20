from fb_ad_analysis.fetch.query_api_by_page_id import query_api_by_page_id 
from fb_ad_analysis.fetch.parse_demographic_data import parse_demographic_data

import pandas as pd

def fetch_ads(token, search_phrases, filename=None, ad_time_start=None, ad_time_end=None):
    data = []
    for search_phrase in search_phrases:
        query_output = query_api_by_page_id(token, search_phrase, ad_time_start=ad_time_start)
        if query_output is not None:
            print(query_output)
            parsed_query_output = parse_demographic_data(query_output)
            data.extend(parsed_query_output)

    if 'filename' in locals():
        df = pd.DataFrame.from_dict(data)
        df.to_csv(filename)

    return data