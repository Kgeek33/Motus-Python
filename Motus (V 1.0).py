from random import choice, randint
from rich.console import Console
from time import sleep
import os

console = Console()
with open("Dictionnaire.txt", encoding="utf-8") as file:
    contenu_du_fichier = file.readlines()
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

version_actuelle = "1.0"
fichiers = os.listdir()
fichiers_mise_a_jour = [fichier for fichier in fichiers if fichier.startswith("Motus (V")]

if fichiers_mise_a_jour:
    fichiers_mise_a_jour.sort(reverse=True)
    dernier_fichier = fichiers_mise_a_jour[0]
    debut_version = dernier_fichier.index("V") + 2
    fin_version = dernier_fichier.index(")")
    derniere_version = dernier_fichier[debut_version:fin_version]
    
    if derniere_version > version_actuelle:
        print("Une nouvelle version est disponible :", derniere_version)
        choix = input("Voulez-vous utiliser la nouvelle version ? (O/N): ")
        
        if choix.lower() == "O" or choix.lower() == "o":
            console.print("Téléchargement de la mise à jour en cours...")
            sleep(10)
            console.print("Installation de la mise à jour...")
            sleep(5)
            console.clear()
            console.print(f"Mise à jour installé ! Pour pouvoir l'utiliser, assuez-vous d'écrire sur l'Invite de commandes : ", end="")
            console.print(f'[bold underline]python "Motus (V {derniere_version})".py')
            exit()
        else:
            print("Vous continuez à utiliser la version actuelle.")


while motadeviner != motAffiche:
    console.print(f"{motAffiche} -> {nbLettres} lettres")
    motsaisi = input("Quel mot proposes-tu ? -> ").strip().upper()
    nbLettresSaisi = len(motsaisi)

    if nbLettresSaisi != nbLettres:
        console.print("Le nombre de lettres est incorrect !", style="bold red")
    else:
        letter_count = {}
        for letter in motadeviner:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
        motAffiche = list(motAffiche)
        for i in range(nbLettres):
            if motsaisi[i] == motadeviner[i]:
                letter_count[motsaisi[i]] -= 1
                if letter_count[motsaisi[i]] == 0:
                    del letter_count[motsaisi[i]]
                lstResult[i] = 1
                motAffiche[i] = motadeviner[i]
        for i in range(nbLettres):
            if motsaisi[i] in letter_count:
                letter_count[motsaisi[i]] -= 1
                if letter_count[motsaisi[i]] == 0:
                    del letter_count[motsaisi[i]]
                lstResult[i] = 2
            else:
                lstResult[i] = 0

        for i in range(nbLettres):
            if lstResult[i] == 1:
                console.print(motsaisi[i], style="red", end="")
            elif lstResult[i] == 2:
                console.print(motsaisi[i], style="yellow", end="")
            else:
                console.print(motsaisi[i], end="")

        motAffiche = "".join(motAffiche)
        console.print("\n----------")

console.print("Félicitations, vous avez trouvé le mot : " + motadeviner, style="green")
