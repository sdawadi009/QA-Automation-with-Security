class SimpleCookieChecker:
    def __init__(self,cookie_simplifier,website_url):
        self.cookie_simplifier=cookie_simplifier
        self.website_url=website_url
        self.issues_found=[]

        self.tracking_cookies = {
            '_ga', '_ga_', '_gid', '_fbp', '_gcl_au', 'permutive-id',
            '_pubcid', 'blaize_tracking_id', '__gads', '__gpi'
        }

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
         print (self.issues_found)
         return self.issues_found
    
    def check_tracking_consent(self):
        print("\n Checking tracking cookies")
        cookies_list =self.cookie_simplifier.simplify_all()

        for cookie in cookies_list:
            cookie_name =cookie.get('name','Unknown')

            if self.is_tracking_cookie(cookie_name):
                print(f" {cookie_name}: Tracking cookie requires consent")
                self.issues_found.append({
                    'cookie':cookie_name,
                    'issue': ' Tracking cookie without consent',
                    'risk': ' Processing personal data without legal basis',    
                })
            
            else:
                print(f"{cookie_name}: Not a tracking cookie")
        return self.issues_found
    
    def check_data_retention(self):
        """GDPR Article 5(1)(c): Data Minimisation"""
        print("\n Checking retention period for GDPR compliance...")
        cookies_list = self.cookie_simplifier.simplify_all()

        for cookie in cookies_list:
            cookie_name = cookie.get('name','Unknown')
            days_left = cookie.get('days_left')

            if days_left is None:
                print(f"{cookie_name}: Session cookie (expires when browser closes)")
            elif days_left > 365:
                print(f"{cookie_name}: Expires in {days_left} days (exceeds 1 year)")

                self.issues_found.append({
                    'cookie':cookie_name,
                    'issue': ' Tracking cookie without consent',
                    'risk': ' Violates data minimisation principle',    
                })
            else: 
                print(f"{cookie_name}: Expires in {days_left} days ")
            
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
