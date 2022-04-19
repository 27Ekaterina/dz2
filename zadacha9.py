# Найти максимальную цифру в числе

my_number = input("Введите любое число: ")
max = 0
for i in my_number:
    if int(i) > max:
        max = int(i)

print("Максимальная цифра равна: ", max)