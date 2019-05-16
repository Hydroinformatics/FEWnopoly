import random

class players:
    def __init__(self, governor, farmer1, farmer2, farmer3):
        self.governor = governor
        self.farmer1 = farmer1
        self.farmer2 = farmer2
        self.farmer3 = farmer3



class Setup:
    def __init__(self, mode="easy"):
        self.mode = mode
        self.gw_lim = 0
        self.env_lim = 0
        self.gw_track = 100
        self.sw_track = 0


    def dieroll():
        return random.randrange(1, 6, 1)

    def select_mode(self):
        if (self.mode == "easy"):
            print("easy")
            self.gw_lim = 65 + dieroll()
            self.env_lim = 0 + dieroll()
            print("Current Groundwater Tracker: " + str(self.gw_lim))
            print("Current Environmental Tracker: " + str(self.env_lim))
        elif (self.mode == "medium"):
            print("medium")
            return 30
        elif (self.mode == "hard"):
            print("hard")
            return 0
        else:
            print("easy")

    def track_gw(self,a):
        return self.gw_track - int(a)
    def track_sw(self,b):
        return self.sw_track - int(b)

class Energy:
    def __init__(self, e):
        self.Energy = 24
        self.e = 0

    def Buy_Energy(self, e):
        return self.Energy - int(e)



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

def dieroll():
    return random.randrange(1,6,1)
