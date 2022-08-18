options_list = "1. + \n" "2. - \n" "3. / \n" "4. * \n"

a = float(input("Type first value: "))
b = float(input("Type second value: "))
print(options_list)
c = input("Choose action: ")


list_operations = {
    "1": lambda x, y: x + y,
    "2": lambda x, y: x - y,
    "3": lambda x, y: (x / y) if y != 0 else "Division by 0!",
    "4": lambda x, y: x * y,
}

if c in list_operations.keys():
    print(list_operations[c](a,b))
else:
    print("There is no such operation!")
