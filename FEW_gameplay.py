# -*- coding: utf-8 -*-

import numpy as np
import FEWnopoly

# Gameplay Setup

# gov = input('Enter Governer's Name: ')
# f1 = input('Enter Farmer 1's Name: ')
# f2 = input('Enter Farmer 2's Name: ')
# f3 = input('Enter Farmer 3's Name')
#players_names = [gov,f1,f2,f3] #Commenting out while in development
players_names = ['Nick','Sammy','Andrew','Joel']

#players = FEWnopoly.players(players_names) # Random assigment of roles
players_roles = ['governor','farmer','farmer','farmer']
players = FEWnopoly.players(players_names,players_roles) #Specified assigment of roles

#print('Governer: ' + players.player['governor']['name'])
#print('Farmer 1: ' + players.player['farmer1']['name'])
#print('Farmer 2: ' + players.player['farmer2']['name'])
#print('Farmer 3: ' + players.player['farmer3']['name'])


#m = input('Enter a mode; easy medium or hard: ') #Commenting out while in development
m = 'easy'
game = FEWnopoly.Boardgame(m,players.player)
energy = FEWnopoly.Energy_Resources()

#draw_ecard = FEWnopoly.DrawEventCard()


# --------------------------------------------------------
# ROUND counter

rounds = 0

# Step 1: ENERGY PORTFOLIO---PURCHASE ENERGY COLLECTIVELY
check_bool = 1#check boolean [0=no error, 1=error] in case there is user input errors

#e_coal = input('How many total energy units of coal will all parties be purchasing this round?: ')#Commenting out while in development
#e_hydro = input('How many total energy units of hydropower will all parties be purchasing this round?: ')#Commenting out while in development
#e_rewble = input('How many total energy units of renewables will all parties be purchasing this round?: ')#Commenting out while in development
#e_portfolio = {'coal': e_coal, 'hydro': e_hydro, 'renewable': e_rewble}

# Energy portfolio with error in requested energy from coal (ie. more than max. capacity) 
# Used to verify that the error is capture by the code.
e_portfolio = {'coal': 40, 'hydro': 5, 'renewable': 5} 


while(check_bool == 1):

    check_bool, tcost, envcost = energy.Buy_Energy(e_portfolio, game)
    if check_bool == 1:
        print('Invalid total of energy units requested. More energy units than available capacity of sources')
        #e_coal = input('How many total energy units of coal will all parties be purchasing this round?: ')#Commenting out while in development
        #e_hydro = input('How many total energy units of hydropower will all parties be purchasing this round?: ')#Commenting out while in development
        #e_rewble = input('How many total energy units of renewables will all parties be purchasing this round?: ')#Commenting out while in development
        #e_portfolio = {'coal': e_coal, 'hydro': e_hydro, 'renewable': e_rewble}
        e_portfolio = {'coal': 5, 'hydro': 5, 'renewable': 5}
    
    if check_bool == 0:
        print('Total energy cost ($): ' + str(tcost))
#        gov = input("Enter Cities' energy payment: ") #Commenting out while in development
#        e_f1 = input('Enter ' + game.players['farmer1']['name'] + "'s" + ' energy payment: ') #Commenting out while in development
#        e_f2 = input('Enter ' + game.players['farmer2']['name'] + "'s" + ' energy payment: ') #Commenting out while in development
#        e_f3 = input('Enter ' + game.players['farmer3']['name'] + "'s" + ' energy payment: ') #Commenting out while in development
        
        #Hypothetical distribution of energy costs
        gov = 20
        e_f1 = 5
        e_f2 = 2
        e_f3 = 3
        
        if gov + e_f1 + e_f2 + e_f3 < tcost:
            print('Total payment is lower than total cost. Please adjust your inputs accordingly')
            check_bool = 1
        
#    adjust_port = input('Do you want to adjust your portfolio? (yes/no) ')
#    if adjust_port.lower() == 'yes':
#        #e_coal = input('How many total energy units of coal will all parties be purchasing this round?: ')#Commenting out while in development
#        #e_hydro = input('How many total energy units of hydropower will all parties be purchasing this round?: ')#Commenting out while in development
#        #e_rewble = input('How many total energy units of renewables will all parties be purchasing this round?: ')#Commenting out while in development
#        #e_portfolio = {'coal': e_coal, 'hydro': e_hydro, 'renewable': e_rewble}
#        
    
#Update players money after investing in energy portfolio
game.players['farmer1']['money'] = game.players['farmer1']['money'] - e_f1
game.players['farmer2']['money'] = game.players['farmer2']['money'] - e_f2
game.players['farmer3']['money'] = game.players['farmer3']['money'] - e_f3
          
#Update env. degradation based on energy portfolio
game.env_level = game.env_level + envcost

# Check status of the game
game.check_status()

# Step 2: BUY, PLANT AND TRADE - PER FARMER
play_order_rec = 4
new_play_order = dict()
for i in range(1,4):
    for player in game.players.keys():
        if 'play_order' in game.players[player]:
            if game.players[player]['play_order'] == i:
                new_play_order[player] = play_order_rec - i # Reverts the order of play for the next round
                
                farmer_actions = FEWnopoly.FarmersActions(player)
                
                farmer_actions.BuyLand(game)
                if farmer_actions.land_f > 0:
                    wr_id = farmer_actions.land_tiles.keys()[0]
                    game.players[player]['land_tiles'][wr_id] = []
                    for i,ii in farmer_actions.land_tiles[wr_id]:
                       game.players[player]['land_tiles'][wr_id].append((i,ii))
                       
                farmer_actions.PlantCrops(game)
                farmer_actions.BuyPipes(game)
                farmer_actions.BuyWells(game)
                
                game.players[player]['money'] = game.players[player]['money'] - farmer_actions.owe_money
                game.players[player]['own_tax'] = game.players[player]['own_tax'] - farmer_actions.owe_taxes
                game.players[player]['land'] = game.players[player]['land'] - farmer_actions.land
                
                for crop in game.crops.keys():
                    game.players[player]['farms'][crop] = game.players[player]['farms'][crop] - farmer_actions.land
                
                
                

#Step 3: Set Surface water level   

FEWnopoly.Boardgame.set_sw_level()


#Step 4: Draw event card
#draw_ecard.EventActions(ecard)
                
                

    


#a = input('how many gw units: ')
#usegw = FEW_calc.Setup(a)
#usegw.GW_track(a)
#
#a = input('how many gw units: ')
#usegw = FEW_calc.Setup(a)
#usegw.GW_track(a)


# playercal = FEW_calc.PersonalCalc()
# playercal.MoneyLoss(buyenergy, 10)

# Buy/Plant/trade Crops
# place water right
# plant crops-- $5 per crop, 3 crops per land
# buy land-- $20 per plot
# buy pipe-- $10 per pipe
# buy well-- $20 per well




# Set SURFACE WATER level
# How do I call out just the SW from sw_init??




# Farm/water crops




# Fish population
# mmmhm fully code all the possibilites or?




# --------------------------------------------------------
# ROUND 2

# a = input('Enter how many groundwater units you wish to use this round: ')
# print('The groundwater level is: ' + str(setup.GW_track(a)))
#
# e = input('How many total energy units will all parties be purchasing this round?: ')
# buyenergy = FEW_calc.Energy()
# buyenergy.Buy_Energy()
# # print(str(buyenergy.Buy_Energy()))
