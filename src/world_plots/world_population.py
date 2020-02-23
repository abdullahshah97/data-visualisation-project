import json
import pygal
from pygal.style import RotateStyle
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

# Group the countries by population level

cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 100000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

wm_style = RotateStyle('#336699')
wm = pygal.maps.world.World()

wm.title = 'World Population in 2010, by Country'

wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')
