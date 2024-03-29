from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

class BrowserSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(BrowserSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class ChromeBrowser(metaclass=BrowserSingleton):
    
    def __init__(self) -> None:
        self.initialize()

    def initialize(self):
        options = Options()
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.wait = WebDriverWait(self.driver, 20)

class router:

    def __init__(self, url):
        self.url = url
    
    def get_object():
        if 
        
