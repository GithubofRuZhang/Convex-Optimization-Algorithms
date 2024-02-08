#!/usr/bin/python

#############################################################################
#                                                                           #
#        DONNEES ASSOCIEES A LA RESOLUTION DES EQUATIONS D'UN RESEAU        #
#                                                                           #
#        Probleme_R : reseau representant un cas relativement realiste      #
#                                                                           #
#############################################################################

# Variables du probleme
#
# nom  : nom du reseau
#
# n    : nombre total d'arcs
# m    : nombre total de noeuds
# mr   : nombre de noeuds de type reservoir
# md   : nombre de noeuds de type demande (= m-mr)
#
# orig : vecteur des numeros des noeuds initiaux des arcs : M(1,n)
# dest : vecteur des numeros des noeuds finaux   des arcs : M(1,n)
# absn : vecteur des abscisses des noeuds                 : M(1,m)
# ordn : vecteur des ordonnees des noeuds                 : M(1,m)
#
# r    : vecteur des resistances des arcs                 : M(n,1)
# pr   : vecteur des pressions des noeuds reservoirs      : M(mr,1)
# fd   : vecteur des flux des noeuds de demande           : M(md,1)

from numpy import array

##### Nom du reseau

nom = 'Realiste'

##### Dimensions du reseau

# Nombre de noeuds et d'arcs
n = 22
m = 16
mr = 3
md = m - mr

##### Caracteristiques des noeuds et des arcs
 
# Numeros des noeuds initiaux et finaux des arcs
orig = array([1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 13, 1, 2, 4, 5, 7, 8, 14, 2, 10])
dest = array([4, 16, 15, 5, 6, 10, 16, 9, 12, 10, 11, 14, 15, 16, 6, 8, 9, 11, 13, 15, 4, 13])

orig = orig - 1 # car Python commence a 0
dest = dest - 1 # car Python commence a 0

# Coordonnees des noeuds
absn = array([11, 18, 38, 4, 8, 15, 26, 4, 10, 19, 26, 7, 21, 33, 33, 16])
ordn = array([28, 21, 8, 21, 17, 17, 26, 9, 13, 13, 18, 4, 9, 18, 12, 24])

# Resistances des arcs
r = array([100, 10, 1000, 100, 100, 10, 1000, 100, 1000, 100, 1000, 1000, 1000, 10, 10, 100 , 100, 1000, 100, 1000, 100, 10])

# Pressions au pied des reservoirs (en m)
pr = array([105, 104, 110])

# Flux aux noeuds de demande (en m3/s)
fd = array([+0.08, -1.30, +0.13, +0.09, +0.16, +0.14, +0.12, +0.07, +0.17, +0.11, +0.25, +0.01, +0.13])
