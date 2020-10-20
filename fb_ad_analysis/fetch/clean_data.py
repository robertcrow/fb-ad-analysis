import requests
import collections
import csv
import pandas as pd
import datetime

def cleanData(data):

    tmp = {'male': {}, 'female': {}, 'unknown': {}}

    for x in data:
        try:
            x['demographic_distribution']

            for y in x['demographic_distribution']:
                tmp[y['gender']][y['age']] = float(y['percentage'])

            for key in tmp:
                tmp[key] = collections.OrderedDict(sorted(tmp[key].items(), key=lambda t: t[0]))

            x['demographic_distribution'] = tmp

        except:
            print("demographic distribution not available")

    return data