
from abc import ABCMeta

class NoticeBase(metaclass = ABCMeta):
    def __init__(self, url):
        self.url = url
