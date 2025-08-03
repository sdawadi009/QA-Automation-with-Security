class StorageInspector:
    def __init__(self):
        self.driver=driver

    def open_url(self, url):
        self.driver.get(url)

    def get_local_storage(self):
        return self.driver.execute_script("return{...localStorage};")
    
    def get_session_storage(self):
        return self.driver.execute_script("return{...sessionStorage};")
    
    def get_cookies(self):
        return self.driver.get_cookies()

