#!/usr/bin/python

#############################################################################
#                                                                           #
#         RESOLUTION D'UN PROBLEME D'OPTIMISATION SANS CONTRAINTES          #
#                                                                           #
#         Methode d'optimisation de SciPy                                   #
#                                                                           #
#############################################################################

def Scipy_Optim(Oracle, x0):
    
    from scipy.optimize import minimize

    results = minimize(lambda x: Oracle(x)[0], x0, jac=lambda x: Oracle(x)[1])

    critere_opt = results.fun
    gradient_opt = results.jac
    x_opt = results.x
    
    mess = results.message
    print(mess)
    
    return critere_opt, gradient_opt, x_opt
