
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

# --------------------------------------------------------
# ROUND counter

rounds = 0

# ENERGY PORTFOLIO---PURCHASE ENERGY COLLECTIVELY

check_bool = 1
#e_coal = input('How many total energy units of coal will all parties be purchasing this round?: ')#Commenting out while in development
#e_hydro = input('How many total energy units of hydropower will all parties be purchasing this round?: ')#Commenting out while in development
#e_rewble = input('How many total energy units of renewables will all parties be purchasing this round?: ')#Commenting out while in development
#e_portfolio = {'coal': e_coal, 'hydro': e_hydro, 'renewable': e_rewble}
e_portfolio = {'coal': 40, 'hydro': 5, 'renewable': 5}
while(check_bool == 1):

    check_bool, tcost, envcost = energy.Buy_Energy(e_portfolio, game)
    if check_bool == 1:
        print 'Invalid total of energy units requested. More energy units than available capacity of sources'
        #e_coal = input('How many total energy units of coal will all parties be purchasing this round?: ')#Commenting out while in development
        #e_hydro = input('How many total energy units of hydropower will all parties be purchasing this round?: ')#Commenting out while in development
        #e_rewble = input('How many total energy units of renewables will all parties be purchasing this round?: ')#Commenting out while in development
        #e_portfolio = {'coal': e_coal, 'hydro': e_hydro, 'renewable': e_rewble}
        e_portfolio = {'coal': 5, 'hydro': 5, 'renewable': 5}
    
    if check_bool == 0:
        print 'Total energy cost ($): ' + str(tcost)
        gov = input("Enter Cities' energy payment: ")
        e_f1 = input('Enter ' + game.players['farmer1']['name'] + "'s" + ' energy payment: ')
        e_f2 = input('Enter ' + game.players['farmer2']['name'] + "'s" + ' energy payment: ')
        e_f3 = input('Enter ' + game.players['farmer3']['name'] + "'s" + ' energy payment: ')
        
        if gov + e_f1 + e_f2 + e_f3 < tcost:
            print 'Total payment is lower than total cost. Please adjust your inputs accordingly'
            check_bool = 1
        
#    adjust_port = input('Do you want to adjust your portfolio? (yes/no) ')
#    if adjust_port.lower() == 'yes':
#        #e_coal = input('How many total energy units of coal will all parties be purchasing this round?: ')#Commenting out while in development
#        #e_hydro = input('How many total energy units of hydropower will all parties be purchasing this round?: ')#Commenting out while in development
#        #e_rewble = input('How many total energy units of renewables will all parties be purchasing this round?: ')#Commenting out while in development
#        #e_portfolio = {'coal': e_coal, 'hydro': e_hydro, 'renewable': e_rewble}
#        
    
#Update players money
game.players['farmer1']['money'] = game.players['farmer1']['money'] - e_f1
game.players['farmer2']['money'] = game.players['farmer2']['money'] - e_f2
game.players['farmer3']['money'] = game.players['farmer3']['money'] - e_f3
          
#Update env. degradation
game.env_level = game.env_level + envcost

# Check status of the game
game.check_status()




# BUY, PLANT AND TRADE - PER FARMER

for i in range(1,4):
    
    if game.players['farmer' + str(i)]['play_order'] == i:
        print game.players['farmer' + str(i)]['name'] 
#    e_f1 = input('Enter ' + game.players['farmer' + str(i)]['name'] + "'s" + ' energy payment: ')
#    e_f2 = input('Enter ' + game.players['farmer' + str(i)]['name'] + "'s" + ' energy payment: ')
#    e_f3 = input('Enter ' + game.players['farmer' + str(i)]['name'] + "'s" + ' energy payment: ')
    


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
