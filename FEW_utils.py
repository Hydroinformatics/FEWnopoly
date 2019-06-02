# -*- coding: utf-8 -*-

import random, json
import numpy as np

def shuffle_strings(data):
#    shuffle_data = []
#    for w in random.sample(data, len(data)):
#        shuffle_data.append(w)
    return random.sample(data, len(data))
        
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


def init_farmers(players,inhr_cards):
    
    wr_cards = random.sample(list(inhr_cards.keys()),len(list(inhr_cards.keys())))
    counter = 0
    wr_seniority = []
    for player in players.keys():
        if player != 'governor':
            players[player]['money'] = inhr_cards[wr_cards[counter]]['money']
            players[player]['water_right']['order'] = inhr_cards[wr_cards[counter]]['order']
            players[player]['water_right']['volume'] = inhr_cards[wr_cards[counter]]['volume']
            wr_seniority.append(inhr_cards[wr_cards[counter]]['order'])
            counter = counter + 1
            
    play_order = np.argsort(wr_seniority) #index of sort wr orders
    counter = 0
    for player in players.keys():
        if player != 'governor':
            players[player]['play_order'] = play_order[counter]+1
            counter = counter + 1
    
    return players
            

## Read Json files with boardgame data
with open('./data/cities_data.json', 'r') as f:
    cities_table = json.load(f)    

with open('./data/event_cards.json', 'r') as f:
    event_cards = json.load(f)
    
with open('./data/fish_pop_table.json', 'r') as f:
    fish_pop_table = json.load(f)
    
with open('./data/inheritance_cards.json', 'r') as f:
    inheritance_cards = json.load(f)

with open('./data/energy_tabs.json', 'r') as f:
    energy_tabs = json.load(f)

