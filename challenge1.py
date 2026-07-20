# The South African Fuel Cost Calculator

kilometers = float(input("enter kilometers, km 100"))
petrol_price_per_liter = 22.45

liters_needed = kilometers/10
total_cost = liters_needed * petrol_price_per_liter

print(f"kilometers entered: {kilometers}")
print(f"liters needed: {round(liters_needed, 2)}")

print(f"total cost: R{round(total_cost, 2)}")
print(f"petrol price per liter: R{petrol_price_per_liter}")