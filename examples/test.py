import fb_ad_analysis

token = 'EAAGaLEBcXCcBAN86M4JBMbYs0RmprZCTx8gqI6S5kFmRqqs9AK1ieZAWpRStwEgcf6v8ftPdGPWVusroxdVZCxdLZC1KJXHCZAQVEIHz353MxEspnzwi5LCAdYwyMyoOj0PtYr5ox4Hhd9KFheeMxy7ysZCGQTZBN1c7ciy5BQud4dn3loSIy0P'

api = fb_ad_analysis.api.connectToAPI(token)
ads = fb_ad_analysis.api.fetchAds(token, ['Conservaties'], 'examples/test.csv')


