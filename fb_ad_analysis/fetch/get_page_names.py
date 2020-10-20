def getPageNamesFromAdReport(datasheet):
    with open(datasheet,
              'r',
              encoding='utf-8-sig',
              newline='\n') as csv_file:

        report_data = csv.reader(csv_file, delimiter=',')
        report_data = pd.DataFrame(report_data)
        col_names = report_data.loc[0, :]
        report_data = report_data.iloc[1:]
        report_data.columns = col_names

        advertisers = list(report_data['Page ID'])

    return advertisers