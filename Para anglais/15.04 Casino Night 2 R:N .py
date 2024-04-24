'''
Casino night !

'''
#deposit of the player
somme_joueur= 100

#I import the time function so that the program can run with latencies
#between lines of code and make everything more readable

import time
import random


Rouge = [1,3,5,7,9,12,14,15,16,18,19,21,23,25,27,30,32,34,35,36]
Noir = [2,4,6,8,10,11,13,17,20,22,24,26,28,29,31,33]
#Beginning statement

print("Bruxelles Casino vous remercie de votre participation à notre grand concours de roulette !")
#time.sleep(1)
print("Un chiffre aléatoire de 1 à 36 va être généré à l'écran , vous avez l'occassion de parier comme ceci:")
#time.sleep(1)
print("Miser sur un chiffre précis , en cas de succès votre mise fera x36 ((mise*35)+mise)=gain")
#time.sleep(1)
print("Miser sur pair ou impair,ceci doublera la mise (mise+mise)= gain")
#time.sleep(1)
print("Miser sur rouge ou noir,ceci doublera la mise (mise+mise)= gain")
print(" Les noirs : " + str(Noir[:]))
print(" Les rouges : " + str(Rouge[:]))
#time.sleep(1)
print("Vous êtes le heureux propriétaire de 100 €")
#time.sleep(1)

#Repetitive bet / WHILE
#If somme_joueur = 0 , the game stops
#If pari > somme_joueur : the info is not taken in account ,
#the player is notticed  and the game restart 
while somme_joueur>0 :
    
    pari=input("Quelle somme souhaitez vous parier?")
    pari= int(pari)
    time.sleep(1)

    #conditions put in place according to the doability of the bet

    if pari>somme_joueur :
        print("Votre pari est plus grand que vos dépôts ! ")
        continue 
        
    elif pari==somme_joueur :
        print("All-in!")
        #We remove the bet from the deposit availaible of the player 
        somme_joueur = somme_joueur - pari
     
    elif pari<= 0:
        print("Vous ne pouvez pas miser en négatif ! ")
        continue
    else :
        print("Votre mise est de " + str(pari) + "€")
        #We remove the bet from the deposit availaible of the player 
        somme_joueur = somme_joueur - pari
        
    print("Pour rappel , votre déposit disponible est de " + str(somme_joueur) + "€")

    time.sleep(0.5)
    #BET CHOICES
    print("voulez vous parier sur pair / impair , sur Rouge / Noir ou sur un nombre ?")
    choice_bet= input("Tapez 1 pour le premier , 2 pour le second et 3 pour le dernier")
    choice_bet= int(choice_bet)
    
    if choice_bet == 1 :
        bet1_2= input("Tapez 1 pour impair et 2 pour pair ")
        bet1_2= int(bet1_2)
    elif choice_bet ==3 :
        betx = input ("Tapez le nombre désiré pour parier sa valeur ")
        betx= int(betx)
        if betx < 0 and betx > 36 :
            print("votre pari ne peut être plus petit que 0 et plus grand que 36")
            continue 
    elif choice_bet == 2:
        betr_n = input("tapez sur 1 pour le Rouge et sur 2 pour le noir ")
        betr_n = int(betr_n)
        
    #BET
    #on crée le chiffre gagnant :
    print("Faites vos jeux ! Rien ne va plus !")
    time.sleep(1)
    print("roulement de roulette...")
    time.sleep(1)
    print("... roll ... roll ... roll ...")
    time.sleep(1)
    roul_res = random.randint (0,36)
    print("Le numéro "+ str(roul_res) + "est tombé!")
    
    
    #on décide quel pari est d'application , puis on applique les conditions de gain
    if choice_bet == 1:
        
        #impair gagnant
        if bet1_2 == 1 and roul_res%2 != 0 :
            print("waw Impair gagnant !")
            gain = (pari *2)
        #Pair gagnat
        elif bet1_2 == 2 and roul_res%2 != 1 and roul_res != 0:
            print("waw Pair gagnant !")
            gain = (pari *2)
        #Impair perdant
        elif bet1_2 == 1 and roul_res% 2 == 0 :
            print("Oh noooooon")
            gain = 0
        #Pair perdant
        elif bet1_2 == 2 and roul_res% 2 == 1 :
            print("oh nooooooon")
            gain = 0
        elif roul_res == 0 :
            print("0 n'est ni pair ou impair !! Désolé...")
            gain= 0
        else :
            print("error")
    
    elif choice_bet == 2:
        #Noir gagnant
        if roul_res in Noir and betr_n in Noir :
            print("Noir gagnant!")
            gain = (pari *2)
        #Rouge gagnant
        elif roul_res in Rouge and betr_n in Rouge:
            print("Rouge gagnant !")
            gain = (pari *2)
        #Noir perdant
        elif roul_res in Rouge and betr_n in Noir :
            print("Noir perdant !")
            gain = 0
        #Rouge perdant
        elif roul_res in Noir and betr_n in Rouge :
            print("Rouge perdant !")
            gain = 0
        #0 perdant 
        else :
            print("0 est perdant ! Ni rouge ni Noir")
            gain = 0
            
        #precise Bet
    elif choice_bet == 3 :
        if betx == roul_res:
            print("WAOUUUW SA MER")
            gain = (pari * 36)
        elif betx != roul_res :
            print(".... c'était un pari risqué")
            gain = 0
        else :
            print(error)
            
        
    
    
    somme_joueur = somme_joueur + gain
    print("Votre argent en dépot est actuellement de : " + str(somme_joueur)+"€")
    
else :
    leave = "Votre déposit est passé à 0€ ... je vais devoir vous demander de sortir d'ici "
    print(leave)
  
            
    
        

    