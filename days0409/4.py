import requests


response = requests.get("https://imgsa.baidu.com/news/q%3D100/sign=d87a6c4a3bfae6cd0ab4af613fb20f9e/b21c8701a18b87d6682e2662090828381f30fd5b.jpg")


# res = "https://imgsa.baidu.com/news/q%3D100/sign=d87a6c4a3bfae6cd0ab4af613fb20f9e/b21c8701a18b87d6682e2662090828381f30fd5b.jpg"

with open("img/data.jpg","wb") as file:
    file.write(response.content)


with open("data.jpg","rb") as file:
    print(file.read())

# with open(str(response.content)+".jpg",'rb') as file1:
#     with open('image/','wb') as file2:
#         file2.write(file1.read())