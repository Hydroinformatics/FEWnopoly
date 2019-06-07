# -*- coding: utf-8 -*-

# Create Json files needed for game
import json
import numpy as np

event_cards = {'Onion Blight': 'All onion farmers roll a die. If you get a number below 3, you can harvest 2 of your onion farms.',
              'Potato Blight':'All potato farmers roll a die. If you get a number below 3, you can harvest 2 of your potato farms.',
              'Environmental Tax': 'The whole group must pay a total of however much enviromental damage has been incurred.',
              'Rainy Year': 'Add specified units to the surface water level',
              'Drought': 'Substract specified units from surface water',
              'Extreme Drought': 'Substract specified units from surface water for the next 2 turns',
              'City Grows': 'The food needs of the cities increase',
              'Farmer Sell Water Right': 'Farmer selects a water right card randomly and auction it off'}


fish_pop_table = {'Inf-20':{'max': float('Inf'), 'min':20, 'pop_rates':[5,5,5,4,4,3,2,2,1,1]},
                  '19-16':{'max': 19, 'min':16, 'pop_rates':[3,2,2,2,1,1,0,0,0,-1]},
                  '15-12':{'max': 15, 'min':12, 'pop_rates':[-6,-6,-6,-5,-5,-4,-3,-3,-3,-float('Inf')]},
                  '11-8': {'max': 11, 'min':8, 'pop_rates':[-12,-10,-8,-7,-6,-6,-6,-6,-6,-float('Inf')]},
                  '7-5':{'max': 7, 'min':5, 'pop_rates':[-20,-16,-14,-12,-10,-9,-9,-8,-float('Inf'),-float('Inf')]},
                  '3-1':{'max': 3, 'min':1, 'pop_rates':[-44,-39,-34,-29,-24,-19,-14,-9,-float('Inf'),-float('Inf')]},
                  'Fish pop range': ['49-45','44-40','39-35','34-30','29-25','24-20','19-15','14-10','9-5','4-1']}


inheritance_cards = {1:{'order': 1, 'money': 100, 'volume': float('Inf')},
                     2:{'order': 3, 'money': 110, 'volume': float('Inf')},
                     3:{'order': 5, 'money': 125, 'volume': float('Inf')}}

hydro_cost = {30: 1, 20: 2, 10: 3, 0:4}
energy_tabs = {'coal':{1:{'max_capacity': 15, 'env_cost': 1.0/3, 'dollar_cost': 1}},
               'renewable':{1:{'max_capacity': 9, 'env_cost': 1.0/9, 'dollar_cost': 2}},
               'hydro':{1:{'max_capacity': 24, 'env_cost': 1.0/12, 'dollar_cost': hydro_cost}}}


crops = {'alfalfa': 2, 'potatos': 1, 'melon': 1, 'wheat': 0}
cities = {'Pendleton':{'crops':{'alfalfa': 16, 'potatos':11, 'melon':10, 'wheat':8}, 'tax_money': 15, 'energy': 9, 'water': 1, 'food_needs': 8, 'total_food_needs': 14},
          'Hermiston':{'crops':{'alfalfa': 13, 'potatos':11, 'melon':12, 'wheat':8}, 'tax_money': 15, 'energy': 9, 'water': 1, 'food_needs': 8, 'total_food_needs': 14}}          
                      

pumping_cost_easy = {'100 - 90':{'max': 100, 'min': 90, 'pump_rate': 0},
                     '89 - 80':{'max': 89, 'min': 80, 'pump_rate': 1},
                     '79 - 75':{'max': 79, 'min': 75, 'pump_rate': 2},
                     '74 - 70':{'max': 74, 'min': 70, 'pump_rate': 3},
                     '69 - 0':{'max': 69, 'min': 0, 'pump_rate': 4}}

pumping_cost_medium = {'100 - 70':{'max': 100, 'min': 70, 'pump_rate': 0},
                     '69 - 55':{'max': 69, 'min': 55, 'pump_rate': 1},
                     '54 - 45':{'max': 54, 'min': 45, 'pump_rate': 2},
                     '44 - 40':{'max': 44, 'min': 40, 'pump_rate': 3},
                     '39 - 0':{'max': 39, 'min': 0, 'pump_rate': 4}}

pumping_cost_hard = {'100 - 50':{'max': 100, 'min': 50, 'pump_rate': 0},
                     '49 - 25':{'max': 49, 'min': 25, 'pump_rate': 1},
                     '24 - 20':{'max': 24, 'min': 20, 'pump_rate': 2},
                     '19 - 10':{'max': 19, 'min': 10, 'pump_rate': 3},
                     '9 - 0':{'max': 9, 'min': 0, 'pump_rate': 4}}


with open('crops_data.json', 'w') as fp:
    json.dump(crops, fp)

with open('cities_data.json', 'w') as fp:
    json.dump(cities, fp)

with open('fish_pop_table.json', 'w') as fp:
    json.dump(fish_pop_table, fp)
    
with open('event_cards.json', 'w') as fp:
    json.dump(event_cards, fp)
    
with open('inheritance_cards.json', 'w') as fp:
    json.dump(inheritance_cards, fp)
    
with open('energy_tabs.json', 'w') as fp:
    json.dump(energy_tabs, fp)

with open('pumping_cost_easy.json', 'w') as fp:
    json.dump(pumping_cost_easy, fp)
    
with open('pumping_cost_medium.json', 'w') as fp:
    json.dump(pumping_cost_medium, fp)

with open('pumping_cost_hard.json', 'w') as fp:
    json.dump(pumping_cost_hard, fp)
