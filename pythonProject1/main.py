print('*' * 40)
print("Exersice1")
class Data():
    def __init__(self, day_data, month_data, year_data):
        self.day_data = int(day_data)
        self.month_data = int(month_data)
        self.year_data = int(year_data)
    @classmethod
    def set_data(cls, data):
        li = []
        for i in range(len(data)):
            if data[i] != '-':
                li.append(data[i])
        b = int(li[1])
        a = int(li[0]) * 10 + b
        b1 = int(li[3])
        a1 = int(li[2]) * 10 + b1
        y2 = int(li[5]) * 100
        y3 = int(li[6]) * 10
        y4 = int(li[7])
        y1 = int(li[4]) * 1000 + y2 + y3 + y4
        return cls(a, a1, y1)
    @staticmethod
    def get_data(day_data, month_data, year_data):
        if day_data < 31 and day_data > 0:
            print(day_data)
        else:
            print("Error")
        if month_data <= 12 and month_data > 0:
            print(month_data)
        else:
            print("Error")
        if year_data > 0 and year_data < 2022:
            print(year_data)
        else:
            print("Error")
d1 = '21-12-2002'
d = Data.set_data(d1)
print(d.year_data, d.month_data, d.day_data)
print(d.get_data(21, 12, 2002))


print('*' * 40)
print("Exersice2")
class Zero(Exception):
    def __init__(self, txt):
        self.txt = txt
num = input("Enter first number: ")
num_2 = input('Enter second number: ')
try:
    num = float(num)
    num_2 = float(num_2)
    if num_2 == 0:
        raise Zero('error, you enter zero')
    else:
        y = num / num_2
except (ValueError, TypeError, Zero) as err:
    print(err)
else:
    print(y)
finally:
    print('end')


print('*' * 40)
print("Exersice3")
class Number(Exception):
    def __init__(self, li):
        self.li = li
li = []
b = 'start'
while b != 'stop':
    b = input('Enter element or Enter: ')
    try:
        b = float(b)
    except ValueError:
        print("Error, not a number")
    try:
        if b != float(b):
            raise Number('not a number')
        else:
            li.append(b)
    except (ValueError, Number) as err:
        print(err)
    finally:
        print(li)
print(f'Final li: {li}')


print('*' * 40)
print("Exersice4")

from datetime import datetime

class Hospital:
    def __init__(self, title):
        self.title = title
        self.li = {}
        self.li1 = {}

    def take_to_Hospital(self, name):
        self.name = name
# внесение в словарь имя и фамилия пацента, номер карты и время поступления
        t = datetime.now()
        self.li.update({name.card_number: name.title})
        print(f'В госпиталь: {self.title}. Поступил пациент: {self.name}. Номер карты: {str(name.card_number)}. Дата: {str(t.day)}.{str(t.month)}.{str(t.year)}')
    def give_to_Hospital(self, name, other):
# перевод пациента в другое отделение или госпиталь
        t = datetime.now()
        self.li1.update({name.card_number: name.title})
        print(f'Переведён пациент: {name.title}. Hомер карты: {str(name.card_number)}. Дата:{str(t.day)}.{str(t.month)}.{str(t.year)}')
        other.take_to_Hospital(name)
    def take_list_patients(self):
        print(f'В {self.title}. Поступил патицент:')
        print(self.li)
        print(f'Общее количество поступивших: {len(self.li)}')
    def give_list_patients(self):
        print(f'Из госпиталя: {self.title}. Переведён пациент:')
        print(self.li1)
        print(f'Общее количество выбывших:{len(self.li1)}')
class Patients:
    def __init__(self, title, card_number):
        self.title = title
        self.card_number = card_number

    def __str__(self):
        return str(self.title)

class Cardiology(Patients):
    def __init__(self, title, card_number, disease):
        Patients.__init__(self, title, card_number)
        self.disease = disease

    def __str__(self):
        return f'{Patients.__str__(self)}. Заболевание: {self.disease}'


class Neurology(Patients):
    def __init__(self, title, card_number, disease):
        Patients.__init__(self, title, card_number)
        self.disease = disease

    def __str__(self):
        return f'{Patients.__str__(self)}. Заболевание: {self.disease}'

class Traumatology(Patients):
    def __init__(self, title, card_number, disease):
        Patients.__init__(self, title, card_number)
        self.disease = disease

    def __str__(self):
        return f'{Patients.__str__(self)}. Заболевание: {self.disease}'


store1 = Hospital('Bubnova')
store2 = Hospital('Voroncova')
a = Cardiology('Ivan Ivanov', 345678, "Гипертонический криз")
b = Neurology('Petr Petrovich', 123456, "Инсульт")
c = Traumatology('Irina Ivanova', 987654, "Перелом лучезапястного сустава")
d = Cardiology('Maria Simashko', 245678, "Острый инфаркт миокарда")

store1.take_to_Hospital(a)
store1.take_to_Hospital(b)
store1.take_to_Hospital(c)
store2.take_to_Hospital(d)
store1.give_to_Hospital(b, store2)
store2.take_to_Hospital(d)
store2.give_to_Hospital(d, store1)

print(store1.take_list_patients())
print(store2.give_list_patients())


print('*' * 40)
print("Exersice7")
class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.d = '(a + b) * i'

    def __add__(self, other):
        print(f'Сумма d1 и d2 равна')
        return f'd = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение d1 и d2 равно')
        return f'd = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'd = {self.a} + {self.b} * i'


d1 = ComplexNumber(3, -8)
d2 = ComplexNumber(5, 8)
print(d1)
print(d1 + d2)
print(d1 * d2)


