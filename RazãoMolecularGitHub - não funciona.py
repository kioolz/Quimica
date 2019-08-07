# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 20:47:34 2019

@author: Caio
"""

# Projeto de Calculadora Química - 
# Projeto versão 1.00000000000000000 inifinitos três pontos ... 1

# Criando compostos químicos

class MassadosNumeradoresdaRazaoMolecular:
    listamassa1=[] #Lista do átomo do numerador
    m1=float(input()) #Insere a variável do tipo real para a massa 1 
    print(m1) #Escreve a variável do tipo massa
    listamassa1.append(m1)
    print(listamassa1)

class MassadosDenominadoresdaRazaoMolecular:
    listamassa2=[] #Lista do átomo do denominador
    m2=float(input()) #Insere a variável do tipo real para a massa 1 
    print(m2) #Escreve a variável do tipo massa
    listamassa2.append(m2)
    print(listamassa2)    

class MassadaRazaoMolecular:
        listarazaomolecular=[]  
        mi=m1/m2
        print(mi)
        listarazaomolecular.append(mi)
        print(listarazaomolecular)
        
        