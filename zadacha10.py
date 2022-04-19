# Найти количество цифр 5 в числе

my_number = input("Введите любое число: ")
my_sum = 0
for i in my_number:
    if int(i) == 5:
        my_sum += 1
print("Количество цифр 5 в числе равно: ", my_sum)