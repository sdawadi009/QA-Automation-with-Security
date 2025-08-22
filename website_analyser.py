from checkingbrowser import BrowserManager
from storage_inspector import StorageInspector
from cookie_simplifier import CookieSimplifier
from simplecookiechecker import SimpleCookieChecker
from config import CONFIG

class WebsiteAnalyser:

    """ Simple facade for website compliance analysis """

    def __init__(self, url =None):
        self.url = url or CONFIG["url"]

    def analyse(self):
        self.browser=BrowserManager()
        self.browser.go_to_website(self.url)

        storage = StorageInspector(self.browser.driver)
        cookie_simplify = CookieSimplifier(storage, self.url)
        self.checker = SimpleCookieChecker(cookie_simplify, self.url)

        for c in cookie_simplify.simplify_all():
            print(c)

        self.checker.check_secure_flag()
        self.checker.check_data_retention()
        self.checker.check_httponly_flag()
        self.checker.check_same_site_attribure()

        print("All simplfied cookies:")

        return self.checker.print_summary()
    