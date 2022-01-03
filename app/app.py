import requests
from bs4 import BeautifulSoup
import bs4

from abc import *

from modules.notice import Blog, Post
from modules.user import Bloger


# res = requests.get("https://blog.naver.com/SympathyHistoryList.naver?blogId=wjdalsry277&logNo=222190961111&layoutWidthClassName=contw-966&currentPage=1")

# html = BeautifulSoup(res.text, 'html.parser')
# with open("index.html", "w", encoding='utf-8') as f:
#     f.write(html.prettify(formatter='html'))
# print(html)


# _ = []
# for i in range(1, 10):
#     print("i : ", i)
#     target = Blog(f"https://blog.naver.com/SympathyHistoryList.naver?blogId=wjdalsry277&logNo=222190961111&layoutWidthClassName=contw-966&currentPage={i}")

#     blogers = target.like()

#     for key, bloger in enumerate(blogers):
#         print(f"[{key}] bloger - name : {bloger.name}, id : {bloger.id}")
#         _.append(bloger)
#     if len(blogers) < 60:
#         break

target = Blog(f"http://m.search.naver.com/search.naver?where=m_view&sm=mtb_jum&query=대구+보건소+코로나검사+무료&url=https://m.blog.naver.com/assa9370/222190726272")
like_url = target.like_url()
print(like_url)

print(_)
print("length : ", len(_))

# with open("index.html", "w", encoding="utf-8") as f:
#     f.write(html.prettify(formmater="html"))