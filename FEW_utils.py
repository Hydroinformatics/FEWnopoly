# -*- coding: utf-8 -*-

import random

def dieroll():
    return random.randrange(1,6,1)
def three_dieroll():
    return random.randrange(1, 6, 1) + random.randrange(1, 6, 1) + random.randrange(1, 6, 1)

def init_event_cards(mode,ecards):
    #Missing the controling for event card types explained in the rules
    event_cards = []
    if mode == 'easy':
        for i in range(0,6):
            event_cards.append(random.choice(list(ecards.keys())))
    elif mode == 'medium': 
        for i in range(0,13):
            event_cards.append(random.choice(list(ecards.keys())))
    elif mode == 'hard':
        for i in range(0,16):
            event_cards.append(random.choice(list(ecards.keys())))

    return event_cards

event_cards = {'Onion Blight':'All onion farmers roll a die. If you get a number below 3, you can harvest 2 of your onion farms.',
              'Potatos Blight':'All potato farmers roll a die. If you get a number below 3, you can harvest 2 of your onion farms.',
              'Enviromental tax': 'The whole group must pay a total of however much enviromental damage has been incurred.',
              'Rainy year': 'Add specified units to the surface water level',
              'Drought': 'Substract specified units from surface water',
              'Extreme Drought': 'Substract specified units from surface water for the next 2 turns',
              'City Grows': 'The food needs of the cities increase',
              'Farmer sell water rights': 'Farmer selects a water right card randomly and auction it off'}


fish_pop_table = {'Inf-20':{'max': float('Inf'), 'min':20, 'pop_rates':[5,5,5,4,4,3,2,2,1,1]},
                  '19-16':{'max': 19, 'min':16, 'pop_rates':[3,2,2,2,1,1,0,0,0,-1]},
                  '15-12':{'max': 15, 'min':12, 'pop_rates':[-6,-6,-6,-5,-5,-4,-3,-3,-3,-float('Inf')]},
                  '11-8': {'max': 11, 'min':8, 'pop_rates':[-12,-10,-8,-7,-6,-6,-6,-6,-6,-float('Inf')]},
                  '7-5':{'max': 7, 'min':5, 'pop_rates':[-20,-16,-14,-12,-10,-9,-9,-8,-float('Inf'),-float('Inf')]},
                  '3-1':{'max': 3, 'min':1, 'pop_rates':[-44,-39,-34,-29,-24,-19,-14,-9,-float('Inf'),-float('Inf')]},
                  'Fish pop range': ['49-45','44-40','39-35','34-30','29-25','24-20','19-15','14-10','9-5','4-1']}