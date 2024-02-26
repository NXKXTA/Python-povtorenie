import os

# Проверить файл
str_path = "./file3.txt"
if not os.path.exists(str_path):
    print("Файла нет")
    exit()

# Открыть файл
with open(str_path, "r", encoding="utf-8") as file:
    lines = [list(line.rstrip().split(" ")) for line in file]

# Ввод числа N
try:
    N = float(input("Введите число:"))
except ValueError:
    print("Введено не число!")
    exit()

# Сортировка по баллам
val_lines = sorted(lines, key=lambda x: x[1])
print(f"Отсортирован по баллам: {val_lines}")

# Сортировка по именам
name_lines = sorted(lines, key=lambda x: x[0])
print(f"Отсортирован по именам: {name_lines}")

# Запись файла
s = ""
for line in name_lines:
    if int(line[1]) > N:
        s += f"{line[0]}\n"
        with open("./res3.txt", "w", encoding='utf-8') as f:
            f.write(s)
