# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 18:29:31 2019

@author: Caio
"""










# Criando uma lista que será preenchida com o nome dos elementos.
Elementos = []



#Código que preenche uma tabela que o usuário irá escolher os elementos que deseja trabalhar
#Enquanto não preenche a lista com os 118 elementos da tabela
for i in range(118):    
    print('Escreva um elemento : (Aperte enter sem digitar nada para sair)') #Escreve um nome elemento na tabela
    Elemento = str(input()) #Usuário insere o elemento na lista de elementos
    
    if Elemento =='': #Se o elemento estiver vazio, pare o For
        break
    else: # Se não estiver vazio, e não estiver dentro da lista de elementos.
        if Elemento not in Elementos:
            print ("O elemento não está na tabela, mas será inserido agora")
            Elementos.append(Elemento) # Insere o elemento dentro da lista de elementos            
            
#Escreve a lista do programa caso o usuário queira verificar se está completa.
print("Esta é sua lista de elementos:", Elementos) 



#Usando a biblioteca pandas para criar uma tabela de dados simples com as propriedades dos átomos para o usuário

import pandas as pd


#Cria o dicionário principal que contem as informações da tabela periódica.
TabelaPeriodica = [{'Átomos da tabela periódica': Elementos}]
Substâncias = [{}]



pd.DataFrame(TabelaPeriodica)




