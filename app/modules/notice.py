from modules.info import BlogInfo, PostInfo
from modules.worker import BlogWorker, PostWorker
from modules.base import NoticeBase

class Blog(BlogWorker, BlogInfo):
    ...

class Post(PostWorker, PostInfo):
    ...

class Crawler:

    def __init__(self, notice: NoticeBase):
        self.notice = notice
    
    def like(self):
        return self.notice.like_total()
