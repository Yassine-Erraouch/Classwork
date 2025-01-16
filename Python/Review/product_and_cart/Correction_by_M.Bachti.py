"""
        •	Créer une classe => ajouter un nouveau type à la liste des types
        •	Classe est modèle , un plan qui décrit la structure (attributs et méthodes des objets)
        •	Objet est une variable complexe de type classe
        •	Pour construire un objet on doit appeler le constructeur de la classe
        •	Les constructeurs de la classe sont des méthodes magiques qui portent le nom __init__
        •	Une classe peut avoir plusieurs constructeurs (constructeur par défaut , constructeur d’initialisation …)
        •	Une classe peut avoir d’autres méthodes magiques qui facilitent la manipulation des objets de cette classe :
        o	__str__ : -convertir un objet de type classe  en string
        o	__repre__ : si __str__ n est pas définie 
        o	__eq__   : pour définir la logique de comparaison de deux objets de type classe ( ==)
        o	__lt__ : pour vérifier si un objet est inférieur à un autre
        o	__gt__ : 
        NB. On les appelle méthode magiques parce qu’on les appelle implicitement                                              
"""
class Produit:
    #les methodes magiques
    """def __init__(self):
        self.codeP=0
        self.intitule=""
        self.prix=0"""
    def __init__(self,c,nom,p):
        self.codeP=c
        self.intitule=nom
        self.prix=p
    def __str__(self):
        return f'{self.codeP}-{self.intitule}-{self.prix}'
    def __eq__(self,p):
        return p.codeP==self.codeP
    #les méthodes d instance
    def afficher(self):
        print(f"{self.intitule}**{self.prix}")


#créer la classe Cart 
### attribut : listProduit initialisé par défaut une liste vide 
class Cart:
    def __init__(self):
        self.listP=[]
    #define addProduct(self,product)=>ajoute au produit l'attribut qte avec la valeur par defaut 1
    def addProduct(self,product):
        if(product in self.listP):
            pos=self.listP.index(product)
            self.listP[pos].qte+=1
        else:
            product.qte=1
            self.listP.append(product)
    #define removeProductFrmCart(self,codeP)
    def removeProduct(self,codeP):
        for p in self.listP:
            if p.codeP==codeP:
                self.listP.remove(p)
                return
        print("Product not found !!!!")
       
    #define incrementQte(self,codeP)  =>
    def incrementQte(self,codeP):
        for p in self.listP:
            if p.codeP==codeP:
                p.qte+=1
                return
        print("Product not found !!!!")

    # define decrementQte(self,codeP) => decremente la qte et si la qte devient 0 le produit doit être ecrasé de la carte
    def decrementQte(self,codeP):
        for p in self.listP:
            if p.codeP==codeP:
                p.qte-=1
                if p.qte==0: self.listP.remove(p)
                return
        print("Product not found !!!!")
    #define TotalAmount(self): =>   calculer le prix total de tous les produits; 
    def TotalAmount(self):
        total=sum([p.qte*p.prix for p in self.listP])
        return total
    #define __str__
    def __str__(self):
        ch=("codeP\tIntitule\tPrix\tQte\tpht\n")
        for p in self.listP:
             ch+=f"{p.codeP}\t{p.intitule}\t{p.prix}\t{p.qte}\t{p.qte*p.prix}\n"
        ch+=f"\n{'\t'*6} Montant Total : {self.TotalAmount()}"
        return ch

myCart=Cart()

for i in range(10):
    myCart.addProduct(Produit(1000+i,f"product{i+1}",10000+100*i))
print(myCart)
myCart.incrementQte(1002)
print(myCart)
myCart.decrementQte(1004)
print(myCart)  
myCart.removeProduct(1002)
print(myCart)