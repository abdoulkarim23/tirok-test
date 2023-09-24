import openpyxl

# Crée un nouveau classeur Excel
classeur = openpyxl.Workbook()

# Sélectionne la feuille de calcul active (par défaut, il y en a une appelée "Sheet")
feuille = classeur.active

# Ajoute des données dans la feuille de calcul
feuille['A1'] = "Investisseur"
feuille['B1'] = "Solde"
feuille['C1'] = "Rendement"

# Exemple d'investisseurs
investisseurs = [("Investisseur 1", 5000, 750),
                 ("Investisseur 2", 8000, 1200),
                 ("Investisseur 3", 12000, 1800)]

# Remplit la feuille de calcul avec les données des investisseurs
for i, (nom, solde, rendement) in enumerate(investisseurs, start=2):
    feuille[f'A{i}'] = nom
    feuille[f'B{i}'] = solde
    feuille[f'C{i}'] = rendement

# Sauvegarde le classeur Excel dans un fichier
classeur.save("investisseurs.xlsx")


# Je regrette, mais je ne peux pas fournir de code en version Excel, 
# car Excel est une application de tableur qui n'accepte pas directement du code Python ou
#  d'autres langages de programmation. Cependant, Voici un code Python utilisant la bibliothèque openpyxl 
# pour créer un fichier Excel et y ajouter des données