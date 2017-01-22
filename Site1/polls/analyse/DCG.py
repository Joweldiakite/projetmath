import os
import webbrowser  #importation de la Bibliotheque webbrowser pour lancer le navigateur web
import random
import numpy
from scipy import stats # pour les statistiques
import matplotlib.pyplot as plt


### sous fonction pour lire differents type de fichiers de donnees

def Lecture_data(data):
    #with open(Nom_fichier, 'r') as fichier:
    #    data_temp = fichier.readlines()

    #data = [line.split() for line in data_temp]
    data = numpy.asfarray(data)

    ligne = len(data)  # nombre de donnees
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

### sous fonction pour le calcul des quartiles

def FDR_CG(x_G,x_D,Effectif):
## fonction de repartition empirique pour les donnees continues  groupees
    n=numpy.sum(Effectif)  # nombre total d'observations
    F=numpy.cumsum(Effectif)
    #F(i)= fonction de repartition empirique de la Classe N° i
    return [x/n for x in F]

def Quantile_CG(x_G,x_D,Effectif,alpha):
# x_alpha (Quantile d'ordra_alpha) verifie : F(x_alpha)=alpha


    F=FDR_CG(x_G,x_D,Effectif)
    temp=min([i for i in range(len(F)) if F[i]> alpha])
    # temp = premier indice tel F(x) > alpha

# x_alpha appartient à l'intervalle ]x_G[temp] ; x_D[temp][
# interpolation :
# (x_alpha-x_G[temp])/(x_D[temp]-x_G[temp]) = (F(x_alpha)-F(x_G[temp]))/(F(x_D[temp])-F(x_G[temp]))
    x_alpha=x_G[temp]+(x_D[temp]-x_G[temp])*(alpha-F[temp-1])/(F[temp]-F[temp-1])
    return x_alpha
###############################################

### sous fonction pour ecriture en format LateX



### sous fonction pour ecriture en format HTML

def EcrireHTML_DCG(Nom_entree):

    # recuperer le chemin du fichier
    base=os.path.basename(Nom_entree)
    # on separe le repertoire courant du reste du chemin
    chemin,repertoire = os.path.split(os.getcwd())
    # on creer le nouveau chemin vers les donnees
    donnees = os.path.join(chemin, 'data')
    # on se place dans le dossier des donnees
    os.chdir(donnees)

    # pour reccuperer le nom du fichier sans extention
    Nom_fichier=os.path.splitext(base)[0]


    Nom_Figure = "".join((Nom_fichier, ".png"))

    ###  lecture des donnees   ###
    nb_obs,x_g,x_d,Effectifs=Lecture_data(Nom_entree)


    ###  Determiner les  bornes et effectifs  ###
    Centre = Center(x_g, x_d)
    Frequences =[Effectifs[i]/numpy.sum(Effectifs) for i in range(len(Effectifs))]
    FDR = numpy.cumsum(Frequences)

    ###  Tracer l'histogramme  ###
    Histo_DCG(x_g, x_d, Centre, Effectifs,Nom_Figure)


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
    fichier.write("font-size: 14px;\n")                         #taille texte haut gauche
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
    fichier.write("color: #ffffff;\n")                          #couleur texte haut gauche
    fichier.write("border-top: 1px solid #ffffff;\n")
    fichier.write("padding: 5px 15px 5px 15px;\n")
    fichier.write("background: #5EB6DD;\n")                     #couleur fond texte (haut gauche)
    fichier.write("margin-left: 1px;\n")
    fichier.write("white-space: nowrap;\n")
    fichier.write("}\n")
    fichier.write("ul li a:hover {\n")
    fichier.write("background: #8CC6D7;\n")                     #couleur surbrillance (haut gauche)
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

    fichier.write("<a id=""Table des frequences""> </a>\n")


    fichier.write("<br> <br> <br>\n")


    fichier.write("<br><br>\n" )
    fichier.write("<CENTER>\n" )
    fichier.write("<TABLE cellpadding=""10"" width=60%% BORDER=10 BORDERCOLOR=""#007FFF"" bgcolor=""#F5F5F5"" >\n")
    fichier.write("<TR>\n" )
    fichier.write("<TD colspan=8 align=center><b>Table des fr&eacutequences<b></TD>\n" )
    fichier.write("</TR>\n" )
    fichier.write("<tr>\n" )
    fichier.write("<th width=""20%%"" align=""center"">Borne Gauche</th>\n" )
    fichier.write("<th width=""20%%"" align=""center"">Borne Droite</th>\n" )
    fichier.write("<th width=""20%%"" align=""center"">Effectifs</th>\n" )
    fichier.write("<th width=""20%%"" align=""center"">Fr&eacutequences</th>\n" )
    fichier.write("<th width=""20%%"" align=""center"">Fr&eacutequences cumul&eacutees</th>\n" )
    fichier.write("</tr>\n" )
    fichier.write("\n" )


    m = max(enumerate(Effectifs), key=(lambda x: x[1]))
    bornegauche = x_g[m[0]]
    bornedroite = x_d[m[0]]

    z=0
    X=numpy.ones(nb_obs)                            #creation d'un tableau X a une dimension de taille nb_obs

    for i in range(len(Effectifs)):
        fichier.write("<tr>\n" )
        fichier.write("<td align=""center"">%6d</td><td align=""center"">%6d</td><td align=""center"">%10d </td><td align=""center"">%6.4f </td>\n<td align=""center"">%6.4f</td>" %(x_g[i], x_d[i], Effectifs[i],Frequences[i], FDR[i]))
        fichier.write("</tr>\n" )
        for k in range(Effectifs[i]):               #permet de remplir le tableau X avec tous les centres
            X[z]=Centre[i]
            z=z+1

    fichier.write("</TABLE>\n" )


    fichier.write("<a id=""Tableau des resultats"">  </a>\n")
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
    fichier.write("<td align=""center"">%d </td>\n" %(nb_obs) )
    fichier.write("</tr>\n" )
    #
    fichier.write("<tr>\n" )
    fichier.write("<td align=""center""> Minimum  </td>\n" )
    fichier.write("<td align=""center"">%d </td>\n" %(numpy.min(x_g))  )
    fichier.write("</tr>\n" )
    #
    fichier.write("<tr>\n" )
    fichier.write("<td align=""center""> Maximum  </td>\n" )
    fichier.write("<td align=""center"">%d </td>\n"  %(numpy.max(x_d)) )
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
    fichier.write("<td align=""center""> %.1f</td>\n" %Quantile_CG(x_g,x_d,Effectifs,0.25))
    fichier.write("</tr>\n" )
    #
    fichier.write("<tr>\n" )
    fichier.write("<td align=""center""> M&eacutediane   </td>\n" )
    fichier.write("<td align=""center""> %.1f</td>\n" %Quantile_CG(x_g,x_d,Effectifs,0.5))
    fichier.write("</tr>\n" )
    #
    fichier.write("<tr>\n" )
    fichier.write("<td align=""center"">Troisi&egraveme quartile   </td>\n" )
    fichier.write("<td align=""center""> %.1f</td>\n" %Quantile_CG(x_g,x_d,Effectifs,0.75))
    fichier.write("</tr>\n" )
    #
    fichier.write("<tr>\n" )
    fichier.write("<td align=""center""> Classe Modale   </td>\n" )
    fichier.write("<td align=""center""> [ %d ; %d ] </td>\n" %(bornegauche, bornedroite))
    fichier.write("</tr>\n" )
    #
    fichier.write("<tr>\n" )
    fichier.write("<td align=""center""> Moyenne Quadratique  </td>\n" )
    fichier.write("<td align=""center"">%6.6f </td>\n" %(numpy.sqrt(numpy.mean(X**2))))
    fichier.write("</tr>\n" )

# condition pour la moyenne Geometrique
    if numpy.min(X) > 0:
        fichier.write("<tr>\n" )
        fichier.write("<td align=""center""> Moyenne G&eacuteom&eacutetrique  </td>\n" )
        fichier.write("<td align=""center"">%6.6f </td>\n" %(stats.gmean(X)))
        fichier.write("</tr>\n" )

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


###fin sous fonction
###############################################


### sous fonction pour faire un histogramme

def Histo_DCG(Gauche, Droite, centre, effectif ,Nom_figure):

    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.hold(True)
    for i in range(len(effectif)):
        largeur = Droite[i]-Gauche[i]
        plt.bar(centre[i], effectif[i],color=[numpy.random.rand(),numpy.random.rand(),numpy.random.rand()],
            edgecolor='white',width=largeur, align = 'center')
        ax.text(centre[i], effectif[i]+7,'%d' %(effectif[i]),
                horizontalalignment='center',
                verticalalignment='center', fontsize=10)

    plt.ylim([0,numpy.max(effectif)+0.5])
    plt.xlim([numpy.min(centre)-largeur,numpy.max(centre)+largeur])

    plt.xticks([k for k in Gauche+Droite])
    plt.yticks([])
    plt.ylabel('Effectifs', size=16)
    plt.xlabel('Valeurs', size=16)

    plt.savefig(Nom_figure,format='png')
    plt.close()

###fin sous fonction
###############################################

#sous fonction pour calculer le centre
def Center(Gauche, Droite):

    centre = []         # initialisation du tableau centre
    for i in range(len(Gauche)):     # pour i en fonction de la longueur du tableau Gauche, on fait
         centre.append(((Droite[i]-Gauche[i])/2)+Gauche[i])
    return centre

###fin sous fonction
#######################################


if __name__ == '__main__':

    EcrireHTML_DCG(Nom_entree)
