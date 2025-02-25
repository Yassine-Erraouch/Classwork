from abc import ABC, abstractmethod


class InvalidBudgetError(Exception):
    def __init__(self):
        self.message = 'Error: Budget is null or negative'
                


# AdCampaign: abstract parent class
class AdCampaign (ABC):
    def __init__(self, nom, budget, canal):
        try:
            if budget < 0 or budget ==0 :
                raise InvalidBudgetError
        except:
            self.__nom = nom
            self.__budget = budget
            self.__canal = canal
    
    
    @classmethod
    def calculer_portée(self):
        raise NotImplementedError('Method is not implemented by this sub class.')
    
    def afficher_details(self):
        return f"Campagne: {self.__nom} | Budget {self.__budget:2f} € | Canal: {self.__canal}"

    
    
    # __str__ method
    def __str__(self):
        return f"Campagne: {self.__nom} | Budget {self.__budget:2f} € | Canal: {self.__canal}"
    
    # __eq__
    def __eq__(self, other):
        return self.__name == other.__name and self.__budget == other.__budget and self.__canal == other.__canal
    
     # Getters and Setters
    # @property
    # def nom(self):
    #     return self.__nom

    # @property
    # def budget(self):
    #     return self.__budget

    # @property
    # def canal(self):
    #     return self.__canal
    
    
    

# Google ads class
class GoogleAdsCampaign(AdCampaign):
    def __init__(self, nom, budget, canal, cpc):
        super().__init__(nom, budget, canal)
        self.cpc = cpc
    
    def caclculer_portée(self):
        return self.budget / self.cpc
    



# Facebook ads class
class FacebookAdsCampaign(AdCampaign):
    def __init__(self, nom, budget, canal, cpm):
        super().__init__(nom, budget, canal)
        self.cpm = cpm  
    
    

    def caclculer_portée(self):
        return ((self.budget/self.cpm)*1000)
    
    
# Youtube ads class
class YoutubeAdsCampaign(AdCampaign):
    def __init__(self, nom, budget, canal, cpv):
        super().__init__(nom, budget, canal)
        self.cpv = cpv
    
    def caclculer_portée(self):
        return self.budget/ self.cpv
    
    
# Influencers class
class InfluencersCampaign(AdCampaign):
    def __init__(self, nom, budget, canal, cpe):
        super().__init__(nom, budget, canal)
        self.cpe = cpe
    def caclculer_portée(self):
        return self.budget/ self.cpv
        