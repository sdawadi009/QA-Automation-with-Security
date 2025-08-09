class StorageInspector:
    def __init__(self,driver):
        self.driver=driver

    def get_cookies(self):
        return self.driver.get_cookies() ##This returns all the cookies present 
    
    def get_cookie(self,name):
        return self.driver.get_cookie(name) ##This is specific to the cookie name , eg: session Id;
    
    def set_cookies(self,name,value,**kwargs):    ##This is for security testing purpose to add extra details in the cookies
        cookie ={"name":name,"value":value}
        cookie.updated(kwargs)
        self.drvier.add_cookie(cookie)
    
    def delete_cookie(self,name):
        self.driver.delete_cookie(name)

    def delete_all_cookies(self):
        self.driver.delete_all_cookies()

    ##--This is for the Local Storage

    def get_local_storage_items(self):
      ##  script = "return{...localStorage};"
      ##  return self.driver.execute_script(script)

      script = """
      const items = {};
      for (let i=0; i<window.localStorage.length; i++){
        const k = window.localStorage.key(i);
        items[k]= window.localStorage.getItem(k);
      }
      return items;
      """
      return self.driver.execute_script(script)

    def get_local_storage_item(self,key):
        return self.driver.execute_scrpit("return window.localStorage.getItem(arguments[0]);",key
         )
    
    def clear_local_storage_item(self):
        self.driver.execute_script("window.localStorage.clear();")

    
