# Функция с алгоритмом
def number_to_1(number):
    line = f"{number}"
    counter = 0
    maximum_number = number
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1
        if maximum_number < number:
            maximum_number = number
        line += f"->{number}"
        counter += 1
    return line, maximum_number, counter


# Ввод числа:
try:
    num = int(input("Введите натуральное число:"))
except ValueError:
    print("Введено не натуральное число!")
    exit()

if num < 0:
    print("Введено не натуральное число!")
    exit()

sequence, mx_num, cnt = number_to_1(num)

# Вывод:
print(sequence)
print(f"Пик последовательности: {mx_num}")
print(f"Кол-во чисел в последовательности: {cnt}")
