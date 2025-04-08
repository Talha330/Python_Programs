print("Price Comparison")
print()

price1 = float(input("Price of 64 oz size:  \t"))
price2 = float(input("Price of 32 oz size:  \t"))
print()

p1 = price1/64
p2 = price2/32

print(f"Price per oz (64 oz) : \t {round(p1,2)}")
print(f"Price per oz (64 oz) : \t {round(p2,2)}")
