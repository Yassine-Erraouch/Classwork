import re



# my custom  errors
class DomaineExistantException(Exception): # error for when a domaine already eixsts
    def __init__(self, message):
        super().__init__(message)
        self.message = "Domaine already exists"

class DomaineInexistantException(Exception): # error for when a domaine doesn't exist
    def __init__(self, message):
        super().__init__(message)
        self.message = "Domaine doesn't exist"
        
class FormatInvalideException(Exception): #error for when domaine or ip format is invalid
    def __init__(self, message):
        super().__init__(message)
        self.message = "Domaine or IP format is invalid"

# regular expressions for domaine and ip

domaine_regex = r'^[a-zA-Z0-9][a-zA-Z0-9-]{0,61}[a-zA-Z0-9]\.[a-zA-Z]{2,}$'
ip_regex = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'

class DNS:
    domaines = {
    "google.com": "216.58.194.174",
    "facebook.com": "157.240.2.35",
    "amazon.com": "54.239.28.85",
    "youtube.com": "216.58.194.174",
    "wikipedia.org": "208.80.154.224",
    "twitter.com": "104.244.42.129",
    "instagram.com": "157.240.2.35",
    "reddit.com": "151.101.1.140",
    "github.com": "192.30.253.112",
    "stackoverflow.com": "151.101.1.69"
}
    
    cache = []
    def validate_format(domaine=str, ip=str):
        if not re.match(domaine_regex, domaine):
            raise FormatInvalideException()
        if not re.match(ip_regex, ip):
            raise FormatInvalideException()
    def add_domaine(self, domaine=str, ip=str):
        self.validate_format(domaine, ip)
        if domaine in DNS.domaines:
            raise DomaineExistantException()
        else:
            DNS.domaines[domaine] = ip
            DNS.cache.append(f'added {domaine} with IP: {ip}')
            
    def find_ip(self, domaine=str):
        self.validate_format(domaine)
        if domaine in DNS.domaines:
            return DNS.domaines[domaine]
        else:
            raise DomaineInexistantException()
        
    def update_domaine(self,domaine=str, new_ip=str):
        self.validate_format(domaine, new_ip)
        if domaine in DNS.domaines:
            DNS.domaines[domaine] = new_ip
            DNS.cache.append(f"updated {domaine} with new IP: {new_ip}")
        else:
            raise DomaineInexistantException()
        
    def remove_domaine(self, domaine=str):
        self.validate_format(domaine)
        if domaine in DNS.domaines:
            del DNS.domaines[domaine]
            DNS.cache.append(f"removed {domaine} with IP: {DNS.domaines[domaine]}")
        else:
            raise DomaineInexistantException()
        
    def show_cache():
        print("DNS cache:")
        for i in DNS.cache:
            print(i)
    
    def show_domaines(cls):
        for i in cls.domaines:
            print(i)
            
            
ip = DNS()

