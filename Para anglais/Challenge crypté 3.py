'''

un challenge crypté

Fhfl hvw xqh sduwlh gx whawh, iéolflwdwlrqv.

'''
alphabet = "abcdefghijklmnopqrstuvwxyz"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

P = '''"Fhfl hvw xqh sduwlh gx whawh, iéolflwdwlrqv.
Pdokhxuhxvhphqw, fhwwh sduwlh hvw xq slèjh srxu frqwuhu o'dssurfkh xqltxhphqw pdqxhooh.
Ohv oljqhv gx edv rqw xq dxwuh géfdodjh txh fhv oljqhv flv.
Lo idxw wurxyhu ohxu géfdodjh fdu fh vrqw hoohv txl frqwlhqqhqw oh yudl lqglfh.
Ev wrzkvj grj rkkvekzfe rlo 4 czxevj rl uvjjlj, vccvj jlzmvek le rlkiv uétrcrxv, drzj jfek zelkzcvj.
Cvj 4 czxevj jlzmrekvj jfek cvj gclj zdgfikrekvj:
Dfe givdzvi vjk lev efkv uv dljzhlv.
Urej dfe uvlozèdv fe gvlk kiflmvi uv c'fi.
Cv tfigj yldrze vjk wrzk à 60% uv dfe kifzjzèdv.
Dfe kflk vjk le avl uv jftzéké u'fizxzev tyzefzjv.
"'''

def app_deca (x):
    if x in alphabet or x in ALPHABET:
        if x.islower():
            pos_x = alphabet.index(x)
        elif x.isupper():
            pos_x = ALPHABET.index(x)
        if pos_x > 25 :
            pos_x = pos_x -26
        pos_x = pos_x - decalage 
        pos_x = alphabet[pos_x]
        return pos_x 
    else :
        return " "     
        
#pos_a = alphabet.index("a")      

decalage = 0

for tries in range(1,26):
    print('Message numéro'+str(tries)+":")
    decalage = decalage + 1 
    for lettre in P:
        lettre_decale = app_deca(lettre)
        print(lettre_decale , end="" )
    print("")  
