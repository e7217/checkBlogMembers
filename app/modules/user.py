from typing import Optional


class User:
    def __init__(self, name: Optional[str], id: Optional[str]):
        self.name = name
        self.id = id

    def link(self):
        return "https://blog.naver.com/" + self.id

class Bloger(User):
    def __init__(self):
        super().__init__()

    def like_list(self):
        pass

    def like_complete_list(self):
        pass
