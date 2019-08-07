# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 21:18:08 2019

@author: Caio
"""
#Se dois elementos A e B formarem mais de um composto, 
#as massas de A que se combinam com a mesma massa de B, nos diferentes compostos, devem ter
# como razões, números inteiros.


# Variável booleana que mantém o programa funcionando

V = True 

# Botões

Sim = True
Não = False

#Programa 

while V!=False:
    
    listademassa1=[]
    listadedemassa2=[]
    listaderazoes=[]
    
    print ("Insira o primeiro numerador")
    massa1=float(input())
    print("insira o primeiro denominador")
    massa2=float(input())
    
    listademassa1.append(massa1)
    listademassa2.append(massa2)
