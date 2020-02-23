import json
import pygal
from country_codes import get_country_code

#Load the data into a list
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

#Print the 2010 population for each country
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(pop_dict['Country Name'])
        if code:
            print(code + ' : ' + str(population))
            cc_populations[code] = population
        else:
            print('ERROR - ' +country_name)

wm = pygal.maps.world.World()
wm.title = 'World Population in 2010, by Country'
wm.add('2010', cc_populations)

wm.render_to_file('world_population.svg')
