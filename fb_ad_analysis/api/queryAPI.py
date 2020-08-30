import requests
import collections
import csv
import pandas as pd
import datetime

def queryAPI(token, phrase, ad_time_start=None, ad_time_end=None):
    if ad_time_start == None:
        ad_time_start = "2019-08-06T00:00:00+0200"
        ad_time_end = "2019-12-12T00:00:00+0200"
    
    posts = requests.get("https://graph.facebook.com/v2.11/ads_archive?"
                         #"search_terms=" + str(phrase) +
                         "search_page_ids=" + str(phrase) +
                         "&limit=50&fields=page_id,page_name,ad_snapshot_url,ad_creative_body,ad_delivery_start_time,ad_delivery_stop_time,\
                         impressions,demographic_distribution,funding_entity,currency,spend" +
                         "&ad_reached_countries=PL&active_status=all&ad_type=political_and_issue_ads&country=PL" +
                         "&ad_delivery_start_time=" + ad_time_start +
                         "&ad_active_status=ALL" +
                         "&access_token=" + token,
                         headers={'Content-type': 'text/plain; charset=utf-8'})

    posts_json = posts.json()

    try:
        ad_data = posts_json['data']
        tmp = True

        while tmp is True:
            try:
                next_url = posts_json['paging']['next']
                posts_json = requests.get(next_url).json()
                ad_data.extend(posts_json['data'])
            except:
                tmp = False

        return ad_data

    except:
        ad_data = None
        print('search for phrase' + phrase + 'returned corrupt output\n')