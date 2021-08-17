#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 23:51:27 2021

@author: hb
"""

import re
def num_carte(text):

    
    N_carte = []
    N = re.findall(r'[x]{12}\d{4}',text.lower())
    if len(N):
        N_carte = N
    else:
        N_carte.append("Aucune carte bancaire trouvée")
    return ' '.join(N_carte)