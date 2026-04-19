from DATA.dao_salle import DataSalle
from Models.salle import Salle

dao = DataSalle()


print("Connexion OK")


s = Salle("S001", "Labo Info", "Laboratoire", 30)
dao.insert_salle(s)


for salle in dao.get_salles():
    salle.afficher_infos()


s2 = dao.get_salle("S001")
print(s2.description)


s2.capacite = 40
dao.update_salle(s2)


dao.delete_salle("S001")