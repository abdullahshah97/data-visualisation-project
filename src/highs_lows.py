import csv
from matplotlib import pyplot as plt

#Weather file
filename = 'sitka_weather_07-2014.csv'

# CSV reader object and read line by line
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Retrieve column title and indexes
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Retrieving max temps, first column of row has this value, convert to int so read by matplotlib
    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)

    print(highs)

# Plot the data
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(highs, c='red')

#Format plot
plt.title("Daily High Temperatures, July 2014", fontsize = 24)
plt.xlabel('', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
