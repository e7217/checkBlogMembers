from abc import abstractmethod
from bs4 import BeautifulSoup

import requests
import re

from modules.base import NoticeBase

class NoticeInfo(NoticeBase):

    @abstractmethod
    def like_url_param(self):
        ...

    @abstractmethod
    def like_url(self):
        ...

class BlogInfo(NoticeInfo):

    def like_url_param(self):
        res = requests.get(self.url)
        match = re.search("naver.com/[a-zA-Z0-9]+/[0-9]+", res.text)
        match = match.group().split('/')
        user_id, blog_id = match[-2], match[-1]
        return user_id, blog_id

    
    def like_url(self):
        user_id, blog_id = self.like_url_param()
        return f"https://blog.naver.com/SympathyHistoryList.naver?blogId={user_id}&logNo={blog_id}&layoutWidthClassName=contw-966"

class PostInfo(NoticeInfo):

    def like_url_param(self):
        res = requests.get(self.url)
        html = BeautifulSoup(res.text, 'html.parser')
        member_no = html.find('meta', {'property':'nv:news:author_no'}).get('content')
        volume_no = html.find('meta', {'property':'nv:news:volume_no'}).get('content')        
        return member_no, volume_no


    def like_url(self):
        member_no, volume_no = self.like_url_param()
        return f"https://m.post.naver.com/like/likeMembers.naver?volumeMemberNo={member_no}&volumeNo={volume_no}"
