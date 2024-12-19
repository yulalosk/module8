def personal_sum(numbers:list):
    result=0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            print(f'Некорректный тип данных -{i}')
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers:list):
    summa = personal_sum(numbers)
    try:
        return summa[0] / (len(numbers) - summa[1])
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('Неверный тип данных')





#s = personal_sum([42, 15, 36, 13])
s = personal_sum([1, "Строка", 3, "Ещё Строка"])
print(s)
print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать