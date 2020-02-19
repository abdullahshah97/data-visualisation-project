import csv
from datetime import datetime

from matplotlib import pyplot as plt


#Weather file
#filename = 'sitka_weather_07-2014.csv'
#filename = 'sitka_weather_2014'
filename = 'death_valley_2014.csv'

# CSV reader object and read line by line
# Get dates and max temps from file.
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Print column title and indexes
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # First column contains dates
    # Retrieving max temps, second column of row has this value, convert to int so read by matplotlib
    # Minimum temperatures retrieved also
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0],'%Y-%m-%d')
            low = int(row[3])
            high = int(row[1])

        except ValueError:
            print(current_date, 'Missing data for this date')

        else:
            dates.append(current_date)
            lows.append(low)
            highs.append(high)
        print(highs)

# Plot the data
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
# plt.title("Daily High Temperatures, July 2014", fontsize = 24)
title = "Daily High and Low Temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize = 20)
plt.xlabel('Date', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.savefig('death_valley.png')
