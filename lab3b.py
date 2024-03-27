import math
import sys
import random

def zad1():
    lista = []
    while 0 < 1:
        a = input("Podaj:")
        if a == "end":
            print(lista)
            break
        else:
            if a.isdigit() == True:
                lista.append(a)
                print(lista)
            else:
                print(lista)
                continue

def zad2():
    a = int(input("Podaj a"))
    b = int(input("Podaj b"))

    if a < 0:
        print("Funkcja y=",a,'x+',b," jest malejąca")
    else:
        if a == 0:
            print("Funkcja y=", a, 'x+', b, " jest stała")
        else:
            print("Funkcja y=", a, 'x+', b, " jest rosnąca")


def zad4():
    a = int(input("Podaj długośc przyprostokątnej a"))
    b = int(input("Podaj długośc przyprostokątnej b"))

    c = math.sqrt(a*a + b*b)
    print("Przeciwprostokątna wynosi:", c)

def zad5(a1 = 1, r = 1, ile = 10):
    sum = a1
    for i in range(ile):
        sum += r

    print(sum)

def quess_the_number():
    punkty = 0
    for i in range(5):
        x = random.randint(1, 10)
        a = int(input("Zgadnij liczbę:"))

        if x == a:
            punkty += 10
            print("Wylosowana liczba to", x, " Zdobywasz 10 punktów")
        else:
            punkty -= 1
            print("Wylosowana liczba to", x, " Tracisz 1 punkt")
    print("Koniec gry. Twoja punktacja to", punkty, "punktów!")


def zad8(num):
    n = num
    if num < 10:
        print(num)
    else:
        while n > 10:
            num =num%10
            n //= 10



def multipli_game():
    pop = 0
    bad = 0
    for i in range(1,11):
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        print("Pytanie", i,":", x, "*", y)
        a = int(input("Odpowiedź:"))
        if a == x*y:
            print("Poprawna odpowiedź!")
            pop =+ 1
        else:
            print("Błędna odpowiedź, poprawną odpowiedzią jest", x*y)
            bad += 1
    print("Bledne odpowiedzi:", bad)
    print("Poprawne odpowiedzi", pop)


def main():
#   zad1()
#   zad2()
#   zad4()
#   zad5(3, 2, 3)
#   quess_the_number()
    zad8(35)
#   multipli_game()

main()