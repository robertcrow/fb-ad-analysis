from fb_ad_analysis.api import queryAPI, cleanData
import pandas as pd

def fetchAds(token, phrases, filename, ad_time_start=None, time_end=None):
    data = []
    database = []
    for x in phrases:
        data = queryAPI(token, x, ad_time_start=ad_time_start)
        if data is not None:
            data = cleanData(data)
            database.extend(data)

    df = pd.DataFrame.from_dict(database)
    if 'filename' in locals():
        df.to_csv(filename)

    return database