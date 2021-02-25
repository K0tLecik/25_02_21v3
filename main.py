from math import *
import math

# Zad1. Napisz pierwszy skrypt, w którym zadeklarujesz po dwie zmienne każdego typu a następnie wyświetl te zmiennea

print("zadanie 1:\n")

a=13
a1 = 5
a2 = 10
b1 = 5.1
b2 = 5.2
c1 = 'cos1'
c2 = 'cos2'
d1 = (5j+5)
d2 = (10j+5)

print(a1,a2,b1,b2,c1,c2,d1,d2)

# Zad2. Stwórz skrypt kalkulator, w którym wykorzystać wszystkie podstawowe działania arytmetyczne

print("zadanie 2\n")

dodawanie = a1+b1
odejmowanie = a1-b1
mnozenie = a1*b1
dzielenie = a2/a1

print(dodawanie, odejmowanie, mnozenie, dzielenie)

# Zad3. Napisz skrypt, w którym stworzysz operatory przyrostkowe dla operacji: +, -, *, /, **, %

print("zadanie 3:\n")

x=a+a
print(x)
x=a-a
print(x)
x=a*a
print(x)
x=a/a
print(x)
x=a**a
print(x)
x=a%a
print(x)

# Zad4. Napisz skrypt, który policzy i wyświetli następujące wyrażenia:

print("zadanie 4:\n")

print(math.e**10)
print("\n")
y=pow((math.log(5+((math.sin(8.00)**2)))),1/6)
print(y)
print("\n")
