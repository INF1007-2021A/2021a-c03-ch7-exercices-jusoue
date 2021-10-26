#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
from turtle import *

# TODO: Définissez vos fonction ici
def volume_ellipsoide(a, b, c, volumic_mass):
    volume = (4/3) * math.pi * a * b * c
    mass = volumic_mass * volume
    return (volume, mass)

def frequence(sentence):
    letter_dic = {}
    for letter in sentence:
        if (letter != " " and letter not in letter_dic):
            letter_dic[letter] = 0
        if letter in letter_dic:
            letter_dic[letter] += 1
    return letter_dic

def draw_branch(branch_len, pen_len, angle):
    if (branch_len > 0 and pen_len > 0):
        pensize(pen_len)
        forward(branch_len)
        right(angle)
        draw_branch(branch_len - 10, pen_len - 1, angle - 5)
        left(angle * 2)
        draw_branch(branch_len - 10, pen_len - 1, angle - 5)
        right(angle)
        back(branch_len)

def draw_tree():
    setheading(90)
    color("brown")
    draw_branch(70, 7, 35)
    done()

def valide(string):
    valide = True
    for letter in string:
        if (letter != "a" and letter != "t" and letter != "g" and letter != "c"):
            print("entrez une chaine valide.")
            valide = False
            break
    return valide 

def proportion(chaine, sequence):
    if valide(chaine) and valide(sequence):
        print("chaine: ", chaine)
        print("sequence:", sequence)
        print("Il y a {0:.2f}% de {1}".format((chaine.count(sequence) / len(chaine)) * 100, sequence))
    return None

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    volumic_mass = float(input("Entrez la masse volumique ici: "))
    print(volume_ellipsoide(a, b, c, volumic_mass))

    sentence = "patrick sebastien is a very young and handsome person"
    print(sorted(frequence(sentence).items(), key = lambda x: x[1])[-1])

    draw_tree()
    exitonclick()

    chaine = input("entrez une chaine valide:")
    sequence = input("entrez une sequence valide:") 
    proportion(chaine, sequence)