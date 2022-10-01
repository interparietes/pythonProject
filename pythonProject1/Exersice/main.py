# with open(r'liba/text.txt', 'r+', encoding='utf-8') as f:
#     l = 1638
#     f.writelines(['Привет\nnew info added'])
#     print(f.tell())
#     f.seek(0)
#     # f.seek(8)
#     # f.seek(14)
#     # f.seek(5)
#     print(f.read())
#
# import os
# a = r"liba\тренировка.py"
# os.remove(a)
# os.rename(r'liba\task.txt', r'liba\text.txt')
# print(os.path.basename('C:/Users/User/Desktop/pythonProject1/Exersice/main.py'))
# print(os.path.dirname('C:/Users/User/Desktop/pythonProject1/Exersice/main.py'))
# print(os.path.join('C:/Users/User/Desktop/pythonProject1/Exersice', 'main.py'))
#
# print(os.path.exists('C:/Users/User/Desktop/pythonProject1/Exersice/main.py'))
# import json
# data = {
#     'income': {
#         'salary': 5000,
#         'bonus': 2000
#     }
# }
# print(type(data))
# with open(r'liba\data.txt', 'r', encoding='utf-8') as f:
#     print(f)
# os.remove(r'liba\data.txt')
# with open(r'liba\data.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f)
# path = json.dumps(data)
# print(path)
# print(type(path))
# with open(r'liba\data.json', 'r', encoding='utf-8') as f:
#     p_data = json.load(f)
# print(type(p_data))
# import os
# os.remove(r'Exersice\task.txt')
# os.remove('liba/data.json')

print('*' * 40)
print('Exersice 1')
with open('Exersice/str.txt', 'w', encoding='utf-8') as f:
    n = input("Введите строку: ")
    while n != "":
        f.write(f'{n}\n')
        n = input("Введите строку: ")


print('*' * 40)
print('Exersice 2')
n = 1
with open(r'Exersice/text.txt', 'r', encoding='utf-8') as f:
    for line in f:
        m = line.strip('\n')
        c = (m.count(" ") + 1)
        print(f'Количество слов в {n} строке: {c}')
        n = n + 1
    n = n - 1
    print(f"Количтсво строк: {n}")


print('*' * 40)
print('Exersice 3')
b = 0
n = 0
with open(r'Exersice/text2.txt', 'r', encoding='utf-8') as f:
    for line in f:
        m = line.strip('\n')
        k = m.split(" ")
        n = n + 1
        for i in range(len(k)):
            a = float(k[1])
            if a < 20000:
                print(f"<20 000: {m}")
        b = a + b
    b = b / n
    print(f'Средняя величина дохода сотрудников: {b}')

print('*' * 40)
print('Exersice 4')
n = 0
dic = {'One': "Один", 'Two': "Два", 'Three': "Три", 'Four': "Четыре"}
li = []
with open(r"Exersice/text4.txt", 'w', encoding='utf-8') as f:
    f2 = open(r"Exersice/text3.txt", "r", encoding='utf-8')
    for line in f2:
        k = line.split(" ", 1)
        li.append(dic[k[0]] + ' ' + k[1])
        print(li)
    print(li)
    f.writelines(li)
    f2.close()

print('*' * 40)
print('Exersice 5')
sum = 0
with open(r'Exersice/text5.txt', 'w', encoding='utf-8') as f:
    a = input('Введите числа через пробел: ')
    f.write(a)
with open(r'Exersice/text5.txt', 'r', encoding='utf-8') as f:
    for line in f:
        k = line.split()
        print(k)
        for i in k:
            i = int(i)
            sum = i + sum
print(f"Сумма чисел равна: {sum}")

print('*' * 40)
print('Exersice 6')
dic = {}
li = []
from functools import reduce
with open(r'Exersice/text6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        a = line.strip("\n")
        b = a.split(" ", 1)
        for i in range(len(b)):
            w1 = b[1].split()
        for l in range(len(w1)):
            n = w1[l].split("(")
            for k in n:
                try:
                    k = int(k)
                    li.append(k)
                except ValueError:
                    if k == "-":
                        k = 0
                        li.append(k)
                    else:
                        pass
        # print(li)
        def summa(a,b):
            return a + b
        sum = reduce(summa, li)
        li = []
        t = 0
        for i in range(len(li)):
            print(li[i])
        for i in range(len(b)):
            w = b[0].split(":")
            for y in range(len(w)):
                dic[w[0]] = sum
        # print(dic)
    print(dic)



