import requests
from bs4 import BeautifulSoup
import bs4
import re

from abc import *
from modules.user import User


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
    def like_url(self):
        pass

    # @abstractmethod
    # def _get_liked_bloger(self):
    #     pass

class Blog(Notice):

    def get_bloger(self, tag: bs4.element.Tag):
        # return super().get_bloger(tag)
        try:
            user_name = tag.find("span", attrs={"class":"ell2"}).a.text
            user_id = tag.find("span", attrs={"class":"ell2"}).a["href"].split("/")[-1]
        except AttributeError as e:
            print(e)
            user_name = None
            user_id = None
            
        return User(user_name, user_id)

    def like_url(self):
        res = requests.get(self.url)
        match = re.search("naver.com/[a-zA-Z0-9]+/[0-9]+", res.text)
        match = match.group().split('/')
        user_id, blog_id = match[-2], match[-1]
        return user_id, blog_id

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

    def get_bloger(self, tag: bs4.element.Tag):
        ...
    
    def like(self):
        ...