
# ##############################################################################

# import re
# import imutils
# import json
# import matplotlib.pyplot as plt
# import numpy as np
# import os
# import pandas as pd
# import requests
# import time
# from Ocr import *
# from Ocr import image_to_text
# ##############################################################################
# from base64 import b64encode
# from IPython.display import Image
# from pylab import rcParams
# rcParams['figure.figsize'] = 10, 20
# import string
# import datetime
# ##############################################################################

# time_start = time.time()


# import pandas as pd
# zipcodes= pd.read_csv('allCountriesCSV.csv')
# zipcodes=zipcodes[['COUNTRY', 'POSTAL_CODE', 'CITY']]
# zipcodes['COUNTRY']= zipcodes['COUNTRY'].astype(str)
# zipcodes['POSTAL_CODE']= zipcodes['POSTAL_CODE'].astype(str)
# zipcodes['CITY']= zipcodes['CITY'].astype(str)


# import pycountry
# list_alpha_2 = [i.alpha_2 for i in list(pycountry.countries)]
# list_alpha_3 = [i.alpha_3 for i in list(pycountry.countries)]    

# def country_flag(code):
#     if (len(code)==2 and code in list_alpha_2):
#         return pycountry.countries.get(alpha_2=code).name
#     elif (len(code)==3 and code in list_alpha_3):
#         return pycountry.countries.get(alpha_3=code).name
#     else:
#         return ['Nan']
    
    
# import re
# imgpath = '7ff67d7db19ecd365f583bd81288e70d.jpg'
# results = image_to_text.requestOCR('https://vision.googleapis.com/v1/images:annotate','AIzaSyDOQ4gFyIPJqwnH5fJselRcMZRA6-hG3dw' , img)
# l=[]
# for res in results:
    
#     total_len= len(res)
#     part_len= round(total_len*30 /100)
#     ll=[]
#     all_text= ' '.join(text for text in res[: int(part_len)])+ ' '.join(text for text in res[int(-part_len):])
#     for i in range(len(zipcodes)):
#         if zipcodes['CITY'][i].lower().replace('-', ' ') in all_text.lower().replace('-', ' ') and zipcodes['POSTAL_CODE'][i] in all_text.split():
#             ll.append(country_flag(zipcodes['COUNTRY'][i]))
#             break
#         else:
#             continue
#     if ll== []:
#         ll.append('')
#     l.append(list(set(ll)))
    
# fr_data= pd.read_csv('Countries_information.csv')

# fr_count=[]
# for res in results:
#     ll=[]
#     total_len= len(res)
#     part_len= round(total_len*30 /100)
#     all_text= (' '.join(text for text in res[: part_len])+ ' '.join(text for text in res[-part_len:]))
#     all_text= all_text.lower()
    
#     for i in range(len(fr_data)):
        
#         if fr_data['country'][i].lower() in all_text.lower():
#             before= all_text[: all_text.index(fr_data['country'][i].lower())]
#             after= all_text[all_text.index(fr_data['country'][i].lower()) + len(fr_data['country'][i].lower()):]
#             if before== '':
#                 before= ' '
#             if after== '':
#                 after= ' '
#             if before[-1].isalnum()==False and after[0].isalnum()==False:
#                 ll.append(fr_data['country'][i])
#             else:
#                 continue
#         else:
#             continue
#     if ll== []:
#         ll.append('')
#     fr_count.append(list(set(ll)))
# for i in range(len(dev_raw)):
#     all_text= ' '.join(results[i])
#     all_text= all_text.replace(',','.') 
#     parts=all_text.split()
#     perc=[]
#     for j in range(len(parts)):
#         word = parts[j]
#         if '%' in word:
#             #print(word)
#             perc.append(word.split("%")[0])
#     m= list(filter(None, list(set(perc))))
#     type_tva[i].extend(m)
#     print(type_tva[i])
#     #print('___________________________________')
# final_final= []
# for i in range(len(type_tva)):
#     final_final.append(str(type_tva[i]))
# print(final_final)