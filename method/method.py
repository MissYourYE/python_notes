# -*- coding: utf-8 -*-


# python定义函数的方式:
# def methodName (param1,param2,...):
def my_abs(a):
    if not isinstance(a, (int, float)):
        raise TypeError('参数类型错误')
    if a < 0:
        a = -a
    return a


# print(my_abs(''))


# 空函数
def nop():
    pass


# print(nop())


# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# # 9
# print(power(3))
#
#
# def registered(name, age, sex='n', city='bj'):
#     return name, age, sex, city
#
#
# # ('dubm', '25', 'n', 'bj')
# print(registered('dubm', '25'))
# # ('dubm', '25', 'n', 'hb')
# print(registered('dubm', '25', city='hb'))
#
#
# # 坑点：
# def append_end(L=[]):
#     L.append('END')
#     return L
#
#
# # ['END']
# print(append_end())
# # ['END', 'END']
# print(append_end())
# # ['END', 'END', 'END']
# print(append_end())
#
#
# # Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
# # 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# # 定义默认参数要牢记一点：默认参数必须指向不变对象！
#
# def append_end(l=None):
#     if l is None:
#         l = []
#     l.append('END')
#     return l
#
#
# # ['END']
# print(append_end())
# # ['END']
# print(append_end())
# # ['END']
# print(append_end())


# 可变参数
# 给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。
# 参数前面加一个*号
def calc(*numbers):
    s = 0
    for n in numbers:
        s = s + n * n
    return s


# # 5
# print(calc(1, 2))
# # 30
# print(calc(1, 2, 3, 4))
#
# # 将一个已存在的List或者tuple作为可变参数
# # 可在List或者tuple前加*
# a = [1, 2, 3, 4]
#
# # 30
# print(calc(*a))


# 关键字参数
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


# # name: zs age: 18 other: {'city': 'beijing'}
# person('zs', '18', city='beijing')
# # name: zs age: 18 other: {'city': 'beijing', 'sex': 'n'}
# person('zs', '18', city='beijing', sex='n')
# # 简化写法
# extra = {'city': 'beijing', 'sex': 'n'}
# # name: zs age: 20 other: {'city': 'beijing', 'sex': 'n'}
# person('zs', '20', **extra)


# 命名关键字参数
def student(name, age, *, city, job):
    print(name, age, city, job)


# zs 18 beijing code
# student('zs',18,city='beijing',job='code')


# 递归函数
# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
# 举个例子，我们来计算阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示，可以看出：
# fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n
# 所以，fact(n)可以表示为n x fact(n-1)，只有n=1时需要特殊处理。
# 于是，fact(n)用递归的方式写出来就是：
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


# 使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
# 针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。
# Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。
# 24
print(fact(4))


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


# 6
print(fact_iter(3, 1))
