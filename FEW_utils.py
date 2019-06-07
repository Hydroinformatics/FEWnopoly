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

    if mode == 'easy':
        deck = list(event_cards.items())
        random.shuffle(deck)
        # for value in deck:
        #     (value)
        card1 = deck[0][0]
        card2 = deck[1][0]
        card3 = deck[2][0]
        card4 = deck[3][0]
        card5 = deck[4][0]
        card6 = deck[5][0]
        card7 = deck[6][0]
        card8 = deck[7][0]

        if card1 == "Onion Blight":
            print('1')
        if card1 == "Potatos Blight":
            print('2')
        if card1 == "Environmental tax":

            print('3')

        if card1 == "Rainy year":
            print('4')
        if card1 == "Drought":
            print('5')
        if card1 == "Extreme Drought":
            print('6')
        if card1 == "City Grows":
            print('7')
        if card1 == "Farmer sell water rights":
            print('8')



        print('card: ' + card1)
        # print(card2)
        # print(card3)
        # print(card4)
        # print(card5)
        # print(card6)
        # print(card7)

        # keys = list(event_cards.keys())
        # random.shuffle(keys)
        # for key in keys:
        #     return(key, event_cards[key])


        # for card1 in range(0,1):
        #     event_cards.append(random.choice(list(ecards.keys())))
        #     print(event_cards)
            # print(event_cards[1]['card'])






         # EXAMPLE IF STATEMENT FOR EVENT CARD FUNCTINALITY
        # for card2 in range (1,6):
        #     # event_cards[card2]
        #     print(event_cards[card2])
        #     # print(card2)
        # if 'Potatos Blight' == event_cards[card1]:
        #     print('test')
        # else:
        #     print('fail')


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
            players[player]['water_rights'][counter] = dict()
            players[player]['water_rights'][counter]['order'] = inhr_cards[wr_cards[counter]]['order']
            players[player]['water_rights'][counter]['volume'] = inhr_cards[wr_cards[counter]]['volume']
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

with open('./data/pumping_cost_easy.json', 'r') as f:
    pumping_cost_easy = json.load(f)

with open('./data/pumping_cost_medium.json', 'r') as f:
    pumping_cost_medium = json.load(f)

with open('./data/pumping_cost_hard.json', 'r') as f:
    pumping_cost_hard = json.load(f)

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