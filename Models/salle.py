class Salle:
    def __init__(self, code, description, categorie, capacite):
        self.code = code
        self.description = description
        self.categorie = categorie
        self.capacite = capacite

    def afficher_infos(self):
        print(f"Code: {self.code} | Description: {self.description} | "
              f"Catégorie: {self.categorie} | Capacité: {self.capacite}")