import random
def dieroll():
    return random.randrange(1,6,1)
def three_dieroll():
    return random.randrange(1, 6, 1) + random.randrange(1, 6, 1) + random.randrange(1, 6, 1)

class players:
    def __init__(self, governor, farmer1, farmer2, farmer3):
        self.governor = governor
        self.farmer1 = farmer1
        self.farmer2 = farmer2
        self.farmer3 = farmer3

# assign roles randomly?

gw = 100

class Setup:
    def __init__(self, a, mode="easy"):
        self.mode = mode
        self.gw_init = 100
        self.env_init = 0
        self.sw_init = 0
        self.gw_lim = 0
        self.env_lim = 0
        self.fish_init = 0
        self.fish_lim = 15
        self.a = a

    def select_mode(self):
        if (self.mode == "easy"):
            print("easy")
            self.gw_lim = 65 + dieroll()
            self.gw_init = 100
            self.env_init = dieroll()
            self.env_lim = 25 + dieroll()
            self.sw_init = 14 + three_dieroll()
            self.fish_init = 15 + dieroll()
            self.fish_lim = 15
            
            print("Initial Surface Water Tracker: " + str(self.sw_init))
            print("Initial Groundwater Tracker: " + str(self.gw_init))
            print("Initial Environmental Tracker: " + str(self.env_init))
            
        elif (self.mode == "medium"):
            print("medium")
            return 30
        
        elif (self.mode == "hard"):
            print("hard")
            return 0
        else:
            print("easy")

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

