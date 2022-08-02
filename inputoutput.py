a=10
b=20
c=a+b
print(a,b,c,sep="=>")
print(a,b,c,end=" ")
totalAmt=50000
pin=input("\n Enter you pin:")
cash=input("\n Enter your cash:")
"""pin,cash=input(" \n Enter pin and cash :").split(',')"""
print("Pin and cash are:", pin,cash)
cashAmt=int(cash)
BalanceAmt=totalAmt - cashAmt
print(BalanceAmt)
print("your balance amount is:", BalanceAmt)
print("your balance amount is : {}".format(BalanceAmt))
print(cashAmt)
print(type(cashAmt))