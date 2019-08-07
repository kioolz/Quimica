# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 18:38:04 2019

@author: Caio
"""






# De acordo com a Lei de Dalton, as substâncias seriam formadas por átomos indivisiveis de massa e raio bem especificos
# Atomos iguais teriam massas e raios iguais
# A combinação de atomos geram substâncias conhecidas em proporções específicas



# De acordo com a Lei Volumétrica de Gay Lussac, proporções especificas de volumes formam volumes específicos de substâncias
# O que implica que, são necessárias quantidades fixas de moléculas de cada átomo elementar, para a formação de novas substâncias
# 2 Volumes moleculares de Gás Hidrogênio Contém 4 átomos de hidrogênio que combinados a 1 volume molecular de oxigênio formam 2 moléculas de água



# A hipótese de Avogrado diz que existem a mesma quantidade de moléculas por unidade de volume nos átomos.




#Define a classe Densidade Molecular - Isso permite definir a síntese de substâncias - Afinal estamos tratando de moléculas por volume.




class SíntesedeSubstâncias:
    
    def DensidadeMolecular():
        
        print ("Insira a quantidade de moléculas")
        N=int(input()) # Número de moléculas expresso em número inteiro
        print("A quantidade de moléculas é:", N)
        
        print ("Insira o valor absoluto do volume que as contém")
        V=float(input()) #Valor do volume -Expresso em unidades de volume
        print("O volume que contém as moléculas é:", V)
        
        n = N/V
        print("A densidade molecular é:", n)
        
        
        
        
    DensidadeMolecular()



#
    def MonóxidodeNitrogênio():
        # Insere a quantidade de moléculas de cada elemento
        MoleculasdeNitrogênio=int(input("Insira a quantidade de moléculas de nitrogênio:",)) 
        MoleculasdeOxigênio=int(input("Insira a quantidade de moléculas de oxigênio:", ))
        #Exibe uma mensagem para o usuário informando a quantidade de moléculas 
        print("Total de moléculas de nitrogênio", MoleculasdeNitrogênio, '\n', "MoleculasdeOxigenio", MoleculasdeOxigênio)
               
        MonóxidodeNitrogênioProduzido= 2 * MoleculasdeNitrogênio + 2 * MoleculasdeOxigênio
               
        #Função para calcular o total de Moléculas de Monóxido de Nitrogênio produzidas
        print("Esta é a quantidade de Átomos produzidas de Monóxido de Nitrogênio:", MonóxidodeNitrogênioProduzido)
               
    MonóxidodeNitrogênio()



    def Água():
    
        Hidrogênio=int(input())
        Oxigênio=int(input())
        Água = 2 * Hidrogênio + 1 *Oxigênio
        print(Hidrogênio)
        print(Oxigênio)
        print(Água)
    Água()


    def Amônia():
        
        Nitrogênio=int(input())
        Hidrogênio=int(input())
        Amônia=Nitrogênio+3*Hidrogênio
        
        print ("Foram produzidas:", Amônia,"moléculas de amônia")
        
    Amônia()


#Este programa não está completo pois ele não considera que os átomos respeitam proporções definidas para formarem substâncias
   # E eu teria de fazer isso manualmente, o que torna muito complicado.














