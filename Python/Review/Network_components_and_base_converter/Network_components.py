from abc import ABC, abstractmethod
import re

# creating the abstract method NetworkComponent
class NetworkComponent(ABC):
    def info():
        pass
    
    def function():
        return f"The network component serves a function ¯\_(ツ)_/¯"
    

# creating the child class IPv4
class IPv4(NetworkComponent):
    def __init__(self, adress):
        if self.isValidIPv4(adress):
            self.adress = adress
        else:
            return f"{adress} is not a valid IPv4 address"
    
    def isValidIPv4(self, adress):
        if not re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", adress):
            return False
        segments = adress.split(".")
        for segment in segments:
            if not 0 <= int(segment) <= 255:
                return False
        return True
    
    def getClass(self):
        first_section = int(self.adress.split(".")[0])
       
        if first_section in range(1,128):
            return "A"
        elif first_section in range(128,192):
            return "B"
        elif first_section in range(192,224):
            return "C"
        elif first_section in range(224, 239):
            return "D"
        else:
            return "E"
    
    def getMask(self):
        mask = ""
        if self.getClass() == "A":
            mask = "255.0.0.0"
        elif self.getClass() == "B":
            mask = "255.255.0.0"
        elif self.getClass() == "C":
            mask = "255.255.255.0"
        else: 
            return f"{self.getClass} Adresses don't use masks"
        return mask
    
    def getNetworkId(self):
        # mask = self.getMask().split(".")
        ip = self.adress.split(".")
        networkClass = self.getClass()
        if networkClass == "A":
            return f"{ip[0]}.0.0.0"
        elif networkClass == "B":
            return f"{ip[0]}.{ip[1]}.0.0"
        elif networkClass == "C":
            return f"{ip[0]}.{ip[1]}.{ip[2]}.0"
    
    def getHost(self):
        mask = self.getMask().split(".")
        ip = self.adress.split(".")
        networkClass = self.getClass()
        if networkClass == "A":
            return f"{ip[1]}.{ip[2]}.{ip[3]}"
        elif networkClass == "B":
            return f"{ip[2]}.{ip[3]}"
        elif networkClass == "C":
            return f"{ip[3]}"
        
    def getNofHosts(self):
        host = self.getHost().split(".") # [***.***.***]
        bits = len(host)*8
        maxHosts = 2**bits -2
        return maxHosts
            
    def info(self):
        return f"IP: {self.adress} , Class: {self.getClass()} , Subnet Mask: {self.getMask()} , Network ID: {self.getNetworkId()} , Host: {self.getHost()} , Number of Hosts: {self.getNofHosts()}"
    
    def function(self):
        return f"The IP adress gives us a unique identifier for the device"
class DNS(NetworkComponent):
    def __init__(self):
        self.index = dict()
        self.cache = dict()
    
    def addToIndex(self, domain, ip):
        self.index[domain] = ip
        # we also add to cache
        self.cache[domain] = ip
    
    def removeFromIndex(self, domain):
        if domain in self.index:
            del self.index[domain]
        else:
            raise ValueError("Domain not found in the index")
    
    def resolve(self,domain):
        if domain in self.cache:
            return self.cache[domain]
        elif domain in self.index:
            return self.index[domain]
        else:
            raise ValueError("Domain not found")
    
    def clearCache(self):
        self.cache.clear()
    
    def indexList(self):
        if self.index:
            for domain in self.index:
                print(f"{domain}: {self.index[domain]}")
        else:
            print("The index is empty")
            
    def cacheList(self):
       if self.cache:
            for domain in self.cache:
                print(f"{domain}: {self.cache[domain]}")
       else:
            print("The cache is empty")
    
    def info(self):
        return f"DNS Index:\n{self.index} , Cache:\n{self.cache}"
    
    def function(self):
        return f"DNS allows us to find the IP address of a domain name and connect to it"

class DHCP(NetworkComponent):
    def __init__(self):
        self.adressPool = list()
        self.assignedAdresses = dict()
        
    def addAdress(self, *ips): # takes one or more ip adresses
        if ips not in self.adressPool:
            self.adressPool.extend(ips)
        else:
            raise ValueError("Adresses already in the pool")
    
    def assignAdress(self, device, ip):
        if ip in self.adressPool:
            self.assignedAdresses[device] = ip
            self.adressPool.remove(ip)
        else:
            raise ValueError("Adress not in the pool")
    
    def freeAdress(self, device):
        if device in self.assignedAdresses:
            self.adressPool.append(self.assignedAdresses[device])
            del self.assignedAdresses[device]
        else:
            raise ValueError("Device not found")
        
    def availableIPsList(self):
        print("Available IPs: ")
        for ip in self.adressPool:
            print(ip)
    
    def assignedIPsList(self):
        print("Assigned IPs: ")
        for device in self.assignedAdresses:
            print(f"{device}: {self.assignedAdresses[device]}")
    
    def info(self):
        return f"Adress Pool:\n{self.adressPool} , Assigned Adresses:\n{self.assignedAdresses}"
    
    def function(self):
        return f"DHCP allows us to automatically assign unique IP adresses to devices"
            
            
    
# Testing the IPv4 class
try:
    ipv4 = IPv4("192.168.1.1")
    ipv4_2 = IPv4("10.0.0.1")
    ipv4_3 = IPv4("172.16.1.1")
    ipv4_4 = IPv4("192.168.0.1")
    ipv4_5 = IPv4("10.0.1.1")

    print(f"IPv4 Address: {ipv4.adress}")
    print(f"Class: {ipv4.getClass()}")
    print(f"Subnet Mask: {ipv4.getMask()}")
    print(f"Network ID: {ipv4.getNetworkId()}")
    print(f"Host: {ipv4.getHost()}")
    print(f"Number of Hosts: {ipv4.getNofHosts()}")

    print(f"IPv4 Address: {ipv4_2.adress}")
    print(f"Class: {ipv4_2.getClass()}")
    print(f"Subnet Mask: {ipv4_2.getMask()}")
    print(f"Network ID: {ipv4_2.getNetworkId()}")
    print(f"Host: {ipv4_2.getHost()}")
    print(f"Number of Hosts: {ipv4_2.getNofHosts()}")

    print(f"IPv4 Address: {ipv4_3.adress}")
    print(f"Class: {ipv4_3.getClass()}")
    print(f"Subnet Mask: {ipv4_3.getMask()}")
    print(f"Network ID: {ipv4_3.getNetworkId()}")
    print(f"Host: {ipv4_3.getHost()}")
    print(f"Number of Hosts: {ipv4_3.getNofHosts()}")

    print(f"IPv4 Address: {ipv4_4.adress}")
    print(f"Class: {ipv4_4.getClass()}")
    print(f"Subnet Mask: {ipv4_4.getMask()}")
    print(f"Network ID: {ipv4_4.getNetworkId()}")
    print(f"Host: {ipv4_4.getHost()}")
    print(f"Number of Hosts: {ipv4_4.getNofHosts()}")

    print(f"IPv4 Address: {ipv4_5.adress}")
    print(f"Class: {ipv4_5.getClass()}")
    print(f"Subnet Mask: {ipv4_5.getMask()}")
    print(f"Network ID: {ipv4_5.getNetworkId()}")
    print(f"Host: {ipv4_5.getHost()}")
    print(f"Number of Hosts: {ipv4_5.getNofHosts()}")

except ValueError as e:
    print(e)

# Testing the DNS class
dns = DNS()
dns.addToIndex("google.com", "216.58.194.174")
dns.addToIndex("facebook.com", "157.240.2.35")
dns.addToIndex("amazon.com", "54.239.28.85")
dns.addToIndex("youtube.com", "216.58.194.174")
dns.addToIndex("wikipedia.org", "208.80.154.224")

print("\nDNS Index:")
dns.indexList()

print("\nResolving google.com:", dns.resolve("google.com"))
print("Resolving facebook.com:", dns.resolve("facebook.com"))
print("Resolving amazon.com:", dns.resolve("amazon.com"))
print("Resolving youtube.com:", dns.resolve("youtube.com"))
print("Resolving wikipedia.org:", dns.resolve("wikipedia.org"))

dns.removeFromIndex("amazon.com")
print("\nDNS Index after removal:")
dns.indexList()

# Testing the DHCP class
dhcp = DHCP()
dhcp.addAdress("192.168.1.100", "192.168.1.101", "10.0.0.100", "10.0.0.101", "172.16.1.100", "172.16.1.101", "192.168.2.100", "192.168.2.101", "10.1.1.100", "10.1.1.101", "192.168.3.100", "192.168.3.101", "10.2.2.100", "10.2.2.101", "172.17.2.100", "172.17.2.101")
dhcp.assignAdress("iPhone", "192.168.1.100")
dhcp.assignAdress("Samsung Smart TV", "192.168.1.101")
dhcp.assignAdress("Laptop", "10.0.0.100")
dhcp.assignAdress("Printer", "10.0.0.101")
dhcp.assignAdress("Smartphone", "172.16.1.100")
dhcp.assignAdress("Tablet", "192.168.2.100")
dhcp.assignAdress("PC", "192.168.2.101")
dhcp.assignAdress("Smartwatch", "10.1.1.100")
dhcp.assignAdress("Headphones", "10.1.1.101")
dhcp.assignAdress("Projector", "192.168.3.100")
dhcp.assignAdress("Smart Speaker", "192.168.3.101")
dhcp.assignAdress("Webcam", "10.2.2.100")
dhcp.assignAdress("Router", "10.2.2.101")
dhcp.assignAdress("Switch", "172.17.2.100")
dhcp.assignAdress("Server", "172.17.2.101")

print("\nAssigned IPs:")
dhcp.assignedIPsList()

print("\nAvailable IPs:")
dhcp.availableIPsList()

dhcp.freeAdress("iPhone")

dhcp.assignedIPsList()


dhcp.availableIPsList()


