import requests
from bs4 import BeautifulSoup
import bs4

from abc import *


# res = requests.get("https://blog.naver.com/SympathyHistoryList.naver?blogId=wjdalsry277&logNo=222190961111&layoutWidthClassName=contw-966&currentPage=1")

# html = BeautifulSoup(res.text, 'html.parser')
# with open("index.html", "w", encoding='utf-8') as f:
#     f.write(html.prettify(formatter='html'))
# print(html)

class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def link(self):
        return "https://blog.naver.com/" + self.id

class Notice(metaclass = ABCMeta):
    def __init__(self, url):
        self.url = url
        pass

    def info(self):
        pass

    @abstractmethod
    def get_bloger(self, tag: bs4.element.Tag):
        pass

    @abstractmethod
    def like(self):
        pass


    @abstractmethod
    def _get_liked_bloger(self):
        pass

class Blog(Notice):

    def get_bloger(self, tag: bs4.element.Tag):
        # return super().get_bloger(tag)
        try:
            name = tag.find("span", attrs={"class":"ell2"}).a.text
            id = tag.find("span", attrs={"class":"ell2"}).a["href"].split("/")[-1]
        except AttributeError as e:
            print(e)
            name = None
            id = None
            
        return User(name, id)

    def like(self):
        # return super().like()
        res = requests.get(self.url)
        html = BeautifulSoup(res.text, 'html.parser')
        liked_bloger = html.find_all('div', {'class':'bloger'})
        _bloger = []
        for bloger in liked_bloger:
            _bloger.append(self.get_bloger(bloger))
        return _bloger

    ...

class Post(Notice):
    ...

class Bloger(User):
    def __init__(self):
        super().__init__()

    def like_list(self):
        pass

    def like_complete_list(self):
        pass

_ = []
for i in range(1, 10):
    print("i : ", i)
    target = Notice(f"https://blog.naver.com/SympathyHistoryList.naver?blogId=wjdalsry277&logNo=222190961111&layoutWidthClassName=contw-966&currentPage={i}")

    blogers = target.like()

    for key, bloger in enumerate(blogers):
        print(f"[{key}] bloger - name : {bloger.name}, id : {bloger.id}")
        _.append(bloger)
    if len(blogers) < 60:
        break

print(_)
print("length : ", len(_))

# with open("index.html", "w", encoding="utf-8") as f:
#     f.write(html.prettify(formmater="html"))