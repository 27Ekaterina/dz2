# Найти произведение цифр числа.

my_number = input("Введите любое число: ")
my_mult = 1
for i in my_number:
    my_mult *= int(i)
print("Произведение цифр числа равно: ", my_mult)