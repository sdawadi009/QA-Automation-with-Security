import time
from checkingbrowser import BrowserManager
from storage_inspector import StorageInspector

if __name__ == "__main__":
    browser =BrowserManager()

    browser.go_to_website("https://google.com")
    time.sleep(5)

    storage =StorageInspector(browser.driver)

    print("Get cookies:", storage.get_cookies())

    print("Initial local sotrage:", storage.get_local_storage_items())





