total_bills = float(input("Enter total_bills"))
is_member = input("yes/no")
if(total_bills >= 1000 and is_member == ("yes")):
    final_price = total_bills * 10/100
    print(final_price)
elif(total_bills >= 1000 and is_member == ("no")):
    final_price = total_bills * 5/100
    print(final_price)
else:
    print("no discount")
