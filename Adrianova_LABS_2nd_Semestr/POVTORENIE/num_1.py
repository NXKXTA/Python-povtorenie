# Ввод строки и ключевого слова
user_input = input("Введите строку из 10 слов, разделенных ';'\n")
keyword = input("Введите ключевое слово: ")

# Разбиение строки на слова и проверка на их количество
words = user_input.split(";")
if len(words) - words.count('') < 10:
    print("Введено не 10 слов")
    exit()

# Ищем слова, начинающиеся с ключевого слова
matching_words = [word for word in words if word.startswith(keyword)]

print(*matching_words)
