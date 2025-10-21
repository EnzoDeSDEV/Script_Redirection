import csv

with open ( '../csv/rewrite_rules.csv','r') as f1, \
     open('../csv/htaccess.csv','r') as f2:
    
    Nredirection = []
    Oredirection = []
    doublons = []
    lecteur1 = csv.reader(f1 , delimiter=';')
    lecteur2 = csv.reader(f2 , delimiter=';')

    for ligne in lecteur1:
        if ligne:
            Nredirection.append(ligne[0].strip())
                

    for ligne in lecteur2:
            if ligne:
                valeur = ligne[0].strip()
            for n in Nredirection[:]:  # copie pour pouvoir modifier la liste
                if n.lower() == valeur.lower():
                    doublons.append(valeur)
                    Nredirection.remove(n)
                    break  # on sort pour éviter de supprimer plusieurs fois

print("============Dossier sans doublon============ :\n")
for n in Nredirection:
    print(n)

print("============Dossier doublon============ :\n")
for d in doublons:
    print(d)
print("============Dossier doublon============ :\n")