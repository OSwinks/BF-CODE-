#Legrand QUIZZZZ project = 10 Questions while suggesting number of possibilities and keeping track of a score
#Also going to suggest differents questions depending of the result of the first questions
print("Hellooooooo ! ")
print("You're going to be challenged at 10 questions for a WONDERFUL PRIZE !!! Are you ready ?")
ready_answer = input("If you're ready press 1! - if not press 2! ")
ready_answer = int(ready_answer)
#The answer decide which scenario is put in 1 / 2 or something else 
if ready_answer == 2 :
    print("")
    print("OOooook ... Well ... whenever you want to play ... i mean ... ok ... ugh..")
    print("What a mess that guy ... i mean what a jerk really!")
    print("No prize for him i guess !!! >< ")
    exit()
    
if ready_answer == 1 :
    print("")
    print("Oooooooh yeaaaaah !! You're READY !! AND IT FEELS GOOOOOOD !!!")
    print("So ... uhm ... i''m gonna ask you few questions , the answers to these questions will be kept in your score as we go !")
    print("So you'll be challenged into the first question ! ")
    print("")
    
   
    
else :
    print("")
    print(" you have typed another answer than 1 r 2 ... are you good ? Have you fallen into a coma on your laptop ... ? ")
    print(" i'm going to call an ambulance for you just in case ... *call 911*")
    print("Help is on it's way !! Hang up in there buddy !!")
    exit()
           
#Question 1
print("What is the capital of Ecuador ?")
#We decide if we want 2 or 4 suggestions
_2or4 = input("So how many choices do you want ? 2 or 4?")
_2or4 = int(_2or4)
#We define the "score" variable
score = 0

if _2or4 == 2 :
    print('For "Quito" press 1')
    print('For "Ouagadougou" press 2')
    A = input("What will your answer be ? 1 or 2?")
if _2or4 == 4 :
    print('For "Quito" press 1')
    print('For "Ouagadougou" press 2')
    print('For "Paris" press 3')
    print('For "San diego" press 4')
    A = input("What will your answer be ? 1,2,3 or 4?")
    
A= int(A)
if A== 1 :
    score = (score+1)
    print("Wonderful !! good answer !! You are a natural ! ")
    
if A== 2 :
    score = (score+0)
    print('Ouuuupsie ... bad answer !!')
    
if A== 3 :
    score = (score+0)
    print('Ouuuupsie ... bad answer !!')

if A== 4 :
    score = (score+0)
    print('Ouuuupsie ... bad answer !!')
    
    
#We annonce the score by turning it to a string / printing it / then turning it into a int again for later
score = str(score)
print("You have "+ score + " points so far!")
score = int(score)

#Question 2
print("Second question right there !What is the highest tower in the world ?")
#We decide if we want 2 or 4 suggestions
_2or4 = input("So how many choices do you want ? 2 or 4?")
_2or4 = int(_2or4)

#Here i want the answer of the two possibilities to not necessary be the same number, the correct answer of the 2 choices is on the 1 Where the 4 choices answer is on the 4
if _2or4 == 2 :
    print('For "Burj Khalifa" press 1')
    print('For "Shangai tower" press 2')
    A = input("What will your answer be ? 1 or 2?")
    A = int(A)
    if A== 1 :
        print("Wonderful !! good answer !! You know so much about stuffs !! ")
    score = (score+1)
    if A== 2 :
        print('Ouuuupsie ... bad answer !!')

    
if _2or4 == 4 :
    print('For "Shangai tower" press 1')
    print('For "Empire state building" press 2')
    print('For "Goldin finance" press 3')
    print('For "Burj Khalifa" press 4')
    A = input("What will your answer be ? 1,2,3 or 4?")
    A= int(A)
    if A==1:
        print('Ouuuupsie ... bad answer !!')
    if A==2:
        print('Ouuuupsie ... bad answer !!')
    if A==3:
        print('Ouuuupsie ... bad answer !!')
    if A==4:
        print("Wonderful !! good answer !! You know so much about stuffs !! ")
        score =(score+1)
        
        
#We annonce the score by turning it to a string / printing it / then turning it into a int again for later
score = str(score)
print("You have "+ score + " points so far!")
score = int(score)

#Question 3
print("Who is the actual president of USA ?")
#We decide if we want 2 or 4 suggestions
_2or4 = input("So how many choices do you want ? 2 or 4?")
_2or4 = int(_2or4)

# 2 right is 2 / 4 right is 3
if _2or4 == 2 :
    print(' for "Donald J trump" press 1')
    print('Joe Biden" press 2')
    A = input("What will your answer be ? 1 or 2?")
    A = int(A)
    if A== 2 :
        print("Wonderful !! good answer !! You know so much about stuffs !! ")
    score = (score+1)
    if A== 1 :
        print('Ouuuupsie ... bad answer !!')

    
if _2or4 == 4 :
    print('For "Barack Obama" press 1')
    print('For "Donald J Trump" press 2')
    print('For "Joe Biden" press 3')
    print('For "Ruth Bady Gisberg" press 4')
    A = input("What will your answer be ? 1,2,3 or 4?")
    A= int(A)
    if A==1:
        print('Ouuuupsie ... bad answer !!')
    if A==2:
        print('Ouuuupsie ... bad answer !!')
    if A==4:
        print('Ouuuupsie ... bad answer !!')
    if A==3:
        print("Wonderful !! good answer !! You know so much about stuffs !! ")
        score =(score+1)
        
        
#Score as line 68
score = str(score)
print("You have "+ score + " points so far!")
score = int(score)






#Question 4 !!!!
#We're going to formate the questions and answers into Strings for to make it easier to copy paste :
question = str("En quelle année l'homme est il allé sur la lune ?")
p1 = str("1999")
p2 =str("1969")
p3 =str("1678")
p4 =str("1789")
print(question)
#We decide if we want 2 or 4 suggestions
_2or4 = input("So how many choices do you want ? 2 or 4?")
_2or4 = int(_2or4)

# 2 right is 2 / 4 right is 4
if _2or4 == 2 :
    print('For "'+p1+'" press 1')
    print('For "'+p2+" press 2')
    A = input("What will your answer be ? 1 or 2?")
    A = int(A)
    if A== 2 :
        print("Wonderful !! good answer !! You know so much about stuffs !! ")
    score = (score+1)
    if A== 1 :
        print('Ouuuupsie ... bad answer !!')

    
if _2or4 == 4 :
    print('For "'+p1+" press 1')
    print('For "'+p3+" press 2')
    print('For "P'+p4+" press 3')
    print('For "'+p2+" press 4')
    A = input("What will your answer be ? 1,2,3 or 4?")
    A= int(A)
    if A==1:
        print('Ouuuupsie ... bad answer !!')
    if A==3:
        print('Ouuuupsie ... bad answer !!')
    if A==4:
        print('Ouuuupsie ... bad answer !!')
    if A==2:
        print("Wonderful !! good answer !! You know so much about stuffs !! ")
        score =(score+1)
        
        
#Score as line 68
score = str(score)
print("You have "+ score + " points so far!")
score = int(score)


