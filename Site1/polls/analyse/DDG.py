import os
import webbrowser  #importation de la Bibliotheque webbrowser pour lancer le navigateur web
import random
import numpy
from scipy import stats # pour les statistiques
import matplotlib.pyplot as plt



### sous fonction pour lire differents type de fichiers de données

def Lecture_data(data_temp):
    #with open(Nom_fichier, 'r') as fichier:
        #data_temp = fichier.readlines()
    data = [line.split() for line in data_temp.split('\n')]
    print(data.pop())
    data = numpy.asfarray(data)

    ligne = len(data)  # nombre de données
    colonne=len(data[0])

# fichiers à 1-colonne
    if colonne==1:
        x=[float(data[i]) for i in range(ligne)]
        return int(ligne), x

# fichiers à 2-colonnes
    if colonne==2:
        x=[float(data[i][0]) for i in range(ligne)]
        Effectifs=[int(data[i][1]) for i in range(ligne)]
        return int(numpy.sum(Effectifs)), x, Effectifs

# fichiers à 3-colonnes
    if colonne==3:
        x_g=[float(data[i][0]) for i in range(ligne)]
        x_d=[float(data[i][1]) for i in range(ligne)]
        Effectifs=[int(data[i][2]) for i in range(ligne)]
        return int(numpy.sum(Effectifs)), x_g, x_d, Effectifs

### fin sous fonction
#########################################

### sous fonction pour ecriture en format LaTeX


### sous fonction pour ecriture en format HTML

def EcrireHTML_DDG(data):

# recuperer le chemin du fichier
    #base=os.path.basename(Nom_entree)
# on separe le repertoire courant du reste du chemin
    #chemin,repertoire = os.path.split(os.getcwd())
# on creer le nouveau chemin vers les donnees
    #donnees = os.path.join(chemin, 'data')
# on se place dans le dossier des donnees
    #os.chdir(donnees)
# pour recuperer le nom du fichier sans extention
    Nom_fichier= "polls/result"

    Nom_Figure = "".join((Nom_fichier, ".png"))

###  lecture des donnees   ###
    nb_obs, modalites, effectifs=Lecture_data(data)

###  Determiner les frequences  ###
    Frequences =[effectifs[i]/numpy.sum(effectifs) for i in range(len(effectifs))]
    FDR = numpy.cumsum(Frequences)


###  Tracer l'histogramme  ###
    Histo_DDG(modalites, effectifs,Nom_Figure)


    # fichier contenant les commandes Html
    Nom_html= "".join((Nom_fichier, ".html"))
    fichier= open(Nom_html, 'w')

    fichier.write("<!doctype html> \n")
    fichier.write(" <html lang=""fr""> \n")
    fichier.write("<meta charset=UTF-8"" />\n" )

    fichier.write("<head>\n")

    fichier.write("<a name=""haut""></a>\n")
    fichier.write("<style>\n")
    fichier.write("ul { \n")
    fichier.write("font-family: Arial, Verdana;\n")
    fichier.write("font-size: 14px;\n")
    fichier.write("margin: 0;\n")
    fichier.write("padding: 0;\n")
    fichier.write("list-style: none;\n")
    fichier.write("}\n")
    fichier.write("ul li {\n")
    fichier.write("display: block;\n")
    fichier.write("position: relative;\n")
    fichier.write("float: left;\n")
    fichier.write("}\n")
    fichier.write("li ul {\n")
    fichier.write("display: none;\n")
    fichier.write("}\n")
    fichier.write("ul li a {\n")
    fichier.write("display: block;\n")
    fichier.write("text-decoration: none;\n")
    fichier.write("color: #ffffff;\n")
    fichier.write("border-top: 1px solid #ffffff;\n")
    fichier.write("padding: 5px 15px 5px 15px;\n")
    fichier.write("background: #5EB6DD;\n")
    fichier.write("margin-left: 1px;\n")
    fichier.write("white-space: nowrap;\n")
    fichier.write("}\n")
    fichier.write("ul li a:hover {\n")
    fichier.write("background: #8CC6D7;\n")
    fichier.write("}\n")
    fichier.write("li:hover ul {\n")
    fichier.write("display: block;\n")
    fichier.write("position: absolute;\n")
    fichier.write("}\n")
    fichier.write("li:hover li {\n")
    fichier.write("float: none;\n")
    fichier.write("font-size: 11px;\n")
    fichier.write("}\n")
    fichier.write("li:hover a { background: #3b3b3b; }\n")
    fichier.write(" li:hover li a:hover {\n")
    fichier.write("background: #1e7c9a;\n")
    fichier.write("}\n")
    fichier.write("</style>\n")
    fichier.write("</head>\n")
    Nom_html
    #fichier.write("<body style="background: rgb(210, 216, 206)" > \n")
    fichier.write("<BODY style=""background-color: rgb(210, 216, 206)"" alink=""#000099"" link=""#000099"" vlink=""#990099""> \n")


    fichier.write("<nav><ul>\n")
    fichier.write("<li><a href=""#Table des fr&eacutequences"">Table des fr&eacutequences</a></li>\n")
    fichier.write("<li><a href=""#Tableau des r&eacutesultats"">Tableau des r&eacutesultats</a></li>\n")
    fichier.write("<li><a href=""#Histogramme"">Histogramme</a></li>\n")
    fichier.write("</ul></nav>\n")
    fichier.write("<br> <br> <br>\n")

    fichier.write("<a id=""Table des fréquences""> </a>\n")


    fichier.write("<br> <br> <br>\n")


    fichier.write("<br><br>\n" )
    fichier.write("<CENTER>\n" )
    fichier.write("<TABLE cellpadding=""10"" width=60%% BORDER=10 BORDERCOLOR=""#007FFF"" bgcolor=""#F5F5F5"" >\n")
    fichier.write("<TR>\n" )
    fichier.write("<TD colspan=8 align=center><b>Table des fr&eacutequences<b></TD>\n" )
    fichier.write("</TR>\n" )
    fichier.write("<tr>\n" )
    fichier.write("<th width=""25%%"" align=""center"">Modalit&eacutes</th>\n" )
    fichier.write("<th width=""25%%"" align=""center"">Effectifs</th>\n" )
    fichier.write("<th width=""25%%"" align=""center"">Fr&eacutequences</th>\n" )
    fichier.write("<th width=""25%%"" align=""center"">Fr&eacutequences cumul&eacutees</th>\n" )
    fichier.write("</tr>\n" )
    fichier.write("\n" )

    z=0
    X=numpy.ones(nb_obs)

    for i in range(len(effectifs)):
        fichier.write("<tr>\n" )
        fichier.write("<td align=""center"">%6d</td><td align=""center"">%6d</td><td align=""center"">%6.4f </td><td align=""center"">%6.4f </td>\n"
                      %(modalites[i], effectifs[i],Frequences[i] , FDR[i]))
        fichier.write("</tr>\n" )
        for k in range(effectifs[i]):
            X[z]=modalites[i]
            z=z+1

    fichier.write("</TABLE>\n" )

    fichier.write("<a id=""Tableau des résultats"">  </a>\n")
    #fichier.write("</a>\n")

    fichier.write("</CENTER>\n" )

    fichier.write(" <br><br> <a href=''#haut''>Haut de la page</a> <br> <br> \n" )
    fichier.write("<br><br>\n" )
    fichier.write("<CENTER>\n" )
    fichier.write("<TABLE cellpadding=""10"" width=60%% BORDER=10 BORDERCOLOR=""#007FFF"" bgcolor=""#F5F5F5"" >\n")
    fichier.write("<TR>\n" )
    fichier.write("<TD colspan=5 align=center><b>Statistiques descriptives des donn&eacutees<b></TD>\n" )
    fichier.write("</TR>\n" )

    fichier.write("<tr>\n" )
    fichier.write("<td align=""center"">Nombre d'observations </td>\n" )
    fichier.write("<td align=""center"">%d </td>\n" %(len(X)) )
    fichier.write("</tr>\n" )
    #
    fichier.write("<tr>\n" )
    fichier.write("<td align=""center""> Minimum  </td>\n" )
    fichier.write("<td align=""center"">%d </td>\n" %(numpy.min(X))  )
    fichier.write("</tr>\n" )
    #
    fichier.write("<tr>\n" )
    fichier.write("<td align=""center""> Maximum  </td>\n" )
    fichier.write("<td align=""center"">%d </td>\n"  %(numpy.max(X)) )
    fichier.write("</tr>\n" )
    #
    fichier.write("<tr>\n" )
    fichier.write("<td align=""center"">Moyenne   </td>\n" )
    fichier.write("<td align=""center"">%6.6f </td>\n" %(numpy.mean(X)) )
    fichier.write("</tr>\n" )

    fichier.write("<tr>\n" )
    fichier.write("<td align=""center""> Ecart Moyen   </td>\n" )
    fichier.write("<td align=""center"">%6.6f </td>\n" %(numpy.mean(numpy.fabs(X-numpy.mean(X)))) )
    fichier.write("</tr>\n" )


    #
    fichier.write("<tr>\n" )
    fichier.write("<td align=""center""> Variance   </td>\n" )
    fichier.write("<td align=""center"">%6.6f </td>\n" %(numpy.var(X))  )
    fichier.write("</tr>\n" )
    #
    fichier.write("<tr>\n" )
    fichier.write("<td align=""center"">Ecart-type   </td>\n" )
    fichier.write("<td align=""center""> %6.6f</td>\n" %(numpy.std(X)) )
    fichier.write("</tr>\n" )
    #
    fichier.write("<tr>\n" )
    fichier.write("<td align=""center"">Premier quartile   </td>\n" )
    fichier.write("<td align=""center""> %d</td>\n" %(numpy.percentile(X, 25)))
    fichier.write("</tr>\n" )
    #
    fichier.write("<tr>\n" )
    fichier.write("<td align=""center""> M&eacutediane   </td>\n" )
    fichier.write("<td align=""center""> %d</td>\n" %(numpy.percentile(X, 50)))
    fichier.write("</tr>\n" )
    #
    fichier.write("<tr>\n" )
    fichier.write("<td align=""center"">Troisi&egraveme quartile   </td>\n" )
    fichier.write("<td align=""center""> %d</td>\n" %(numpy.percentile(X, 75)))
    fichier.write("</tr>\n" )
    #
    fichier.write("<tr>\n" )
    fichier.write("<td align=""center""> Mode   </td>\n" )
    fichier.write("<td align=""center""> %d</td>\n"  %(stats.mode(X)[0][0]))
    fichier.write("</tr>\n" )
    #
    fichier.write("<tr>\n" )
    fichier.write("<td align=""center""> Moyenne Quadratique  </td>\n" )
    fichier.write("<td align=""center"">%6.6f </td>\n" %(numpy.sqrt(numpy.mean(X**2))))
    fichier.write("</tr>\n" )

# condition pour la moyenne Géométrique
    if numpy.min(X) > 0:
        fichier.write("<tr>\n" )
        fichier.write("<td align=""center""> Moyenne G&eacuteom&eacutetrique  </td>\n" )
        fichier.write("<td align=""center"">%6.6f </td>\n" %(stats.gmean(X)))
        fichier.write("</tr>\n" )

    if numpy.min(X) > 0:
        fichier.write("<tr>\n" )
        fichier.write("<td align=""center"">Moyenne Harmonique   </td>\n" )
        fichier.write("<td align=""center"">%6.6f </td>\n" %(stats.hmean(X)))
        fichier.write("</tr>\n" )

#

    fichier.write("<tr>\n" )
    fichier.write("<td align=""center"">Skewness   </td>\n" )
    fichier.write("<td align=""center"">%6.6f </td>\n" %(stats.skew(X)))
    fichier.write("</tr>\n" )


#
    fichier.write("<tr>\n" )
    fichier.write("<td align=""center"">Kurtosis   </td>\n" )
    fichier.write("<td align=""center"">%6.6f </td>\n" %(stats.kurtosis(X, fisher=True)))
    fichier.write("</tr>\n" )

    fichier.write("</TABLE>\n" )
    fichier.write("</CENTER>\n" )


    fichier.write("<br><br> <a href=''#haut''>Haut de la page</a> <br> <br> \n ")
    fichier.write("<p align=""center"" > \n")

    fichier.write("<p align=""center"" > \n")
    fichier.write("<a id=""Histogramme"">\n")

    # Inclure la figure en format png
    fichier.write("<br><br><br>\n" )

    fichier.write("<p align=""center"" ><IMG SRC=""%s""  \n" %(Nom_Figure))
    fichier.write("width=""650"" height=""500"" border=""0"" \n" )
    fichier.write("align=""middle""\n" )
    fichier.write("TITLE=""Histogramme des donn&eacutees""></p>\n" )
    fichier.write("<p align=""center""><b>Histogramme des donn&eacutees</b></p>\n" )

    fichier.write("\n" )
    fichier.write("</a>  </p>\n")

    fichier.write("<a href=''#haut''>Haut de la page</a>\n")
    fichier.write("</body>\n" )
    fichier.write("</html>\n" )

    fichier.close()



    webbrowser.open(Nom_html)  #ouverture du fichier HTML dans le navigateur web

### fin sous fonction

def Histo_DDG(valeurs, nb_obs,Nom_figure):
    largeur=0.4
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.hold(True)
    for i in range(len(valeurs)):
        plt.bar(valeurs[i], nb_obs[i],color=[numpy.random.rand(),numpy.random.rand(),numpy.random.rand()],
            edgecolor='white',width=largeur, align = 'center')
        ax.text(valeurs[i], nb_obs[i]+0.3,'%d' %(nb_obs[i]),
                horizontalalignment='center',
                verticalalignment='center', fontsize=10)

    plt.ylim([0,numpy.max(nb_obs)+0.5])
    plt.xlim([numpy.min(valeurs)-largeur,numpy.max(valeurs)+largeur])

    plt.xticks([k for k in valeurs])
    plt.yticks([])
    plt.ylabel('Effectifs', size=16)
    plt.xlabel('Valeurs', size=16)

    plt.savefig(Nom_figure,format='png')
    plt.close()


if __name__ == '__main__':

    EcrireHTML_DDG(Nom_entree)
