employees = (("John", "IT", 50000),("Jane", "HR", 45000),("Mike", "IT", 60000),("Sara", "Finance", 70000))
name = 0
for name, department, salary in employees:
    if department == ("IT"):
        print(name)
