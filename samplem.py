user_name = input("Enter a name: ")
total = 0
while True:
    product = input("Enter product name: ")
    quantity= float(input(f"Enter qunatity of {product}: "))
    price = int(input(f"Enter price of {product}: "))
    another_product = input("Do you want to add another product? yes/no:")

    amount = quantity * price
    total = total + amount
    if another_product.lower() == 'no':
        print("Total amount = ", total)
        break    


