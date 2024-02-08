#!/usr/bin/python

###############################################################################
#                                                                             #
#  STRUCTURES DE DONNEES NECESSAIRES A LA RESOLUTION DES EQUATIONS DU RESEAU  #
#                                                                             #
#  Structures_S : matrices creuses                                           #
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
from numpy import zeros
from numpy import ones
from numpy import array
from numpy import int64
from numpy import concatenate

from scipy import sparse
from scipy.sparse import eye
from scipy.sparse import coo_matrix
from scipy.sparse import vstack
from scipy.sparse.linalg import inv

##### Probleme_P : probleme de taille parametrable

from Probleme_P import *

##### Matrice d'incidence et sous-matrices associees

# Matrice d'incidence noeuds-arcs du graphe
row_ind = concatenate((orig.astype(int64), dest.astype(int64)), axis=0)
col_ind = concatenate((array(range(0,n)), array(range(0,n))), axis=0)
mat_dat = concatenate((-ones(n), ones(n)), axis=0)
A = coo_matrix((mat_dat, (row_ind, col_ind)))

# Passage en mode entier CSC
A = A.tocsc()
A = A.astype(int64)

# Partition de A suivant le type des noeuds
Ar = A[:mr,:]
Ad = A[mr:m,:]

# Sous-matrice de Ad associee a un arbre et inverse
AdT = Ad[:,:md]
AdI = inv(AdT).astype(int64)

# Sous matrice de Ad associee a un coarbre
AdC = Ad[:,md:n]

# Matrice d'incidence arcs-cycles
B1 = - dot(AdI, AdC)
B2 = eye(n-md, dtype=int64, format="csc")
B = vstack([B1,B2], format="csc")

###### Vecteur des debits admissibles
q0 = zeros(n)
q0[:md] = AdI.dot(fd)
