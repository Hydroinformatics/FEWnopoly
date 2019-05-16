
import FEW_calc

# Gameplay Setup

# gov = input("Enter Governer's Name: ")
# f1 = input("Enter Farmer 1's Name: ")
# f2 = input("Enter Farmer 2's Name: ")
# f3 = input("Enter Farmer 3's Name")
# name = FEW_calc.players(gov, f1, f2, f3)
# print("Governer: " + name.governor)
# print("Farmer 1: " + name.farmer1)
# print("Farmer 2: " + name.farmer2)
# print("Farmer 3: " + name.farmer3)


m = input("Enter a mode; easy medium or hard: ")
setup = FEW_calc.Setup(m)
setup.select_mode()


a = input("Enter how many groundwater units you wish to use this round: ")
print("The groundwater level is: " + str(setup.track_gw(a)))

# --------------------------------------------------------
# ROUND 1


# PURCHASE ENERGY
e = input("How many energy units will you be purchasing this round?: ")
buyenergy = FEW_calc.Energy(e)
print(str(buyenergy.Buy_Energy(e)))

