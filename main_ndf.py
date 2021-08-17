#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 11:15:15 2021

@author: hedi_bouchelliga
"""
from Extraire_dates import *
from Extraire_devise import *
from Extraire_prestataire import *
from Extraire_type_p import *
from Extraire_TVA_type import *
from Extraire_montant import *
from Ocr import *
from Extraire_email import *
##############################################################################
from Extraire_devise import Devises
from Extraire_dates import Date
from Extraire_montant import Montants
from Extraire_prestataire import Enseigne
from Extraire_email import Email
from Extraire_type_p import Numero_de_carte
from Ocr import image_to_text
from Extraire_type_p import type_paiement
##############################################################################
import re
import imutils
import json
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import requests
import time
from base64 import b64encode
from IPython.display import Image
from pylab import rcParams  
rcParams['figure.figsize'] = 10, 20
import string
import datetime
##############################################################################
time_start = time.time()
##############################################################################





def main(result):
    
    #result = image_to_text.requestOCR('https://vision.googleapis.com/v1/images:annotate', 'AIzaSyDOQ4gFyIPJqwnH5fJselRcMZRA6-hG3dw', imgpath)
    text_result = []
    
    #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#
    if result.status_code != 200 or result.json().get('error'):
        print ("Error  ")
    else:
        result = result.json()['responses'][0]['textAnnotations'][0]["description"].split('\n')
    text_result.extend(result)
    text = ' '.join(text_result)
    my_dict = {}
    my_dict = {'Prestataire et adresse' : list(Enseigne.enseigne(text_result)) , 'la date' : Date.date_type(text) , 'le devise' : Devises.devise(text) ,'ttc': Montants.extract_TTC(text),'TYPE DE PAIEMENT':' '.join(type_paiement.type_de_paiement(text_result)),'le numero de la carte' : Numero_de_carte.num_carte(text) ,'type de TVA' :'Non défini' }

    
    #my_dict = {'Prestataire et adresse' : list(Enseigne.enseigne(text_result)) ,'la date' : Date.date_type(text) ,'TYPE DE PAIEMENT':' '.join(type_paiement.type_de_paiement(text_result)),'le numero de la carte' : Numero_de_carte.num_carte(text) ,'type de TVA' :'Non définit il y essssssssssst' ,'E-mail' :' '.join(Email.email(text)),'devise' : Devises.devise(text)}
    
    return my_dict
   
    
   
    
                    ######################################################
                    #########******###*****####******#####*******#########
                    ###########**#####*########**###########**############
                    ###########**#####*****####******#######**############
                    ###########**#####*############**#######**############
                    ###########**#####*****####******#######**############
                    ######################################################
                    #****************************************************#
                    #****************************************************#
                    ######################################################

'''imgpath = '7ff67d7db19ecd365f583bd81288e70d.jpg'
res = image_to_text.requestOCR('https://vision.googleapis.com/v1/images:annotate', 'AIzaSyDOQ4gFyIPJqwnH5fJselRcMZRA6-hG3dw', imgpath)
print(main(imgpath))'''
