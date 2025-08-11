from browser_manager import BrowserManager

#setup the browser
browser = BrowserManager()
driver=browser.get_driver()

#Go to page
driver.get("https://google.com")