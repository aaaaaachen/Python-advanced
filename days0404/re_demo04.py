import requests,re

response = requests.get('http://quote.stockstar.com/stock/ranklist_a_3_1_1.html')
# print(response.text)

# res = '<a.*?href=//stock.quote.*?>.*?</a>'
urls = re.findall(r'<a.*?href=.*?stockstar.com/(\d{6}).*?shtml.*?>(\D*?)</a>',response.text,re.M)
for u in urls:
    print(u)
# urls = re.findall(r'<a.*?href=.*?stockstar.com/[0-9][0-9][0-9][0-9][0-9][0-9].*?shtml.*?>.*?</a>',response.text)
# print(urls)


urls = re.findall(r"<span.*?red.*?>(.*?)</span>",response.text)
print(urls)
