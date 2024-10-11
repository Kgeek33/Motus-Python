"""Voici la version 4.0 ! Ce programme reprend le célèbre jeu Motus"""

"""Modules"""
from random import choice, randint
from rich.console import Console
from rich.progress import Progress, SpinnerColumn
from time import sleep

"""Préparation des variables"""
console = Console()
console.clear()
progress = Progress(SpinnerColumn())
nbLettresUsr = int(input("Combien de lettres chaque mot à deviner -> "))
with open("Dictionnaire.txt", encoding="utf-8") as file:
    contenu_du_fichier = file.read().splitlines()
    motadeviner = choice(contenu_du_fichier).strip().upper()
nbLettres = len(motadeviner)
while nbLettres != nbLettresUsr:
    motadeviner = choice(contenu_du_fichier).strip().upper()
    nbLettres = len(motadeviner)
index_aleatoire = randint(1, nbLettres - 1)
index_premiere_lettre = randint(0, nbLettres - 1)
motAffiche = motadeviner[0] + "." * (nbLettres - 1)
motAffiche = motAffiche[:index_aleatoire] + motadeviner[index_aleatoire] + motAffiche[index_aleatoire + 1:]
lstResult = [0 for i in range(nbLettres)]
nbSaisi = 0
motSaisi = 0

"""Nombres de joueurs"""
nbJoueurs = int(input("Combien de joueur(s) participe(nt) ? -> "))
#Préparation du jeu en fonction du nombre(s) de joueur(s)
console.clear()
match nbJoueurs:
    case 1:
        nbManches = 0
        joueurActuel = 1
    case other:
        Participants = {}
        for i in range(1,nbJoueurs + 1):
            Participants[i] = 0
        nbManches = 1
        joueurActuel = 1
        console.print(f"Manche {nbManches}/5 -> ", end="")
        console.print(f"C'est au joueur {joueurActuel} de commencer !")
        console.print("\n----------")

"""Jeu"""
while motadeviner != motSaisi:
#Vérification de l'affichage des variables, du nombre de saisie(s) et de manches
    if isinstance(motadeviner, list) is True:
        motadeviner = "".join(motadeviner)
    if isinstance(motAffiche, list) is True:
        motAffiche = "".join(motAffiche)
    if isinstance(motSaisi, list) is True:
        motSaisi = "".join(motSaisi)
    match nbSaisi:
        case 0:
            console.print(f"[green]Il reste {8-nbSaisi} saisies autorisées !")
        case 1 | 2 | 3:
            console.print(f"[bright_green]Il reste {8-nbSaisi} saisies autorisées !")
        case 4 | 5 | 6:
            console.print(f"[dark_orange]Il reste {8-nbSaisi} saisies autorisées !")
        case 6:
            console.print(f"[red]Il reste {8-nbSaisi} saisies autorisées !")
        case 7:
            console.print(f"[bright_red]Il reste {8-nbSaisi} saisie autorisée !")
        case 8:
            if nbJoueurs == 1:
                console.print(f"[bright_black]Perdu ! Il fallait trouver : [underline]{motadeviner}")
                sleep(1.5)
                choix = input("Veux-tu rejouer (O/N) -> ")
                match choix:
                    case "O" | "o":
                        motadeviner = choice(contenu_du_fichier).strip().upper()
                        nbLettres = len(motadeviner)
                        while nbLettres != nbLettresUsr:
                            motadeviner = choice(contenu_du_fichier).strip().upper()
                            nbLettres = len(motadeviner)
                        index_aleatoire = randint(1, nbLettres - 1)
                        index_premiere_lettre = randint(0, nbLettres - 1)
                        motAffiche = motadeviner[0] + "." * (nbLettres - 1)
                        motAffiche = motAffiche[:index_aleatoire] + motadeviner[index_aleatoire] + motAffiche[index_aleatoire + 1:]
                        lstResult = [0 for i in range(nbLettres)]
                        nbSaisi = 0
                        motSaisi = 0
                        console.clear()
                        continue
                    case other:
                        console.print("Merci d'avoir joué, à bientôt !")
                        exit()
            else:
                console.print(f"[bright_black]Perdu ! Il fallait trouver : [underline]{motadeviner}")
                motadeviner = choice(contenu_du_fichier).strip().upper()
                nbLettres = len(motadeviner)
                while nbLettres != nbLettresUsr:
                    motadeviner = choice(contenu_du_fichier).strip().upper()
                    nbLettres = len(motadeviner)
                index_aleatoire = randint(1, nbLettres - 1)
                index_premiere_lettre = randint(0, nbLettres - 1)
                motAffiche = motadeviner[0] + "." * (nbLettres - 1)
                motAffiche = motAffiche[:index_aleatoire] + motadeviner[index_aleatoire] + motAffiche[index_aleatoire + 1:]
                lstResult = [0 for i in range(nbLettres)]
                nbSaisi = 0
                motSaisi = 0
                console.print(f"Nouveau mot à deviner ! -> ", end="")
                console.print(f"C'est au joueur {joueurActuel} de commencer !")
                console.print("\n----------")
                continue
    console.print(f"{motAffiche} -> {nbLettres} lettres")
    motSaisi = input("Quel mot proposes-tu ? -> ").strip().upper()
#Vérification du mot saisi en fonction des différentes conditions
    motAffiche = list(motAffiche)
    motSaisi = list(motSaisi)
    motadeviner = list(motadeviner)
    nbLettresSaisi = len(motSaisi)
    progress = Progress(SpinnerColumn())
    with console.status("[blue]Vérification de la 1ère lettre...") as status:
        sleep(0.5)
    if motSaisi == [] or motSaisi[0] != motadeviner[0]:
        console.print("❌ La première lettre ne correspond pas !", style="bold bright_red")
        sleep(1)
        console.print("\n----------")
        if nbJoueurs > 1:
            if nbSaisi < 8:
                joueurActuel += 1
                if "." in motAffiche:
                    ltrBns = motAffiche.index(".")
                    motAffiche[ltrBns] = motadeviner[ltrBns]
                    if joueurActuel > nbJoueurs:
                        joueurActuel = 1
                    console.print(f"Joueur {joueurActuel}, à ton tour avec la lettre BONUS : [underline bold]{motadeviner[ltrBns]}")
                else:
                    if joueurActuel > nbJoueurs:
                        joueurActuel = 1
                    console.print(f"Joueur {joueurActuel}, à ton tour")
        else:
            nbSaisi += 1
            if "." in motAffiche:
                ltrBns = motAffiche.index(".")
                motAffiche[ltrBns] = motadeviner[ltrBns]
                console.print(f"Voici la lettre BONUS : [underline bold]{motadeviner[ltrBns]}")          
        continue
    console.print("✅ 1ère lettre respectée !", style="green")
    with console.status("[blue]Vérification de la longueur du mot saisi...") as status:
        sleep(0.5)
    if len(motSaisi) != len(motadeviner):
        console.print(f"❌ {nbLettresSaisi} lettres sur {len(motadeviner)} de saisie(s) !", style="bold bright_red")
        sleep(1)
        console.print("\n----------")
        if nbJoueurs > 1:
            if nbSaisi < 8:
                joueurActuel += 1
                if "." in motAffiche:
                    ltrBns = motAffiche.index(".")
                    motAffiche[ltrBns] = motadeviner[ltrBns]
                    if joueurActuel > nbJoueurs:
                        joueurActuel = 1
                    console.print(f"Joueur {joueurActuel}, à ton tour avec la lettre BONUS : [underline bold]{motadeviner[ltrBns]}")
                else:
                    if joueurActuel > nbJoueurs:
                        joueurActuel = 1
                    console.print(f"Joueur {joueurActuel}, à ton tour")
        else:
            nbSaisi += 1
            if "." in motAffiche:
                ltrBns = motAffiche.index(".")
                motAffiche[ltrBns] = motadeviner[ltrBns]
                console.print(f"Voici la lettre BONUS : [underline bold]{motadeviner[ltrBns]}")          
        continue
    console.print(f"✅ {nbLettresSaisi} lettres respectées !", style="green")
    with console.status("[blue]Vérification de l'existante du mot saisi") as status:
        sleep(0.5)
    motSaisi = "".join(motSaisi)
    if motSaisi not in contenu_du_fichier:
        console.print("❌ Le mot n'existe pas dans le dictionnaire !", style="bold bright_red")
        sleep(1)
        console.print("\n----------")
        if nbJoueurs > 1:
            if nbSaisi < 8:
                joueurActuel += 1
                if "." in motAffiche:
                    ltrBns = motAffiche.index(".")
                    motAffiche[ltrBns] = motadeviner[ltrBns]
                    if joueurActuel > nbJoueurs:
                        joueurActuel = 1
                    console.print(f"Joueur {joueurActuel}, à ton tour avec la lettre BONUS : [underline bold]{motadeviner[ltrBns]}")
                else:
                    if joueurActuel > nbJoueurs:
                        joueurActuel = 1
                    console.print(f"Joueur {joueurActuel}, à ton tour")
        else:
            nbSaisi += 1
            if "." in motAffiche:
                ltrBns = motAffiche.index(".")
                motAffiche[ltrBns] = motadeviner[ltrBns]
                console.print(f"Voici la lettre BONUS : [underline bold]{motadeviner[ltrBns]}")          
        continue
    console.print("✅ Le mot existe bien dans le dictionnaire !", style="green")
    motSaisi = list(motSaisi)
    with console.status("[blue]Analyse du mot saisi...") as status:
        sleep(0.5)
    if nbJoueurs > 1 and nbManches < 5:
        if motSaisi == motadeviner:
#S'il y a plusieurs joueurs et que le mot a été deviné
            motadeviner = "".join(motadeviner)
            nbSaisi += 1
            console.print("Félicitations, tu as trouvé le mot : " + motadeviner + f" en {nbSaisi} saisie(s) !", style="green")
            sleep(3)
            console.clear()
            Participants[joueurActuel] += 50
            motadeviner = choice(contenu_du_fichier).strip().upper()
            nbLettres = len(motadeviner)
            while nbLettres != nbLettresUsr:
                motadeviner = choice(contenu_du_fichier).strip().upper()
                nbLettres = len(motadeviner)
            index_aleatoire = randint(1, nbLettres - 1)
            index_premiere_lettre = randint(0, nbLettres - 1)
            motAffiche = motadeviner[0] + "." * (nbLettres - 1)
            motAffiche = motAffiche[:index_aleatoire] + motadeviner[index_aleatoire] + motAffiche[index_aleatoire + 1:]
            lstResult = [0 for i in range(nbLettres)]
            nbSaisi = 0
            motSaisi = 0
            nbManches += 1
            console.print(f"Manche {nbManches}/5 -> ", end="")
            console.print(f"C'est au joueur {joueurActuel} de commencer !")
            console.print("\n----------")
#Lancement d'une nouvelle manche
            continue
    elif nbJoueurs == 1:
        if motSaisi == motadeviner:
#S'il y a 1 joueur et que le mot a été trouvé 
            motadeviner = "".join(motadeviner)
            nbSaisi += 1
            console.print("Félicitations, tu as trouvé le mot : " + motadeviner + f" en {nbSaisi} saisie(s) !", style="green")
            sleep(3)
            choix = input("Veux-tu rejouer (O/N) -> ")
            if choix == "O" or choix == "o":
                nbSaisi += 1
                motadeviner = choice(contenu_du_fichier).strip().upper()
                nbLettres = len(motadeviner)
                while nbLettres != nbLettresUsr:
                    motadeviner = choice(contenu_du_fichier).strip().upper()
                    nbLettres = len(motadeviner)
                index_aleatoire = randint(1, nbLettres - 1)
                index_premiere_lettre = randint(0, nbLettres - 1)
                motAffiche = motadeviner[0] + "." * (nbLettres - 1)
                motAffiche = motAffiche[:index_aleatoire] + motadeviner[index_aleatoire] + motAffiche[index_aleatoire + 1:]
                lstResult = [0 for i in range(nbLettres)]
                nbSaisi = 0
                motSaisi = 0
                console.clear()
                continue
            else:
                console.print("Merci d'avoir joué, à bientôt !")
                exit()
    else:
        if motSaisi == motadeviner:
            motadeviner = "".join(motadeviner)
            nbSaisi += 1
            console.print("Félicitations, tu as trouvé le mot : " + motadeviner + f" en {nbSaisi} saisie(s) !", style="green")
            Participants[joueurActuel] += 50
            sleep(3)
            """Annonce le score + Fin du programme"""
            console.clear()
            console.print("Partie terminée ! Voici les scores :")
            for joueur, score in Participants.items():
                console.print(f"Joueur {joueur} -> {score} points")
            exit()
#Création d'une map
    letter_count = {}
    for letter in motadeviner:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
#Création d'une liste permettant de générer les couleurs
    for i in range(nbLettres):
        lstResult[i]=0
        if motSaisi[i] == motadeviner[i] and motSaisi[i] in letter_count:
            letter_count[motSaisi[i]] -= 1
            if letter_count[motSaisi[i]] == 0:
                del letter_count[motSaisi[i]]
            lstResult[i] = 1
            motAffiche[i] = motadeviner[i]
    for i in range(nbLettres):
            if lstResult[i] == 0 and motSaisi[i] in letter_count:
                letter_count[motSaisi[i]] -= 1
                if letter_count[motSaisi[i]] == 0:
                    del letter_count[motSaisi[i]]
                lstResult[i] = 2
            elif lstResult[i] == 0:
                lstResult[i] = 0
#Génération des couleurs
    console.print("Résultat ->", style="underline", end="")
    console.print(" ",end="")
    for i in range(nbLettres):
        if lstResult[i] == 1:
            console.print(f"{motSaisi[i]}", style="red", end="")
        elif lstResult[i] == 2:
            console.print(f"{motSaisi[i]}", style="yellow", end="")
        else:
            console.print(f"{motSaisi[i]}", end="")
    console.print("")
    console.print("\n----------")
    nbSaisi += 1
    if nbJoueurs > 1:
        joueurActuel += 1
        if joueurActuel > nbJoueurs:
            joueurActuel = 1
        console.print(f"Joueur {joueurActuel}, à ton tour")