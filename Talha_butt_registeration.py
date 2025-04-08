#!usr/bin/env python3

print("Registeration Form")
print()

fName = input("First name:\t")
lName = input("Last name :\t")
bYear = input("Birth year:\t")
print()

#print("Welcome "+fName+" "+lName+"!")

print(f"Welcome {fName} {lName}!")
print("Your registeration is complete.")
print(f"Your temporary password is: {fName}*{bYear}")
