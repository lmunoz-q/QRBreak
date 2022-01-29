import qrcode
import csv

#Nom du csv a QR coder
f = open('Salles Entrainement.xlsx - Feuil1.csv')
fileCSV = csv.reader(f)
for line in fileCSV:
    print(line)
    img = qrcode.make("Photo : " + line[0] + "\nNom & Prenom : " + line[1] + "\nTel : " + line[2] + "\nMail : "
                      + line[3] + "\nSalles : " + line[4] + "\nDate de paiement : " + line[5])
    img.save(line[1] + ".jpg")
