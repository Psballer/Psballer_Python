students = (("Alice", 78), ("Bob", 45), ("Charlie", 90), ("Diana", 62), ("Kent", 30))
passed = 0
for name, score in students:
    if score >= 50:
        passed += 1
print(passed)
