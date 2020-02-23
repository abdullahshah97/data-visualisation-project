import csv
from datetime import datetime

from matplotlib import pyplot as plt


#Weather file
#filename = 'sitka_weather_07-2014.csv'
filename = 'sitka_weather_2014'

# CSV reader object and read line by line
# Get dates and max temps from file.
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Retrieve column title and indexes
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # First column contains dates
    # Retrieving max temps, second column of row has this value, convert to int so read by matplotlib
    # Minimum temperatures retrieved also
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0],'%Y-%m-%d')
        dates.append(current_date)

        low = int(row[3])
        lows.append(low)

        high = int(row[1])
        highs.append(high)

    print(highs)

# Plot the data
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
# plt.title("Daily High Temperatures, July 2014", fontsize = 24)
plt.title("Daily High and Low Temperatures - 2014", fontsize = 24)
plt.xlabel('Date', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.savefig('high_low_2014_fill_in.png')
