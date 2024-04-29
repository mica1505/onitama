import matplotlib.pyplot as plt
import numpy as np


def graphics(matchs,scores_ia_facile,scores_ia_moyen,ia_petit,ia_grand):


    plt.figure(figsize=(10, 6))


    plt.bar([match - 0.2 for match in matchs], scores_ia_facile, width=0.4, color='blue', label='IA Facile')

    plt.bar([match + 0.2 for match in matchs], scores_ia_moyen, width=0.4, color='orange', label='IA Moyen')


    plt.title('Résultats des matchs entre IA Facile et IA Moyen')
    plt.xlabel('Matchs')
    plt.ylabel('Scores')
    plt.xticks(matchs)
    plt.legend()
    plt.show()


    #HISTOGRAMME DE PARTIES GAGNES PAR CHAQUE IA

    victoires_ia_facile = sum(scores_ia_facile)
    victoires_ia_moyen = sum(scores_ia_moyen)

    plt.figure(figsize=(8, 6))
    plt.bar([ia_petit, ia_grand], [victoires_ia_facile, victoires_ia_moyen], color=['blue', 'orange'])

    plt.title('Nombre de victoires de chaque IA dans le tournoi')
    plt.xlabel('IA')
    plt.ylabel('Nombre de victoires')

    plt.show()

    #TRACE

    # Comptage du nombre de victoires pour chaque IA
    victoires_ia_facile = sum(score_facile > score_moyen for score_facile, score_moyen in zip(scores_ia_facile, scores_ia_moyen))
    victoires_ia_moyen = sum(score_moyen > score_facile for score_facile, score_moyen in zip(scores_ia_facile, scores_ia_moyen))

    plt.figure(figsize=(8, 6))

    plt.plot(range(1, len(scores_ia_facile) + 1), scores_ia_facile, label=ia_petit, marker='o', color='blue')
    plt.plot(range(1, len(scores_ia_moyen) + 1), scores_ia_moyen, label=ia_grand, marker='o', color='orange')

    plt.title('Victoires de chaque IA dans le tournoi')
    plt.xlabel('Matchs')
    plt.ylabel('Nombre de victoires')
    plt.legend()

#---------------------FACILE vs MOYEN--------------------------------------
'''
matchs = [1, 2, 3, 4, 5, 6, 7]
scores_ia_facile = [10, 25, 23, 0, 24, 22, 14]
scores_ia_moyen = [20, 25, 27, 6, 26, 28, 36]
graphics(matchs,scores_ia_facile,scores_ia_moyen,"IA Facile","IA Moyen")'''
#---------------------FACILE vs DIFFICILE--------------------------------------
m = [1,2,3,4,5,6,7,8]
scores_facile = [12,4,10,27,1,6,0,1]
scores_difficile = [0,2,1,17,6,5,3,2]

#graphics(m,scores_facile,scores_difficile,"IA Facile", "IA Difficile")


#-----------------MOYEN vs DIFFICILE-------------------------------------------
m = [1,2]
scores_moyen = [41,38]
scores_difficile = [9,12]

graphics(m,scores_moyen,scores_difficile,"IA Moyen","IA Difficile")