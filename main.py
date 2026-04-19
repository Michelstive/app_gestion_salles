from DATA.dao_salle import DataSalle
from Models.salle import Salle

dao = DataSalle()

# Test connexion
print("Connexion OK")

# Ajouter une salle
s = Salle("S001", "Labo Info", "Laboratoire", 30)
dao.insert_salle(s)

# Récupérer toutes les salles
for salle in dao.get_salles():
    salle.afficher_infos()

# Rechercher une salle
s2 = dao.get_salle("S001")
print(s2.description)

# Modifier
s2.capacite = 40
dao.update_salle(s2)

# Supprimer
dao.delete_salle("S001")