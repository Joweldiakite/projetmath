from __future__ import division ## La division 
import random
import webbrowser  # Bibliotheque pour le navigateur WEB
import matplotlib.pyplot as plt
from scipy import stats # pour les statistiques
import os
import numpy
import math

######################################################################
###### sous Fonction pour lire le fichiers de donnees pour DNCG ######
######################################################################

def Lecture_data(Nom_fichier, Nbre_Classe):
    with open(Nom_fichier, 'r') as fichier:
        data_temp = fichier.readlines()             

    data = [line.split() for line in data_temp]
    data = numpy.asfarray(data)                                 #Une liste de donnees groupees dans un fichier "Data"

    ligne = len(data)                                           # Nombre de Donnees à afficher "Notre fichier est un vecteur colonne"
    colonne=len(data[0])                                        # La taille de fichier (Le fichier de donnees) Colonne=1

    # fichiers à 1-colonne  "DCNG" : Le fichier test est represente par une colonne de donnees
    if colonne==1:                                              # La liste des donnees contenus dans un des fichiers
        x=[float(data[i]) for i in range(ligne)]
        return int(ligne), x, data                              # Retourne le nombre d'observation et les donnees 

######################################################################
########################## Fin sous Fonction #########################
######################################################################
    
def FDR_CNG(data,x):
## fonction de répartition empirique pour les données continues non groupées
    data=sorted(data)
    n=len(data)
    return len([i for i in range(n) if data[i] <= x])/n

def Quantile_CNG(data,alpha):
# x_alpha (Quantile d'ordra_alpha) vérifie : F(x_alpha)=alpha

    data=sorted(data)
    F=[FDR_CNG(data,data[i]) for i in range(len(data))]
    #temp=min([i for i in range(len(data)) if FDR_CNG(data,data[i])> alpha])
    temp=min([i for i in range(len(data)) if F[i]> alpha])
    # temp = premier indice tel F(x) > alpha
    
# x_alpha appartient à l'intervalle ]data[temp-1] ; data[temp][
# interpolation :
# (x_alpha-data[temp-1])/(data[temp]-data[temp-1]) = (F(x_alpha)-F(data[temp-1]))/(F(data[temp])-F(data[temp-1]))
    x_alpha=data[temp-1]+(data[temp]-data[temp-1])*(alpha-F[temp-1])/(F[temp]-F[temp-1])
    return x_alpha
    
######################################################################
############ sous Fonction pour ecriture en format HTML ##############
######################################################################

def EcrireHTML_DCNG(Nom_entree, Nbre_Classe):
    # recuperer le chemin du fichier
    base=os.path.basename(Nom_entree)
    # on separe le repertoire courant du reste du chemin
    chemin,repertoire = os.path.split(os.getcwd())
    # on creer le nouveau chemin vers les donnees
    donnees = os.path.join(chemin, 'data')
    # on se place dans le dossier des donnees
    os.chdir(donnees)
    
    ## pour reccuperer le nom du fichier sans extention ##
    Nom_fichier=os.path.splitext(base)[0]
    Nom_Figure = "".join((Nom_fichier, ".png"))


    ##  lecture des donnees   ##
    [Nbre_Observ, X, Y]=Lecture_data(Nom_entree, Nbre_Classe)                           # Lecture_data a en entree Nom_entree et on recupere le nombre d'observation et les donnees 
    
    ##  Determiner les  modalites et effectifs  ##
    [Modalites, effectifs] = TableData(X,Nbre_Classe)                                   # La Fonction TableData (Entree : les donnees X et Le nombre de classe / Sortie : Modalite qui represente les extremites de nos classes, Effectifs qui correspond au nombre d'observation par classe) 
    Frequences =[effectifs[i]/numpy.sum(effectifs) for i in range(len(effectifs))]      # La Frequence qui correspond au nombre d'effectif par classe sur l'ensemble d'effectifs de toutes les classes
    FDR = numpy.cumsum(Frequences)                                                      # La fonction de repartition : la frequence cumulee de l'ensembe des classes 

    ## La Determination de La Classe Modale ##
    maxEffect=max(effectifs)                     ## On recupere La Classe qui compose le plus d'effectifs      
    LeMax=numpy.argmax(effectifs)

    ClasseModale = [Modalites[LeMax] , Modalites[LeMax+1]] ## La Classe Modale 
    
     
    ## Pour Tracer l'histogramme :
    histo_CNG(X,Nbre_Classe,Nom_Figure) 
    
    # fichier contenant les commandes HTML
    Nom_html= "".join((Nom_fichier, ".html"))
    fichier= open(Nom_html, 'w')

    fichier.write("<!doctype html> \n")
    fichier.write(" <html lang=""fr""> \n")
    fichier.write("<meta charset=UTF-8"" />\n")

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
    fichier.write("<BODY style=""background-color: rgb(210, 216, 206)"" alink=""#000099"" link=""#000099"" vlink=""#990099""> \n")


    fichier.write("<nav><ul>\n")
    fichier.write("<li><a href=""#Table des fr&eacutequences"">Table des fr&eacutequences</a></li>\n")
    fichier.write("<li><a href=""#Tableau des r&eacutesultats"">Tableau des r&eacutesultats</a></li>\n")
    fichier.write("<li><a href=""#Histogramme"">Histogramme</a></li>\n")
    fichier.write("</ul></nav>\n")
    fichier.write("<br> <br> <br>\n") 
    
    fichier.write("<a id=""Table des frequences""> </a>\n")
    
    
    fichier.write("<br> <br> <br>\n")


    fichier.write("<br><br>\n")
    fichier.write("<CENTER>\n")
    fichier.write("<TABLE cellpadding=""10"" width=60%% BORDER=10 BORDERCOLOR=""#007FFF"" bgcolor=""#F5F5F5"" >\n")
    fichier.write("<TR>\n")
    fichier.write("<TD colspan=8 align=center><b>Table des fr&eacutequences<b></TD>\n")
    fichier.write("</TR>\n")
    fichier.write("<tr>\n")
    fichier.write("<th width=""20%%"" align=""center"">Bornes Gauches</th>\n")
    fichier.write("<th width=""20%%"" align=""center"">Bornes Droites</th>\n")
    fichier.write("<th width=""20%%"" align=""center"">Effectifs</th>\n")
    fichier.write("<th width=""20%%"" align=""center"">Fr&eacutequences</th>\n")
    fichier.write("<th width=""20%%"" align=""center"">Fr&eacutequences cumul&eacutees</th>\n")
    fichier.write("</tr>\n")
    fichier.write("\n")


    for i in range(len(effectifs)):
        fichier.write("<tr>\n")
        fichier.write("<td align=""center"">%6.2f</td><td align=""center"">%6.2f</td><td align=""center"">%6d</td><td align=""center"">%6.4f </td><td align=""center"">%6.4f </td>\n"
                      %(Modalites[i], Modalites[i+1], effectifs[i], Frequences[i], FDR[i]))
        fichier.write("</tr>\n")


    fichier.write("</TABLE>\n")


    fichier.write("<a id=""Tableau des resultats"">  </a>\n")

    fichier.write("</CENTER>\n")

    fichier.write(" <br><br> <a href=''#haut''>Haut de la page</a> <br> <br> \n")
    fichier.write("<br><br>\n")
    fichier.write("<CENTER>\n")
    fichier.write("<TABLE cellpadding=""10"" width=60%% BORDER=10 BORDERCOLOR=""#007FFF"" bgcolor=""#F5F5F5"" >\n")
    fichier.write("<TR>\n")
    fichier.write("<TD colspan=5 align=center><b>Statistiques descriptives des donn&eacutees<b></TD>\n")
    fichier.write("</TR>\n")

    ### Le Nombre d'element dans X ### 
    fichier.write("<tr>\n")
    fichier.write("<td align=""center""> Nombre d'observations </td>\n")
    fichier.write("<td align=""center""> %d </td>\n" %(len(X)))                                          
    fichier.write("</tr>\n")
    
    ### La Valeur Mini ###
    fichier.write("<tr>\n")
    fichier.write("<td align=""center""> Minimum  </td>\n")
    fichier.write("<td align=""center""> %.6f </td>\n" %(numpy.min(X)))                                    
    fichier.write("</tr>\n")           

    ### La Valeur Maxi de X ###
    fichier.write("<tr>\n")
    fichier.write("<td align=""center""> Maximum  </td>\n")
    fichier.write("<td align=""center""> %.6f </td>\n"  %(numpy.max(X)))                                   
    fichier.write("</tr>\n")

    ### La Valeur Moyenne ###
    fichier.write("<tr>\n")
    fichier.write("<td align=""center""> Moyenne   </td>\n")
    fichier.write("<td align=""center""> %.6f </td>\n" %(numpy.mean(X)))                                
    fichier.write("</tr>\n")

    ### L'ecart-Moyen ###
    fichier.write("<tr>\n")
    fichier.write("<td align=""center""> Ecart Moyen   </td>\n")
    fichier.write("<td align=""center""> %.6f </td>\n" %(numpy.mean(numpy.fabs(X-numpy.mean(X)))))      
    fichier.write("</tr>\n")

    ### La Variance ###
    fichier.write("<tr>\n")
    fichier.write("<td align=""center""> Variance   </td>\n")
    fichier.write("<td align=""center""> %.6f </td>\n" %(numpy.var(X)))                                 
    fichier.write("</tr>\n")

    ### L'ecart-Type ###
    fichier.write("<tr>\n")
    fichier.write("<td align=""center""> Ecart-type   </td>\n")
    fichier.write("<td align=""center""> %.6f </td>\n" %(numpy.std(X)))                                 # Calcule & Affichage de l'ecart-type de X                  
    fichier.write("</tr>\n")

    ### Calcule du Quartile ### 
    fichier.write("<tr>\n")
    fichier.write("<td align=""center""> Premier quartile   </td>\n")
    fichier.write("<td align=""center"">%6.6f </td>\n" %Quantile_CNG(X,0.25))
    fichier.write("</tr>\n")
    
    fichier.write("<tr>\n")
    fichier.write("<td align=""center""> M&eacutediane   </td>\n")
    fichier.write("<td align=""center"">%6.6f </td>\n" %Quantile_CNG(X,0.5))
    fichier.write("</tr>\n")

    fichier.write("<tr>\n")
    fichier.write("<td align=""center"">Troisi&egraveme quartile   </td>\n")
    fichier.write("<td align=""center"">%6.6f </td>\n" %Quantile_CNG(X,0.75))
    fichier.write("</tr>\n")

    ### Les Modes ###
    fichier.write("<tr>\n")
    fichier.write("<td align=""center""> Mode   </td>\n")
    fichier.write("<td align=""center"">%6.6f </td>\n"  %(stats.mode(X)[0][0]))                                                            
    fichier.write("</tr>\n")
    
    ### La Valeur Effectif Max ###
    fichier.write("<tr>\n")
    fichier.write("<td align=""center""> Effectif Max   </td>\n")
    fichier.write("<td align=""center""> %.6f  </td>\n"  %(maxEffect))
    fichier.write("</tr>\n")

    ### La Classe Modale ###
    fichier.write("<tr>\n")
    fichier.write("<td align=""center""> Classe Modale   </td>\n")
    fichier.write("<td align=""center""> [%.6f , %.6f] </td>\n"  %(Modalites[LeMax] , Modalites[LeMax+1]))
    fichier.write("</tr>\n")

    ### La Moyenne Quadratique ###
    fichier.write("<tr>\n")
    fichier.write("<td align=""center""> Moyenne Quadratique  </td>\n")
    fichier.write("<td align=""center"">%6.6f </td>\n" %(numpy.sqrt(numpy.mean(Y**2))))                 
    fichier.write("</tr>\n")
    
    ### La Moyenne Geometrique ###
    if numpy.min(X) > 0:
        fichier.write("<tr>\n")
        fichier.write("<td align=""center""> Moyenne G&eacuteom&eacutetrique  </td>\n")
        fichier.write("<td align=""center"">%6.6f </td>\n" %(stats.gmean(X)))                           
        fichier.write("</tr>\n")

    ### La Moyenne Harmonique ###
    if numpy.min(X) > 0:
        fichier.write("<tr>\n")
        fichier.write("<td align=""center"">Moyenne Harmonique   </td>\n")
        fichier.write("<td align=""center"">%6.6f </td>\n" %(stats.hmean(X)))                               
        fichier.write("</tr>\n")


    fichier.write("</TABLE>\n")
    fichier.write("</CENTER>\n")


    fichier.write("<br><br> <a href=''#haut''>Haut de la page</a> <br> <br> \n ")
    fichier.write("<p align=""center"" > \n")

    fichier.write("<p align=""center"" > \n")
    fichier.write("<a id=""Histogramme"">\n")
        
    # Inclure la figure en format png
    fichier.write("<br><br><br>\n")
    
    fichier.write("<p align=""center"" ><IMG SRC=""%s""  \n" %(Nom_Figure))
    fichier.write("width=""650"" height=""500"" border=""0"" \n")
    fichier.write("align=""middle""\n")
    fichier.write("TITLE=""Histogramme des donn&eacutees""></p>\n")
    fichier.write("<p align=""center""><b>Histogramme des donn&eacutees</b></p>\n")

    fichier.write("\n")
    fichier.write("</a>  </p>\n")

    fichier.write("<a href=''#haut''>Haut de la page</a>\n")
    fichier.write("</body>\n")
    fichier.write("</html>\n")

    fichier.close()

    
    webbrowser.open(Nom_html)  # ouverture du fichier HTML dans le navigateur web

#####################################################################
########################## Fin sous Fonction ########################
#####################################################################
    

########################################################################
############### sous Fonction pour l'affichage du Histo ################
########################################################################

### Fonction Histogramme ###
def histo_CNG(data,Nbre_Classe,Nom_figure):
    Taille = len(data)                              # La taille du fichier de donnees 
    X0=numpy.min(data)                              # Extremite gauche de l'Histo
    X1=numpy.max(data)                              # Extremite droite de l'Histo
    Y=numpy.array([X0+(X1-X0)*i/Nbre_Classe for i in range(Nbre_Classe+1)])  # Les Bornes des 10 classes

    Nbre_Observ=numpy.empty(Nbre_Classe)            # Cree les 10 classes avec des valeurs aleatoires 
    Centre=numpy.empty(Nbre_Classe)                 # Cree un tableau de 10 valeurs aleatoires qui correspond initialement au centre des classes

    for i in range(Nbre_Classe):
        Centre[i]=0.5*(Y[i+1]+Y[i])
        Nbre_Observ[i]=0
        for j in range(Taille):
            if (data[j] >= Y[i] and data[j] <= Y[i+1]):
                Nbre_Observ[i]=Nbre_Observ[i]+1

    largeur = Y[1]-Y[0]
    fig = plt.figure()
    plt.gcf().subplots_adjust(bottom=0.2)
    ax = fig.add_subplot(111)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.hold(True)
    for i in range(Nbre_Classe):
        plt.bar(Centre[i], Nbre_Observ[i],color=[random.random(),random.random(),random.random()],edgecolor='red',width=largeur, align = 'center')
        ax.text(Centre[i], Nbre_Observ[i]+10,'%d' %(Nbre_Observ[i]),horizontalalignment='center',verticalalignment='center', fontsize=10)

    plt.ylim([0,numpy.max(Nbre_Observ)*1.1])
    plt.xlim([X0-(largeur/2),X1+(largeur/2)])
    
    plt.xticks([k for k in numpy.sort(numpy.append(Y,Centre))], fontsize=8,rotation=-45)
    plt.yticks([])
    
    plt.ylabel('Effectifs', size=16)
    plt.xlabel('Valeurs', horizontalalignment='center', verticalalignment='top',fontsize=16)
    plt.title("Repartitions des donnees en %d classes" %(Nbre_Classe),fontsize=10)
    
    plt.savefig(Nom_figure,format='png')
    ## plt.show()##
    plt.close()

    
### Fonction TableData (Modalites & Effectifs) ###
def TableData(data, Nbre_Classe):
    Taille = len(data)

    X0=numpy.min(data)
    ##print('Extremite Gauche Histo :', X0)
    X1=numpy.max(data)
    ##print('Extremite Droite Histo :', X1, " \n")


    Y=numpy.array([X0+(X1-X0)*i/Nbre_Classe for i in range(Nbre_Classe+1)])
    ##print('Les Classes :', Y, " \n")

    Nbre_Observ=numpy.empty(Nbre_Classe)
    Centre=numpy.empty(Nbre_Classe)
    
    for i in range(Nbre_Classe):
        Centre[i]=0.5*(Y[i+1]+Y[i])
        Nbre_Observ[i]=0
        for j in range(Taille):
            if (data[j] >= Y[i] and data[j] <= Y[i+1]):
                Nbre_Observ[i]=Nbre_Observ[i]+1               
    
    ##print("Centre des Classes :", Centre, " \n")
    return Y, Nbre_Observ  



######################################################################
##################### Execution du fichier DCNG  #####################
######################################################################

 
## Execution par defaut

if __name__ == '__main__':

    EcrireHTML_DCNG(Nom_entree, Nbre_Classe)

    
