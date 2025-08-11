from urllib.parse import urlparse
from datetime import datetime, timezone

class CookieSimplifier:
    def __init__(self, storage_inspector,site_url):
        self.storage= storage_inspector
        self.site_url = site_url
        self.host = (urlparse(site_url).hostname or "").lower()

    def simplify_all(self):
        simplified_list = []
        for cookie in self.storage.get_cookies():
            simplified_list.append(self._simplify_dict(cookie))
        return simplified_list
    
    def simplify_one(self,name):
        """Simplify a single cookie by name."""
        cookie = self.storage.get_cookie(name)
        if cookie:
            return self._simplify_dict(cookie)
        return None
    
    def _simplify_dict(self, cookie):
        domain = cookie.get("domain", "")
        same_party = self.host.endswith(domain.lstrip(".")) or self.host == domain.lstrip(".")

        expiry = cookie.get("expiry")
        expiry_date = None
        days_left = None
        if expiry:
            expiry_date = datetime.fromtimestamp(int(expiry), tz=timezone.utc).isoformat().replace("+00:00", "Z")
            days_left = max(0, (int(expiry) - int(datetime.now(tz=timezone.utc).timestamp())) // 86400)

        return {
            "name": cookie.get("name"),
            "domain": domain,
            "secure": cookie.get("secure"),
            "httpOnly": cookie.get("httpOnly"),
            "sameSite":cookie.get("sameSite"),
            "persistent": expiry is not None,
            "expiry_date": expiry_date,
            "days_left": days_left,
            "third_party": not same_party
        }
        