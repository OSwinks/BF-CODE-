'''
Casino night !

'''
# on importe les libraires Time et random
import time
import random
#Fonction print with sleep 
def slow_print1 (x) :
    print(x)
    time.sleep(0.5)
def slow_print0_5 (x) :
    print(x)
    time.sleep(0.5)
def slow_print2 (x) :
    print(x)
    time.sleep(0.5)

#deposit of the player
somme_joueur= 100
#Red and Black lists 
Rouge = [1,3,5,7,9,12,14,15,16,18,19,21,23,25,27,30,32,34,35,36]
Noir = [2,4,6,8,10,11,13,17,20,22,24,26,28,29,31,33]

#Fonctions pour determiner le nombre de paris:
def nmb_bet(x):
    if x>somme_joueur:
        print("Vous ne pouvez parier plus de paris que votre dépôt ne le permets (1€/pari)")
    elif somme_joueur==0 :
        print("Votre dépôt est à zéro")
    else : 
        return x 

#fonction pour determiner le paris 
def bet_choice(x):
    print("c'est votre pari numéro " + str(i+1) +"!")
    print("Voulez vous parier sur pair / impair , sur Rouge / Noir ou sur un nombre ?\n Tapez sur 1 , 2 ou 3!")
    def_bet = int(input("Quel paris souhaitez vous réaliser ? "))
    #Conditions fausses
    if def_bet > 3 :
        print("Mauvaise réponse")      
    elif def_bet<= 0:
        print("Mauvaise réponse")    
    else : 
        return def_bet
#Fonction pair / Impair 

    #Pair / Impair
def bet_1_2 (x):
        b1_2 = int(input("Voulez vous parier impair(1) ou sur pair?(2)"))
        if b1_2 != 1 and b1_2 != 2 :
            print("mauvaise réponse")
        elif b1_2 == 1 :
            print("Votre pari "+str([i+1]) + "est Impair! ")
            return b1_2
        else : 
            ("Votre pari "+str([i+1]) + "est Pair ")
            return b1_2
 #Fonction Rouge / Black 
    #Rouge / Black
def bet_R_B (x):
        bR_B = int(input("Voulez vous pariez Rouge(1) ou Noir (2)"))
        if bR_B != 1 and bR_B != 2 :
            print("mauvaise réponse")
        elif bR_B == 1 :
            print("Votre pari est Rouge! ")
            return bR_B
        else : 
            ("Votre pari est Pair ")
            return bR_B
#Fonction nombre précis 

    #Nombre précis 
def bet_nmb (x) :
        b_nmb = int(input("Quel nombre souhaitez vous parier ?"))
        if b_nmb < 0 or b_nmb > 36 :
            print("mauvaise réponse")
        else:
            print("Votre pari "+str([i+1]) +  "est sur le numéro" +str(b_nmb) + " ." )
            return b_nmb




slow_print1("Bruxelles Casino vous remercie de votre participation à notre grand concours de roulette !\nUn chiffre aléatoire de 1 à 36 va être généré à l'écran , vous avez l'occassion de parier comme ceci:")
slow_print0_5("Miser sur un chiffre précis , en cas de succès votre mise fera x36 ((mise*35)+mise)=gain\nMiser sur pair ou impair,ceci doublera la mise (mise+mise)= gain")
slow_print0_5("Miser sur rouge ou noir,ceci doublera la mise (mise+mise)= gain")
slow_print0_5(" Les noirs : " + str(Noir[:]))
slow_print0_5(" Les rouges : " + str(Rouge[:]))
slow_print0_5("Vous êtes le heureux propriétaire de 100 €")

Bets = dict()
#Loop de jeu 
while somme_joueur > 0:
    nmb_betz = nmb_bet(int(input("Combien de paris souhaitez vous faire sur ce jeu ci ? ")))
    #Loop nombre paris 
    for i in range(nmb_betz) :
        x = bet_choice(input)
        Bets[i]["pari"]= x 
        if Bets[i]["pari"] == 1 :
            y = bet_1_2 (input)
            if y == 1 : 
                Bets[i]["pair impair"] = 1
            elif y == 2 :
                Bets[i]["pair impair"] = 2

        elif Bets[i]["pari"] == 2:
            y = bet_R_B(input)
            if y == 1: 
                Bets[i]["Rouge ou Noir"] = 1
            elif y == 2 :
                Bets[i]["Rouge ou Noir"]= 2
        else :
             y= bet_nmb(input)

             Bets[i]["Nombre"]= y 
        mise = int(input("Quelle mise souhaitez vous réaliser sur ce paris ? "))
        if mise > somme_joueur or mise <= 0 : 
            print("Vous ne pouvez pas parier plus que ce que vous posséder ou 0")
        else :
            somme_joueur = somme_joueur - mise
            Bets[i]["mise"] = mise 
        
    #Roulement de la roulette : 
    roul_res = random.randint (0,36)
    slow_print1("Faites vos jeux ! Rien ne va plus !")
    slow_print1("roulement de roulette...")
    slow_print1("... roll ... roll ... roll ...")
    slow_print1("Le numéro "+ str(roul_res) + "est tombé!")

    #For i in range (nmb_betz) pour les résultats 
    for i in range(nmb_betz):
        #Verification paris pairs et impairs 
        if Bets[i]["pari"] == 1:
            if Bets[i]["pair impair"]== 1 :
                if roul_res % 2 == 1 :
                    print("C'est gagné !")
                    somme_joueur = somme_joueur+Bets[i]["mise"]*2
                elif roul_res%2 == 0 :
                    print("c'est perdu")
            elif Bets[i]["pair impair"] == 2 : 
                if roul_res % 2 == 0 :
                    print("C'est gagné !")
                    somme_joueur = somme_joueur+Bets[i]["mise"]*2
                elif roul_res%2 == 1 : 
                    print("c'est perdu")
        #Paris Rouge ou noir 
        if Bets[i]["pari"]==2:
            #Noir gagnant 
            if Bets[i]["Rouge ou Noir"] in Noir and roul_res in Noir:
                print("Noir Gagnant - C'est gagné!")
                somme_joueur = somme_joueur+Bets[i]["mise"]*2 
                
            #Rouge gagnant 
            if Bets[i]["Rouge ou Noir"] in Rouge and roul_res in Rouge:
                print("Rouge gagnant ! C'est gagné !")
                somme_joueur = somme_joueur+Bets[i]["mise"]*2
            #Else perdu 
            else : 
                print("C'est perdu - Rouge ou Noir perdant ")
        #Chiffre gagnant ? 
        elif Bets[i]["pari"]==3:
            if Bets[i]["Nombre"] == roul_res :
                print("WAOUW- chiffre Gagnaaaant")
                somme_joueur = somme_joueur + Bets[i]["mise"]*36
            else : 
                print("Perdu ... Pari risqué !! ")
    print("Votre dépôt est de " + str(somme_joueur)+"€ .")
    
print("Votre dépôt est négatif ... Sortez d'ici !! ")

    