#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import sys
sys.path.insert(0, "C:\\Users\\69juj\\Google Drive\\Sauvegarde PC\\Cours\Polytech\\2021 TRIM-3\\INF1007\\Exercice dossier git\\2021a-c01-ch6-1-exercices-Julien9969")
from exercice_chap6 import frequence
import math
import turtle as ttl
import time



# TODO: Définissez vos fonction ici
def V_elipsoide(a, b, c, Mv):
    volume = (4 / 3) * math.pi * a * b * c
    masse = volume * Mv
    return volume, masse

def frequence_chap6(phrase: str):
    # freq = frequence(sentence)
    xtx = frequence(phrase)
    
    return 

def arbre(taille):
    if taille < 60 :
        return
    else:
        ttl.color("green")
        ttl.forward(taille)
        ttl.left(30)
        arbre(taille*0.75)
        ttl.right(60)
        arbre(taille*0.75)
        ttl.left(30)
        ttl.backward(taille)
        

    # if taille < 10 :
    #     return
    # else:
    #     ttl.color("red")
    #     ttl.forward(taille)
    #     ttl.left(30)
    #     arbre(taille*0.75)
    #     ttl.right(60)
    #     arbre(taille*0.75)
    #     ttl.left(30)
    #     arbre(taille*0.75)
    #     ttl.backward(taille)
        
        
    
def adn_proportion (chaine, sequence):
    nb_seq = chaine.count(sequence)
    longueur_chaine = len(chaine)
    proportion = round((nb_seq/longueur_chaine) * 100 , 2)

    return proportion






if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    volume, masse = V_elipsoide(2, 3, 4, 10)
    txt = "le volume de l'elipsoide est {} et sa masse est {}"
    print(txt.format(volume, masse))

    phrase = "le volume de l'elipsoide est 100.53096491487338 et sa masse est 1005.3096491487338"
    print(frequence_chap6(phrase))

    taille = 100
    ttl.left(90)
    arbre(taille)
    ttl.done()



    valide_letter = set("atgc")
    print("chaine et sequence sont une combinaison de a,t,g,c")
    chaine = input("saisir chaine : ")
    set_chaine = set(chaine)
    for letter in set_chaine:
        if letter not in valide_letter:
            print("chaine invalide \n")
            chaine = input("saisir chaine : ")
            break

    sequence = input("saisir sequence : ")
    set_sequence = set(sequence)

    for letter in set_sequence:
        if letter not in valide_letter:
            print("chaine invalide \n")
            chaine = input("saisir chaine : ")
            break


    proportion = adn_proportion(chaine, sequence) 

    txt = "chaîne : {} \n" + "séquence : {} \n" + "Il y a {} % de {}."
    print(txt.format(chaine, sequence, proportion, sequence))


