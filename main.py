import csv
import json
import pandas as pd


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


csvIn = r'cdr_test.csv'
csvOut = r'cdr_processed.csv'
jsonPath = r'data.json'


def csv_to_json(csvDocPath, jsonFilePath):
    jsonArray = []

    with open(csvDocPath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for row in csvReader:
            jsonArray.append(row)

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


def csv_add_column(csvInbound, csvOutbound):
    data = pd.read_csv(csvInbound,
                       usecols=['Date', 'Account', 'CallerID', 'Destination', 'Description', 'Seconds', 'Rate',
                                'Total', 'UniqueID'],
                       dtype={'Date': str, 'Time': str, 'Account': str,
                              'CallerID': str, 'Destination': str,
                              'Description': str,
                              'Seconds': str, 'Rate': str, 'Total': str,
                              'UniqueID': str})

    data[['Date', 'Time']] = data.Date.str.split(expand=True, )
    data.to_csv(csvOutbound,
                columns=['Date', 'Time', 'Account', 'CallerID', 'Destination', 'Description', 'Seconds', 'Rate',
                         'Total', 'UniqueID'], index=False)


if __name__ == '__main__':
    print_hi('PyCharm')
    csv_add_column(csvIn, csvOut)
    csv_to_json(csvOut, jsonPath)
