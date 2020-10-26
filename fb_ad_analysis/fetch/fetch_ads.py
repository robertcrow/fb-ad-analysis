from fb_ad_analysis.fetch.query_api_by_page_id import query_api_by_page_id 
from fb_ad_analysis.fetch.parse_demographic_data import parse_demographic_data
from fb_ad_analysis.fetch.parse_spend_and_reach_data import parse_spend_and_reach_data

import pandas as pd

def fetch_ads(token, search_phrases, filename=None, ad_time_start=None, ad_time_end=None):
    data = []
    for search_phrase in search_phrases:
        query_output = query_api_by_page_id(token, search_phrase, ad_time_start=ad_time_start)
        if query_output is not None:
            with_parsed_demographics = parse_demographic_data(query_output)
            with_parsed_spend_and_reach = parse_spend_and_reach_data(with_parsed_demographics)
            data.extend(with_parsed_spend_and_reach)

    if 'filename' in locals():
        df = pd.DataFrame.from_dict(data)
        df.to_csv(filename)

    return data