from datetime import date
print("===Age calculator===")
DateofBirth= input()
print("Entered age :", DateofBirth)
print(date.today())
currentyear=date.today().year
print(currentyear)
currentAge=currentyear-int(DateofBirth)
print(currentAge)