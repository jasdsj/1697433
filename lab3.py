import math
import sys

def zad2():
    a = int(input("wysokosc wiezy"))
    temp = 0
    i = 1
    lista = []
    while i <= a:
        lista.append("A")
        print("")
        for j in range(len(lista)):
            print(lista[j], end = " ")
        i+=1

def zad3():
    a = int(input("wysokosc piramidy"))
    temp = 0
    i = 1
    lista = []
    for x in range(a):
        lista.insert(0, " ")
    while i <= a:
        lista.append("A A")
        lista.pop(0)
        print("")
        for j in range(len(lista)):
            print(lista[j], end = " ")
        i+=1
def main():
#   zad2()
#   zad3()



main()
