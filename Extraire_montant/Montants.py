import re
def text_modification(text):
    text_c = text
    txt = text_c.replace("$"," ")
    txt = text_c.replace("eur"," ")
    txt = text_c.replace("usd"," ")
    txt = text_c.replace("€"," ")
    txt = text_c.replace("chf"," ")
    txt = text_c.replace(",",".")
    return txt

def extract_TTC(text):
    #text.replace()
    txt = text_modification(text)
    #print(txt,'\n')
    
    text_1 = txt.replace("€"," ")
    #print(text_1,'\n')



    p1 = r'\s\d{2}\.[0-9]{2}\s'
    p2 = r'\s\d{1}\.[0-9]{2}\sCHF'
    x = re.findall(r'\s\d{2}\.[0-9]{2}\s|\d{2}\.[0-9]{2}\s|\s\d{1}\.[0-9]{2}\s|\s\d{3}\.[0-9]{2}\s|\s[1-9]\.\d{3}\.[0-9]{2}\s', text_1)
    #print(x)
    M = sorted(list(dict.fromkeys(x)),key = lambda x:float(x),reverse=True)
    if len(M):
        
        TTC = M[0]
 
        return TTC
    else:
        return 'Pas de montans detecté'