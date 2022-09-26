# li = [1, 2, 3, 4]
#
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
from liba.тренировка import password, func1
print(func1())
print(password)


