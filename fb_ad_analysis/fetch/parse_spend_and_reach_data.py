import re


def parse_spend_and_reach_data(data):
    for x in data:
        x['spend'] = clean_label(x['spend'])
        x['impressions'] = clean_label(x['impressions'])

    return data


def clean_label(label):
    match = re.findall("[0-9]+", str(label))
    if len(match) == 2:
        label = 'between ' + match[0] + ' and ' + match[1]
    elif len(match) == 1:
        label = 'above ' + match[0]
    else: pass

    return label
