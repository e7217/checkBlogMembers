from abc import abstractmethod
import unicodedata

from bs4 import BeautifulSoup
import bs4
import requests

from modules.base import NoticeBase
from modules.user import User


class NoticeWorker(NoticeBase):

    @abstractmethod
    def get_bloger(self):
        ...

    @abstractmethod
    def like_total(self):
        ...

class BlogWorker(NoticeWorker):

    def get_bloger(self, tag: bs4.element.Tag):
        try:
            user_name = tag.find("span", attrs={"class":"ell2"}).a.text
            user_id = tag.find("span", attrs={"class":"ell2"}).a["href"].split("/")[-1]
        except AttributeError as e:
            print(e)
            user_name = None
            user_id = None
            
        return User(user_name, user_id)

    def like_in_page(self, url):
        res = requests.get(url)
        html = BeautifulSoup(res.text, 'html.parser')
        liked_bloger = html.find_all('div', {'class':'bloger'})
        _bloger = []
        for bloger in liked_bloger:
            _bloger.append(self.get_bloger(bloger))
        return _bloger

    def like_total(self):
        page_num = 1
        like_total = []
        while 1:
            like_list = self.like_in_page(self.like_url() + f'&currentPage={page_num}')
            if not like_list:
                break
            else: 
                like_total += like_list
                page_num += 1
        return like_total

class PostWorker(NoticeWorker):

    def get_bloger(self, tag: bs4.element.Tag):
        try:
            user_name = tag.find("span", attrs={"class":"ell2"}).a.text
            user_id = tag.find("span", attrs={"class":"ell2"}).a["href"].split("/")[-1]
        except AttributeError as e:
            print(e)
            user_name = None
            user_id = None
            
        return User(user_name, user_id)

    def _get_like_count(self, html):
        content = html.find('div',{"class":"cont_header_inner"}).find('h2')
        content_unicode = unicodedata.normalize('NFKD', content.get_text())
        count = content_unicode.split(' ')[-1]
        return count

    def like_in_page(self, url):
        res = requests.get(url)
        html = BeautifulSoup(res.text, 'html.parser')
        like_count = self._get_like_count(html)
        liked_bloger = html.find_all('div', {'class':'bloger'})
        if not int(like_count) <= len(html.find_all('li', {"class":"user_info_item"})):
            return False
        return liked_bloger
            

        _bloger = []
        for bloger in liked_bloger:
            _bloger.append(self.get_bloger(bloger))
        return _bloger

    def like_total(self):
        page_num = 1
        like_total = []
        while 1:
            like_list = self.like_in_page(self.like_url() + f'&fromNo={page_num}')
            if not like_list:
                page_num += 1
                continue
            else: 
                like_total += like_list
        return like_total