from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class BrowserManager:
    def __init__(self):
        self.driver=webdriver.Chrome(ChromeDriverManager.install())
    def get_driver(self):
        return self.driver()
    def close_browser(self);
        return self.driver.quit()

        