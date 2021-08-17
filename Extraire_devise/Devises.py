import string
import re

def devise(text):
    
    punct= string.punctuation.replace('$','')

    matches = []

    pattern1 = "eur"
    pattern1_1 = "€"
    pattern2 = "$"
    pattern2_2 = "usd"
    pattern3 = "chf"
    match_1 = re.findall(r'eur|€',text.lower())   
    match_2 = re.findall(r'$|usd',text.lower())
    match_3 = re.findall(r'chf',text.lower())

    if match_1 != None:
        matches.extend(match_1)
    if match_2 !=None:
        matches.extend(match_2)
    if match_3 != None:
        matches.extend(match_3)

    
    #Devises = list(dict.fromkeys(matches))
    ##Devises = list(filter(None,matches))
    DEVISE = list(dict.fromkeys(filter(None,matches)))
    if 'eur' and 'chf' in DEVISE:
        
        for i in range(len(DEVISE)):
            DEVISE[i] = 'chf'
    
    if len(DEVISE):   ## empty list  error out of range
        
        return DEVISE[0]
    else:
        return 'Pas de devise detecté'


# text = 'LE NID BAR 14, ALLEE DES VIREVOLTES 45127 MEUDON-LA-BEDOULE LUNDI 20 MARS 2017 TICKET N°158-51584 SERVI PAR : JUANITO SERVICE AU BAR PERRIER CAFE EXPRESSO DESTOP TURBO 3.50 2.00 8.00 (DONT TVA 10%: 1.35 €) TOTAL TTC: 13.50 € LA PROCHAINE FOIS, LAISSEZ UN POURBOIRE ESPECE DE GROS RAT ^_^ NNN'

# print(devise(text))


