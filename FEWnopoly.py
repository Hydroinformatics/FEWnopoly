# -*- coding: utf-8 -*-

import FEW_utils as ut
import sys
input = raw_input

class players:
    def __init__(self, names,roles=None):
        self.player = dict()
        if roles == None: # Assigns random roles
            names = ut.shuffle_strings(names)
            self.player['governor'] = dict()
            self.player['governor']['name'] = names[0]
            self.player['governor']['money'] = 50
            for i in range(1,4):
                self.player['farmer' + str(i)]=dict()
                self.player['farmer' + str(i)]['name']  = names[i]
                self.player['farmer' + str(i)]['money']  = 0
                self.player['farmer' + str(i)]['land']  = 0
                self.player['farmer' + str(i)]['own_tax']  = 0
                self.player['farmer' + str(i)]['energy']  = 0
                self.player['farmer' + str(i)]['play_order']  = None
                self.player['farmer' + str(i)]['water_right'] = dict()
                self.player['farmer' + str(i)]['farms'] = dict()
                self.player['farmer' + str(i)]['land_tiles'] = []
                
        else: #Respects the chosen roles by users
              # Will fail if words are misspelled. Need to fix.
            farmer_count = 1
            for i in range(len(names)):
                if roles[i] == 'governor':
                    self.player['governor'] = dict()
                    self.player['governor']['name'] = names[i]
                else:
                    self.player['farmer' + str(farmer_count)]  = dict()
                    self.player['farmer' + str(farmer_count)]['name']  = names[i]
                    self.player['farmer' + str(farmer_count)]['money']  = 0
                    self.player['farmer' + str(farmer_count)]['land']  = 0
                    self.player['farmer' + str(farmer_count)]['own_tax']  = 0
                    self.player['farmer' + str(farmer_count)]['energy']  = 0
                    self.player['farmer' + str(farmer_count)]['play_order']  = None
                    self.player['farmer' + str(farmer_count)]['water_right'] = dict()
                    self.player['farmer' + str(farmer_count)]['farms'] = dict()
                    self.player['farmer' + str(farmer_count)]['land_tiles'] = []
                    farmer_count = farmer_count + 1
        


class Boardgame:
    def __init__(self, mode='easy', players=None):
        
        # Setting up mode for the game: Needed for rules
        self.mode = mode.lower()
        
        # Set gameboard
        self.board = ut.board
        self.board_nodes = ut.board_nodes
        
        # Set cities and crops data
        self.crops = ut.crops_table
        self.cities = ut.cities_table 
        
        #Initiation of trackers used in the game
        self.gw_level = 100 # groundwater tracker
        self.sw_level = 0 # surface water tracker
        self.env_level = 0 # environmental degradation tracker
        self.fish_level = 0 # Salmon pop. tracker
        
        #Resources thresholds: If any of these is violated, everyone loses in the game
        self.gw_lim = 0 # groundwater limit
        self.env_lim = 0 # environmental degradation limit
        self.fish_lim = 15 # Salmon pop. limit
        
        #Initiate the game & parameters based on selected mode
        self.event_cards = None
        self.fish_pop_table = ut.fish_pop_table
        self.inhr_cards = ut.inheritance_cards
        self.ini_setup()
        
        # Add names of players, roles and attributes
        self.players = ut.init_farmers(players,self.inhr_cards)

    def ini_setup(self):
        if (self.mode == 'easy'):
            print('Setting up game in easy mode')
            
            self.event_cards = ut.init_event_cards(self.mode,ut.event_cards)
            
            self.gw_lim = 65 + ut.dieroll()
            
            self.env_level = ut.dieroll()
            self.env_lim = 25 + ut.dieroll()        
            
            self.fish_level = 15 + ut.dieroll()

            
            print('Initial Surface Water Tracker: ' + str(self.sw_level))
            print('Initial Groundwater Tracker: ' + str(self.gw_level))
            print('Initial Environmental Tracker: ' + str(self.env_level))
            
        elif (self.mode == 'medium'):
            print('Setting up game in easy medium')
            return 30
        
        elif (self.mode == 'hard'):
            print('Setting up game in easy hard')
            return 0


    def check_status(self):
        
        if self.gw_level < self.gw_lim or self.env_level > self.env_lim or self.fish_level < self.fish_lim:
            print("Game Over")
            sys.exit()
        
        if self.players['farmer1']['money'] <= 0 or self.players['farmer2']['money'] <= 0 or self.players['farmer3']['money'] <= 0:
            print("Game Over")
            sys.exit()
        
    
    def set_surface_water_level(self):
        
    def GW_track(self, a):
        self.gw_lim = gw - int(a)
        print(self.gw_init)



class DrawEventCard:
    def __init__(self):
        #self.event_cards = ecards
    
    def EventActions(self, ecard):
        
        
class Energy_Resources:
    def __init__(self):
        self.energy_tabs = ut.energy_tabs        

    def Buy_Energy(self, portfolio, game):
        #Calculates env. cost and dollar amount based on user requests
        
        tcost = 0
        envcost = 0
        check_bool = 0
        
        for e in portfolio.keys():
            eunits = portfolio[e]
            ecounter = 0
            for source in self.energy_tabs[e]:
                if ecounter == eunits:
                    break
                else:
                    if eunits - ecounter >= self.energy_tabs[e][source]['max_capacity']:
                        temp_e = self.energy_tabs[e][source]['max_capacity']
                    else:
                        temp_e = (eunits - ecounter)
                        
                    envcost = envcost + (temp_e*self.energy_tabs[e][source]['env_cost'])
                    if e == 'hydro': # Hydro needs to be calculated differently because it depends on the fish pop
                        hydro_cost_lims = list(self.energy_tabs[e][source]['dollar_cost'].keys()) 
                        hydro_cost_lims.sort(reverse=True)
                        #print hydro_cost_lims
                        for lim in hydro_cost_lims:
                            if game.fish_level >= int(lim):
                                tcost = tcost + (temp_e*self.energy_tabs[e][source]['dollar_cost'][lim])
                                break
                    else:
                        tcost = tcost + (temp_e*self.energy_tabs[e][source]['dollar_cost'])
                    
                    ecounter = ecounter + temp_e
            
            if eunits - ecounter != 0: # If users requested more energy than available
                check_bool = 1
                break
                
        return check_bool, tcost, int(round(envcost))
    
    

class FarmersActions:
    def __init__(self, player):
        self.player = player
        self.owe_money = 0
        self.owe_taxes = 5 #every farmer pays $5 regarless
        
        self.land_f = 0
        self.pipes_f = 0
        self.wells_f = 0
        self.crops_f = dict()
        self.land_tiles = []
        
        
    def BuyLand(self, game):
        check_bool = 1

        while(check_bool == 1):
            owe_money = self.owe_money
            owe_taxes = self.owe_taxes
            
            land_bool = 0
            
            while land_bool == 0:
                land_buy = str(input('Does ' + game.players[self.player]['name'] + ' wants buy land in this round? [yes/no] '))
                if land_buy.lower() == 'yes' or land_buy.lower() == 'no':
                    land_bool = 1
                    
                else:
                    print("Please reply 'yes' or 'no'.")
                
            if land_buy.lower() == 'yes':
                
                land_int = input('Enter the intersection ID for the land ' + game.players[self.player]['name'] + ' wants buy in this round: ')
                while land_int == '':
                    if land_int == '':
                        print("That wasn't a number!")
                    land_int = input('Enter the intersection ID for the land ' + game.players[self.player]['name'] + ' wants buy in this round: ')
                    
                    if land_int != '':
                        if int(land_int) not in game.board_nodes.keys():
                            print("Please enter a valid intersection ID.")
                
                land_int = int(land_int)
                land_f = 0 
                for i in game.board_nodes[land_int][0]:
                    for ii in game.board_nodes[land_int][1]:
                        print(game.board[i,ii])
                
                owe_money = owe_money + land_f*10
                owe_taxes = owe_taxes + (game.players[self.player]['land'] + land_f)*2 #Land tax
                
                if game.players[self.player]['money'] - (owe_money + owe_taxes) < 0 or land_f > 4:
                    if land_f <= 4:
                        print("You don't have enough money to buy the requested resources. Try again.")
                    else:
                        print("You can only buy a max. of four land tiles in a turn.")
                else:
                    self.land_f = land_f
                    self.owe_money = self.owe_money + self.land_f*10
                    self.owe_taxes = self.owe_taxes + (game.players[self.player]['land'] + self.land_f)*2 #Land tax
                    check_bool = 0
            else:
                check_bool = 0
                
                
    def PlantCrops(self, game):
        check_bool = 1

        while(check_bool == 1):
            owe_money = self.owe_money
            owe_taxes = self.owe_taxes
            crops_f = dict()
            needed_land = 0
            
            for crop in game.crops.keys():
                crops_f[crop] = input('Enter the amount of '+ crop + "'s farms " + game.players[self.player]['name'] + ' wants buy in this round: ')
                
                while crops_f[crop] == '':
                    print("That wasn't a number!")
                    crops_f[crop] = input('Enter the amount of '+ crop + "'s farms " + game.players[self.player]['name'] + ' wants buy in this round: ')
                
                crops_f[crop] = int(crops_f[crop])
                owe_money = owe_money + crops_f[crop]*5
                needed_land = needed_land + (crops_f[crop]*1.0/3.0)
                
                if game.players[self.player]['money'] - (owe_money + owe_taxes) < 0 and game.players[self.player]['land'] + self.land_f < needed_land:
                    if game.players[self.player]['money'] - (owe_money + owe_taxes) < 0:
                        print("You don't have enough money to buy the requested resources. Try again.")
                    else:
                        print("You don't have enough land to plant the requested crops. Try again.")
                    check_bool = 1
                else:
                    self.owe_money = self.owe_money + owe_money
                    self.crops_f = crops_f
                    check_bool = 0
                    
                    
    def BuyPipes(self, game):
        check_bool = 1
        
        while(check_bool == 1):
            owe_money = self.owe_money
            owe_taxes = self.owe_taxes
            
            pipes_f = input('Enter the amount of pipes ' + game.players[self.player]['name'] + ' wil buy in this round: ')
            while pipes_f =='':
                print("That wasn't a number!")
                pipes_f = input('Enter the amount of pipes ' + game.players[self.player]['name'] + ' wil buy in this round: ')
            
            pipes_f = int(pipes_f)
            owe_money = owe_money + pipes_f*10
                
            if game.players[self.player]['money'] - (owe_money + owe_taxes) < 0:
                print("You don't have enough money to buy the requested resources. Try again.")
                check_bool = 1
            else:
                self.pipes_f = pipes_f
                self.owe_money = self.owe_money + owe_money
                check_bool = 0
                
                
    def BuyWells(self, game):
        check_bool = 1
        
        while(check_bool == 1):
            owe_money = self.owe_money
            owe_taxes = self.owe_taxes
            
            wells_f = input('Enter the amount of wells ' + game.players[self.player]['name'] + ' wil buy in this round: ')
            while wells_f == '':
                print("That wasn't a number!")
                wells_f = input('Enter the amount of wells ' + game.players[self.player]['name'] + ' wil buy in this round: ')
                
            wells_f = int(wells_f)
            owe_money = owe_money + wells_f*20
            
            if game.players[self.player]['money'] - (owe_money + owe_taxes) < 0:
                print("You don't have enough money to buy the requested resources. Try again.")
                check_bool = 1
            else:
                self.wells_f = wells_f
                self.owe_money = self.owe_money + owe_money
                check_bool = 0
        



class PersonalCalc:
    def __init__(self):
        self.wr = None
        
    def MoneyLoss(self, gamestate, invest):
        loss = gamestate.energy - invest
        return loss
          
# class GW:
#     def __init__(self, r):
#         self.dieroll = None
#         self.gw_init = None
#         r = 0
#
#     def tracker(self):
#         if (self.gw_init == 65):
#             return 65 + r
#         if (self.gw_init == 30):
#             return 30 + self.dieroll
#         else:
#             print ('N/A')
#
#     def limit(self):
#         return 100

# Energy Budget Notes
# 24 hydro --- cost by fish tally --- ENV -2 per 12
# 45 coal --- cost -1 per unit --- ENV -1 per 3
# 36 renewables --- cost -2 per unit --- ENV -1 per 9
# total energy = 105



#setup big class- game class [put together all the classes as below)
# self.GW_tracker = GW_tracker()

