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

def init_event_cards(mode, ecards):
    #Missing the controling for event card types explained in the rules
    event_cards = []
    if mode == 'easy':
        
        for event in ecards.keys():
            if event == 'City Grows' or event == 'Farmer Sell Water Right':
                del ecards[event]
            break

        for i in range(0,6):
            event_cards.append(random.choice(list(ecards.keys())))
        return event_cards

            
    elif mode == 'medium': 
        
        for i in range(0,3):
            random_card = random.choice(list(ecards.keys()))
            if random_card != 'Farmer Sell Water Right' or random_card != 'City Grows':
                event_cards.append(random_card)
        
        event_cards.append('Farmer Sell Water Right')
        event_cards.append('Farmer Sell Water Right')
        event_cards.append('Farmer Sell Water Right')
        event_cards.append('City Grows')
            
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
            wr_id = inhr_cards[wr_cards[counter]]['wr_id']
            players[player]['water_rights'][wr_id] = dict()
            players[player]['water_rights'][wr_id]['order'] = inhr_cards[wr_cards[counter]]['order']
            players[player]['water_rights'][wr_id]['volume'] = inhr_cards[wr_cards[counter]]['volume']
            wr_seniority.append(inhr_cards[wr_cards[counter]]['order'])
            counter = counter + 1
            
    play_order = np.argsort(wr_seniority) #index of sort wr orders
    # Initiates play order for first round based on water right seniority
    counter = 0
    for player in players.keys():
        if player != 'governor':
            players[player]['play_order'] = play_order[counter]+1
            counter = counter + 1
    
    return players
            

## Read Json files with boardgame data
with open('./data/crops_data.json', 'r') as f:
    crops_table = json.load(f)       

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

with open('./data/pumping_costs.json', 'r') as f:
    pumping_costs = json.load(f)

#%% Create game board
board = np.zeros((10,14))

#Water 
board[3,0] = 2
for i in range(1,4):
    board[2,i] = 2
    
for i in range(4,9):
    board[1,i] = 2 
board[0,9] = 2

#Cities
board[2,7] = 3
board[4,10] = 3

#Ag. Land
board[6,10] = 1
cell_ind = [[9,10],[4,12],[1,13],[0,12],[1,11],[1,5],[2,5],[3,4],[3,3]]

for i in range(1,10):
    for ii in range(cell_ind[i-1][0],cell_ind[i-1][1]+1):
        if board[i,ii] == 0:
            board[i,ii] = 1


# Board nodes = intersection points for water rights
board_nodes = dict()    
count = 0
for i in range(1,10):
    for ii in range(1,14):
        
        if board[i-1,ii-1] == 1 or board[i-1,ii] == 1 or board[i,ii-1] == 1 or board[i,ii] == 1:
            board_nodes[count] = [[i-1,i],[ii-1,ii]]
            count = count + 1
        


#import matplotlib.pyplot as plt
#plt.rcParams['text.color'] = 'white'
##plt.pcolor(np.flipud(board), edgecolors='w', linewidths=2)
#plt.pcolor(board, edgecolors='w', linewidths=2)
#for j in board_nodes.keys():
##for i in board_nodes[j][0]:
###        for ii in board_nodes[j][1]:
##
#    plt.plot(board_nodes[j][1][1], board_nodes[j][0][1],'ro')
#    plt.text(board_nodes[j][1][1], board_nodes[j][0][1], str(j)) 
##    
#plt.show()