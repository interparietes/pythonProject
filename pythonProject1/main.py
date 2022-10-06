# class Transport:
#     def __init__(self, year, color):  # construktor
#         self.color = color
#         self.year = year
#         # print(f'year: {self.year} color: {self.color}')
#     def stop(self):
#         return f'stops'
#
#     def start(self):
#         return f'goes'
# class Car(Transport):
#     def drift(self):
#         return "drift"
#     def __init__(self, year, color, name):
#         super().__init__(year, color)
#         self.name = name
#         print(f'{self.year}. {self.color}. {self.year}. {self.name}')
#     pass
#     # name = "Mazda"
#     # count = 0
#     #
#     # def __init__(self, year, color):       #construktor
#     #     print('obj')
#     #     self.co = color
#     #     self.year = year
#     #     Car.count += 1
#     #
#     # # def set_info(self, color, year):
#     # #     self.co = color
#     # #     self.y = year
#     # #     Car.count += 1
#     # def get_info(self):
#     #     return (f'{Car.count}. {Car.name}. {self.co}. {self.year}')
#     # def stop(self):
#     #     return f'car: {self.name} stops'
#     #
#     # def start(self):
#     #     return f'car: {self.name} goes'
#
# class Bus(Transport):
#     def __init__(self, year, color, route):
#         Transport.__init__(self, year, color)
#         self.route = route
#         print(f'{self.year}. {self.color}. {self.route}')
#     def follow_route(self):
#         return f'route {self.route}'
#     # name = "Bus"
#     # def __init__(self, year, color):       #construktor
#     #     self.co = color
#     #     self.year = year
#     #     Car.count += 1
#     #
#     # def get_info(self):
#     #     return (f'{Car.count}. {Car.name}. {self.co}. {self.year}')
#     # def stop(self):
#     #     return f'car: {self.name} stops'
#     #
#     # def start(self):
#     #     return f'car: {self.name} goes'
# #
# #
# #
# # car1 = Car("red", 2019)
# # # car1.set_info("red", 2019)
# # print(car1.get_info())
# # # car1.set_info("red", 2019)
# # # Car.count = 5
# # # print(car1.get_info())
# # # car1.name = "Lada"
# # # print(car1.name)
# #
# # car2 = Car('yellow', 2020)
# # print(car2.name)
# # print(car2.get_info())
# # print(car2.stop())
# # print(car2.start())
#
# car1 = Car(2020, "grey", 'Mazda')
# print(car1.name)
# car2 = Car(2019, 'black', 'Lexus')
# bus1 = Bus(1990, 'green', "12")
# print(bus1.follow_route())
# print(car1.start())
# print(car2.stop())
# print(bus1.start())
# print(bus1.stop())
# print(car1.drift()) #у автобуса такой возможности нет
#
#
# class Player:
#     def method(self):
#         print("Родительский метод класса Player")
#
# class Navigator:
#     def method(self):
#         print("Родительский метод класса Navigator")
#
# class MobilePhone(Player, Navigator):
#     def mobile_method(self):
#         print("Дочерний метод класса MobilePhone")
#
#
# phone = MobilePhone()
# phone.mobile_method()
# phone.method()
# Player.method(phone)
# # phone.navigator_method()
# # phone.player_method()

print("*" * 40)
print("Exersice 1")
import time
class TrafficLight():
    __color = ['Красный', "Желтый", "Зеленый"]
    def running(self):
        n = 0
        while n < 3:
            if n == 0:
                print(f'Переключение на \n {TrafficLight.__color[0]}')
                time.sleep(7)
            elif n == 1:
                print(f'Переключение на \n {TrafficLight.__color[1]}')
                time.sleep(2)
            elif n == 2:
                print(f'Переключение на \n {TrafficLight.__color[2]}')
                time.sleep(1)
            n += 1
Svet = TrafficLight()
print(Svet.running())

print("*" * 40)
print("Exersice 2")
class Road():
    def __init__(self, _length, _width):
        self._length = float(_length)
        self._width = float(_width)
    def summassa(self):
        massa = 25
        thikness = 5
        return f"Масса асфальта, необходимого для покрытия всей дороги: {self._length * self._width * massa * thikness}"

asfalt = Road(42.5, 44.2)
print(asfalt.summassa())

print("*" * 40)
print("Exersice 3")
class Worker():
    def __init__(self, name, surname, position, _wage, _bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._wage = float(_wage)
        self._bonus = float(_bonus)
        self._income = {"wage": self._wage, "bonus": self._bonus}
class Position(Worker):
    def get_full_name(self):
        n = self.name
        return f"Полное имя сотрудника: {self.name} {self.surname} "
    def get_total_income(self):
        s = self._bonus + self._wage
        return f"{self._income}\nIncome: {s}"

name1 = Position("Misha", "Dytlov", "Programist", 13500, 3200)
print(name1.name)
print(name1.surname)
print(name1.position)
print(name1.get_full_name())
print(name1.get_total_income())

print("*" * 40)
print("Exersice 4")
class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = float(speed)
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f"Имя: {self.name}. Текущая скорость: {self.speed}. Цвет: {self.color}. Служебная: {self.is_police}")
    def go(self):
        return f'{self.name} cтарт'
    def stop(self):
        return f"{self.name} cтоп"
    def turn(self, direction):
        return f'{self.name} повернула: {direction}'
    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name}: {self.speed}'
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"{self.name} is {self.speed}: Превышение скорости !!!"
        else:
            return f"{self.name} is {self.speed}: Можете ехать дальше"

class SportCar(Car):
    def drift(self):
        return f'{self.name} can drift'
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"{self.name} is {self.speed}: Превышение скорости !!!"
        else:
            return f"{self.name} is {self.speed}: Можете ехать дальше"
class PoliceCar(Car):
    def Official(self):
        if self.is_police == "True":
            return f'{self.name} is police'
        else:
            return f'{self.name} is not police'

car1 = TownCar(43, "red", "hyundai", "Falce" )
car2 = SportCar(89, 'black', "audi", 'Falce')
car3 = WorkCar(65, 'white', 'toyota', 'Falce')
car4 = PoliceCar(110, 'blue', 'volkswagen', 'True')
print(car1.show_speed())
print(car1.stop())
print(car1.go())
print(car1.turn("left"))
print(car2.turn("right"))
print(car2.show_speed())
print(car3.show_speed())
print(car3.stop())
print(car4.Official())

print("*" * 40)
print("Exersice 5")
class Stationery():
    def __init__(self, title):
        self.title = title
        print(self.title)
    def draw(self):
        print(f"Запуск {self.title} отрисовки")
class Pen(Stationery):
    def draw(self):
        p = self.title.strip('а')
        return f"Запуск отрисовки {p}ой: pen"
class Pencil(Stationery):
    def draw(self):
        return f"Запуск отрисовки {self.title}ом: pencil"
class Handle(Stationery):
    def draw(self):
        return f"Запуск отрисовки {self.title}ом: handle"

pic1 = Handle("маркер")
pic2 = Pencil("карандаш")
pic3 = Pen('ручка')
print(pic1.draw())
print(pic2.draw())
print(pic3.draw())





