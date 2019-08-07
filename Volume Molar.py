# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 14:28:50 2019

@author: Caio
"""

# Volume Molar (Vm)
       
        #1 mol sempre tem 6.02 * 10^23 moléculas
        
        # O mesmo número de moléculas, independentemente da natureza do gás,
        #ocupa sempre o mesmo volume em determinada pressão e temperatura, segundo o que diz a Lei de Avogrado
        # Volumes iguais de gases quaisquer, quando medidos à mesma pressão e temperatura, encerram o mesmo número de moléculas
        
        # O Volume molar (Vm) de um gás, em determinada pressão e temperatura, é o volume que
        #1 mol desse gás ocupa na pressão e temperatura consideradas.
        def VolumeMolar():
            
            "Nas condições normais de pressão e temperatura, o volume molar é 22.4 litros"
            
            
            
            
            Vm = 22.4
            P=input(float())
            print(P)
            V=input(float())
            print(V)
            T=input(float())
            print(T)
            Po=input(float())
            print(Po)
            Vo=input(float())
            print(Vo)
            To=input(float())
            print(To)
            R = 0.082
            # É necessário criar uma estrutura condicional que permita ao usuário escolher em quais unidades trabalhar"
            
            print (R,"atm * litro / kelvin * mol)
            print ()
            
            #Equação de Clapeyron - Equação geral dos gases ideais"
            P*V*T=Po*Vo*To
            
            
            P * V = (m/M) * R * T
            
            #P = Pressão do gás
            #V = volume do gás
            #n = quantidade do gás em mols
            #m = massa do gás em gramas
            #M = massa molar do gás
            #R = constante universal dos gases perfeitos
            #T = temperatura do gás, em kelvins
            VolumeMolar():
        
        