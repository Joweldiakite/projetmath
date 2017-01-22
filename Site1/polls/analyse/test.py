import os
import webbrowser  #importation de la Bibliothèque webbrowser pour lancer le navigateur web
import random
import numpy
from scipy import stats # pour les statistiques
import matplotlib.pyplot as plt




c,d = os.path.split(os.getcwd())
print(c)

e = os.path.join(c, 'data')
print(e)
