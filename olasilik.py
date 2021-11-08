import random
import math
import pandas as pd 
import numpy as np 
from math import sqrt

#########   BASİT SERİ     #########
def basitSeri_soru3():
    boyut=int(input("kaç adet sayi gireceksiniz - >"))
    sayilar=[]
    while True:
        if boyut<=0:
            break
        else:
            for k in range(0,boyut,1):
                sayilar.append(int(input(str(k+1) + ". sayıyı giriniz:")))
                boyut=boyut-1
    for a in range(0,len(sayilar)):
        for i in range(a+1,len(sayilar)):
            if ((i+1)!=len(sayilar)) and (sayilar[a]<sayilar[(i)]):
                c=sayilar[a]
                sayilar[a]=sayilar[i]
                sayilar[i]=c
    sayilar.sort()
    print(sayilar)


#########  PERMUTASYON/KOMBINASYON     #########
def permkomb_soru8():
    a = int(input("Permutasyon/Kombinasyon icin 'n' degerini girin - > "))
    b = int(input("Permutasyon/Kombinasyon icin 'r' degerini girin - > "))
    while(1):
        if(a<0 or b<0):
            print("n ve r degeriniz 0'a esit veya buyuk olmali")
            break
        else:
            print("Permutasyon -> ",permutasyon(a,b))
            print("Kombinasyon -> ",kombinasyon(a,b))
            break
#########       PERMUTASYON     #########
def permutasyon(a,b):
    a=a
    b=b
    faktoriyel=1
    perm=a-b
    faktoriyel_payda=1
    sonuc=1
    if a<0 or b<0:
        while(1):
            print("n ve r degeriniz 0'a esit veya buyuk olmali")
            break
    elif(a==b):
        while(a>1):
            faktoriyel=faktoriyel*a
            a=a-1
        #print("Sonuc - > ",faktoriyel)    
        return faktoriyel
    elif(a>b):
            while(a>1):
                faktoriyel=faktoriyel*a
                a=a-1
            while(perm>1):
                faktoriyel_payda=perm*faktoriyel_payda
                perm=perm-1
            sonuc=faktoriyel/faktoriyel_payda
            #print("Sonuc - > ",sonuc)
            return sonuc
    else:
        print("n degeri r degerinizden buyuk olmali")
#########       KOMBİNASYON     #########
def kombinasyon(a,b):
    a=a
    b=b
    faktoriyel=1
    perm=a-b
    faktoriyel_payda=1
    faktoriyelb=1
    sonuc=1
    if a<0 or b<0:
        while(1):
            print("n ve r degeriniz 0'a esit veya buyuk olmali")
            break
    elif(a==b):
        #print("Sonuc - > 1")    
        return 1
    elif(a>b):
        while(a>1):
            faktoriyel=faktoriyel*a
            a=a-1
        while(perm>1):
            faktoriyel_payda=perm*faktoriyel_payda
            perm=perm-1
        while(b>1):
            faktoriyelb=faktoriyelb*b
            b=b-1
        sonuc=faktoriyel/(faktoriyel_payda*faktoriyelb)
        #print("Sonuc - > ",sonuc)
        return sonuc
    else:
        print("n degeri r degerinizden buyuk olmali")

#########       FREKANS SERİSİ     #########
def frekansSerisi_soru4():
    def countFreq(arr, n):
        enb=1
        visited = [False for i in range(n)]
        for i in range(n):
            if (visited[i] == True):
                continue
            count = 1
            for j in range(i + 1, n, 1):
                if (arr[i] == arr[j]):
                    visited[j] = True
                    count += 1
            print(arr[i],'--', count)
            if(count>enb):
                enb=count
            else:
                continue
        print("fre buyuk - > ",enb)

    if __name__ == '__main__':
       
        arr=[]
        print("frekans serisi icin veri girin. Eger 'a' tusuna basarsaniz veri girme islemi biter.")
        gir=1
        while(True):
        
            abcd=(input(str(gir) + ". sayiyi girin - > "))
            if(abcd=="a"):
                break
            else:
                arr.append(abcd)
                gir+=1

        n = len(arr)
        print("'X'--'f'")
        countFreq(arr, n)

#########       MERKEZİ EGİLİM     #########
def merkeziegilim_soru6():
    def frekansSerisi_soru6(arr, n):
        enb=1
        enbs=1
        visited = [False for i in range(n)]
        for i in range(n):
            if (visited[i] == True):
                continue
            count = 1
            for j in range(i + 1, n, 1):
                if (arr[i] == arr[j]):
                    visited[j] = True
                    count += 1
            if(count>enb):
                enb=count
                enbs=arr[i]
            else:
                continue
        print("Verilerin modu - > ",enb," kez tekrar etti -> ",enbs,"(sayi)")

    boyut=int(input("kaç adet sayi gireceksiniz - >"))
    sayilar=[]
    while True:
        if boyut<=0:
            break
        else:
            for k in range(0,boyut,1):
                sayilar.append(int(input(str(k+1) + ". sayıyı giriniz:")))
                boyut=boyut-1
    for a in range(0,len(sayilar)):
        for i in range(a+1,len(sayilar)):
            if ((i+1)!=len(sayilar)) and (sayilar[a]<sayilar[(i)]):
                c=sayilar[a]
                sayilar[a]=sayilar[i]
                sayilar[i]=c
    sayilar.sort()
    print("Veriler - > ", sayilar)
    print("Verilerin aritmetik ortalamasi - >",sum(sayilar)/len(sayilar))
    medyanindex=int(len(sayilar)/2)
    if(len(sayilar)%2==1):
        print("Verilerin medyani - > " , sayilar[medyanindex])
    else:
        med=int(sayilar[medyanindex]+sayilar[medyanindex-1])
        print("Verilerin medyani - > " , med/2)
    boy=len(sayilar)
    print(frekansSerisi_soru6(sayilar,boy))
#########       RASTGELE     #########
def rastgele_soru1():
    baslangicSinir=0
    bitisSinir=0
    kontrol=True
    while(kontrol):
        baslangicSinir=int(input("Rastgele uretilecek sayi icin baslangic siniri girin - > "))
        bitisSinir=int(input("Rastgele uretilecek sayi icin bitis siniri girin - > "))
        if(baslangicSinir>bitisSinir):
            print("\nbaslangic siniri bitis sinirindan kucuktur. Tekrar deneyin\n")
            kontrol=True
        else:
            kontrol=False

    sinirFarki=abs(abs(bitisSinir)-abs(baslangicSinir))+1
    if(baslangicSinir<0 and bitisSinir>0):
        sinirFarki=abs(baslangicSinir)+bitisSinir+1
    uretilecekSayi=int(input("Bu sinirlar icerisinde kac sayi uretilsin - >"))
    rastgele=[]
    tempUretilecek=uretilecekSayi
    temprast=[]
    if(uretilecekSayi>=sinirFarki):
        for a in range(uretilecekSayi):
            ab=random.randint(baslangicSinir,bitisSinir)
            rastgele.append(ab)
            temprast.append(a)
        print("\nUretilecek sayi adeti sinirlarin farkindan buyuktur.\nTekrarli veriler olabilir\n")
        print("Olusturulan dizi = > ",rastgele,"\nSinirlarin farki = > ",sinirFarki,"\n")
        print("olusturulan sayi = > ",tempUretilecek)
    else:
        print("\nUretilen sayi miktari sinir araligindaki sayi miktarindan azdir.")
        print("Dolayisiyla tekrarli veriler silinip yerine farkli veriler eklenmistir.\n")
        while(uretilecekSayi>0):
            ab=random.randint(baslangicSinir,bitisSinir)
            if(rastgele.count(ab)>=1):
                continue
            else:
                rastgele.append(ab)
                uretilecekSayi -= 1
        print("Olusturulan dizi = > ",rastgele,"\n\nSinirlarin farki = > ",sinirFarki,"\n")
        print("olusturulan sayi = > ",tempUretilecek)
def sistematik_soru2():
    Ndegeri=-1
    ndegeri=-1
    while(Ndegeri<0 or ndegeri<0):
        Ndegeri=int(input("N degerini girin -> "))
        ndegeri=int(input("n degerini girin -> "))
        if(Ndegeri<0 or ndegeri<0):
            print("N degeri veya n degeri negatiftir. Tekrar deneyin.")
    floatdeger=23.2
    kdegeri=Ndegeri/ndegeri
    if(type(floatdeger)==type(kdegeri)):
        kdegeri = math.floor(kdegeri)
    rastgele=[]
    ab=random.randint(0,kdegeri)
    rastgele.append(ab)
    a=1
   
    for i in range(ndegeri-1):
        
        ac=ab+kdegeri*a
        rastgele.append(ac)
        a +=1
    
    
    print("\nk degeri = ", kdegeri)
    print()
    print("Olusan dizi = > ",rastgele,"\n")

def frekanstablosu_soru5():
    dizi=[]
    ndegeri=int(input("Veriseti icin kac sayi gireceksiniz ? -> "))
    for i in range(ndegeri):
        abcd=int(input(str(i+1)+". sayiyi girin - > "))
        dizi.append(abcd)
    rdegeri=max(dizi)-min(dizi)
    kdeger=math.sqrt(ndegeri)
    floats=23.5
    if(type(floats)==type(kdeger)):
        kdeger=math.ceil(kdeger)
    hdegeri=rdegeri/kdeger
    if(type(floats)==type(hdegeri)):
        hdegeri=math.ceil(hdegeri)
    print("k=",kdeger,"h=",hdegeri,"r=",rdegeri)
    print(max(dizi),min(dizi))
    limitalt=[]
    limitalt.append(min(dizi))
    for i in range(kdeger):
        if(i==0):
            continue
        abc=min(dizi)+(i*hdegeri)
        limitalt.append(abc)
    limitust=[]
    limitust.append(limitalt[1]-1)
    for i in range(kdeger):
        if(i==0):
            continue
        abc=limitust[0]+(i*hdegeri)
        limitust.append(abc)
    print("sinif limitleri | alt -> ",limitalt)
    print("sinif limitleri | ust -> ",limitust)
    siniralt=[]
    for i in range(kdeger):
        ab=limitalt[i]-0.5
        siniralt.append(ab)
    sinirust=[]
    for i in range(kdeger):
        ab=limitust[i]+0.5
        sinirust.append(ab)
    print("sinif sinirlari | alt -> ",siniralt)
    print("sinif sinirlari | ust -> ",sinirust)
    siniffre=[]
    for i in range(kdeger):
        ab=0
        siniffre.append(ab)
    for i in range(len(dizi)):
        ab=dizi[i]
        for k in range(kdeger):
            if(ab>=limitalt[k] and ab<=limitust[k]):
                ab=siniffre[k]
                ab += 1
                siniffre[k]=ab
    print("Sinif frekanslari => ",siniffre)
    eklenikfre=[]
    eklenikfre.append(siniffre[0])
    for i in range(kdeger-1):
        ad=siniffre[i+1]+eklenikfre[i]
        eklenikfre.append(ad)
    print("Eklenik frekanslari => ",eklenikfre)
    siniforta=[]
    for i in range(kdeger):
        ab=(limitalt[i]+limitust[i])/2
        siniforta.append(ab)
    print("Sinif orta noktaları = > ",siniforta)
    oransalfre=[]
    for i in range(kdeger):
        ab=siniffre[i]/ndegeri
        oransalfre.append(ab)
    print("Oransal frekanslar = > ",oransalfre)
    oransaleklenikfre=[]
    oransaleklenikfre.append(siniffre[0]/ndegeri)
    for i in range(kdeger-1):
        ad=(oransaleklenikfre[i]+oransalfre[i+1])
        oransaleklenikfre.append(ad)
    print("Oransal eklenik frekanslar = > ",oransaleklenikfre)

def dagilimolculeri_soru7():
    adet=int(input("kac sayi gireceksiniz ? -> "))
    liste = []
    toplamaa=0
    for d in range(adet):
        liste.append(0)
    for b in range(adet):
        ab=float(input(str(b+1) +". sayiyi girin -> "))
        liste[b] = ab
        toplamaa += float(ab)
    ortla=toplamaa/adet


    print(ortla)

    #1.5,1.5,2.6,2.6,3.4,3.8,3.8,4.1,4.1,4.6,4.6,4.6,5.2,5.2
    def standartsapma(a):
        aratop=0
        aratop=0
        ort=0
        sonuc=0
        ort=ortla
    
        
        for b in range(adet):         
            aratop2=a[b]                   
            aratop=aratop+((aratop2-ort)**2)   
        aratop=aratop/(adet-1)                
    
        sonuc=sqrt(aratop)
        print("varyans -> ",aratop)
        
        print("standart sapma -> ",sonuc)  
        degisim= sonuc/ortla
        print("degisim katsayisi -> ",degisim)
    standartsapma(liste)

    series = pd.Series(liste)
    result = series.mad()
    print("Oms -> ",result)


    Q1 = np.percentile(liste, 25, interpolation = 'midpoint')
    
    Q3 = np.percentile(liste, 75, interpolation = 'midpoint')
    
    print("Q1 -> ",Q1)
    print("Q3 -> ",Q3)


a=True
b="d"
while(a):
    print("1.soru (Rastgele sayi uretme) icin 1 'e basin")
    print("2.soru (Sistematik rastgele sayi uretme) icin 2 'ye basin")
    print("3.soru (Basit seri) icin 3 'e basin")
    print("4.soru (Frekans serisi) icin 4 'e basin")
    print("5.soru (Frekans tablosu) icin 5 'e basin")
    print("6.soru (Merkezi egilim olculeri) icin 6 'ya basin")
    print("7.soru (Dagilim olculeri) icin 7 'ye basin")
    print("8.soru (Permutasyon / Kombinasyon) icin 8 'e basin")
    giris = int(input("Secim --> ")) 
    if(giris==1):
        rastgele_soru1()
        b=input("devam etmek ister misiniz ?  e/h 'a basin --> ")
        if(b=="e"):
            a=True
        else:
            a=False
    elif(giris==2):
        sistematik_soru2()
        b=input("devam etmek ister misiniz ?  e/h 'a basin --> ")
        if(b=="e"):
            a=True
        else:
            a=False
    elif(giris==3):
        basitSeri_soru3()
        b=input("devam etmek ister misiniz ?  e/h 'a basin --> ")
        if(b=="e"):
            a=True
        else:
            a=False
    elif(giris==4):
        frekansSerisi_soru4()
        b=input("devam etmek ister misiniz ?  e/h 'a basin --> ")
        if(b=="e"):
            a=True
        else:
            a=False
    elif(giris==5):
        frekanstablosu_soru5()
        b=input("devam etmek ister misiniz ?  e/h 'a basin --> ")
        if(b=="e"):
            a=True
        else:
            a=False
    elif(giris==6):
        merkeziegilim_soru6()
        b=input("devam etmek ister misiniz ?  e/h 'a basin --> ")
        if(b=="e"):
            a=True
        else:
            a=False
    elif(giris==7):
        dagilimolculeri_soru7()
        b=input("devam etmek ister misiniz ?  e/h 'a basin --> ")
        if(b=="e"):
            a=True
        else:
            a=False
    elif(giris==8):
        permkomb_soru8()
        b=input("devam etmek ister misiniz ?  e/h 'a basin --> ")
        if(b=="e"):
            a=True
        else:
            a=False
    else:
        a=True
      