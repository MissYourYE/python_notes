# -*- coding: utf-8 -*-

# 通过列表生成式，我们以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，
# 不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
#
# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。


# # 只要把一个列表生成式的[]改成()，就创建了一个generator：
# # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# l = [x * x for x in range(10)]
# print(l)
#
# # <generator object <genexpr> at 0x107b8da98>
# g = (x * x for x in range(10))
# print(g)
#
# # 调用next(g)，就计算出g的下一个元素的值
# # 0
# print(next(g))
# # 1
# print(next(g))
# # 4
# print(next(g))
# # 9
# print(next(g))
# # 生成器也是可迭代对象
# for x in g:
#     print(x)

# # 用函数实现
# # 著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
#
# # 1
# # 1
# # 2
# # 3
# # 5
# # 8
# # done
# print(fib(6))
#
# # 改成generator
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
#
# # 1
# # 1
# # 2
# # 3
# # 5
# # 8
# for m in fib(6):
#     print(m)

# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
# 再次执行时从上次返回的yield语句处继续执行。
def odd():
    print('step1')
    yield 1
    print('step2')
    yield 2
    print('step3')
    yield 3


o = odd()
# step1
# 1
# step2
# 2
# step3
# 3
for i in o:
    print(i)
