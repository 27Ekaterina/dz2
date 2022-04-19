# Найти сумму цифр числа.

my_number = input("Введите любое число: ")
my_sum = 0
for i in my_number:
    my_sum += int(i)
print("Сумма цифр числа равна: ", my_sum)