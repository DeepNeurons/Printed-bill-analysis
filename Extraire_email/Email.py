#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 13:27:14 2021

@author: hb
"""
import re
def email(text):
    e_mail = []
    
    mail = re.findall(r'(\S|\d)+@\S+', text)
    
    if len(mail):
        e_mail.append(mail)
    else:
        e_mail.append("Pas de e-mail trouvé")
        
    return e_mail
        