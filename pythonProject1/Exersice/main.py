from functools import reduce
from sys import argv
from itertools import count, cycle
# li = [1, 2, 3, 4]
# for a in range(1, 15, 2):
#     print(a)
#
# n = [1, 2, 3, 4, 5, 6, 7]
# new = [el + 10 for el in n if el % 2 == 0]
# print(new)
# rew = [el for el in n if el % 2 != 0]
# print(rew)
# pew = [el ** 2 if el % 2 == 0 else el + 2 for el in n]
# print(pew)
# wew = [i for i in range(1, 15) if i % 2 == 0]
# print(wew)
#
# s1 = [1, 2]
# s2 = [3, 4]
# for i in s1:
#     for i2 in s2:
#         print(i, i2)
# new = [i + i2 for i in s1 for i2 in s2]
# print(new)
#
#
# wew = {n: n ** 2 for n in range(1, 10)}
# print(wew)
#
# di = {"ANN": 123, "Bob": 712, "kate": 333}
# di_2 = {k.lower(): v * 10 for k, v in di.items()}
# print(di_2)
#
# import math as m
# print(m.sin(78))
# print(m.pi)

# from liba import тренировка as new
# from liba.тренировка import password, func1
# print(func1())
# print(password)

# from sys import argv
# print('hello')
# print(argv)
# print(f"ar1 = {argv[1]}, ar2 = {argv[2]}, ar3 = {argv[3]}")
# path, ar1, ar2, ar3 = argv
# print(ar1, ar2, ar3)
# p1, p2, p3 = map(int, argv[1:])
# print(type(p1))

print("*" * 40)
print("Exersice 1")
a = int(argv[1])
b = int(argv[2])
c = int(argv[3])
print("Выработка в часах: ", a)
print("Ставка в час: ", b)
print("Премия: ", c)
p = (a * b) + c
print("Заработная плата сотpудника: ", p)

print("*" * 40)
print("Exersice 2")
n = input("Введите элементы: ").split()
new = [n[i] for i in range(len(n)) if n[i - 1] < n[i]]
print("Результат: ", new)

print("*" * 40)
print("Exersice 3")
# Первый способ с генератором
f = (i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0)
print("Первый способ: ")
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
# Второй способ в одну строчку
print("Второй способ: ")
f = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
print(f)

print("*" * 40)
print("Exersice 4")
# Первый способ с генератором
n = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
li = []
new = (i for i in n if n.count(i) == 1)
li.append(next(new))
li.append(next(new))
li.append(next(new))
li.append(next(new))
li.append(next(new))
li.append(next(new))
print("Первый способ: ", li)

# Второй способ в одну строчку
n = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new = [el for el in n if n.count(el) == 1]
print("Второй способ: ", new)

print("*" * 40)
print("Exersice 5")
# Первый способ с генератором
li = []
n = (i for i in range(100, 1001) if i % 2 == 0)
li.append(next(n))
li.append(next(n))
li.append(next(n))
def multi1(a, b):
    return a * b
print("Первый способ: ", (reduce(multi1, li)))

# Второй способ в одну строчку
n = [i for i in range(100, 1001) if i % 2 == 0]
def multi(a, b):
    return a * b
print("Второй способ: ", (reduce(multi, n)))


print("*" * 40)
print("Exersice 6")
p1 = int(argv[1])
p2 = int(argv[2])
lis = []
for el in count(p1):
    if el <= p2:
        lis.append(el)
    else:
        break
print('Цикл count: ', lis)
li = []
for el in cycle(lis):
    if li.count(el) < 1:
        li.append(el)
    else:
        break
print('Цикл cycle на основе полученного count: ', li)


print("*" * 40)
print("Exersice 7")
def fact(n):
    for el in range(1, n + 1):
        yield el
n = int(input("Введите n число: "))
# res = f(n)
# print(res)
a = 1
for el in fact(n):
    a = el * a
    print(f'{el}! = {a}')
