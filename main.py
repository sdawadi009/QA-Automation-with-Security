import time
from checkingbrowser import BrowserManager
from storage_inspector import StorageInspector
from cookie_simplifier import CookieSimplifier
from simplecookiechecker import SimpleCookieChecker
from config import CONFIG

if __name__ == "__main__":
    url = CONFIG["url"]
    browser =BrowserManager()

    browser.go_to_website(url)
    time.sleep(5)

    storage =StorageInspector(browser.driver)

    cookie_simplify = CookieSimplifier(storage,url)

    print("All simplfied cookies:")
    for c in cookie_simplify.simplify_all():
        print(c)
    
    checker = SimpleCookieChecker(cookie_simplify, url)

    checker.check_secure_flag()
    ##print("Get cookies:", storage.get_cookies())

    ##print("Initial local sotrage:", storage.get_local_storage_items())





