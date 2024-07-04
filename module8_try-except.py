def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    try:
        for number in numbers:
            result += number
        return result, incorrect_data
    except TypeError as e:
        incorrect_data += 1
        print(f'Некорректный тип данных для подсчёта суммы - {e}')
    return result, incorrect_data

def calculate_average(numbers):
    try:
        sum_of_numbers, _ = personal_sum(numbers)
        average = sum_of_numbers / len(numbers)
        return average
    except ZeroDivisionError:
        print('Ошибка деления на ноль')
        return 0
    except TypeError as e:
        print(f'В numbers записан некорректный тип данных - {e}')
        return None

# Вызов функции calculate_average с разными данными
print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')