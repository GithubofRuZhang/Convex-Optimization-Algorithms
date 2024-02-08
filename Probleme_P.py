#!/usr/bin/python

#############################################################################
#                                                                           #
#        DONNEES ASSOCIEES A LA RESOLUTION DES EQUATIONS D'UN RESEAU        #
#                                                                           #
#        Probleme_P : reseau de taille parametrable (arbre binaire)         #
#                                                                           #
#############################################################################

# Variables du probleme
#
# nom  : nom du reseau
#
# T    : nombre de niveaux dans l'arbre
#        les niveaux sont numerotes de 0 a T. On construit un arbre binaire
#        (la racine correspondant au niveau 0), et on ferme tous les cycles
#        elementaires a chaque niveau (soit 2^t - 1 cycles au niveau t).
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

from numpy import ones
from numpy import array
from numpy import concatenate
from numpy import random

##### Nom du reseau

nom = "Parametrable"

##### Nombre de niveaux et initialisation du generateur aleatoire

T = 13

gral = 123
random.seed(gral)

##### Dimensions du reseau

m  = (2**(T+1)) - 1
mr = 1
md = m - mr
n  = ((2**(T+1))-1) + ((2**(T+1))-1) - (T+1) - 1

##### Caracteristiques des noeuds et des arcs

orig = []
dest = []

# Arcs de l'arbre
num = 1
for t in range (0,T):
      ni = (2**t);
      nf = (2**(t+1)) - 1;
      nz = 2 * (nf-ni+1);
      aorg = array([range(ni,nf+1),range(ni,nf+1)])
      orig = concatenate((orig,aorg.flatten('F')), axis=0)
      dest = concatenate((dest,array(range(num+1,num+nz+1))), axis=0)
      num = num + nz;

# Arcs du coarbre
for t in range(1,T+1):
      ni = (2**t);
      nf = (2**(t+1)) - 1;
      orig = concatenate((orig, array(range(ni,nf))), axis=0)
      dest = concatenate((dest, array(range(ni+1,nf+1))), axis=0)

# Python commence a 0...
orig = orig - 1
dest = dest - 1

# Coordonnees des noeuds
absn = []
for t in range(0,T+1):
      ni = (2**t);
      nf = (2**(t+1)) - 1;
      na = 2**(T-t+1);
      nb = 2**(T-t);
      num = na*array(range(0,nf-ni+1)) + nb
      absn = concatenate((absn, num), axis=0)
      
ordn = []
for t in range(0,T+1):
      ni = (2**t);
      nf = (2**(t+1)) - 1;
      ordn = concatenate((ordn, (T-t+1)*ones(nf-ni+1)), axis=0)

# Resistances des arcs
r = 1000 * random.rand(n)

# Pressions au pied du reservoir (en m)
pr = array([200])

# Flux aux noeuds de demande (en m3/s)
fd = 0.1 * (random.rand(md)-0.5)

# Informations sur le reseau
print()
print('Tailles du reseau traite')
print('Nombre de niveaux :', T)
print('Nombre de tuyaux  :', n)
print('Nombre de noeuds  :', m)
