from die import Die
import pygal

# Create a D6 and a D10
die_1 = Die()
die_2 = Die(10)

#Make some rolls, and store results in a list
results = []
results = [die_1.roll() + die_2.roll() for roll_num in range(50000)]

#for roll_num in range (50000):
#    result = die_1.roll() + die_2.roll()
#    results.append(result)

#Analyze the results
frequencies = []
max_result= die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

#for value in range(2, max_result+1):
#    frequency = results.count(value)
#    frequencies.append(frequency)

print(frequencies)

#Visualise the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = [x for x in range(2, 17)]
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')
