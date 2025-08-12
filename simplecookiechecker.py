class SimpleCookieChecker:
    def __init__(self,cookie_simplifier,website_url):
        self.cookie_simplifier=cookie_simplifier
        self.website_url=website_url
        self.issues_found=[]

    def check_secure_flag(self):
        ## This function checks if the secure flag is set or not, GDPR article 32 
         print ("Gettinf cookies from the browser ...")

         cookies_list =self.cookie_simplifier.simplify_all()

         print(f"Found {len(cookies_list)} cookies")
         print("Checking for the secure flag for GDPR compliance ...")

         for cookie in cookies_list:
             
             cookie_name = cookie.get('name','Unknown')
             secure = bool(cookie.get('secure', False))
             
             if secure:
                 print(f" {cookie_name} : Secure Flag is set")
             else:
                print(f"{cookie_name}: Secure Flas is missing")
                self.issues_found.append({
                    'cookie': cookie_name,
                    'issue': 'Missing SECURE flag',
                    'Standard': 'GDPR Article 32',
                    'risk': 'Data can be intercepted over HTTP'
                })
         return self.issues_found

    def print_summary(self):
        """This prints the summary of the finding"""

        total_issues = len(self.issues_found)

        print(f"\n Summary for {self.website_url} :")
        print(f"Issues found: {total_issues}")

        if total_issues>0:
            print(f"\n Issues:")
            for issue in self.issues_found:
                print(f"  - {issue['cookie']}: {issue['issue']}")
            
        else:
            print("All issues have proper security")
