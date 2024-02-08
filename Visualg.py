#!/usr/bin/python

##############################################################################
#                                                                            #
#       VISUALISATION DES ITEREES DE L'ALGORITHME D'OPTIMISATION             #
#                                                                            #
##############################################################################

# Affichage des resultats obtenus durant l'algorithme
#
# Variables en entree
# 
#    - gradient_list : tableau contenant la norme du gradient
#                      du critere a chaque iteration
#                      de l'algorithme d'optimisation.
#    - step_list     : tableau contenant la longueur du pas
#                      de gradient a chaque iteration.
#    - critere_list  : tableau contenant la valeur du critere
#
# Seules la norme du gradient et la longueur du pas sont affichees

def Visualg(gradient_list, step_list, critere_list):

    import matplotlib.pyplot as plt
    
    plt.subplot(2, 1, 1)
    plt.gca().set_title("Norme du gradient au cours des iterations")
    plt.gca().set_yscale('log')
    plt.plot(gradient_list, label="Norme du gradient")
    
    plt.subplot(2, 1, 2)
    plt.gca().set_title("Pas de gradient au cours des iterations")
    plt.gca().set_yscale('log')
    plt.plot(step_list, label="Longueur du pas")
    
    plt.tight_layout(rect=(0, 0, 1, 2))
    plt.show()
