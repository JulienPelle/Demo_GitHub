#annee = input("saisissez une année :")
#annee = int(annee)
#bissextile = False

#if annee%400 == 0:
#	bissextile = True
#elif annee%100 == 0:
#	bissextile = False
#elif annee%4 == 0:
#	bissextile = True

#import os # On importe le module os
#os.system("pause")
#if annee%400==0 or (annee%4==0 and annee%100!=0):
#	print(annee,"est bissextile")
#else:
#print(annee,"n'est pas bissextile")

# Table de multiplication :
#n = int(input("Saisir un nombre"))
#i=0
#while i<=10:
#        print(n, "*",i,"=",n*i)
#        i+=1

# Parcours d'une chaine de caractères
#sequence = input("saisir une chaine de caractères :")
#for lettre in sequence:
#        if lettre in "aeiouAEIOU":
#                print(lettre, "est une voyelle")
#                break
#        else:
#                print(lettre, "est une consonne")
#        print(lettre)

# Test de l'instruction Continue
#i = int(input("saisir un chiffre"))
#while i+4<100:
#        i+=4
#        if i%3==0:
#                print(i,"est un multiple de 3")
#                continue
#        print(i,"n'est pas un multiple de 3")
        
# Fonction Multiplication  (avec max égal à 10 si max non renseigné lors de l'appel)
def multiplication(nb=1,max =10):
        """Fonction affichant la table de multiplication par nb
    de 1*nb à max*nb
    (max >= 0)"""
        i=1
        while i<=max:
                print(nb,"*",i,"est égale à",nb*i)
                i+=1

# Code pas exécuté en cas d'appel du module
if __name__ == __main__:
        print("code pas exécuté en cas d'appel")
                
# Appel fonction multiplication
#multiplication(3,7)
#multiplication(nb=3)
# Appel fonction d'aide pour multiplication
#help(multiplication)

# Appel fonction avec un return
def multiple3 (nb=3):
        return nb%3==0
# Appel précédente fonction
#valeur=multiple3(15)
#print(multiple3(27))

# Autre façon de créer et d'appeler une fonction : lambda
res = lambda x,y: x*y
#print(res(2,3))

# Utilisation de fonctions du module import
import math
#help("math")
#print(math.sqrt(16))
#help("math.sqrt")

# Import seulement de la fonction pi du module math
help("math.exp")
from math import exp
print(exp(2))
# Import de toutes les fonctions du module math sans avoir à taper math
from math import *
