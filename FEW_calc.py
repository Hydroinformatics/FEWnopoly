import random

class players:
    def __init__(self, governor, farmer1, farmer2, farmer3):
        self.governor = governor
        self.farmer1 = farmer1
        self.farmer2 = farmer2
        self.farmer3 = farmer3


# governor = input("Enter the Governor's Name: ")
# farmer1 = input("Enter Farmer 1's Name: ")
# farmer2 = input("Enter Farmer 2's Name: ")
# farmer3 = input("Enter Farmer 3's Name: ")



class Setup:
    def __init__(self, mode="easy"):
        self.mode = mode

        self.gw_track = 100
        self.env_track = 0
        self.sw_track = 0

        self.gw_lim = 0
        self.env_lim = 0
        self.sw_lim = 0

    def select_mode(self):
        if (self.mode == "easy"):
            print("easy")
            self.gw_track = 100
            self.env_track = 0
            self.sw_track = 0

            self.gw_lim = 65
            self.env_lim = 0
            self.sw_lim = 0
        elif (self.mode == "medium"):
            print("medium")
            self.gw_track = 100
            self.env_track = 0
            self.sw_track = 0

            self.gw_lim = 30
            self.env_lim = 0
            self.sw_lim = 0
        elif (self.mode == "hard"):
            print("hard")
            self.gw_track = 100
            self.env_track = 0
            self.sw_track = 0

            self.gw_lim = 0
            self.env_lim = 0
            self.sw_lim = 0
        else:
            print("easy")

# m = Mode(input("enter a mode; easy medium or hard: "))
# print(m.select_mode())



class GW:
    def __init__(self, dieroll):
        self.dieroll = int(dieroll)

    def tracker(self):
        if (m.select_mode() == 65):
            return 65 + self.dieroll
        if (m.select_mode() == 30):
            return 30 + self.dieroll
        else:
            print ("N/A")

    def limit(self):
        return 100

# b = GW(input("enter a number: "))
# print(b.tracker())


#setup big class- game class [put together all the classes as below)
# self.GW_tracker = GW_tracker()

def dieroll():
    return random.randrange(1,6,1)

# class random(self):
#     def __init__(self):
#         self.onedie()
#         self.twodie()
#     self.onedie()
#         return random.randrange(1,6,1)
#     def twodie():
#         return random.randrange(1,12,1)
