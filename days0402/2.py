from collections.abc import Iterator,Iterable

# 判断列表是否可迭代，是否是迭代器
l = []
print(type(l))
print("list can Iterable?",isinstance(l,Iterable))
print("list is Iterator?",isinstance(l,Iterator))


# 判断元组是否可迭代，是否是迭代器
a = tuple()
print(type(a))
print("tuple can Iterable?",isinstance(a,Iterable))
print("tuple is Iterator?",isinstance(a,Iterator))

# 判断字典是否可迭代，是否是迭代器
b = dict()
print(type(b))
print("dict can Iterable?",isinstance(b,Iterable))
print("dict is Iterator?",isinstance(b,Iterator))

# 判断字符串是否可迭代，是否是迭代器
c = "achen"
print(type(c))
print("str can Iterable?",isinstance(c,Iterable))
print("str is Iterator?",isinstance(c,Iterator))

# 判断整形是否可迭代，是否是迭代器
d = 100
print(type(d))
print("Intager can Iterable?",isinstance(d,Iterable))
print("Intager is Iterator?",isinstance(d,Iterator))