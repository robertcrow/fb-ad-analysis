import requests
import collections
import csv
import pandas as pd
import datetime

def parse_demographic_data(data):

    entry = {'male': {}, 'female': {}, 'unknown': {}}

    for x in data:
        try:
            x['demographic_distribution']

            for y in x['demographic_distribution']:
                entry[y['gender']][y['age']] = float(y['percentage'])

            for key in tmp:
                entry[key] = collections.OrderedDict(sorted(entry[key].items(), key=lambda t: t[0]))

            x['demographic_distribution'] = entry

        except:
            print("demographic distribution not available")

    return data