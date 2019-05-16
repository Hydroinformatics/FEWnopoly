
import FEW_calc

# governor = input("Enter the Governor's Name: ")
# farmer1 = input("Enter Farmer 1's Name: ")
# farmer2 = input("Enter Farmer 2's Name: ")
# farmer3 = input("Enter Farmer 3's Name: ")


m = input("enter a mode; easy medium or hard: ")
setup = FEW_calc.Setup(m)
setup.select_mode()

gw_lim = input("roll a single die")
lim = FEW_calc.Setup(gw_lim)
lim.select_mode()

print(setup.select_mode())
print(lim.select_mode())