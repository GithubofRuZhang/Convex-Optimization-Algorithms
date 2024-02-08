#!/usr/bin/python

##############################################################################
#                                                                            #
#  VERIFICATION DES EQUATIONS D'EQUILIBRE D'UN RESEAU DE DISTRIBUTION D'EAU  #
#                                                                            #
##############################################################################

# On suppose determinee la solution du probleme d'optimisation et reconstituee
# les variables hydrauliques du reseau. On calcule le plus grand ecart sur les
# 2 series d'equations qui caracterisent l'equilibre du reseau.
#
# Variables en entree
#
#    - q : vecteur des debits des arcs
#    - z : vecteur des pertes de charge des arcs
#    - f : vecteur des flux aux noeuds
#    - p : vecteur des pressions aux noeuds

def Verification(A, q, z, f, p):

    from numpy import dot
    from numpy import abs
    
    # Ecarts maximaux sur les lois de Kirschoff
    tol_debits = max(abs(A.dot(q) - f))
    tol_pression = max(abs(A.T.dot(p) + z))
    
    # Affichage
    print()
    print("Verification des equations d'equilibre du reseau")
    print("Sur les debits : {}".format(tol_debits))
    print("Sur les pressions : {}".format(tol_pression))

