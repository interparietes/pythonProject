print("*" * 40)
# # p = "Maria"
# # print(p[0:-1])
# # print(p[0:])
# # st = "Hello Maria"
# # print(st[0:7])
# # print(st[:])
# # print(st[0::2])
# # print(st[::-1])
# # print(len(st)) #длина строки
# # print(st[len(st) - 1]) #Последний элемент в строке(на последнем индексе)
# # res = st.split() #Разделяет строку на слова, но могу указать по какому принципу
# # print(res)
# # res = st.split("o")
# # print("2", res)
# # # a = (input("Enter numbers: ")).split("2")
# # # print(a)
# # res = "!".join(['hello', "Maria"]) #через что соединяю строки
# # print(res)
# # st = "Hello Maria"
# # print(st.count("o")) #посчитать ск эдементов подобных в строке
# # print(st.count("ello"))
# # res = st.replace("o", "AAA") #заменить одно другим
# # print(res)
# # #ans = input("Enter name CAPS LOCK: ").lower() #маленькими буквами
# # #print(ans)
# # # ans = input("Enter name: ").upper()
# # # print(ans)
# # print(res.capitalize())
# # print(res.title())
# # st = "Hello, how, are, you"
# # for el in st:
# #     print(el)
# # st = "Hello Maria"
# # for i in range (0, len(st)):
# #     print(st[i])
# li = [2, 3, 4, 5]
# # print(li)
# # print(li[2])
# # print(li[0:-1])
# # li[0], li[-1] = li[-2], li[-2]
# # print(li)
# li.append(1) #Вставляю 1 элемент, если слова, то в ""
# print(li)
# li.extend(["Kate", 2, 3]) # Вставляю целиком несколько элементов
# print(li)
# li.insert(3, "False") #Вставляю False в 3ий индекс
# print(li)
# print(li.count(4)) #считаю 4
# li.remove("False") #удаляю элемент
# li.remove("Kate")
# print(li)
# li.pop(0) #удаляю индекс 0
# print(li)
# li.sort()
# print(li)
# # for el in li:
# #     print(el)
# # for i in li:
# #     print("1", li[i])
# # st = input("enter data: ").lower().split(" ")
# st = "Hello baby"
# st.split()
# for word in st:
#     print(word)
#     if word[0] == 'a':
#         print(word)
#
# for i, el in enumerate(li, 1):
#     print(f"{i}.{el}")
# li[0] = 5
# print(li)
# cort = (2, 3, 5, "hello")
# print(type(cort))
# di = {"Kate": 22, "Nastya": 23, "Alena": 22}
# print(di["Kate"])
# print(di.get("kate"))
# di["Mary"] = 24
# di["Kate"] = 23


print("*" * 40)
a = "Exercise 1\n "
print(a)
li = [2, "Kate", 4, 4.5, 5]
print(li)
for el in li:
    print(el)
    print(type(el))



print("*" * 40)
a = "Exercise 2\n "
print(a)
a = int(input("Сколько элементов?: "))
k = 0
my_list = []
while k < a:
    my_list.append(input("Enter one element: "))
    k += 1
print(my_list)
numero = len(my_list)
el = 0
for i in range(numero//2):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el += 2
print(my_list)



print("*" * 40)
a = "Exercise 3\n "
print(a)
di_list = ["Winter", "Spring", "Summer", "Autumn"]
di_dict = {1: "winter", 2: "spring", 3: "summer", 4: "autumn"}
p = int(input("Enter int number 1-12: "))
if p == 1 or p == 2 or p == 12:
    print(di_dict.get(1))
    print(di_list[0])
elif p == 3 or p == 4 or p == 5:
    print(di_dict.get(2))
    print(di_list[1])
elif p == 6 or p == 7 or p == 8:
    print(di_dict.get(3))
    print(di_list[2])
elif p == 9 or p == 10 or p == 11:
    print(di_dict.get(4))
    print(di_list[3])



print("*" * 40)
a = "Exercise 4\n "
print(a)
n = input("Enter str: ")
# s = n.count(" ") + 1
m = n.split()
k = len(m)
a = 0
for i in m:
    t = len(i)
    a = 0
    if t <= 10:
        print(i)
    elif t > 10:
        print(i[0:10])



print("*" * 40)
b = "Exercise 5\n "
print(b)
m = []
a = int(input("Cколько чисел собираетесь вводить?: "))
n = [int(input("Enter: "))]
while a > 0:
    for i in n:
        m.append(i)
        m.sort()
        print(f"Рейтинг - {m}")
    n = [int(input("Enter: "))]
    a = a - 1


print("*" * 40)
b = "Exercise 6\n "
print(b)
li = []
li_2 = {}
r = "2"
s = 1
p = 1
name = []
cena = []
kolichest = []
edinic = []
while r != "1":
    a = input("Введите название товара: ")
    li_2["Название"] = a
    name.append(a)
    b = input("Введите цену: ")
    li_2["Цена"] = b
    cena.append(b)
    c = input("Введите количество: ")
    li_2["Количество"] = c
    kolichest.append(c)
    d = input("Введите единицу измерения: ")
    li_2["Единицы измерения"] = d
    edinic.append(d)
    li.append((p, li_2))
    print(li)
    p += 1
    li_2 = {}
    r = input("Введите любой знак, кроме 1: ")
print(li)
q = input("Провести аналитику?: ").lower()
if q == "yes":
    analitiq = {"Название": (name), "Цена": (cena), "Количество": (kolichest), "Единицы измерения": (edinic)}
    print(analitiq)
else:
    print(li)


