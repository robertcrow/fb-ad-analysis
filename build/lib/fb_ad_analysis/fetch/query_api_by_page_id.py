import requests
import collections
import csv
import pandas as pd
import datetime

def query_api(token, phrase, ad_time_start="2019-08-06T00:00:00+0200", ad_time_end="2019-12-12T00:00:00+0200"):
    
    response = requests.get("https://graph.facebook.com/v2.11/ads_archive?"
                         #"search_terms=" + str(phrase) +
                         "search_page_ids=" + str(phrase) +
                         "&limit=50&fields=page_id,page_name,ad_snapshot_url,ad_creative_body,ad_delivery_start_time,ad_delivery_stop_time,\
                         impressions,demographic_distribution,funding_entity,currency,spend" +
                         "&ad_reached_countries=PL&active_status=all&ad_type=political_and_issue_ads&country=PL" +
                         "&ad_delivery_start_time=" + ad_time_start +
                         "&ad_active_status=ALL" +
                         "&access_token=" + token,
                         headers={'Content-type': 'text/plain; charset=utf-8'})

    response_json = response.json()

    try:
        ad_data = response_json['data']
        not_fully_parsed = True

        while not_fully_parsed is True:
            try:
                next_url = response_json['paging']['next']
                response_json = requests.get(next_url).json()
                ad_data.extend(response_json['data'])
            except:
                not_fully_parsed = False

        return ad_data

    except:
        ad_data = None
        print('search for phrase' + phrase + 'returned corrupt output\n')