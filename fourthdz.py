options_list = "1. + \n" "2. - \n" "3. / \n" "4. * \n"

a = float(input("Type first value: "))
b = float(input("Type second value: "))
print(options_list)
c = input("Choose action: ")


a1 = a + b
a2 = a - b
a3 = a / b
a4 = a * b


if c == "1":
    print(a1)
elif c == "2":
    print(a2)
elif c == "3":
    if b  == 0:
        print("Division by 0!")
    else:
        print(a3)
elif c == "4":
    print(a4)


  # Только мне не понятно почему выдает ошибку при делении на 0, вроде бы строка написанна как и у Вас