#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import turtle

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

def draw_brench():

    return 0

def draw_tree():

    return 0

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    volumic_mass = float(input("Entrez la masse volumique ici: "))
    print(volume_ellipsoide(a, b, c, volumic_mass))

    sentence = "patrick sebastien is a very young and handsome person"
    print(sorted(frequence(sentence).items(), key = lambda x: x[1])[-1])
