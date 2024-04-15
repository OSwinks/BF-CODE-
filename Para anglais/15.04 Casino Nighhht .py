'''
Casino night !

'''
#Dépôt of the player
somme_joueur= 100

#I import the time function so that the program can run with latencies
#between lines of code and make everything more readable

import time
import random 

#Beginning statement

print("Bruxelles Casino vous remercie de votre participation à notre grand concours !")
time.sleep(1)
print("Vous êtes le heureux propriétaire de 100 €")
time.sleep(1)

#Repetitive bet
#If somme_joueur = 0 , the game stops
#If pari > somme_joueur : the info is not taken in account ,
#the player is notticed  and the game restart 

pari=input("Quelle somme souhaitez vous parier?")
pari= int(pari)
time.sleep(1)


if pari>somme_joueur :
    print("Votre pari est plus grand que vos dépôts ! ")
elif pari==somme_joueur :
    print("All-in!")
elif pari<= 0:
    print("Vous ne pouvez pas miser en négatif ! ")
else :
    print("Votre mise est de " + str(pari) + "€") 
    
 
print(random)
    