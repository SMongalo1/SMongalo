# Calculating the tip

bill = float(input("Enter the bill amount: R"))
tip = 0.15 # written as a decimal

val_tip = bill * tip
total_cost= bill + val_tip

print(f"Here is the tip: {val_tip}")
print(f"Here is the total cost:{round (val_tip, 2)}rounded")

print(f"Here is the total cost: {total_cost}")
print(f"Here is the total cost:{round (total_cost, 2)}rounded")
