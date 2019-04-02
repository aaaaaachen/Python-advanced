from collections.abc import Iterable,Iterator

print(isinstance([],Iterable))
print(isinstance([],Iterator))


print(isinstance({},Iterable))
print(isinstance({},Iterator))


print(isinstance((),Iterable))
print(isinstance((),Iterator))

list = iter([])
print(isinstance(list,Iterator))