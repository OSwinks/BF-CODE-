'''

un challenge crypté

Fhfl hvw xqh sduwlh gx whawh, iéolflwdwlrqv.

chrono 
'''

def shift_alpha (phrase , decalage):
    phrase_decal= int(ord(phrase))+ decalage
    chr(phrase_decal)
    return phrase_decal


phrase = "G"
decalage = 1

for shift in range (1,26):
    phrase_decale = shift_alpha (phrase,decalage)
    decalage = decalage + 1
    print(f'numero de  decalage {decalage} est \n {chr(phrase_decale)}')