import math
import random
import sys
import os


def zad2(min_val, max_val, ile):
    if min_val >= max_val or ile <= 0:
        print("Błąd: Nieprawidłowe parametry.")
        return None

    lista = [random.randint(min_val, max_val) for _ in range(ile)]
    print("Wygenerowana lista:", lista)

    roznice = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] != lista[j]:
                roznice.append(abs(lista[i] - lista[j]))

    return roznice


def main():
    min_val = int(input("Podaj wartość minimalną: "))
    max_val = int(input("Podaj wartość maksymalną: "))
    ile = int(input("Podaj ilość elementów: "))

    roznice = zad2(min_val, max_val, ile)
    if roznice is not None:
        print("Różnice pomiędzy elementami:", roznice)


if __name__ == "__main__":
    main()

'''
def zad3(liczby):
    if not os.path.exists(liczby):
        print("Plik o nazwie", liczby, "nie został znaleziony.")
        return None

    plik = open(liczby, 'r')
    kolumny = zip(*(map(int, linia.split()) for linia in plik))
    wynik = [sum(kolumna) for kolumna in kolumny]
    plik.close()
    return wynik

def zad4(a, h):
    if a <= 0 or h <= 0:
        print("Długość boku podstawy (a) oraz wysokość (h) muszą być dodatnie.")
        sys.exit()
    pp = a * a * 2
    pb = a * h * 4
    pc = pp + pb
    return pc

def main():
    liczby = "liczby.txt"
    wynik = zad3(liczby)
    if wynik is not None:
        print("Sumy kolumn:", wynik)

    a = float(input("Podaj długość boku podstawy (a): "))
    h = float(input("Podaj wysokość graniastosłupa (h): "))
    wynik = zad4(a, h)
    print("Pole powierzchni całkowitej graniastosłupa wynosi:", wynik)

main()
'''
