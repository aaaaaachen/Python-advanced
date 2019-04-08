import re

a = "hello world\nhelloworld"
pat = re.compile('.',re.S)
print(a)
res = pat.findall(a)
print(res)

result = re.findall("e$","abcde\nabcde",re.M)
print(result)

res = pat.findall(a)
