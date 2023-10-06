import random

SorularList = [ "1.65 den uzun mu: ",    #yes(y) or (n)
                "Karakterin Renkli gözlü mü: ",
                "Karakterin Mutlu mu: ",
                "Karakterin Gözlük kullanıyor mu: ",
                "Karakterin Akpli mi: ",
                "Karakterin Kulağım Delik mi: ",
                "Karakterin Lol oynuyormu: ",
                "Karakterin Sevgilim var mı: ",
                "Karakterin Kendimi ryan gosling gibi hissediyor mu: ",
                "Karakterin Kıvırcık saçlı mı: "]


IsimlerList = {"A1ynyynynnny":"Berkay",  #Berkay
                  "A2nyyynyyynn":"Su",  #Su
                  "A3ynynnnyyyn":"Ege2",  #Ege2
                  "A4ynynnnnnnn":"CEKO",  #CEKO
                  "A5ynyynyynny":"Piroz",  #Piroz
                  "A6yynynynnnn":"Yagız",  #Yağız
                  "A7nnynyyynyn":"Batus",  #Batuş
                  "A8yyynnnynyy":"Ege1",  #Ege1
                  "A9yyynnynynn":"Heval",  #Heval
                  "AAyyyynynnyy":"Ozgur",  #Özgür
                  "ABynnynyynyn":"Furkan",  #Furkan
                  "ACynyynnyyny":"Kaan",   #Kaan
                  "ADynnnnnynnn":"Ertan"}  #Ertan

SetList = set() # Sorulan soruda zıt cevapta olanlar buraya kaydediliyor en son diğer liste ile karşılaştırılıp kalan kişinin ismi yazdırılacak
while True:
    question = random.choice(SorularList) # Rastgele bir soru seçiyor ve question değişkinine aktarılıyor
    if "X" in question : continue # Bunun neden olduğunu aşağıda açıklıyacağım (1)
    answer = input(question) #Cevap alınıp answer değişkinine aktarıldı (sadece y veya n ile cevaplayın)
    for n in IsimlerList: #Listeyi gezen for açıldı
     #Bu altta ki satır kontrol amaçlı bunu kapalı tutun gereksiz text !
     #print(f"soru indexi: {SorularList.index(question)} index number: {SorularList.index(question) + 2} index of number: {n[SorularList.index(question) + 2]} ID: " + n)
     if answer  !=  n[SorularList.index(question) + 2] : SetList.add(n) #Burada cevap ile ID' deki index tutmuyorsa Setliste ekliyor ID'yi

    #print(SetList) KONTROL AMAÇLI GEREKSİZ TEXT !

    SorularList[SorularList.index(question)] = question + "X" #(1) bunun amacı aynı soruyu listeden kaldırmadan tekrardan sormamasını sağlamak sorulan soruya X koyup yukarıda kontrol ediyor varsa sormuyor ve başka bir soru seçiyor
    if len(SetList) == len(IsimlerList) - 1 : break #Set ile Listin boyut farkı bir kalınca yani 1 kişi kalınca döngüyü kesiyor
    if len(SetList) == len(IsimlerList)  : #0 eşleşme de bunu veriyor
        print("Aradiginiz ozellikli biri yoktur!")
        break
for x in SetList:
    if x in IsimlerList: del IsimlerList[x]  # Listeyle Seti kesiştiriyor kalan kişiyi yazdırıyor
print(IsimlerList.values())