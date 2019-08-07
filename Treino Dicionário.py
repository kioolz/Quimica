# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 22:39:14 2019

@author: Caio
"""

# Usando dicionários como DataFrames

import pandas as pd

d = [{'cidade': 'Mesquita', "População":1000}, {'cidade':'NovaIguaçu',"População":2000},{'cidade':'Seropedica',"População":3000}]

pd.DataFrame(d)