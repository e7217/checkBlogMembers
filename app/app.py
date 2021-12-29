import requests
from bs4 import BeautifulSoup
import bs4


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

class Notice:
    def __init__(self, url):
        self.url = url
        pass

    def info(self):
        pass

    def get_bloger(self, tag: bs4.element.Tag):
        name = tag.find("span", attrs={"class":"ell2"}).a.text
        id = tag.find("span", attrs={"class":"ell2"}).a["href"].split("/")[-1]

        return User(name, id)

    def liked_bloger(self):
        res = requests.get(self.url)
        html = BeautifulSoup(res.text, 'html.parser')
        liked_bloger = html.find_all('div', {'class':'bloger'})
        _bloger = []
        for bloger in liked_bloger:
            _bloger.append(self.get_bloger(bloger))
        return _bloger

    def _get_liked_bloger(self):
        pass

class Bloger(User):
    def __init__(self):
        super().__init__()

    def like_list(self):
        pass

    def like_complete_list(self):
        pass


target = Notice("https://blog.naver.com/SympathyHistoryList.naver?blogId=wjdalsry277&logNo=222190961111&layoutWidthClassName=contw-966&currentPage=1")

blogers = target.liked_bloger()

for bloger in blogers:
    print(f"bloger - name : {bloger.name}, id : {bloger.id}")

# with open("index.html", "w", encoding="utf-8") as f:
#     f.write(html.prettify(formmater="html"))