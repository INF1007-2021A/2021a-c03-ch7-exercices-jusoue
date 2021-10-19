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

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    volumic_mass = float(input("Entrez la masse volumique ici: "))
    print(volume_ellipsoide(a, b, c, volumic_mass))
