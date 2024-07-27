class IncorrectVinNumber(Exception):
    def __init__(self,message):
        self.message = message
        print(self.message)

class IncorrectCarNumbers(Exception):
    def __init__(self,message):
        self.message = message
        print(self.message)
class Car:
   def __init__(self,model: str, vin: int, numbers: str):
       self.model = model
       self.__vin = vin
       self.__numbers = numbers


    def __is_valid_vin(self,__vin_number):
        try:
            if isinstance(__vin_number,float):
                raise IncorrectVinNumber('Некорректный тип vin номер')
            if __vin_number <= 1000000 and __vin_number >= 9999999:
                raise  IncorrectVinNumber('Неверный диапазон для vin номера')
        except:
            return True
    def __is_valid_numbers(self,__numbers):
        try:
            if isinstance(self.__numbers, str):
                raise IncorrectVinNumber('Некорректный тип данных для номеров')
            if len(self.__numbers) > 6:
                raise IncorrectCarNumbers('Неверная длина номера')
        except:
            return True







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