def filter(product):
    sum_price = 0
    for item, price in product:
        sum_price = sum_price + price
    return sum_price
        
        
products = [("Laptop", 1200),    ("Mouse", 25),    ("Keyboard", 45),    ("Monitor", 300),    ("USB Cable", 10)]
print(filter(products))       
        
        

