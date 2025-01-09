from abc import abstractmethod



class Livre:
    def __init__(self, titre=str, auteur=str, annee_publication=int, disponible=bool):
        self.__titre = titre
        self.__auteur = auteur
        self.__annee_publication = annee_publication
        self.__disponible = disponible
    
    def afficer_detail(self):
        return f"Titre: {self.__titre}, auteur: {self.__auteur}, année de publication: {self.__annee_publication}, disponibilité: {self.__disponible}"
    
    def get_attributes(self):
        return self.__titre, self.__auteur, self.__annee_publication, self.__disponible

    def set_attributes(self, titre=str, auteur=str, annee_publication=int, disponible=bool):
        self.__titre, self.__auteur, self.__annee_publication, self.__disponible = titre, auteur, annee_publication, disponible

class Utilisateur:
    def __init__(self, nom=str, email=str, livres_empruntes=str):
        self.nom = nom
        self.email = email
        self.livres_empruntes = livres_empruntes
    def afficher_details(self):
        return f"nom: {self.nom}, email: {self.email} livre empruntes: {self.livres_empruntes}"

class Bibliothecaire(Utilisateur):
    def __init__(self, nom, email, livres_empruntes):
        super().__init__(self, nom, email, livres_empruntes)
    
    def ajouter_livre(self):
        
        pass
    
    
    def afficher_details(self):
        return f"nom: {self.nom}, email: {self.email} livre empruntes: {self.livres_empruntes}, type d'utilsateur: Bibliothecaire"
    
class Personne(abc):
    @abstractmethod
    def afficher_details():
        pass