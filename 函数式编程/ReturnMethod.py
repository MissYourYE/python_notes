# -*- coding: utf-8 -*-
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。


# 定义一个求和函数
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


# 如果不需要立即求和，而是在后面的代码中在需要的时候再进行求和，可以返回求和的函数
def lazy_sum(*args):
    def cal_sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return cal_sum


f = lazy_sum(1, 2, 3, 4)
# <function lazy_sum.<locals>.calc_sum at 0x1086c5400>
print(f)
# 调用f函数时，才进行计算
# lazy_sum(1, 2, 3, 4)
# 10
print(f())

# 我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，
# 相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
# 注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1, 2, 3, 4)
f2 = lazy_sum(1, 2, 3, 4)
# False
print(f1 == f2)


# 闭包
# 注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，
# 其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
# 另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。我们来看一个例子：
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


m1, m2, m3 = count()
# 9
print(m1())
# 9
print(m2())
# 9
print(m3())


# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
