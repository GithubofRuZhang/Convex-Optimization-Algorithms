#!/usr/bin/python

###############################################################################
#                                                                             #
# CALCUL DES VARIABLES HYDRAULIQUES DU RESEAU A PARTIR DES DEBITS DU CO-ARBRE #
#                                                                             #
###############################################################################

# Supposant connu le vecteur des debits sur le co-arbre, on calcule l'ensemble
# des variables  hydrauliques du reseau ; on dispose pour cela des matrices et
# du debit admissible qui ont ete calcules precedemment.
#
# Variables en entree
#
#    - qc   : vecteur des debits des arcs du co-arbre
#
# Variables en sortie
#
#    - q    : vecteur des debits des arcs
#    - z    : vecteur des pertes de charge des arcs
#    - f    : vecteur des flux des noeuds
#    - p    : vecteur des pressions des noeuds

def HydrauliqueP(qc, m, mr, md, r, pr, fd, Ar, AdI, B, q0):
    
    from numpy import dot
    from numpy import abs
    from numpy import zeros

    # Debits des arcs
    q = q0 + B.dot(qc)
    
    # Pertes de charge des arcs
    z = r * abs(q) * q
    
    # Flux des noeuds
    f = zeros(m)
    f[:mr] = Ar.dot(q)
    f[mr:] = fd
    
    # Pression aux noeuds
    p = zeros(m)
    p[:mr] = pr
    tmp = Ar.T.dot(pr) + z
    p[mr:] = - AdI.T.dot(tmp[:md])

    return q, z, f, p
