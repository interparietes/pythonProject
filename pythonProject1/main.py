print("*" * 40)
print("Exersice 1")

# import copy
# test_1 = [1, 2, 3, [1, 2, 3]]
# test_deepcopy = copy.deepcopy(test_1)
# test_copy = copy.copy(test_1)
# print(test_deepcopy)
# print(test_copy)
class Matrix:
    def __init__(self, p):
        self.p = p
    def __str__(self):
        res =''
        for k in self.p:
            for t in k:
                t = str(t)
                res = res + t + '\t'
        return res
    def __add__(self, other):
        import copy
        res = copy.copy(self.p)
        for i in range(len(self.p)):
            for k in range(len(self.p[i])):
                res[i][k] = self.p[i][k] + other.p[i][k]
        return Matrix(res)


m1 = Matrix([[1], [2]])
m2 = Matrix([[8], [9]])
m3 = Matrix([[10], [11]])
print(m1)
print(m2)
print(m3)
m4 = m1 + m2
print(f'Сложение матриц(1+2):\n{m4}')
m5 = m3 + m4
print(f'Сложение матриц(полученная+3):\n{m5}')
print('\n')
p1 = Matrix([[1, 2], [3]])
p2 = Matrix([[8, 9], [10]])
p3 = Matrix([[11, 12], [13]])
print(p1)
print(p2)
print(p3)
p4 = p1 + p2
print(f'Сложение матриц(1+2):\n{p4}')
p5 = p3 + p4
print(f'Сложение матриц(полученная+3):\n{p5}')
print('\n')
t1 = Matrix([[1, 2], [3, 4]])
t2 = Matrix([[8, 9], [10, 11]])
print(t1)
print(t2)
t3 = t1 + t2
print(f'Новая матрица:\n{t3}')

print("*" * 40)
print("Exersice 2")
from abc import ABC, abstractmethod
class MyAbstract(ABC):
    @abstractmethod
    def consum(self, vh):
        pass
class Coat(MyAbstract):
    def consum(self, v):
        # V = "sice"
        self.v =float(v)
        return self.v / 6.5 + 0.5
class Costume(MyAbstract):
    def consum(self, h):
        # H = 'height'
        self.h =float(h)
        return 2 * self.h + 0.3

c1 = Coat()
print(f'Абстрактный метод: {c1.consum(13.5)}')
c2 = Costume()
print(f'Абстрактный метод: {c2.consum(13.5)}')

class Clothes:
    def __init__(self, vh):
        self.vh = float(vh)
    def __add__(self, other):
        return self.vh + other.vh
class Coat(Clothes):
    @property
    def consum(self):
        # V = "sice"
        self.vh = self.vh / 6.5 + 0.5
        return self.vh
class Costume(Clothes):
    @property
    def consum(self):
        # H = 'height'
        self.vh = 2 * self.vh + 0.3
        return self.vh

c1 = Coat(13.5)
c2 = Costume(13.5)
print(f'Расход  ткани на пальто: {c1.consum}')
print(f'Расход  ткани на костюм: {c2.consum}')
print(f'Общий расход  ткани: {c1 + c2}')


print("*" * 40)
print("Exersice 3")
class Cell:
    def __init__(self, cell):
        self.cell = int(cell)
        # y = self.cell * '*'
        # print(y)

    def __str__(self):
        return str(f'Количество: - {self.cell}')

    def __sub__(self, other):
        return Cell(abs(self.cell - other.cell))

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)

    def __add__(self, other):
        return Cell(abs(self.cell + other.cell))

    def make_order(self, ar1):
        if self.cell//ar1 == 0:
            for i in range((self.cell//ar1)):
                r = '*' * ar1 + '\n'
                print(r)
                break
        else:
            for i in range((self.cell//ar1)):
                r1 = '*' * ar1 + '\n'
                print(r1)
            n = self.cell % ar1
            m = "*" * n
            print(m)
        return "\n"

a = Cell(8)
b = Cell(15)
c = Cell(13)
d = Cell(10)

print(a + b)
print(a - b)
print(a * b)
print(c / d)

print(a.make_order(3))
print(b.make_order(5))
print(c.make_order(4))
print(d.make_order(2))

