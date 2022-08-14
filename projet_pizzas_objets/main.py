class Pizza:

    def __init__(self, nom, prix, ingredients, vegetarienne=False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne

    def afficher(self):
        veg_str = ""
        if self.vegetarienne:
            veg_str = "- VEGETRIENNE"
        print(f"Pizza {self.nom} : {self.prix} euro " + veg_str)
        print(", ".join(self.ingredients))
        print()

class PizzaPersonnalisee(Pizza):
    #PIZZAS_PERSONNALISEES = 2
    PRIX_DE_BASE = 7
    PRIX_PAR_INGREDIENT = 1.2
    dernier_numero = 0
    def __init__(self):
        PizzaPersonnalisee.dernier_numero += 1
        self.numero = PizzaPersonnalisee.dernier_numero
        super().__init__("Personnalisee " + str(self.numero), 0, [])
        self.demander_ingredients_utilisateur()
        self.calculer_le_prix()

    def demander_ingredients_utilisateur(self):
        print()
        print("Ingredients pour la pizza personnalisee " + str(self.numero))
        while True:
            ingredient = input("Ajouter un ingredient ou (ENTER pour terminer)")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"Vous avez ajouter {len(self.ingredients)} ingredient(s) : {', '.join(self.ingredients)}")

    def calculer_le_prix(self):
        self.prix = self.PRIX_DE_BASE + self.PRIX_PAR_INGREDIENT * len(self.ingredients)


pizzas = [
          Pizza("4 Fromages", 8.5, ("brie", "emmental", "compte", "parmesan"), True),
          Pizza("vegetarienne", 10.5, ("tomate", "oignon", "jambon", "chanpignon", "Olive")),
          Pizza("Hawai", 11.5, ("oeufs", "poivron", "emmental")),
          Pizza("4 saisons", 9.5, ("tomate", "annanas", "oignon"), True),
          PizzaPersonnalisee(),
          PizzaPersonnalisee(),
          PizzaPersonnalisee()
        ]

def tri(e):
    return e.prix

# (1) les pizzas vegetariennes
# (2) les pizzas non vegetariennes
# (3) les pizzas avec de la tomate
# (1) les pizzas en moins de 10euro
#pizzas.sort(key=tri)
for i in pizzas:
    # if i.vegetarienne:
    # if not i.vegetarienne:
    # if "tomate" in i.ingredients:
    #if i.prix < 10.0:
    i.afficher()