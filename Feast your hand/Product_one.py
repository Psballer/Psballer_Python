def filtern(products):
    for item, price in products:
#        if price > 100:
         print(item, price)
                      
products = [("Laptop", 1200),    ("Mouse", 25),    ("Keyboard", 45),    ("Monitor", 300),    ("USB Cable", 10)]
print(filtration(products))
