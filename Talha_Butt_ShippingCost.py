print("="*40)
print("Shipping Calculator")
print("="*40)

choice = "y"
while choice.lower() == "y":
#entering while loop
    cost=float(input("Cost of item ordered:\t"))
    if cost < 0:
        print("You must enter a positive number. Please try again.")
        continue
        
    if cost >= 75:
        shipping_cost = 0
        
    elif cost >=50:
        shipping_cost = 9.95
        
    elif cost >= 30:
        shipping_cost = 7.95
        
    else:
        shipping_cost = 5.95

    total_cost = cost + shipping_cost
    print(f"Shipping cost:         {round(shipping_cost,2)} ")
    print(f"Total cost:            {round(total_cost,2)}")
    
    choice = input("Continue? (y/n): ")
#exiting while loop

print("Bye!")
