#Convertisseur avec selection de donnée au préalable( 1€ = 1,09$)
print("Quelle valeur souhaitez vous convertir ?")
print("€->$? - tapez 1")
print("$->€? - tapez 2")
Mesure = input('quel est votre choix? ')
Mesure = int(Mesure)
if Mesure == 1:
    val_dol= input("Quel montant souhaitez vous convertir en $?")
    val_dol= float(val_dol)
    val_dol= (val_dol/1.09)
    val_dol= str(val_dol)
    print(val_dol+"$")
    
if Mesure == 2:
    val_eur =input("Quel montant en $ souhaitez vous convertir en €?")
    val_eur= float(val_eur)
    val_eur= (val_eur*1.09)
    val_eur= str(val_eur)
    print(val_eur+"€")