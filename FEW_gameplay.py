
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

# assign random roles?

m = input("Enter a mode; easy medium or hard:")
setup = FEW_calc.Setup(m)
setup.select_mode()


# --------------------------------------------------------
# ROUND 1

# ENERGY PORTFOLIO---PURCHASE ENERGY COLLECTIVELY
e = input("How many total energy units will all parties be purchasing this round?: ")
buyenergy = FEW_calc.Energy(e)
buyenergy.Buy_Energy()
# print(buyenergy.Buy_Energy())


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

# a = input("Enter how many groundwater units you wish to use this round: ")
# print("The groundwater level is: " + str(setup.GW_track(a)))
#
# e = input("How many total energy units will all parties be purchasing this round?: ")
# buyenergy = FEW_calc.Energy()
# buyenergy.Buy_Energy()
# # print(str(buyenergy.Buy_Energy()))
