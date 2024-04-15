print("Vous allez me donner un nombre d'heure, de minutes et de secondes que je vais convertir en secondes:")
val_h = input("Donnez moi un nombre d'heures")
val_m = input('Donnez moi un nombre de minutes')
val_s = input('Donnez moi un nombre de secondes')
val_h = int(val_h)
val_m = int(val_m)
val_s = int(val_s)
#val_hts = value hour to  seconds , et ainsi de suite 
val_hts = (val_h*3600)
val_mts = (val_m*60)
Msg = (val_hts+ val_mts+val_s)
Msg = str(Msg)
print("la durée en secondes est de :+"+Msg)

