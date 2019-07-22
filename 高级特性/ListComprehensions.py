# -*- coding: utf-8 -*-


# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
# 要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(1, 11)))

# 生成[1x1, 2x2, 3x3, ..., 10x10]
# 方法一循环：
l = []
for x in list(range(1, 11)):
    l.append(x * x)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(l)

# 方法二
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([x * x for x in list(range(1, 11))])

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
# [4, 16, 36, 64, 100]
print([x * x for x in list(range(1, 11)) if x % 2 == 0])

# 使用两层循环，可以生成全排列：
# ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
print([m + n for m in 'ABC' for n in 'XYZ'])

# 列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os

# ['ListComprehensions.py', 'Slice.py', 'Iterration.py']
print([d for d in os.listdir('.')])
