from math import floor
from numpy import percentile
print("==Datatypes==")
maths=97
science=94
english=91
telugu=87
sanskrit=95
biology=87
StudentMarks=maths+science+english+telugu+sanskrit+biology
TotalMarks=600
percentile= (StudentMarks/TotalMarks)*100
print(percentile)
print(type(percentile))
print(floor(percentile))
print("==complex numbers==")
x= 10+5j
print(x.real)
print(x.imag)
print(x.conjugate())
print("===sequence types= strings===")
EmployeeName= "Gopikrishna"
Designation="DevopsEngineer"
Emp_ID=1430857
str=("EmployeeName:","Designation:","Emp_ID:",EmployeeName,Designation,Emp_ID)
print(str)
print("==Indexing==")
str1=print(EmployeeName[0:8:1])
str2=print(EmployeeName[::-1]) #Reversing the string
print(EmployeeName[5])
print(EmployeeName[5]*3)
print("krishna"in EmployeeName)
print("sid" not in EmployeeName)
print('==List==')
marks=[97,98,94,91,87,75]
print(type(marks))
students=[1001,1002,1003,'gk','pk','ak'] # we can keep different datatypes in list 
print(type(students))
print(students)
students1=[1001,1002,1003,1003,'gk','pk','ak','ak']
print(type(students1))
print(students1)
lenofStudents=print(len(students1))
bioData=[28,9642555414,"address:20-425,ASM",students1]
print(bioData)
print(bioData[-1])
print(bioData[2])