import math
import sys

#zad1

#zdanie = input("podaj zdanie")
#print(zdanie.count(" ")+1)


#Zad2

#a = int(input("liczba a"))
#b = int(input("liczba b"))
#c = int(input("liczba c"))

#temp = a**b
#print(temp+c)

#Zad3

#napis = input("napis")
#temp = 0
#for i in range(1,len(napis),1):
#  if (napis[i-1] == napis[-i]):
#        continue
#    else:
#        print(napis, "nie jest palindromem")
#        temp += 1
#        break

#if (temp == 0):
#    print(napis, "jest palindromem")

#Zad 4

#a = int(input("liczba:"))

#i = 2
#while i<a:
#    if (a%i==0):
#        print("nie jest liczba pierwsza")
#        break

#    else:
#        i += 1
#        continue

#else:
#    print("liczba jest liczba pierwsza")

#Zad 5

#a = int(input("liczba:"))

#temp = 0
#i = 1
#while i<a:
#    if (a%i==0):
#        temp += i
#        i += 1
#        continue
#    else:
#        i += 1
#        continue
#else:
#    if(temp == a):
#        print(a, "jest liczba doskonałą")
#    else:
#        print(a, "nie jest liczba doskonałą")


#Zad 6

#lista = [1,2,1.2,33,1.5,2.3]

#for i in range(len(lista)):
#    lista[i] *= lista[i]

#print(lista)

#Zad7
#lista = []
#i=0
#while i < 10:
#    a = int(input("liczba:"))
#    if (a%2==0):
#        lista.append(a)
#        i+=1
#    else:
#        i+=1
#print(lista)

#Zad8
lista = ["a", "b", "c", "c", "a", "d", "e", "a"]
slownik = {}
i = 0
y = 0
lis = []
size = len(lista)
while i < size:
    slownik[lista[i]] = 0
    i+=1
else:
    while y < size:
        slownik[lista[y]] += 1
        y += 1
    else:
        lis = slownik.keys()
        for x in range(len(lis)):
            if(lis[x].is_integer()==false):
                del.slownik(lis[x])

print(slownik)

