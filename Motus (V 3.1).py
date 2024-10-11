"""Voici la version 3.1 du programme Motus. Ce programme reprend le célèbre jeu Motus"""

"""Modules"""
from random import choice, randint
from rich.console import Console
from rich.progress import Progress, SpinnerColumn
from time import sleep
from tqdm import tqdm
import os

"""Préparation"""
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
index_premiere_lettre = randint(0, nbLettres - 1)
motAffiche = motadeviner[0] + "." * (nbLettres - 1)
motAffiche = motAffiche[:index_aleatoire] + motadeviner[index_aleatoire] + motAffiche[index_aleatoire + 1:]
lstResult = [0 for i in range(nbLettres)]
nbSaisi = 0
motSaisi = 0
total = 100

"""Vérification des mises à jour"""
version_actuelle = "3.1"
fichiers = os.listdir()
fichiers_mise_a_jour = [fichier for fichier in fichiers if fichier.startswith("Motus (V")]

if fichiers_mise_a_jour:
    fichiers_mise_a_jour.sort(reverse=True)
    dernier_fichier = fichiers_mise_a_jour[0]
    debut_version = dernier_fichier.index("V") + 2
    fin_version = dernier_fichier.index(")")
    derniere_version = dernier_fichier[debut_version:fin_version]
    
    with console.status("[bright_black]Vérification des mises à jour...") as status:
        sleep(1.5)
    if derniere_version > version_actuelle:
        console.clear()
        console.print(f"Une mise à jour est disponible : {version_actuelle} -> {derniere_version}")
        choix = input("Voulez-vous mettre à jour Motus (O/N) ? ")
        
        if choix.lower() == "O" or choix.lower() == "o":
            with tqdm(total=total, desc="Téléchargement de la mise à jour ") as pbar:
                for i in range(total):
                    sleep(0.1)
                    pbar.update(1)
            sleep(1)
            with console.status("[red]Installation de la mise à jour") as status:
                sleep(5)
                console.clear()
                console.print(f"Mise à jour installé ! Pour pouvoir l'utiliser, assuez-vous d'écrire sur l'Invite de commandes : ", end="")
                console.print(f'[bold underline]python "Motus (V {derniere_version})".py')
                exit()
        else:
            console.clear()
    else:
        console.print("✅ Vous utilisez la dernière version !")
        sleep(1)
        console.clear()

"""Jeu"""
console.print(f"[bright_cyan]Tu as droit à [bold underline green]8[/bold underline green] saisies ! [italic](ne compte pas les erreurs)")
while motadeviner != motSaisi:
    if nbSaisi != 0:
        if nbSaisi<=3:
            console.print(f"[bright_green]Il te reste {8-nbSaisi} saisies !")
        elif nbSaisi<6:
            console.print(f"[dark_orange]Il te reste {8-nbSaisi} saisies !")
        elif nbSaisi==6:
            console.print(f"[red]Il te reste {8-nbSaisi} saisies !")
        elif nbSaisi==7:
            console.print(f"[bright_red]Il te reste {8-nbSaisi} saisi !")
        else:
            console.print(f"[bright_black]Perdu ! Il fallait trouver : [underline]{motadeviner}")
            exit()
    console.print(f"{motAffiche} -> {nbLettres} lettres")
    motSaisi = input("Quel mot proposes-tu ? -> ").strip().upper()
    nbLettresSaisi = len(motSaisi)
    progress = Progress(SpinnerColumn())
    #Vérification des conditions du mot saisi
    with console.status("[blue]Vérification de la 1ère lettre...") as status:
        sleep(1.5)
        if motSaisi == "" or motSaisi[0] != motadeviner[0]:
            console.print("❌ La première lettre ne correspond pas !", style="bold bright_red")
            console.print("\n----------")
            continue
        console.print("✅ 1ère lettre respectée !", style="green")
    with console.status("[blue]Vérification de la longueur du mot saisi...") as status:
        sleep(1.5)
        if len(motSaisi) != len(motadeviner):
            console.print(f"❌ {nbLettresSaisi} lettres sur {len(motadeviner)} de saisie(s) !", style="bold bright_red")
            console.print("\n----------")
            continue
        console.print(f"✅ {nbLettresSaisi} lettres respectées !", style="green")
    with console.status("[blue]Vérification de l'existante du mot saisi") as status:
        sleep(1.5)
        if motSaisi not in contenu_du_fichier:
            console.print("❌ Le mot n'existe pas dans le dictionnaire !", style="bold bright_red")
            console.print("\n----------")
            continue
        console.print("✅ Le mot existe bien dans le dictionnaire !", style="green")
    with console.status("[blue]Analyse du mot saisi...") as status:
        sleep(1.5)
    letter_count = {}
    #Création d'une map
    for letter in motadeviner:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    motAffiche = list(motAffiche)
    motSaisi = list(motSaisi)
    motadeviner = list(motadeviner)
    #Création dee lsResult permettant de générer les couleurs
    for i in range(nbLettres):
        if motSaisi[i] == motadeviner[i]:
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
        #Affichage des couleurs
    console.print("Résultat ->", style="underline", end="")
    console.print(" ",end="")
    for i in range(nbLettres):
        if lstResult[i] == 1:
            console.print(f"{motSaisi[i]}", style="red", end="")
        elif lstResult[i] == 2:
            console.print(f"{motSaisi[i]}", style="yellow", end="")
        else:
            console.print(f"{motSaisi[i]}", end="")
    motAffiche = "".join(motAffiche)
    motSaisi = "".join(motSaisi)
    motadeviner = "".join(motadeviner)
    console.print("")
    console.print("\n----------")
    nbSaisi += 1
#Message lorsque le mot a été deviné
console.print("Félicitations, vous avez trouvé le mot : " + motadeviner + f" en {nbSaisi} saisies !", style="green")