# ShoutOut to everyone program:
# import pyttsx3

# engine = pyttsx3.init()
# names = ["DhruvRaj Gupta", "Suryansh Singh", "Rajat","Salman Khan","Harry Bhai "]

# for name in names:
#     print(f"Shoutout to {name}!")
#     engine.say(f"Shoutout to {name}")
#     engine.runAndWait()

# Requests Module:
# import requests
# r = requests.get("https://www.youtube.com")
# print(r.text)
# with open ("Day-26/youtube.html",'w',encoding='utf-8') as f:
#     f.write(r.text)
# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
# print(r.status_code)
# print(r.headers['content-type'])
# print(r.encoding)
# print(r.text)
# print(r.json())
# r = requests.post("https://httpbin.org/post", data={'Rajat':'value'})
# print(r.text)
# # POST REQUESTS
# data = {
#     "username": "rajat",
#     "password": "1234"
# }

# response = requests.post("https://httpbin.org/post", data=data)
# print(response.status_code)
# print(response.json()) 
# PUT REQUEST
# r = requests.put("https://httpbin.org/put",data = {"a":10,"b":20})
# print(r.text)
# print(r.json())
# r = requests.delete("https://httpbin.org/delete")
# r = requests.head("https://httpbin.org/get") # For headers only(no body)
# r = requests.options("https://httpbin.org/get") #Supported methods and headers

# Downloading images:
import requests
from PIL import Image # PIL-python image library
from io import BytesIO

r = requests.get("https://www.pixelstalk.net/wp-content/uploads/2016/07/Desktop-hd-3d-nature-images-download.jpg")
i = Image.open(BytesIO(r.content))
fp = open("Day-26/img.jpg",'wb')
i.save(fp)
fp.close()

r = requests.get("https://tse3.mm.bing.net/th/id/OIP.IjGQ6GgPX1y0PuEXMRbotwAAAA?r=0&w=474&h=266&rs=1&pid=ImgDetMain&o=7&rm=3")
i = Image.open(BytesIO(r.content))
fp = open("Day-26/favorite.jpg",'wb')
i.save(fp)
fp.close()



