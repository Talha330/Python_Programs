print("Tip Calculator")
print()

mealCost = float(input("Cost of Meal:    \t"))
tipPercent = float(input("Tip Percent:    \t"))
print()

tipAmount = mealCost*(tipPercent/100)
totalAmount = tipAmount+mealCost

print(f"Tip Amount:   \t {round(tipAmount,2)}")
print(f"Total Amount: \t {round(totalAmount,2)}")
