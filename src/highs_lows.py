import csv

filename = 'sitka_weather_07-2014.csv'

#CSV reader object and read line by line
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #Retrieve column title and indexes
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    #Retrieving max temps, first column of row has this value, convert to int so read by matplotlib
    highs = []
    for row in reader:
        highs.append(int(row[1]))

    print(highs)
