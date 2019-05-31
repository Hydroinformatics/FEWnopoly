import FEW_utils as ut

class players:
    def __init__(self, governor, farmer1, farmer2, farmer3):
        self.governor = governor
        self.farmer1 = farmer1
        self.farmer2 = farmer2
        self.farmer3 = farmer3

# assign roles randomly?

gw = 100

class Boardgame:
    def __init__(self, a, mode='easy'):
        
        # Setting up mode for the game: Needed for rules
        self.mode = mode.lower()
        
        #Initiation of trackers used in the game
        self.gw_init = 100 # groundwater tracker
        self.sw_init = 0 # surface water tracker
        self.env_init = 0 # environmental degradation tracker
        self.fish_init = 0 # Salmon pop. tracker
        
        #Resources thresholds: If any of these is violated, everyone loses in the game
        self.gw_lim = 0 # groundwater limit
        self.env_lim = 0 # environmental degradation limit
        self.fish_lim = 15 # Salmon pop. limit
        
        #Initiate the game & parameters based on selected mode
        self.event_cards = None
        self.fish_pop_table = ut.fish_pop_table
        self.ini_setup()
        
        
        self.a = a

    def ini_setup(self):
        if (self.mode == 'easy'):
            print('Setting up game in easy mode')
            self.event_cards = ut.init_event_cards(self.mode,ut.event_cards)
            self.gw_lim = 65 + ut.dieroll()
            self.gw_init = 100
            self.env_init = ut.dieroll()
            self.env_lim = 25 + ut.dieroll()
            self.sw_init = 14 + ut.three_dieroll()
            self.fish_init = 15 + ut.dieroll()
            self.fish_lim = 15
            
            print("Initial Surface Water Tracker: " + str(self.sw_init))
            print("Initial Groundwater Tracker: " + str(self.gw_init))
            print("Initial Environmental Tracker: " + str(self.env_init))
            
        elif (self.mode == 'medium'):
            print('Setting up game in easy medium')
            return 30
        
        elif (self.mode == 'hard'):
            print('Setting up game in easy hard')
            return 0

    def GW_track(self, a):
        self.gw_lim = gw - int(a)
        print(self.gw_init)






class Energy:
    def __init__(self, e):
        self.e = e
        self.energy = 24
        

    def Buy_Energy(self):
        return self.energy - int(self.e)

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
#             print ("N/A")
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

