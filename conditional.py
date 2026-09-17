age = int(input("enter your age: "))

if age < 13:
    category = "child"
elif age < 20:
    category = "teenager"
else:
    category = "adult"

print(category)


