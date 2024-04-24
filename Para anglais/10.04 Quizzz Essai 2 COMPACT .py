#QUIZZZ 2 tentative de limiter le nombre de lignes de codes en fonctionnant par répétiton :
#Le format sera donné par Q1 par forme de liste [] représenté par ce symbole
#un compteur sera mis en place pour générer les différentes listes et questions par via un ifcmpt_q
#Le quizz récompense de 2 points les bonnes réponses sur un choix de 4 énnoncés et de 1 point celles avec 2 énnoncés
#We're going to formate the questions and answers into Strings for to make it easier to copy paste :

#info à voir : boucle for et boucle while /
#liste à la place des variables



score = 0
#Questions sous forme de listes
Q1= ["En quelle année l'homme est il allé sur la lune ?","1969","1678","1789","1887"]
Q2= ["Quel pays est connu pour ses frittes?","La Belgique","La France","La Hollande","La Suisse"]
Q3= ["Quelle est le nom de la grande place au centre de Bruxelles?","La Grand place","La Place Verte","La Place bleue","La Place des anciens combatants"]
Q4= ["Quel est notre sport préféré des Belges ?","Football","Hockey","Tennis","Pétanque"]
liste_q = [Q1 , Q2, Q3,Q4]
#Avec cette variable nmb_q, je compte remplacer les questions et les réponses 
nmb_q= 1
#A = Answer , variable se renouvellant à chaque question



print("Voici la question numéro "+str(nmb_q)+".")    
print(liste_q[0])
#We decide if we want 2 or 4 suggestions
_2or4 = input("Combien de propositions voulez-vous ? 2 ou 4?")
_2or4 = int(_2or4)

# 2 right is 2 / 4 right is 4
if _2or4 == 2 :
    print('For "'+Q1[2]+'" press 1')
    print('For "'+Q1[1]+'" press 2')
    A = input("What will your answer be ? 1 or 2?")
    A = int(A)
    if A== 2 :
        print("Waouw! Bonne réponse ,  ")
    score = (score+1)
    if A== 1 :
        print('Ouuuupsie ... mauvaise réponse !!')

    
if _2or4 == 4 :
    print('For "'+Q1[2]+'" press 1')
    print('For "'+Q1[3]+'" press 2')
    print('For "'+Q1[4]+'" press 3')
    print('For "'+Q1[1]+'" press 4')
    A = input("What will your answer be ? 1,2,3 or 4?")
    A= int(A)
    if A==1:
        print('Ouuuupsie ... mauvaise réponse !!')
    if A==3:
        print('Ouuuupsie ... mauvaise réponse !!')
    if A==2:
        print('Ouuuupsie ... mauvaise réponse !!')
    if A==4:
        print("Waouw , bonne réponse !! DOUBLE POINTS BONUS !!")
        score =(score+2)
nmb_q = (nmb_q+1)    
print("Vous avez "+ str(score) + " points pour le moment!")
    

#On doit relancer le programme avec une fonction repeat / et faire changer le nombre de la question 
    #replace (Q1,Q2)
    #replace (Q2,Q3)
    
    
print("Voici la question numéro "+str(nmb_q)+".")    
print(Q1[0])
#We decide if we want 2 or 4 suggestions
_2or4 = input("Combien de propositions voulez-vous ? 2 ou 4?")
_2or4 = int(_2or4)

# 2 right is 2 / 4 right is 4
if _2or4 == 2 :
    print('For "'+Q1[2]+'" press 1')
    print('For "'+Q1[1]+'" press 2')
    A = input("Quelle sera votre réponse? 1 or 2? ")
    A = int(A)
    if A== 2 :
        print("Waouw! Bonne réponse ,  ")
    score = (score+1)
    if A== 1 :
        print('Ouuuupsie ... mauvaise réponse !!')
   
    
if _2or4 == 4 :
    print('For "'+Q1[2]+'" press 1')
    print('For "'+Q1[3]+'" press 2')
    print('For "'+Q1[4]+'" press 3')
    print('For "'+Q1[1]+'" press 4')
    A = input("Quelle sera votre réponse? 1,2,3 or 4? ")
    A= int(A)
    if A==1:
        print('Ouuuupsie ... mauvaise réponse !!')
    if A==3:
        print('Ouuuupsie ... mauvaise réponse !!')
    if A==2:
        print('Ouuuupsie ... mauvaise réponse !!')
    if A==4:
        print("Waouw , bonne réponse !! DOUBLE POINTS BONUS !!")
        score =(score+2)
nmb_q = (nmb_q+1)    
print("Vous avez "+ str(score) + " points pour le moment!")    
         
