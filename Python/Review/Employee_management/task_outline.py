#créer la classe Employe
#####  attributs : matricule , nom (pattern [A-Z]{2,}(\s[A-Z]{2,})*),prenom(pattern = [A-Z][a-z]{2,}(\s[A-Z][a-z]{2,})*)
                   #DATEnAISSANCE (doit être inf a 01-01-2000  si une custom exception doit levée)
                   #DateEmbauche  (la diff entre dateEmb -  dateNaiss doit être au moins 24 ans sinon une custom exception levée)
                   #salaire 
                   # la gestion des attributs se fait au niveau du constructeur
####    methode  : __str___ , __eq__  (deux emp sont égaux si ils ont le memee matricule)
                  #CalculAnciennete(self) =>  diff between current date et date embauche
                  #CalculAge(self)  => diff between current date et date naissance
                  #CalculDateRetraite(self)



