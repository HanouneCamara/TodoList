todo_list = []

def ajouter_tache():
    tache = input("Entrez la tâche à ajouter : ")
    todo_list.append(tache)
    print("Tâche ajoutée.")

def afficher_liste():
    print("Liste des tâches :")
    for i, tache in enumerate(todo_list, 1):
        print(f"{i}. {tache}")

while True:
    print("\nOptions :")
    print("A. Ajouter une tâche")
    print("B. Afficher la liste des tâches")
    print("C. Quitter")
    choix = input("Choisissez une option :")
    
    if choix == "A":
        ajouter_tache()
    elif choix == "B":
        afficher_liste()
    elif choix == "C":
        break
    else:
        print("Option invalide. Veuillez réessayer.")

    
    