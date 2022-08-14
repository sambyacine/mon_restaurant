# def tri_personnalise(e):
#     return len(e)


def afficher(collection, n_premier_elements=-1):
    if collection == []:
        print("AUCUNE PIZZA")
        return
    #collection.sort(reverse=True, key=tri_personnalise)
    c = collection
    if not n_premier_elements == -1:
        c = collection[:n_premier_elements]
    nb_pizzas = len(c)
    print(f"----------LISTE DES PIZZAS ({nb_pizzas})---------------")
    for pizza in c:
        print(pizza)
    print()
    print("Premiere pizza", c[0])
    print("Derniere pizza", c[-1])

def ajouter_pizza_utilisateur(collection):
    pizza_ajouter = input("Pizza a ajouter: ")
    #if pizza_existe(pizza_ajouter, collection):
    if pizza_ajouter.lower() in collection:
        print("Erreur: Cette pizza existe deja")
    else:
        collection.append(pizza_ajouter)

# def pizza_existe(e, collection):
#     for i in collection:
#         if i == e:
#             return True
#     return False

vide = []
pizzas = ["4 fromages", "vegetarienne", "hawai", "calzone"]

ajouter_pizza_utilisateur(pizzas)
afficher(pizzas, 3)