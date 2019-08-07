# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 10:45:03 2019

@author: Caio
"""


class Átomos():
    
    # O Numero atômico (Z): corresponde ao número de prótons (P) no núcleo do átomo
    
    # O numero atômico caracteriza o elemento químico
    
    # O numero de massa (A)  é a soma do número de prótons com o numero de neutrôns
    
    
    # Organizando os elementos pelo numero de massa (A)"
    
    def ListadoNumerodeMassas():
        
        NumerosdeMassa=[]
        
        for i in range(118):
            
        
        
            Z = int(input("Insira o numero atômico ou de protons: ")) #Número de Protons
            N = int(input("Insira o numero de neutrôns")) #Número de neutrôns
            NumerosdeMassa.append(Z+N)
            print(NumerosdeMassa)
            
            
        return NumerosdeMassa
        
    






    
