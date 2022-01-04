import requests
from bs4 import BeautifulSoup
import bs4

from abc import *
from modules.notice import Crawler

from modules.notice import Blog, Post
from modules.user import Bloger


# target = Blog(f"http://m.search.naver.com/search.naver?where=m_view&sm=mtb_jum&query=대구+보건소+코로나검사+무료&url=https://m.blog.naver.com/assa9370/222190726272")
target = Crawler(Post("https://m.post.naver.com/viewer/postView.nhn?volumeNo=30412957"))
like = target.like()
print(like)
