from abc import abstractmethod
import unicodedata

from bs4 import BeautifulSoup
import bs4
import requests
from selenium.webdriver.remote.webelement import WebElement

from modules.base import NoticeBase
from modules.user import User
from modules.utils import ChromeBrowser


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

    def __init__(self, url):
        super().__init__(url)
        self.crawler = ChromeBrowser()

    def get_bloger(self, element: WebElement):
        try:
            user_name = element.find_element_by_tag_name("em").text
            user_id = None
            # user_id = element.find("span", attrs={"class":"ell2"}).a["href"].split("/")[-1]
        except AttributeError as e:
            print(e)
            user_name = None
            user_id = None
            
        return User(user_name, user_id)

    def _get_like_count(self):
        likers = self.crawler.driver.find_elements_by_xpath("//*[@id='cont']/div[1]/div/div/ul/li")
        return likers

    def like_in_page(self, url):

        self.crawler.driver.get(url)      
        likers = self._get_like_count()

        _bloger = []
        for bloger in likers:
            _bloger.append(self.get_bloger(bloger))
        return _bloger

    def like_total(self):
        page_num = 1
        like_total = []
        count_pre = 0
        while 1:
            like_list = self.like_in_page(self.like_url() + f'&fromNo={page_num}')
            count_current = len(like_list)
            if count_current <= count_pre:
                break
            if not like_list:
                break
            else: 
                like_total = like_list
                count_pre = len(like_list)
                page_num += 1
        return like_total