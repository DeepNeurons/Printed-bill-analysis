#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 10:32:08 2021

@author: hb
"""

results = [['LAGARDERE TR FRANCE SNC',
  "1 AV DE L'HOPITAL",
  '74374 METZ TESSY (FR)',
  "N'siret 54209533613446 NAF 4762Z",
  'NOTVA FR25542095336',
  'DUPLICATA TICKET',
  'VENTE',
  'Document N° 143',
  'Ticket réimprimé 1 fois',
  'Document original B0044 (dYjo)',
  'B0044 (Ntp7) - TCPOS Version 4.5.18',
  'Nbre ligne(s): 4',
  'Date : 05/11/2020 11:27:20',
  'Caisse : 2 - Ets: 384701',
  'Caissier: 4 - ELOISE4',
  'Designation Article',
  'Quat é Prix Uté',
  'TTC EUR TX',
  'CAFE EXPRESSO',
  '1,00 x 1,25',
  '1,25 10',
  'CAFE LATTE',
  '1.00',
  '1.85',
  '1,85 10',
  'TRIO CHOCO GOURMAND S CHOCOLATS',
  '1,00 x 2,05',
  '2,05 6',
  'TRIO CHOCO GOURMAND 3 CHOC. ATS',
  '1,00 x 2,05',
  '2,05 6',
  'Total TTC EUR',
  '7,20',
  'TVA',
  '0 5.50%',
  '(9) 0.00%',
  'HT',
  '3,89',
  '2.82',
  '6.71',
  'TVA',
  '0,21',
  '0.28',
  '0.49',
  'TTC',
  '4, 10',
  '3,10',
  'TO AUX',
  '7.20',
  'CARTE BNCAIRE',
  '7.20',
  '6660014312564326',
  ''],
 ['MAXIBAZAR',
  'ANNEMASSE',
  '#LOGO_1#',
  'SAS QUEST HARMONIE',
  '22 rue de la resistance',
  '74100 ANNEMASSE',
  'Code NAF : 4759B',
  'SIRET : 312 326 978 00334',
  'Capital de capital de 182 882.45 -',
  'TVA intra : FR37 312 326 978',
  'Impression n°1',
  'CARTE BANCAIRE',
  'SANS CONTACT',
  '00',
  'CLIENT COMPTOIR FR',
  'France',
  'VENTE',
  'A0000000421010',
  'CB',
  'LE 27/02/21 A 14:43:54',
  'OUEST HARMONIE 74',
  'ANNEMASSE',
  '7849204 31232697 800334',
  '30077',
  '############5778',
  '01436B FC021847 FF',
  '001 000014 33 C',
  'MONTANT :',
  '15,99 EUR',
  'DEBIT',
  'Le 27/02/2021 à 14:44',
  'Caissier : 23 | DEBORAH',
  'Vendeur :',
  'Ticket nº 096-3-3178',
  'PA Tot.',
  'PX Unit.',
  'Qté',
  '170155739',
  'PORTE MANTEAU METAL 8 TIGES',
  '15.99',
  '1.00',
  'Total net HT',
  'Total net TTC 13.33',
  '15.99',
  'TVA',
  'TAUX',
  'HT',
  'TVA',
  'TTC',
  '1 20.00% 13.33',
  '2.66 15.99',
  'Règlement',
  '15.99',
  'EUR/carte bancaire',
  '03/1/PVG5',
  '507-3.9.7/B0079aaum',
  'Maxi Bazar vous remercie de votre visa',
  '04.50.04.92.72',
  'ouverture du lundi au samedi',
  'Retour avec avoir uniquement',
  'Echange sous 15 jours',
  "avec emballage d'origine",
  'Les articles en soldes',
  'ne sont ni repris ni échangés',
  'Avoir valable 2 mois',
  'www.maxibazar.fr',
  '']]

def tva(resultat_api):
    import pandas as pd
    zipcodes= pd.read_csv('allCountriesCSV.csv')
    zipcodes=zipcodes[['COUNTRY', 'POSTAL_CODE', 'CITY']]
    zipcodes['COUNTRY']= zipcodes['COUNTRY'].astype(str)
    zipcodes['POSTAL_CODE']= zipcodes['POSTAL_CODE'].astype(str)
    zipcodes['CITY']= zipcodes['CITY'].astype(str)
    

    import pycountry
    list_alpha_2 = [i.alpha_2 for i in list(pycountry.countries)]
    list_alpha_3 = [i.alpha_3 for i in list(pycountry.countries)]    
    
    def country_flag(code):
        if (len(code)==2 and code in list_alpha_2):
            return pycountry.countries.get(alpha_2=code).name
        elif (len(code)==3 and code in list_alpha_3):
            return pycountry.countries.get(alpha_3=code).name
        else:
            return ['Nan']
        
    
    
    import re
    l=[]
    for res in resultat_api:
        total_len= len(res)
        part_len= round(total_len*30 /100)
        ll=[]
        all_text= ' '.join(text for text in res[: part_len])+ ' '.join(text for text in res[-part_len:])
        for i in range(len(zipcodes)):
            if zipcodes['CITY'][i].lower().replace('-', ' ') in all_text.lower().replace('-', ' ') and zipcodes['POSTAL_CODE'][i] in all_text.split():
                ll.append(country_flag(zipcodes['COUNTRY'][i]))
                break
            else:
                continue
        if ll== []:
            ll.append('')
        l.append(list(set(ll)))
    

    
    fr_data= pd.read_csv('Countries_information.csv')
    
    
    
    fr_count=[]
    for res in resultat_api:
        ll=[]
        total_len= len(res)
        part_len= round(total_len*30 /100)
        all_text= ' '.join(text for text in res[: part_len])+ ' '.join(text for text in res[-part_len:])
        all_text= all_text.lower()
        
        for i in range(len(fr_data)):
            
            if fr_data['country'][i].lower() in all_text.lower():
                before= all_text[: all_text.index(fr_data['country'][i].lower())]
                after= all_text[all_text.index(fr_data['country'][i].lower()) + len(fr_data['country'][i].lower()):]
                if before== '':
                    before= ' '
                if after== '':
                    after= ' '
                if before[-1].isalnum()==False and after[0].isalnum()==False:
                    ll.append(fr_data['country'][i])
                else:
                    continue
            else:
                continue
        if ll== []:
            ll.append('')
        fr_count.append(list(set(ll)))
        
        
    type_tva=[[''] for _ in range(len(l))]
    for i in range(len(l)):
        print(dev_raw[i])
        if 'CHF' in dev_raw[i]:
            type_tva[i]=[['Switzerland']]        
        elif l[i] != ['']:
            type_tva[i]=[l[i]]
        else:
            type_tva[i]= [fr_count[i]]
            
    for i in range(len(dev_raw)):
        all_text= ' '.join(resultat_api[i])
        all_text= all_text.replace(',','.') 
        parts=all_text.split()
        perc=[]
        for j in range(len(parts)):
            word = parts[j]
            if '%' in word:
                #print(word)
                perc.append(word.split("%")[0])
        m= list(filter(None, list(set(perc))))
        type_tva[i].extend(m)
        print(type_tva[i])
        #print('___________________________________')
        
        
    final_final= []
    for i in range(len(type_tva)):
        final_final.append(str(type_tva[i]))
    return final_final

print(tva(results))