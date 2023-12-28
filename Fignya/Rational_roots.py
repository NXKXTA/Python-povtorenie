def read_integers():
    integers_list = []  # Создание пустого списка для целых чисел
    try:
        n = int(input("Enter the number of integers: "))  # Запрос количества целых чисел у пользователя
    except ValueError:
        print("Wrong number")  # Вывод сообщения об ошибке при неверном вводе
        exit()  # Выход из программы
    for _ in range(n):  # Цикл для ввода указанного количества целых чисел
        try:
            num = int(input("Enter the number: "))  # Запрос очередного целого числа у пользователя
        except ValueError:
            print("Wrong number")  # Вывод сообщения об ошибке при неверном вводе
            exit()  # Выход из программы
        integers_list.append(num)  # Добавление введенного числа в список
    return integers_list  # Возвращение списка целых чисел


def find_rational_roots(coefficients):
    rational_roots = []  # Создание пустого списка для хранения рациональных корней
    leading_coefficient = coefficients[0]  # Получение старшего коэффициента многочлена
    svobodniy_chlen = coefficients[-1]  # Получение свободного члена многочлена

    deliteli_svobodny_chlena = [
        i for i in range(1, abs(svobodniy_chlen) + 1) if svobodniy_chlen % i == 0
    ]  # Формирование списка делителей свободного члена

    deliteli_starshego_chlena = [
        i for i in range(1, abs(leading_coefficient) + 1) if leading_coefficient % i == 0
    ]  # Формирование списка делителей старшего коэффициента

    for divisor_svobodnogo in deliteli_svobodny_chlena:  # Цикл по всем делителям свободного члена
        for divisor_leading in deliteli_starshego_chlena:  # Вложенный цикл по всем делителям старшего коэффициента
            potential_root = divisor_svobodnogo / divisor_leading  # Расчет потенциального рационального корня
            if horner_scheme(potential_root,
                             coefficients) == 0:  # Проверка, является ли потенциальный корень корнем многочлена
                rational_roots.append(
                    potential_root)  # Добавление корня в список рациональных корней, если он является таковым

    return rational_roots  # Возвращение списка найденных рациональных корней


def horner_scheme(x, coefficients):
    result = coefficients[0]  # Инициализация результата значением первого коэффициента многочлена
    for i in range(1, len(coefficients)):  # Цикл по всем остальным коэффициентам многочлена
        result = result * x + coefficients[i]  # Применение схемы Горнера для вычисления значения многочлена в точке x
    return result  # Возврат полученного значения многочлена в точке x


# Пример использования
coefficients = read_integers()  # Получение списка коэффициентов многочлена от пользователя
roots = find_rational_roots(coefficients)  # Нахождение рациональных корней многочлена
print("Рациональные корни многочлена:", roots)  # Вывод рациональных корней
