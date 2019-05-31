# -*- coding: utf-8 -*-

import random, json


def shuffle_strings(data):
    shuffle_data = []
    for w in random.sample(data, len(data)):
        shuffle_data.append(w)
    return shuffle_data
    
    
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


## Read Json files with boardgame data
with open('./data/event_cards.json', 'r') as f:
    event_cards = json.load(f)
    
with open('./data/fish_pop_table.json', 'r') as f:
    fish_pop_table = json.load(f)
