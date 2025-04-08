print("Tip Calculator")
print("")

choice = "y"
while choice == "y" or choice =="Y":
    cost = float(input("Cost of meal : "))
    for i in range(15,26,5):
        print("")
        print(str(i)+"%")
        amount = i*cost/100
        print("Tip amount:    "+str(round(amount,2)))
        print("Total amount : "+str(round(amount+cost,2)))
        print("")
    choice = input("Continue? (y/n)")

print("Bye!")
