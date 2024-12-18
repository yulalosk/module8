class Car:
    def __init__(self, model, vin:int, numbers:str):
        self.model = model
        if self.__is_valid_vin(vin):
            self.vin = vin
        if self.__is_valid_numbers(numbers):
            self.numbers = numbers

    def __is_valid_vin(self,vin_number):
        if not isinstance(vin_number,int):
            raise IncorrectVinNumber('некорректный VIN')
        elif  vin_number not in range(1000000,99999999):
            raise IncorrectVinNumber('неверный диапазон')
        return True

    def __is_valid_numbers(self,numbers):
            if not isinstance(numbers, str):
                raise IncorrectCarNumbers('некорректный тип номера')
            elif len(numbers) != 6:
                raise IncorrectCarNumbers('неверная длина номера')
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')


try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')

try:
  fourth = Car('Model1', 1000000, 123456)
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{fourth.model} успешно создан')
