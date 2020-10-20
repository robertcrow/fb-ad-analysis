from fb_ad_analysis.fetch import connect_to_api, fetch_ads

token = "EAAGr0hQ1MZCcBAMpPYJ6KFZBfQ0NucsI2hPodPRYRtnZAZBNfzNoGADwuo8mywZA6teXOsiRFAiuS9ZCX7NLaAsx5R9nCbRBzYdOpC6RA6aLiUTC4jNapi9Ra7bBQ7er4oKZCXeUjC5s6yJi5xojbKZBmWQgTahQM2qI09XHcrGYRBJ9qebCi5du"
api = connect_to_api(token, version="7.0")

# test params
phrases = ["8807334278"]
ad_time_start="2019-11-06T00:00:00+0000"
ad_time_end="2019-12-13T00:00:00+0000"

# # phrase list
# with open(datasheet,
#               'r',
#               encoding='utf-8-sig',
#               newline='\n') as csv_file:

#         report_data = csv.reader(csv_file, delimiter=',')
#         report_data = pd.DataFrame(report_data)
#         col_names = report_data.loc[0, :]
#         report_data = report_data.iloc[1:]
#         report_data.columns = col_names

#         advertisers = list(report_data['Page ID'])


data = fetch_ads(token, phrases, ad_time_start="2019-11-06T00:00:00+0000", ad_time_end="2019-12-13T00:00:00+0000")
print(data)