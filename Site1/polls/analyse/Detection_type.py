# -*- coding:utf-8 -*-

import os
import random
import math

## pour dictionnaire
from operator import itemgetter
from collections import OrderedDict

## Faire Appel Aux Differents Donnees ##
from .DCG import*
from .DDG import*
from .DDNG import*
from .DCNG import*

########################################################
#### Fonction Pour Determiner Le Type de Donnees #######
########################################################
def Type_Donnees(*args):

# on separe le repertoire courant du reste du chemin
      #chemin,repertoire = os.path.split(os.getcwd())
# on creer le nouveau chemin vers les donnees
      #donnees = os.path.join(chemin, 'data')
      #fichiers = os.path.join(chemin,repertoire)
# on se place dans le dossier des donnees
      #os.chdir(donnees)
      ## args[0] = Nom_entree
      ## args[1] = Nbre_Classe

      #### Lecture des Donnees ####
      #with open(args[0], 'r') as fichier:
      #        data_temp = fichier.readlines()      
      data = [line.split() for line in args[0].split('\n')]
      print(data)
      Nbre_Col=len(data[0])
      print(' Nombre de Colonne : ', Nbre_Col)

      #os.chdir(fichiers)
      #### Si Nombre de Colonne =3, Il s'agit de DCG ####
      if Nbre_Col==3:
            Resultat='DCG'
            print(Resultat)
            return EcrireHTML_DCG(args[0])                     #### appel : Type_Donnees('exo4.dat')

      #### Si Nombre de Colonne =2, Il s'agit de DDG ####
      if Nbre_Col==2:
            Resultat='DDG'
            print(Resultat)
            return EcrireHTML_DDG(args[0])                    #### appel : Type_Donnees('exo03.dat')

      #### Si Nombre de Colonne =1 ####
      if Nbre_Col==1:
            Valeurs,Effectifs=Table_Valeurs([eval(data[i][0])
            for i in range(len(data))])
            if max(Effectifs)>2:                                  #### Valeurs Apparaissant 2 fois, Donc DDNG
                  Resultat='DDNG'
                  print(Resultat)
                  return EcrireHTML_DDNG(args[0])             #### appel : Type_Donnees('exo01.dat')

            else:                                                 #### Sinon, DCNG
                  Resultat='DCNG'
                  print(Resultat)
                  return EcrireHTML_DCNG(args[0], args[1])     #### appel : Type_Donnees('data_cng1.dat', 10)

############################################################
####  Fonctions Pour Determiner les Valeurs & Effectifs ####
############################################################
def Table_Valeurs(data):
      Table = {}

      ### On cree un dictionnaire :
      ### Valeurs=Table.keys();
      ### Effectifs=Table.values();

      for x in data:
            if (x in Table):
                  Table[x] += 1
            else:
                  Table[x] = 1

      ### Ordonner le dictionnaire par les valeurs :
      ### OrderedDict(sorted(Table.items(), key=lambda t: t[0]))
      ### Ordonner le dictionnaire par les Effectifs :
      ### OrderedDict(sorted(Table.items(), key=lambda t: t[1]))


      Valeurs=[x for x in Table.keys()]
      Effectifs=[int(n) for n in Table.values()]

      return Valeurs,Effectifs


################################################################


#if __name__ == '__main__':

##    Type_Donnees('exo3.dat', 5)
##    Type_Donnees('exo01.dat')
##    Type_Donnees('exo03.dat')
##    Type_Donnees('exo4.dat'
