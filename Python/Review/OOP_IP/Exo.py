
class CustomError(Exception):
    """A custom error class"""
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class IPv4:
    def __init__(self, ip=list):
        if len(ip) != 4:
            raise CustomError("l'adresse IP doit avoir 4 segments")
        
        if not (ip[0]  in range(0, 256) and ip[1]  in range(0, 256) and ip[2]  in range(0, 256) and ip[3]  in range(0, 256)):
            raise CustomError("les segments de l'adresse IP doivent avoir une valeur comprise entre 0 et 255")
        self.ip = ip
        self.masque = self.getMasque()
        self.classe = self.GetClasse()
             
        
    def adresse_reseau(self,masque=list): #  gives us the network adress using a given mask
        adresse_reseau = []
        for i in range (0,4):
            if masque[i] == 255:
                adresse_reseau.append(self.ip[i])
            else:
                adresse_reseau.append(0) 
        return adresse_reseau           
    
    def GetClasse(self):# tells me the class of the IP adress
        segment = self.ip[0]
        classe = ''
        if segment in range(0,128):
            classe = "A"
        elif segment in range(128, 192):
            classe = "B"
        elif segment in range(192, 224):
            classe = "C"
        elif segment in range(224, 240):
            classe = "D"
        else: 
            classe = "E"
        return classe 
    
    def GetAdresseReseau(self): #
        adresseReseau = self.ip
        if self.GetClasse() == "A":
            adresseReseau[1], adresseReseau[2], adresseReseau[3] = 0, 0, 0
        elif self.GetClasse() == "B":
            adresseReseau[2], adresseReseau[3] = 0, 0
        elif self.GetClasse() == "C":
            adresseReseau[3] = 0
        return adresseReseau
    
    def GetMasque(self):
        if self.GetClasse() == "A":
            return [255, 0, 0, 0]
        elif self.GetClasse() == "B":
            return [255, 255, 0, 0]
        elif self.GetClasse() == "C":
            return [255, 255, 255, 0]
        
        
ip = IPv4([192, 168, 0, 1])
# calling the class methods
print(ip.GetAdresseReseau())
print(ip.GetClasse())
print(ip.GetMasque())
print(ip.adresse_reseau([255, 255, 255, 255]))

ip2 = IPv4([0, 0, 0, 300])
