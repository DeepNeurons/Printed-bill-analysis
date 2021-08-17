import re

def type_de_paiement(result_list):

    modalite = []
    #for res in result_list:
    all_text= ' '.join(result_list)
    if 'visa' in all_text.lower() or 'carte' in all_text.lower() or 'bancaire' in all_text.lower() or 'sans contact' in all_text.lower() :
        modalite.append('Carte bancaire')
    if 'chèque' in all_text.lower() or 'cheque' in all_text.lower() or 'check' in all_text.lower():
        modalite.append('Chèque')        
    else:
        modalite.append('Espèce')
    return modalite


