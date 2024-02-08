#!/usr/bin/python

###############################################################################
#                                                                             #
#  STRUCTURES DE DONNEES NECESSAIRES A LA RESOLUTION DES EQUATIONS DU RESEAU  #
#                                                                             #
#  Structures_N : matrices normales                                           #
#                                                                             #
###############################################################################

# Matrices issues de la topologie du reseau
#
# A    : matrice d'incidence noeuds-arcs du graphe        : M(m,n)
# Ar   : sous-matrice de A correspondant aux reservoirs   : M(mr,n)
# Ad   : sous-matrice complementaire de Ar pour A         : M(md,n)
# AdT  : plus grande sous-matrice carree inversible de Ad : M(md,md)
# AdI  : matrice inverse de AdT                           : M(md,md)
# AdC  : sous-matrice complementaire de AdT pour Ad       : M(md,n-md)
# B    : matrice d'incidence arcs-cycles du graphe        : M(n,n-md)
#
# Debit admissible
#
# q0   : vecteur des debits admissibles des arcs          : M(n,1)

from numpy import dot
from numpy import eye
from numpy import zeros
from numpy.linalg import inv

##### Probleme_R : probleme realiste

from Probleme_R import *

##### Matrice d'incidence et sous-matrices associees

# Matrice d'incidence noeuds-arcs du graphe
A = zeros((m, n))
for i in range(m):
    A[i, orig == i] = -1
    A[i, dest == i] = +1

# Partition de A suivant le type des noeuds
Ar = A[:mr,:]
Ad = A[mr:m,:]

# Sous-matrice de Ad associee a un arbre et inverse
AdT = Ad[:,:md]
AdI = inv(AdT)

# Sous matrice de Ad associee a un coarbre
AdC = Ad[:,md:n]

# Matrice d'incidence arcs-cycles
B = zeros((n, n-md))
B[:md,:] = -dot(AdI, AdC)
B[md:,:] = eye(n-md)

##### Vecteur des debits admissibles
q0 = zeros(n)
q0[:md] = dot(AdI,fd)
