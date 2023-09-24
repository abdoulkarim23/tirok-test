
import random


# Classe pour représenter un investisseur.Ce code représente une structure de base pour un système d'investissement. 
class Investisseur:
    def __init__(self, nom, pib_du_pays):
        self.nom = nom
        self.solde = 0
        self.rendement = 0
        self.niveau = 1
        self.parrains = []
        self.pib_du_pays = pib_du_pays

    def investir(self, montant):
        self.solde += montant
        # Vérifier si l'investisseur atteint un nouveau niveau
        if self.solde >= self.niveau * 1000:
            self.niveau += 1
            print(f"{self.nom} est passé au niveau {self.niveau} !")

    def calculer_rendement(self):
        self.rendement = self.solde * random.uniform(0.05, 0.15)  # Rendement aléatoire entre 5% et 15%

    def parrainer(self, autre_investisseur):
        self.parrains.append(autre_investisseur)

    def est_independant(self):
        return self.solde >= self.pib_du_pays * 12  # Supposons que l'indépendance financière nécessite un an de PIB

# Classe pour représenter le système d'investissement
class SystemeInvestissement:
    def __init__(self):
        self.investisseurs = []

    def ajouter_investisseur(self, investisseur):
        self.investisseurs.append(investisseur)

    def effectuer_investissement(self, investisseur, montant):
        investisseur.investir(montant)

    def calculer_rendements(self):
        for investisseur in self.investisseurs:
            investisseur.calculer_rendement()

    def attribuer_recompenses_parrainage(self):
        for investisseur in self.investisseurs:
            for parrain in investisseur.parrains:
                parrain.solde += 50  # Récompense de 50 unités monétaires pour chaque parrainage réussi

# Exemple d'utilisation
if __name__ == "__main__":
    systeme = SystemeInvestissement()

    # Création d'investisseurs
    investisseur1 = Investisseur("Investisseur 1", 50000)  # Exemple de PIB du pays : 50 000 unités monétaires
    investisseur2 = Investisseur("Investisseur 2", 50000)
    investisseur3 = Investisseur("Investisseur 3", 50000)

    # Ajout d'investisseurs au système
    systeme.ajouter_investisseur(investisseur1)
    systeme.ajouter_investisseur(investisseur2)
    systeme.ajouter_investisseur(investisseur3)

    # Effectuer des investissements
    systeme.effectuer_investissement(investisseur1, 10000)  # Exemple d'investissement initial
    systeme.effectuer_investissement(investisseur2, 15000)
    systeme.effectuer_investissement(investisseur3, 20000)

    # Parrainage
    #Ce code permet aux investisseurs de parrainer d'autres investisseurs, avec une récompense pour chaque parrainage réussi.
    # De plus, il introduit des niveaux d'investissement basés sur le solde de l'investisseur. 
    investisseur1.parrainer(investisseur2)
    investisseur1.parrainer(investisseur3)

    # Calcul des rendements
    systeme.calculer_rendements()

    # Vérification de l'indépendance financière
    for investisseur in systeme.investisseurs:
        if investisseur.est_independant():
            print(f"{investisseur.nom} est financièrement indépendant !")


#Dans ce code grâce à la  méthode 'est_independant()'à la classe Investisseur qui compare le solde de l'investisseur 
# au PIB du pays pour déterminer s'il est financièrement indépendant.
# Le seuil de l'indépendance financière est défini ici comme équivalent à un an de PIB du pays, 