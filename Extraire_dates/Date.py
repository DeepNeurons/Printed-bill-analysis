import re
def date_type(text):
    date = []
    date2 = re.findall(r'\d{2}[-/.]\d{2}[-/.]\d{4}|\d{2}[-/.]\d{2}[-/.]\d{2} ',text.lower())
    date3 = re.findall(r'\D?(\d{2}\D?)(jan|janvier|fev|fevrier|mar|mars|avr|avril|mai|mai|jun|juin|jul|juillet|aou|aout|sep|septembre|oct|octobre|nov|novembre|dec|decembre)\D?( \d{4})',text)
    if len(date2) == 0 and len(date3) != 0 :
        date.append(date3)
    elif len(date3) == 0 and len(date2) != 0:
        date.append(date2)
    else:
        date.append("date not detected")
    
    return date[0][0]


# # text = 'LE NID BAR 14, ALLEE DES VIREVOLTES 45127 MEUDON-LA-BEDOULE LUNDI 20 MARS 2017 TICKET N°158-51584 SERVI PAR : JUANITO SERVICE AU BAR PERRIER CAFE EXPRESSO DESTOP TURBO 3.50 2.00 8.00 (DONT TVA 10%: 1.35 €) TOTAL TTC: 13.50 € LA PROCHAINE FOIS, LAISSEZ UN POURBOIRE ESPECE DE GROS RAT ^_^ NNN '
# #print(date_type(text))
# text =' JAN|Janvier|FEV|Fevrier|MAR|Mars|AVR|Avril|MAI|Mai|JUN|Juin|JUL|Juillet|AOU|Aout|SEP|Septembre|OCT|Octobre|NOV|Novembre|DEC|Decembre '
# print(text.lower())