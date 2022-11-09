# Написать тесты для встроенных функций filter, map, sorted,
# а также для функций из библиотеки math: pi, sqrt, pow, hypot.

import math


#Тест filter:
def test_filter():
    n = [1, 2, 4, 5, 7, 8, 10, 11, 25, 9, 81, 16]
    s = ["Python", "Scala", "JavaScript", "Go", "PHP", "CSharp", "Python", "Pascal"]
    assert list(filter(lambda x: x % 2 == 0, n)) == [2, 4, 8, 10, 16]
    assert list(filter(lambda x: x ** 2 in n, n)) == [1, 2, 4, 5, 9]
    assert list(filter(lambda x: 'Python' in x, s)) == ['Python', 'Python']
    assert list(filter(lambda x: len(x) == 6, s)) == ['Python', 'CSharp', 'Python', 'Pascal']


#Тест map:

def test_map():
    n = [1, 2, 4, 5, 7, 8, 10, 11, 25, 9, 81, 16]
    s = ["Python", "Scala", "JavaScript", "Go", "PHP", "CSharp", "Python", "Pascal"]
    assert list(map(lambda x: x ** 2, n)) == [1, 4, 16, 25, 49, 64, 100, 121, 625, 81, 6561, 256]
    assert list(map(lambda x: x - 5, n)) == [-4, -3, -1, 0, 2, 3, 5, 6, 20, 4, 76, 11]
    assert list(map(lambda x: x + 20, n)) == [21, 22, 24, 25, 27, 28, 30, 31, 45, 29, 101, 36]
    assert list(map(lambda x: x[1], s)) == ['y', 'c', 'a', 'o', 'H', 'S', 'y', 'a']
    assert list(map(lambda x: x[::-1], s)) == ['nohtyP', 'alacS', 'tpircSavaJ', 'oG', 'PHP', 'prahSC', 'nohtyP', 'lacsaP']


# Тест sorted:

def test_sorted():
    n = [1, 2, 4, 5, 7, 8, 10, 11, 25, 9, 81, 16]
    s = ["Python", "Scala", "JavaScript", "Go", "PHP", "CSharp", "Python", "Pascal"]
    assert list(sorted(n)) == [1, 2, 4, 5, 7, 8, 9, 10, 11, 16, 25, 81]
    assert list(sorted(n, reverse=True)) == [81, 25, 16, 11, 10, 9, 8, 7, 5, 4, 2, 1]
    assert list(sorted(s)) == ['CSharp', 'Go', 'JavaScript', 'PHP', 'Pascal', 'Python', 'Python', 'Scala']
    assert list(sorted(s, key=len)) == ['Go', 'PHP', 'Scala', 'Python', 'CSharp', 'Python', 'Pascal', 'JavaScript']


# Тест math - pi, sqrt, pow, hypot:

# Тест pow:
def test_math_pow():
    assert math.pow(5, 9) == 1953125.0
    assert math.pow(4, 22) == 17592186044416.0
    assert math.pow(2, 6) == 64.0
    assert math.pow(67, 3) == 300763.0

# Тест sqrt:
def test_math_sqrt():
    assert math.sqrt(468) == 21.633307652783937
    assert math.sqrt(527) == 22.956480566497994
    assert math.sqrt(229) == 15.132745950421556
    assert math.sqrt(152) == 12.328828005937952

# Тест hypot:
def test_math_hypot():
    assert math.hypot(5, 10) == 11.180339887498949
    assert math.hypot(3, 6) == 6.708203932499369
    assert math.hypot(4, 9) == 9.848857801796104
    assert math.hypot(8, 3) == 8.54400374531753

# Тест pi:
def test_math_pi():
    assert math.pi == 3.141592653589793