from fb_ad_analysis.fetch import connect_to_api, fetch_ads

token = "EAAGaLEBcXCcBAPfA6GMAxMntqPP7HOaXVJoKgjIznmUq51ZCipY23iWEzJiqyzMcikaoClZBSamsosfx8aiS4pBPn2gZAaJWZB3aeLvxzW6tySocvZCauML0BhdgzUQSkpOFOjBH9GyZAIP3wzmKYBe4LZBwlyeF7p1oKNXiX4PBlDvB8K0of7I"
api = connect_to_api(token, version="7.0")

# test params
phrases = "Conservatives"
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


database = fetch_ads(token, phrases, ad_time_start="2019-11-06T00:00:00+0000", ad_time_end="2019-12-13T00:00:00+0000")