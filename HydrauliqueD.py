#!/usr/bin/python

##############################################################################
#                                                                            #
# CALCUL DES VARIABLES HYDRAULIQUES DU RESEAU A PARTIR DES PRESSIONS NODALES #
#                                                                            #
##############################################################################

# Supposant connues les pressions aux noeuds de demande, on calcule l'ensemble
# des variables hydrauliques du reseau ; on dispose pour cela des matrices qui
# ont ete calculees precedemment.
#
# Variables en entree
#
#    - pd   : vecteur des pressions aux noeuds de demande
#
# Variables en sortie
#
#    - q    : vecteur des debits des arcs
#    - z    : vecteur des pertes de charge des arcs
#    - f    : vecteur des flux des noeuds
#    - p    : vecteur des pressions des noeuds

def HydrauliqueD(pd, m, mr, r, pr, fd, A, Ar):

    from numpy import dot
    from numpy import abs
    from numpy import sqrt
    from numpy import zeros

    # Pressions aux noeuds
    p = zeros(m)
    p[:mr] = pr
    p[mr:m] = pd
    
    # Pertes de charge des arcs
    z = - A.T.dot(p)
    
    # Debits des arcs
    q = z / sqrt(r*abs(z))
    
    # Flux aux noeuds
    f = zeros(m)
    f[:mr] = Ar.dot(q)
    f[mr:m]= fd
    
    return q, z, f, p
    
