num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter thrid number"))
largest = num1
if num2 > largest:
    largest = num1
if num3 > largest:
    largest = num3
print(largest)
