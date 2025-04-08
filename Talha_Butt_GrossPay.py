print("Paycheck Calculator")
print()

taxRate = 18.0
hWorked = float(input("Hours Worked:    \t"))
hPayrate= float(input("Hourly Pay  Rate:\t"))
print()

grossPay= hWorked*hPayrate
taxAmount = grossPay*(taxRate/100)
takeHomePay = grossPay-taxAmount

print(f"Gross Pay    \t: {round(grossPay,1)}")
print(f"Tax Rate     \t: {round(taxRate,0)}%")
print(f"Tax Amount   \t: {round(taxAmount,2)}")
print(f"Take Home Pay\t: {round(takeHomePay,2)}")
