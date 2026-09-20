num1 = int(input("Enter number: "))
num2= int(input("Enter number; "))
num3= int(input("Enter number: "))
num4 = int(input("Enter number: "))

largest =  num1
if(num2 > largest):
    largest = num2
elif(numb3 > largest):
    largest = num3
elif(num4 > largest):
    largest = num4
print(largest)

smallest = num1
if(num2 < smallest):
    smallest = num2
elif(num3 < smallest):
    smallest< num3
elif(num4 < smallest):
    smallest = num4
print(smallest)

sum = num1 + num2 + num3 + num4
print(sum)

mean = sum / 4
print(mean)


