# -*- coding: utf-8 -*-
"""PythonBasics1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wh1RV5bT5fIQAFmh9kQzanDHH7fu9uU3

### Versiyon Kontrolü
"""

!python --version

""" ### Her yazılım dilinin ilk adımı "Hello World!"
 ![Image of Yaktocat](https://yavuzyalcintas.com/wp-content/uploads/2020/08/hello-world.png)
"""

print("Hello World!")

print('Hello World')

print("Hello1")
print("Hello2")
print("Hello3")
print("Welcome to PG1926")

print "Hello World"

print(Hello)

print("Hello')

"""### Yorum Satırı

"""

#taking some notes 
#taking some notes
#take a note

'''Michael Irwin Jordan is an American scientist, professor at the University of California, 
Berkeley and researcher in machine learning, statistics, and artificial intelligence.
He is one of the leading figures in machine learning, 
and in 2016 Science reported him as the world's most influential computer scientist.
'''.replace("\n"," ")

"""write something

### Değişken Tanımlama

* variable = value

* n = 5
"""

n = 1 
print(n)

p = n
print(p)

"""### Veri Tipleri
* Integer (Tam sayı)
* Float (Kayar noktalı sayı)
* String (Karakter dizisi)
* Boolean
* Complex (Karmaşık sayılar)
* List (Liste)
* Dictionary (Sözlük)
* Tuple (Demet)
* Set (Küme)

"""

#String
hello = "World"

print(hello) #print variable
print("World") #print value
print(n)

#type() 
type(hello)

print(type(hello)) #print data type

#Integer
int_value = 5
int_value

print(type(int_value))

t = 3.19
print(type(t))

type('x')

#Boolean
t, f = True, False
print(type(t))
print(t)
print(f)

#swapping
data1 = 7 
data2 = 12
data3 = 23
data4 = 33

data1, data2, data3 , data4 = data2 , data1, data4, data3
print(data1, data2, data3, data4)

print("data1:", data1, "data:", data2)

metin = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

Section 1.10.32 of "de Finibus Bonorum et Malorum", written by Cicero in 45 BC
"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"

1914 translation by H. Rackham
"But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?"""

len(metin)

print(len(metin)) #print data length

len(5)

len(15.6)

a = 15
b = 23

a, b = b, a
print(a)
print(b)

data12 = 5
data13 = 90
print("My value:{} and Your value:{}".format(data12, data13))

"""### Aritmetik Operatörler"""

#Üslü ifadeler
5**2

5**3

35+67

"35"+"67"

"PG" + "1926"

"35" + 67

"35"*3

"hello"*4

"hello" "world"

x = 10

print(x+2)
print(x-2)
print(x*2)
print(x**2)
print(x**4)
print(x/2)
print(x//2) 
print(x%2)

y = 13
print(y/2)
print(y//2)
print(y % 2)

z= 5
z +=2 #z = z + 2
z

z*=2      # z = z * 2
z

"""### Tür Dönüşümleri
* str() 
* float() 
* int()
"""

str("Python")

float(5)

type(5.0)

int(float(5.7))

float("6.2")

float("Hello")

int(5.5)

"""### İndexleme ve Dilimleme"""

hello = "Hello"
print(hello)
print(hello[0])
print(hello[1])
print(hello[2])
print(hello[3])
print(hello[4])

hello2 = " Hello"
hello2[0]

print(hello[5])

job = " Engineering"

print(job[-5])

print(hello)

hello

hello[2:4]  # [x:y] --> x elemanını dahil eder fakat y elemanını dahil etmez.

hello[::-1]

world

world[2:4:1]   # [start:end:step]

city = "istanbul"
city[0:6:2]

word = 'machine learning'
print(word.capitalize())

print(word.upper())

print(word.replace('machine','artificial'))

word

word2 = "          artificial general      intelligence"
print(word2.strip())

y = input("Please enter a city name: ")  #input methodu değeri her zaman string ifadesi olarak tutar 
print(y)

type(y)

x = int(input("Please enter an integer: "))
print(x)

type(x)

"""### If/Else Durumları

if "condition":


> "doing sth"

print()

"""

ort = input('Ortalamanızı Girin : ')
if(int(ort)>=50):
      print("Geçtiniz")
else:
      print("Kaldınız")

sayi = input('Sayı : ')
if(int(sayi)%2==0):
      print("Sayı Çift")
else:
      print("Sayı Tek")

a = int(input("Bir sayı giriniz: "))

if a < 100:
    print("verdiğiniz sayı 100'den küçüktür.")

elif a < 50:
    print("verdiğiniz sayı 50'den küçüktür.")

elif a == 100:
    print("verdiğiniz sayı 100'dür.")

elif a > 150:
    print("verdiğiniz sayı 150'den büyüktür.")

elif a > 100:
    print("verdiğiniz sayı 100'den büyüktür.")

kullanıcı_adı = input("Kullanıcı adınız: ")
parola        = input("Parolanız       : ")

toplam_uzunluk = len(kullanıcı_adı) + len(parola)


if toplam_uzunluk > 40:
    print("Kullanıcı adınız ile parolanızın ",
          "toplam uzunluğu 40 karakteri geçmemeli!")
else:
    print("Sisteme hoşgeldiniz!")

"""### Liste (list)
Python list, yani liste, herhangi bir sayıda diğer objeleri içinde bulunduran bir sandık vazifesi görüyor. Diğer dillerdeki listelerden en önemli farkı ise, bir listede birden fazla tip öğenin yanyana bulunabilmesi. Diğer konteynır tarzı objelerden farkı ise, listeler değişebilir (mutable) olması ve sıralı olması diyebiliriz. Diğer konteynırlar nedir derseniz, kümeler (set) ve sözlükler (dict) bunlara örnek olarak gösterilebilir.
"""

# creating a list
mylist = [3,5,6,7]
print(mylist)

type(mylist)

print(mylist[0])
print(mylist[2])
print(mylist[-1])
print(mylist[-3])

a = 5
print(a)

a = 3
print(a)

mylist[2] = "python"   # listeler farklı veri tiplerini bir arada bulundurabilir.
print(mylist)

mylist.append('course')  # append(): listenin sonuna bir eleman ekler.
print(mylist)

mylist = [3,4,5,6,7]
mylist.append('course')
mylist.append('course')
print(mylist)

thelast = mylist.pop()  # pop(): listenin sonundaki son elemanı siler.
print(thelast)
print(mylist)

mylist

mylist.index("course")

mylist.index(4)

mylist.count("course")

list2 = ["Python","Java","R","JavaScript","Ruby","Python","Python"]
list2.count("Python")

mylist

mylist.remove("course")
print(mylist)

mylist.sort()
mylist

list3 = [100,23,87,13,1000]

list3.sort()
list3

list4 = [41,23,78,99,37,2.9,2.8]
list4.sort()
list4

list4.remove()

list5 = [41,23,78,99,37,'python']
list5.sort()
list5

mylist

mylist.remove("course")
mylist.remove("python")
print(mylist)

mylist.remove("course")
print(mylist)

mylist.sort()
mylist

mylist = [3,4,5,6,7]

mylist.reverse()
mylist

mylist2 = ["python", "course", "hello"]
mylist2.sort()
mylist2

mylist

list_in_list = ["python","Java",3.2, 4, 11, [5,65,7,8,9]]
print(list_in_list[5])

list_in_list[-1]

mylist = [2, 3, 4, 5, 6, 'python', 'flutter', 'Android', 'JavaScript', 'dart', 3.2, 5.0]

numbers2 = list(range(2,15,3)) #range(start, stop, step)
print(numbers2)
numbers2.reverse()
print(numbers2)

"""### Sözlük (dictionary)
Sözlükler de Tuple ve List veri türleri gibi farklı veri türleri bulunur fakat sözlükler biraz  farklıdır. Sözlükler süslü parantezler ile ifade edilir ve  iki kısımdan oluşur; keys(anahtar) ve value(değer),  value kısmı bütün veri türünü içerebilir fakat keys kısmı sadece string ve int tipinde olabilir. Sözlüklerde değiştirilebilir veri türü olup ekleme,çıkarma vb. işlemler yapılabilir.



"""

d = {}

print(d)
type(d)

d = {"python":1, "course":2}
print(d)

d2 = {"machine":"learning", "artificial":"intelligence" }
d2

d2["artificial"]

d2["java"] = "programming"
d2

d2["ruby"] = "programming"
d2

d2["ruby"] = "language"
d2

d

d["course"]

d2["deep"] = "learning"
d2

print(d.keys())

d2.keys()

d2.values()

d2.items()

d

d["a"] = [3,4,5]
d

d.pop("python")
d

d.pop("python")
d

d

len(d)

"a" in d

"3" in d #Soru

d2

d2

del d2["deep"]
d2

d2

d2['machine'] = "Deep Learning"
d2

d2_copy = d2.copy()
d2_copy

d2_copy['deep'] = 'AI'
d2_copy

d2

"""### Küme (set)

Liste, sözlük ve demet veri türü gibi birden çok veri türünü birlikte barındıran veri tipidir. Kümeler ile ilgili yaptığınız her türlü işlevi(birleşme,kesişim vs.) bu veri tipi ile yapabilirsiniz.






"""

s = {"python", 5,6,8,5,6,"abc", "python","python","python","python","python","python","python","python","python"}
s

empty = set()
type(empty)

empty2 = {}
type(empty2)

ne = set("pineapple")
print(ne)

6 in s

len(s)

s.add("ai")
s

s.add("ai")
print(s)
len(s)

s2.remove("ai")
print(s2)

"""# Demet (Tuple)

Demetler birden fazla veri türünü bir arada bulundurabilen virgüllerle veya parantez ile gösterilen immutable(değiştirilemeyen) veri tipleridir.


"""

tupl = (1,2,3,4,5)
print(tupl)
print(type(tupl))

tuple2 = ()  
type(tuple2)

print(tupl[3])

tupl[-2]

tupl[:4]

dm3 = ("asli", 5, 8, "september")
dm3.index("september")

dm3.count(5)

dm4 = ("apple","pear","strawberry")

dm4[0] = "cherry"

print(dm4)

dm4.remove("pear")