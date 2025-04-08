print("Table of Powers")
print("")

start = int(input("Start number: "))
end = int(input("End number:  "))
print()

print("Number\t\tSquared\t\tCubed")
print("======\t\t=======\t\t=====")
for i in range(start, end):
    print(i, i **2,      i **3, end=" \n")
