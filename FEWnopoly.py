import FEW_utils as ut
import sys

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
                    farmer_count = farmer_count + 1
        


class Boardgame:
    def __init__(self, mode='easy', players=None):
        
        # Setting up mode for the game: Needed for rules
        self.mode = mode.lower()
        
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
            print "Game Over"
            sys.exit()
        
        if self.players['farmer1']['money'] <= 0 or self.players['farmer2']['money'] <= 0 or self.players['farmer3']['money'] <= 0:
            print "Game Over"
            sys.exit()
        
        
    def GW_track(self, a):
        self.gw_lim = gw - int(a)
        print(self.gw_init)




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
                        hydro_cost_lims = self.energy_tabs[e][source]['dollar_cost'].keys() 
                        hydro_cost_lims.sort(reverse=True)
                        for lim in hydro_cost_lims:
                            if game.fish_level >= lim:
                                tcost = tcost + (temp_e*self.energy_tabs[e][source]['dollar_cost'][lim])
                    else:
                        tcost = tcost + (temp_e*self.energy_tabs[e][source]['dollar_cost'])
                    
                    ecounter = ecounter + temp_e
            
            if eunits - ecounter != 0: # If users requested more energy than available
                check_bool = 1
                break
                
        return check_bool, tcost, int(round(envcost))
    
    
    
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

