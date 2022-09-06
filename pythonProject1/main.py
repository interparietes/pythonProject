print("*" * 40)
print("1)", "\n")
n = 5
print(n)
m = 6
print(m)
c = n + m * 5
print(c)
a = "hello Mary"
print(a)
h = "Katy"
print(h * 4)
d = 'Denis\n'
print(d + h)
print(a + ", " + h)
print(a*5)
print(n*2 + m*3)
age = int(input("enter age:"))
print("Age: ", age)
#name = input("enter name:")
age_2 = int (input())
# age_2 = input()
print('enter age:', age_2)
print(type(age_2))
print ("*" * 40)
print(age_2 * age)
print(6 > 8)
print(6 >= 9)
print(8 >= 8)
print(6 == 6)
print(6 != 6)
k = input("Rain?: ")
l = int(input('Temreature?: '))
if k == 'no' and l <= -1:
    print("Одентесь потеплее")
elif k == "yes" and l <= -1:
    print("Одентесь потеплее и возьмите зонтик")
elif k == "yes" and l > 1:
    print ("Возьмите зонтик")
else:
    print("Приятной прогулки")
print("*" * 40)
print("2)", "\n")
t = int(input("введите секунды: "))
min = t // 60
sec = t % 60
hour = min // 60
min = min % 60
print("чч:", hour, " ", "мм:", min, " ", "сек:", sec)
print("*" * 40)
print("3)", "\n")
n = (input("Enter a number: "))
m = int(n * 2)
t = int(n * 3)
n = int(n)
y = n + m + t
print(y)
print("*" * 40)
print("4)", "\n")
n = int(input("Enter a number: "))
max1 = n % 10
print(max1)
while n >= 1:
        n = n // 10
        print("1)", n)
        if n % 10 > max1:
            print("2)", n)
            print("3)", max1)
            max1 = n % 10
            print("4)", max1)
print('Самая большая цифра: ', max1)
print(h)
print("*" * 40)
print("5)", "\n")
n = float(input("Введите значение выручки: "))
m = float(input("Введите значение издержек: "))
if n > m :
    print("Profit")
else:
    print("Lesion")
print("*" * 40)
print("6)", "\n")
n = float(input("Введите значение выручки: "))
m = float(input("Введите значение издержек: "))
if n > m :
    profit = n - m
    profitability = profit / n
    print("Рентабельность: ", profitability)
    person = int(input("Введите численность сотрудников: "))
    print("Прибыль фирмы в расчете на одного сотрудника: ", profit / person)
else:
    print("Lesion")
print("*" * 40)
print("7)", "\n")
a = float(input("Today: "))
s = a + (a * 0.1)
b = float(input("Killometrs: "))
n = 1
print("Today: ", n, "\n")
while s <= b:
    print("Today killometrs: ")
    s = s + (s * 0.1)
    print(s)
    n = n + 1
    print("Today: ", n, "\n")
print("Номер дня, когда достиг результата: ", n)