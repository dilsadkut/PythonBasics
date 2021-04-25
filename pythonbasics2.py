# -*- coding: utf-8 -*-
"""PythonBasics2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13wfSvoFniRlLQRqNc3E4jSWBEAnGyjbO

### While Döngüsü
"""

a = 1

while a == 1:             #while -> iken, olduğu sürece

a = 1

while a < 6:            #a’nın değeri 6’dan küçük olduğu müddetçe…
  a += 1
  print("5 kez yazdır")

while True:         #Aksi belirtilmediği sürece çalışmaya devam et!
    soru = input("Yapmak istediğiniz işlemin numarasını girin (Çıkmak için q): ")

    if soru == "q":
        print("çıkılıyor...")
        break

#Aksi belirtilmediği sürece kullanıcıya
#aşağıdaki soruyu sormaya devam et!
while True:
    soru = input("Nasılsınız, iyi misiniz?")

    #Eğer kullanıcı 'q' tuşuna basarsa...
    if soru == "q":
        break #döngüyü kır ve programdan çık.

a = 0

while a < 100:
    a += 1
    if a % 2 == 0:
        print(a)

"""### For Döngüsü


"""

for değişken_adı in değişken:
    yapılacak_işlem

tr_harfler = "şçöğüİı"

for harf in tr_harfler:
    print(harf)

sayılar = 123456789
for sayı in sayılar:   
  print(sayı)

for gazi in "PG1926":
    print(gazi)

tr_harfler = "şçöğüİı"

parola = input("Parolanız: ")

for karakter in parola:
    if karakter in tr_harfler:
        print("parolada Türkçe karakter kullanılamaz")

for i in range(0, 10):       #range = aralık
  print(i)                   #range(ilk_sayı, son_sayı)

ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjhu9"
ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"

for s in ilk_metin:
    if not s in ikinci_metin:
        print(s)

"""### Fonksiyonlar"""

def kayıt_oluştur(parametre1, parametre2, parametre3, parametre4):   #Fonksiyon tanımı
    (...)

kayıt_oluştur(parametre1, parametre2, parametre3, parametre4)   #Fonksiyon çağrısı

def selamla():
    print("Selam PG1926!")
selamla()

def selam(isim):
  print("Selam " + isim)

selam('ahmet')

def toplama(a,b):
  toplam = a + b
  print(toplam)

toplama(4,5)

def kayıt_oluştur(isim, soyisim, işsis, şehir):
    print("-"*30)

    print("isim           : ", isim)
    print("soyisim        : ", soyisim)
    print("işletim sistemi: ", işsis)
    print("şehir          : ", şehir)

    print("-"*30)

def ismin_ne():
    isim = input("ismin ne? ")
    print(isim)   #return isim

ismin_ne()

"""### Modüller

Modüller Python programcılarına büyük kolaylık sağlayan yapılardan biridir.Python modüller; içerisinde bir takım özellikleri,fonksiyonları barındıran yapılardır.
"""

import os

from os import name,getcwd
print(name)
print(getcwd())

dir(os) #dir -> directory

if os.name != 'nt':
  print('Kusura bakmayın! Bu programı yalnızca',
  'Windows\'ta kullanabilirsiniz!')
... else:
  print('Hoşgeldin Windows kullanıcısı!')

import subprocess as sb

"""### Nesne Yönelik Programlama (OOP)

Nesne Yönelikli Programlamanın sağladığı kolaylıklar
* Gerçek dünyadaki nesnelerin tasarımları sınıf içinde yapılır.
* Sınıftan nesne üretilip değişiklik yapılmak istendiğinde tüm programda değişiklik yapmak gerekmez sadece oluşturulan nesnenın sınıf içinde değişiklik yapmak yeterlidir.
* Oluşturulan nesneler birbirinden bağımsız olduğu için bilgi gizleme olanağı artar.
 Örneğin A nesnesi B nesnesinin özelliklerini kullanamaz ve erişemez.
* Nesne oluşturma bir sınıf içerisinde gerçekleştirilir ve bu kodlar başka projelerde kullanılabilir.
 Örneğin bir A nesnesi oluşturduysak bunu birçok yerde kullanabiliriz.
* Sınıflar oluşturarak daha az kod oluşturup daha fazla iş yapıp kod tekarı önlenir.
* Örneğin insan sınıfında isim, soyisim, yaş… gibi özellikleri bir defa oluşturup istediğimiz kadar kullanabiliriz.
* Kod tekrarı önlediği için geliştirme sürecinin verimliliğini artırır.

### Sınıflar

Çok kaba ve oldukça soyut bir şekilde tanımlayacak olursak, sınıflar, nesne üretmemizi sağlayan veri tipleridir. İşte nesne tabanlı programlama, adından da anlaşılacağı gibi, nesneler (ve dolayısıyla sınıflar) temel alınarak gerçekleştirilen bir programlama faaliyetidir.
"""

class YeniSınıf():   #Sınıf tanımlama
    pass

def çalışan():
    kabiliyetleri = []
    unvanı = 'işçi'

    print(kabiliyetleri)
    print(unvanı)

class Çalışan():
    kabiliyetleri = []
    unvanı = 'işçi'

    print(kabiliyetleri)
    print(unvanı)

class Çalışan():
    kabiliyetleri = []
    unvanı = 'işçi'

print(Çalışan.kabiliyetleri)
print(Çalışan.unvanı)

class Çalışan():
    kabiliyetleri = []
    unvanı = 'işçi'
    maaşı = 2500
    memleketi = ''
    doğum_tarihi = ''

print(Çalışan.maaşı)
print(Çalışan.memleketi)
print(Çalışan.doğum_tarihi)

Çalışan.isim = 'Ahmet','Mehmet'
Çalışan.yaş = 40

print(Çalışan.isim)

class Asker():
    rütbesi = 'Er'
    standart_teçhizat = ['G3', 'kasatura', 'süngü', 'el bombası']
    gücü = 60
    birliği = ''

Asker.gücü

ahmet = Asker()  #Örnekleme (instance)

ahmet.gücü = 70

print(ahmet.gücü)

ahmet.standart_teçhizat.append("Bıçak")

print(ahmet.standart_teçhizat)

mehmet = Asker()

print(mehmet.gücü)

"""### __init__ Fonksiyonu ve self

İnit nedir?

__init__ metodu initialize – ilklendirmek, initializer – başlatıcı kavramlarından gelmektedir. __init__ , OOP ile programlamada bir class’ın yapıcı (constructor) metodur. Eğer bir class’tan nesne türetecek isek __init__ ,class’ın ilk metodu olmak zorundadır. Class içinden türetilen nesnelere ait özellikler bu metot ile nesnelere atanır.
Aşağıdaki örnekte Arabalar() adında bir class oluşturduk. Genel olarak her arabada bulunan fakat arabadan arabaya değişiklik gösteren marka, model, renk ve vites gibi ayırt edeci özellikleri class’ımıza atadık.

Self nedir?

__init__ metodunun yapısına baktığımızda parantez içinde self kavramı dikkatimizi çekmektedir. self anahtar sözcüğü (keyword) __init__ metodu ile gelen ve class içinden türetmiş olduğumuz nesnelere ulaşmamızı sağlayan bir kavramdır. __init__ metodunu class’tan hemen sonra kullandığımızda gelen self keyword yerine biz kendi keyword’ümüzü de yazabiliriz ve daha sonra, çağırmak istediğimiz her özellik için oluşturduğumuz keyword’ü kullanabiliriz. Tavsiye olarak self sözcüğünü karışıklık olmaması adına değiştirmemenizi tavsiye ederim.
"""

class Arabalar():
    def __init__(self,marka,model,renk,vites):
        self.marka  = marka
        self.model  = model
        self.renk   = renk
        self.vites  = vites

araba_1 = Arabalar("Ford", "Mustang", "Siyah", "Manuel") #nesne yaratmak.

araba_2 = Arabalar("BMW", "X6", "Beyaz", "Otomatik")

araba_3 = Arabalar()

print(araba_1.marka)
print(araba_2.marka)

class Çalışan():
    personel = []

    def __init__(self, isim):
        self.isim = isim
        self.kabiliyetleri = []
        self.personele_ekle()

    def personele_ekle(self):
        self.personel.append(self.isim)
        print('{} adlı kişi personele eklendi'.format(self.isim))

    def personeli_görüntüle(self):
        print('Personel listesi:')
        for kişi in self.personel:
            print(kişi)

    def kabiliyet_ekle(self, kabiliyet):
        self.kabiliyetleri.append(kabiliyet)

    def kabiliyetleri_görüntüle(self):
        print('{} adlı kişinin kabiliyetleri:'.format(self.isim))
        for kabiliyet in self.kabiliyetleri:
            print(kabiliyet)

ç1 = çalışan.Çalışan('Ahmet')



"""### Miras alma & verme"""

class Akademisyen:
    def __init__(self,adi,soyadi,numarasi):
        self.adi = adi
        self.soyadi = soyadi
        self.numarasi = numarasi
 
 
    def giris(self):
        print("Giriş Yapıldı")
 
    def cikis(self):
        print("Çıkış yapıldı")
 
 
class Personel:
    def __init__(self, adi, soyadi, numarasi):
        self.adi = adi
        self.soyadi = soyadi
        self.numarasi = numarasi
 
    def giris(self):
        print("Giriş Yapıldı")
 
    def cikis(self):
        print("Çıkış yapıldı")
 
 
class Ogrenci:
    def __init__(self, adi, soyadi, numarasi):
        self.adi = adi
        self.soyadi = soyadi
        self.numarasi = numarasi
 
    def giris(self):
        print("Giriş Yapıldı")
 
    def cikis(self):
        print("Çıkış yapıldı")

class Kullanici:
    def __init__(self,adi,soyadi,numara):
        print("Kullanıcı sınıfı fonksiyonu")
        self.adi = adi
        self.soyadi = soyadi
        self.numara = numara
 
 
    def giris(self):
        print("Giriş Yapıldı")
 
    def cikis(self):
        print("Çıkış yapıldı")
 
 
 
class Akademisyen(Kullanici):
    pass
class Personel(Kullanici):
    pass
class Ogrenci(Kullanici):
    pass

ogr_ahmet = Kullanici("Ahmet", "Deniz", "123123")

prof_mehmet = Akademisyen("Mehmet", "Beyaz", "123123")

prof_mehmet.numara

