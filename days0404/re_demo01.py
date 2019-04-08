import re


a = "hello world hello word"

# match 开头匹配
# res = re.match("l",a)
# fullmatch 完全匹配
# res = re.fullmatch("hello world",a)

# 扫描目标字符串 匹配对应字符串
# res = re.search('e',a)

# 查找目标字符串中所要匹配的字符串 返回列表
# res = re.findall("l",a)

# 将字符串以对应字符串分割 返回列表
# res = re.split('e',a)

# 将目标字符串中的匹配字串替换 后边可以跟替换次数 flags
# res = re.sub('e',"w",a,1)

# 将匹配到的字符串以迭代器的方式返回
# res = re.finditer('ll',a)
# for r in res:
#     print(r.group())

res = re.compile('hell')
print(res,type(res))

result = res.search(a)
# result = res.sub("www",a)
# result = res.findall(a)
# result = res.match(a)
# result = res.finditer(a)
print(result)
print(result.group())
# for r in result:
#     print(r.group())

#
# print(res,type(res))
# if res:
#     if isinstance(res,re.Match):
#         print(res.group())
#     else:
#         for r in res:
#             print(r)

