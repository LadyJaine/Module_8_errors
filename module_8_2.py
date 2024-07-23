
def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError as exc:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
    return result,incorrect_data


def calculate_average(numbers):

    result1 = 0

    try:
        total_sum, incorrect_data = personal_sum(numbers)
        return total_sum / (len(numbers)-incorrect_data)
    except ZeroDivisionError as exc:
        print(f'Вы забыли ввести числа, тип ошибки: {exc}, вывод 0')
        return 0
    except TypeError as exc:
            print(f'В numbers записан некорректный тип данных - {type(numbers)}')
            return None


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print()
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print()
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print()
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
print()
print(f'Результат 5: {calculate_average([])}')
print()
print(calculate_average([1,2,"3"]))