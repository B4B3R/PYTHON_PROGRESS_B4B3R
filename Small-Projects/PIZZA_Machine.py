class Pizza:
    def __init__(self, base, diametre, type):
        self.base = base
        self.diametre = diametre
        self.type = type

    def Ajout_ingredient(self, ingredient):
        print("On ajoute ", ingredient, " à votre pizza.")

    def Amener_pizza(self, table):
        print("Pizza à la table ", table, " validée.")

calzone = Pizza("blanche",4,"calzone")

calzone.Ajout_ingredient("saumon")