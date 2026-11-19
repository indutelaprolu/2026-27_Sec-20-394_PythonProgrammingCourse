p=int(input("Enter principal amount:"))
r=int(input("Enter rate of interest:"))
t=int(input("Enter time in tears:"))
amount=p*(1+r/100)**t
ci=amount-p
print("Compound interest:", ci)
print("Total amount:", amount)
