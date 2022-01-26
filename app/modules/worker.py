from abc import abstractmethod
import unicodedata
import time

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

    def like_in_page(self):

        likers = self._get_like_count()

        _bloger = [self.get_bloger(liker) for liker in likers]
        return _bloger

    def scroll_bottom(self):
        last_height=0
        while True:
            self.crawler.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # 1초 대기
            time.sleep(1)

            # 스크롤 다운 후 스크롤 높이 다시 가져옴
            new_height = self.crawler.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def like_total(self):
        self.crawler.driver.get(self.like_url())
        self.scroll_bottom()
        likers = self.like_in_page()
        # page_num = 1
        # like_total = []
        # count_pre = 0
        # while 1:
        #     # 타임 스탬프를 같이 넣어주거나 스크롤 동작으로 유저 리스트를 완성시켜야 함
        #     like_list = self.like_in_page(self.like_url() + f'&fromNo={page_num}')
        #     count_current = len(like_list)
        #     if count_current <= count_pre:
        #         break
        #     if not like_list:
        #         break
        #     else: 
        #         like_total = like_list
        #         count_pre = len(like_list)
        #         page_num += 1
        like_total = likers
        return like_total