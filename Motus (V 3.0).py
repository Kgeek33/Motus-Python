"""Voici la version 3.0 du programme Motus. Ce programme reprend le célèbre jeu Motus"""

"""Modules"""
from random import choice, randint
from rich.console import Console
from rich.progress import Progress, SpinnerColumn
from time import sleep
import types

"""Préparation"""
def preparation():
    console = Console()
    progress = Progress(SpinnerColumn())
    with open("Dictionnaire.txt", encoding="utf-8") as file:
        contenu_du_fichier = file.read().splitlines()
        motadeviner = choice(contenu_du_fichier).strip().upper()
    nbLettres = len(motadeviner)
    while nbLettres < 5 or nbLettres > 10:
        motadeviner = choice(contenu_du_fichier).strip().upper()
        nbLettres = len(motadeviner)
    index_aleatoire = randint(1, nbLettres - 1)
    motAffiche = motadeviner[0] + "." * (nbLettres - 1)
    motAffiche = motAffiche[:index_aleatoire] + motadeviner[index_aleatoire] + motAffiche[index_aleatoire + 1:]
    lstResult = [0 for i in range(nbLettres)]
    nbSaisi = 0
    motSaisi = 0
    total = 100
    nbJoueur_s(console,contenu_du_fichier,lstResult,motadeviner,motAffiche,motSaisi,nbLettres,nbSaisi)

"""Nombre de joueur(s)"""
def nbJoueur_s(console,contenu_du_fichier,lstResult,motadeviner,motAffiche,motSaisi,nbLettres,nbSaisi):
    nbJoueurs = int(input("Combien de joueur(s) participe(nt) ? -> "))
    if nbJoueurs == 1:
        console.print(f"[bright_cyan]Tu as droit à [bold underline green]8[/bold underline green] saisies !")
        jou_ekpActuel = 1
        motSaisiUser(console,contenu_du_fichier,jou_ekpActuel,lstResult,motadeviner,motAffiche,motSaisi,nbJoueurs,nbLettres,nbSaisi)
    elif nbJoueurs == 2:
        Participants = {}
        for i in range(1,nbJoueurs + 1):
            Participants[i] = 0
        nbManches = 8
        jou_ekpActuel = 1
        for manche in range(1, nbManches + 1):
            motadeviner = choice(contenu_du_fichier).strip().upper()
            nbLettres = len(motadeviner)
            while nbLettres < 5 or nbLettres > 10:
                motadeviner = choice(contenu_du_fichier).strip().upper()
                nbLettres = len(motadeviner)
            index_aleatoire = randint(1, nbLettres - 1)
            motAffiche = motadeviner[0] + "." * (nbLettres - 1)
            motAffiche = motAffiche[:index_aleatoire] + motadeviner[index_aleatoire] + motAffiche[index_aleatoire + 1:]
            lstResult = [0 for i in range(nbLettres)]
            console.print(f"Manche {manche} -> ", end="")
            console.print(f"C'est au joueur {jou_ekpActuel} de commencer !")
            console.print("\n----------")
            motSaisiUser(console,contenu_du_fichier,jou_ekpActuel,lstResult,motadeviner,motAffiche,motSaisi,nbJoueurs,nbLettres,nbSaisi)
            Participants[jou_ekpActuel] += 50
        console.clear()
        console.print("Partie terminée ! Voici les scores :")
        for joueur, score in Participants.items():
            console.print(f"Joueur {joueur} -> {score} points")
    else:
        Participants = {}
        for i in range(1,nbJoueurs + 1):
            Participants[i] = 0
        nbManches = 8
        jou_ekpActuel = 1
        for manche in range(1, nbManches + 1):
            motadeviner = choice(contenu_du_fichier).strip().upper()
            nbLettres = len(motadeviner)
            while nbLettres < 5 or nbLettres > 10:
                motadeviner = choice(contenu_du_fichier).strip().upper()
                nbLettres = len(motadeviner)
            index_aleatoire = randint(1, nbLettres - 1)
            motAffiche = motadeviner[0] + "." * (nbLettres - 1)
            motAffiche = motAffiche[:index_aleatoire] + motadeviner[index_aleatoire] + motAffiche[index_aleatoire + 1:]
            lstResult = [0 for i in range(nbLettres)]
            console.print(f"Manche {manche} -> ", end="")
            console.print(f"C'est à l'équipe {jou_ekpActuel} de commencer !")
            console.print("\n----------")
            motSaisiUser(console,contenu_du_fichier,jou_ekpActuel,lstResult,motadeviner,motAffiche,motSaisi,nbJoueurs,nbLettres,nbSaisi)
            Participants[jou_ekpActuel] += 50
        console.clear()
        console.print("Partie terminée ! Voici les scores :")
        for joueur, score in Participants.items():
            console.print(f"Joueur {joueur} -> {score} points")

"""Jeu"""
def motSaisiUser(console,contenu_du_fichier,jou_ekpActuel,lstResult,motadeviner,motAffiche,motSaisi,nbJoueurs,nbLettres,nbSaisi):
    while motadeviner != motSaisi:
        if type(motAffiche) is list:
            motAffiche = "".join(motAffiche)
        elif type(motSaisi) is list:
            motSaisi = "".join(motSaisi)
        elif type(motSaisi) is list:
            motadeviner = "".join(motadeviner)
        if nbSaisi != 0:
            if nbSaisi<=3:
                console.print(f"[bright_green]Il reste {8-nbSaisi} saisies autorisées !")
            elif nbSaisi<6:
                console.print(f"[dark_orange]Il reste {8-nbSaisi} saisies autorisées !")
            elif nbSaisi==6:
                console.print(f"[red]Il reste {8-nbSaisi} saisies autorisées !")
            elif nbSaisi==7:
                console.print(f"[bright_red]Il reste {8-nbSaisi} saisie autorisée !")
            else:
                motAffiche = "".join(motAffiche)
                console.print(f"[bright_black]Perdu ! Il fallait trouver : [underline]{motadeviner}")
                choix = input("Veux-tu rejouer (O/N) ? -> ")
                if choix.lower() == "O" or choix.lower() == "o":
                    preparation()
                else:
                    exit()
        else:
            console.print(f"[green]Il reste {8-nbSaisi} saisies autorisées !")
        console.print(f"{motAffiche} -> {nbLettres} lettres")
        motSaisi = input("Quel mot proposes-tu ? -> ").strip().upper()
        nbLettresSaisi = len(motSaisi)
        motAffiche = list(motAffiche)
        motSaisi = list(motSaisi)
        motadeviner = list(motadeviner)
        verifs(console,contenu_du_fichier,jou_ekpActuel,lstResult,motadeviner,motAffiche,motSaisi,nbJoueurs,nbLettres,nbLettresSaisi,nbSaisi)

"""Vérification des conditions du mot saisi"""
def verifs(console,contenu_du_fichier,jou_ekpActuel,lstResult,motadeviner,motAffiche,motSaisi,nbJoueurs,nbLettres,nbLettresSaisi,nbSaisi):
    with console.status("[blue]Vérification de la 1ère lettre...") as status:
        sleep(1.5)
    if motSaisi == "" or motSaisi[0] != motadeviner[0]:
        console.print("❌ La première lettre ne correspond pas !", style="bold bright_red")
        ltrBonus=motAffiche.index(".")
        motAffiche[ltrBonus]=motadeviner[ltrBonus]
        nbSaisi += 1
        sleep(2)
        console.clear()
        if nbJoueurs == 2:
            nbSaisi -= 1
            jou_ekpActuel += 1
            if jou_ekpActuel > nbJoueurs:
                jou_ekpActuel = 1
            console.print(f"C'est au tour du joueur {jou_ekpActuel} avec la lettre BONUS !")
        elif nbJoueurs > 2:
            nbSaisi -= 1
            jou_ekpActuel += 1
            if jou_ekpActuel > nbJoueurs:
                jou_ekpActuel = 1
            console.print(f"C'est au tour de l'équipe {jou_ekpActuel} avec la lettre BONUS !")
        else:
            console.print("Voici la lettre BONUS !")
        motSaisiUser(console,contenu_du_fichier,jou_ekpActuel,lstResult,motadeviner,motAffiche,motSaisi,nbJoueurs,nbLettres,nbSaisi)
    console.print("✅ 1ère lettre respectée !", style="green")
    with console.status("[blue]Vérification de la longueur du mot saisi...") as status:
        sleep(2)
    if len(motSaisi) != len(motadeviner):
        console.print(f"❌ {nbLettresSaisi} lettres sur {len(motadeviner)} de saisie(s) !", style="bold bright_red")
        ltrBonus=motAffiche.index(".")
        motAffiche[ltrBonus]=motadeviner[ltrBonus]
        nbSaisi += 1
        sleep(2)
        console.clear()
        if nbJoueurs == 2:
            nbSaisi -= 1
            jou_ekpActuel += 1
            if jou_ekpActuel > nbJoueurs:
                jou_ekpActuel = 1
            console.print(f"C'est au tour du joueur {jou_ekpActuel} !")
        elif nbJoueurs > 2:
            nbSaisi -= 1
            jou_ekpActuel += 1
            if jou_ekpActuel > nbJoueurs:
                jou_ekpActuel = 1
            console.print(f"C'est au tour de l'équipe {jou_ekpActuel} !")
        else:
            console.print("Voici la lettre BONUS !")
        motSaisiUser(console,contenu_du_fichier,jou_ekpActuel,lstResult,motadeviner,motAffiche,motSaisi,nbJoueurs,nbLettres,nbSaisi)
    console.print(f"✅ {nbLettresSaisi} lettres respectées !", style="green")
    with console.status("[blue]Vérification de l'existante du mot saisi") as status:
        sleep(1.5)
        motSaisi = "".join(motSaisi)
    if motSaisi not in contenu_du_fichier:
        motSaisi = list(motSaisi)
        console.print("❌ Le mot n'existe pas dans le dictionnaire !", style="bold bright_red")
        ltrBonus=motAffiche.index(".")
        motAffiche[ltrBonus]=motadeviner[ltrBonus]
        nbSaisi += 1
        sleep(2)
        console.clear()
        if nbJoueurs == 2:
            nbSaisi -= 1
            jou_ekpActuel += 1
            if jou_ekpActuel > nbJoueurs:
                jou_ekpActuel = 1
            console.print(f"C'est au tour du joueur {jou_ekpActuel} !")
        elif nbJoueurs > 2:
            nbSaisi -= 1
            jou_ekpActuel += 1
            if jou_ekpActuel > nbJoueurs:
                jou_ekpActuel = 1
            console.print(f"C'est au tour de l'équipe {jou_ekpActuel} !")
        else:
            console.print("Voici la lettre BONUS !")
        motSaisiUser(console,contenu_du_fichier,jou_ekpActuel,lstResult,motadeviner,motAffiche,motSaisi,nbJoueurs,nbLettres,nbSaisi)
    console.print("✅ Le mot existe bien dans le dictionnaire !", style="green")
    with console.status("[blue]Analyse du mot saisi...") as status:
        sleep(1.5)
    if motSaisi == motadeviner:
        nbSaisi += 1
        motadeviner = "".join(motadeviner)
        motadevinerTrouve(console,motadeviner,nbJoueurs,nbSaisi)
    else:
        verifsTOP(console,contenu_du_fichier,jou_ekpActuel,lstResult,motadeviner,motAffiche,motSaisi,nbJoueurs,nbLettres,nbSaisi)

"""Quand toutes les vérifications sont respectées"""
def verifsTOP(console,contenu_du_fichier,jou_ekpActuel,lstResult,motadeviner,motAffiche,motSaisi,nbJoueurs,nbLettres,nbSaisi):
    letter_count = {}
    # Création d'une map
    for letter in motadeviner:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    # Création de lstResult permettant de générer les couleurs
    for i in range(nbLettres):
        if motSaisi[i] == motadeviner[i] and motSaisi[i] in letter_count:
            letter_count[motSaisi[i]] -= 1
            if letter_count[motSaisi[i]] == 0:
                del letter_count[motSaisi[i]]
            lstResult[i] = 1
            motAffiche[i] = motadeviner[i]
        else:
            if motSaisi[i] in letter_count:
                letter_count[motSaisi[i]] -= 1
                if letter_count[motSaisi[i]] == 0:
                    del letter_count[motSaisi[i]]
                lstResult[i] = 2
            else:
                lstResult[i] = 0
    # Affichage des couleurs
    console.print("Résultat ->", style="underline", end="")
    console.print(" ", end="")
    for i in range(nbLettres):
        if lstResult[i] == 1:
            console.print(f"{motSaisi[i]}", style="red", end="")
        elif lstResult[i] == 2:
            console.print(f"{motSaisi[i]}", style="yellow", end="")
        else:
            console.print(f"{motSaisi[i]}", end="")
    console.print("\n----------")
    nbSaisi += 1
    if nbSaisi == 8:
        if nbJoueurs == 1:
            console.print(f"[bright_black]Perdu ! Il fallait trouver : [underline]{motadeviner}")
            choix = input("Veux-tu rejouer (O/N) ? -> ")
            if choix.lower() == "O" or choix.lower() == "o":
                preparation()
            else:
                exit()
        elif nbJoueurs == 2:
            nbSaisi -= 1
            jou_ekpActuel += 1
            if jou_ekpActuel > nbJoueurs:
                jou_ekpActuel = 1
            console.print(f"[bold red]Plus de saisies autorisées ![bold red] C'est au tour du joueur {jou_ekpActuel} !")
            console.print("\n----------")
            motSaisiUser(console,contenu_du_fichier,jou_ekpActuel,lstResult,motadeviner,motAffiche,motSaisi,nbJoueurs,nbLettres,nbSaisi)
        else:
            nbSaisi -= 1
            jou_ekpActuel += 1
            if jou_ekpActuel > nbJoueurs:
                jou_ekpActuel = 1
            console.print(f"[bold red]Plus de saisies autorisées ![bold red] C'est au tour de l'équipe {jou_ekpActuel} !")
            console.print("\n----------")
            motSaisiUser(console,contenu_du_fichier,jou_ekpActuel,lstResult,motadeviner,motAffiche,motSaisi,nbJoueurs,nbLettres,nbSaisi)
    motSaisiUser(console,contenu_du_fichier,jou_ekpActuel,lstResult,motadeviner,motAffiche,motSaisi,nbJoueurs,nbLettres,nbSaisi)

"""Message lorsque le mot a été deviné"""
def motadevinerTrouve(console,motadeviner,nbJoueurs,nbSaisi):
    console.print("Félicitations, vous avez trouvé le mot : " + motadeviner + f" en {nbSaisi} saisies !", style="green")
    sleep(1.5)
    console.clear()
    if nbJoueurs == 1:
        choix = input("Veux-tu rejouer (O/N) ? -> ")
        if choix.lower() == "O" or choix.lower() == "o":
            preparation()
        else:
            exit()

"""Début du programme"""
preparation()