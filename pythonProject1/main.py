# def print_num():
#     while True:
#         li = input("enter data: ").split()
#         for num in li:
#             if num == 'stop':
#                 return
#             else:
#                 print(num)
# print_num()
#
# try:
#     n = 0
#     print(1/n)
# except ZeroDivisionError:
#     print("cant devide by zero")
#
# try:
#     n = int(input())
#     print(n)
# except ValueError:
#     print("only digits")


print("*" * 30)
print("Exercise 1")
def numbers(n1, n2):
    res = n1/n2
    try:
        print(n1/n2)
    except ZeroDivisionError:
        print("cant devide by zero")
    return res

numbers(float(input("Enter n1: ")),float(input("Enter n2: ")))

print("*" * 30)
print("Exercise 2")
def profile(n = "Name", s = "Surname", b = "Birthday", c = "City", e = "Email", t = "Tel"):
    print("name: ", n, "surname: ", s, "birthday: ", b, "city: ", c, "email: ", e, "tel: ", t)

profile(input("Enter name: "), input("Enter surname: "), input("Enter birthday: "), input("Enter city: "), input("Enter email: "), input("Enter telephone: "))


print("*" * 30)
print("Exercise 3")
def my_func(a, b, c):
    if a >= c and b > c:
        res = a + b
        print(res)
    elif b >= a and c > a:
        res = b + c
        print(res)
    elif a >= b and c > b:
        res = a + c
        print(res)

my_func(int(input()), int(input()), int(input()))


print("*" * 30)
print("Exercise 4")
def my_func(x, y):
    print(x**y)
    print(pow(x, y))
    b = 1
    if y < 0:
        y = abs(y)
        for i in range(y):
            b = b * x
        res = 1/b
        print(res)
    elif y > 0:
        for i in range(y):
            b = b * x
        print(b)
    elif y == 0:
        print("На ноль делить нельзя")

my_func(float(input("Enter x: ")), int(input("Enter y: ")))


print("*" * 30)
print("Exercise 5")
def sum():
    a = True
    summa = 0
    while a == True:
        n = input("Введите числа: ")
        n = n.split()
        print(n)
        s = 0
        for num in range(len(n)):
            if n[num] != 'stop':
                a = int(n[num])
                s = a + s
            else:
                print(s)
                summa = summa + s
                print("Сумма полностью: ", summa)
                return
        summa = summa + s
        print("Сумма равна: ", summa)
        a = True
sum()


print("*" * 30)
print("Exercise 6")
def int_func(n):
    while n != "Stop":
        n = input("Введите слово: ").capitalize()
        print(n)

int_func("n")

print("*" * 30)
print("Exercise 7")
def int_func(n):
    a = []
    b = True
    while b == True:
        n = input("Введите словa: ").split()
        print(n)
        for l in range(len(n)):
            if n[l] != "stop":
                w = n[l].capitalize()
                a.append(w)
            else:
                print(a)
                return
        print(a)
        b = True

int_func("n")


