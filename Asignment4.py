weight = float(input("Enter weight"))
height = float(input("Enter height"))
bmi = weight/(height * height)
if(weight < 18.5):
   print("underweight")
elif(weight >= 18.5 and weight <= 24.9):
    print("Normal")
elif(weight >= 25 and weight <= 29.9):
    print("Overweight")
elif(weight >= 30):
    print("Obese")
