import re


# res = '123hell \nstudent stu Stu'
#
# pat = re.compile("[^0-3]stu")
# result = pat.findall(res)
# print(result)



# res = re.findall(".*","hwwwgloheezhhhhwhefffheddhe")
# print(res)
#
#
# result = re.findall("hi?", "hi china hello chiina")
# print(result)
#
#
# result = re.findall(r"\bhello\b", "hello world \nhello zhengzhou",re.M)
# print("\bhello world \nhello zhengzhou")
# print(result)

result = re.findall(r"\bhello\b|\bworld\b|\bhi\b", "hello world hi world")
print(result)

retsult = re.match(r".*?@.*?.com", "496575233@qq.com")
print(retsult.group())
retsult = re.match(r"(.*?)@(.*?)(.com)", "496575233@qq.com")
print(retsult.group(), retsult.group(1), retsult.group(2), retsult.group(3))

result = re.search(r'(he).*?h',"hello world hello world")
print(result.group(),"sss",result.group(1))


result = re.match(r"(?P<hname>hello) .*? \1", "hello world hello china")
print(result.group(), result.group("hname"))

