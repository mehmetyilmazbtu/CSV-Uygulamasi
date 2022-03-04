#Python dili ile yazilmistir
import csv
#Dosya okuma

file=open('dosya.csv','r')
fileRead=csv.reader(file)
#Okunan dosyayı degiskene atama
satirlar=[]
for i in fileRead:
    satirlar.append(i)
#Satir ve sutun sayisi
satirSayisi=len(satirlar)
sutunSayisi=len(satirlar[0])

#Ekle fonksiyonu
def Ekle():
    file=open('dosya.csv','a')
    print(sutunSayisi)
    file.write('\n')
    for i in range(0,sutunSayisi):    
        print(satirlar[0][i]," girin:\n")
        yaz=input()
        file.write(str(yaz)+',')
    file.close()


#Bul fonksiyonu
def Bul(string):
    for a in range(0,satirSayisi):
        if satirlar[a][2] == string:
            print("Eslesen ID: "+satirlar[a][0])

Ekle()

Bul("ankara")

file.close()