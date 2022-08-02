sum=10
def calculate():
    global sum
    sum=sum+100
    currentSum=200
    totalSum=currentSum+sum
    print(totalSum)
    print(sum)
calculate();
print(sum)