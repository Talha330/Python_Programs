print("Letter Grade Converter")
print()

choice = "y"
while choice.lower() == "y":
#entering while loop
    grade=int(input("Enter numerical grade:\t"))
    if grade >= 88 and grade <= 100:
        print("Letter grade: A")
        
    elif grade >=80 and grade <=87:
        print("Letter grade: B")
        
    elif grade >= 67 and grade <= 79:
        print("Letter grade: C")
        
    elif grade >= 60 and grade <= 66:
        print("Letter grade: D")
        
    else:
        print("Letter grade: F")
        
    choice = input("Continue? (y/n): ")
#exiting while loop

print("Bye!")
