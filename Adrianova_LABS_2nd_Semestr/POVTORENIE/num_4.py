import os


def get_letter_list(line):
    letter_list = {}
    for letter in line:
        if letter.isalpha():  # Проверка на букву
            letter = letter.lower()  # Преобразуем букву к нижнему регистру
            letter_list[letter] = letter_list.get(letter, 0) + 1
    return letter_list


file_path = "./file4.txt"
if not (os.path.exists(file_path)):
    print("Файла нет")
    exit()

with open(file_path, "r", encoding="utf-8") as file:
    stroka = [line.rstrip() for line in file][0]

result = get_letter_list(stroka)

print(stroka)
print(result)

s = ""
for letter, value in result.items():
    s += f"{letter}:{value}\n"
    with open("./res4.txt", "w", encoding='utf-8') as f:
        f.write(s)
