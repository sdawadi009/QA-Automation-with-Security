import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException

class BrowserManager:
    def __init__(self):
        self.driver=self.create_driver()
    @staticmethod
    def create_driver():
        try:
            # Try to use the system-installed ChromeDriver
            print("Trying system-installed ChromeDriver...")
            driver = webdriver.Chrome()
        except WebDriverException:
            # Fall back to using webdriver-manager
            print("System ChromeDriver not found. Using webdriver-manager...")
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
        return driver
    
    def go_to_website(self,url):
        print(f"Going to URL:{url}")
        return self.driver.get(url)
    
    def close_browser(self):
        print ("Closing Browser")
        self.driver.quit()
        print ("Browser Closed")

if __name__ == "__main__":
    browser = BrowserManager()  # Create an object
    browser.go_to_website("https://google.com")
    time.sleep(6)
    browser.close_browser()

