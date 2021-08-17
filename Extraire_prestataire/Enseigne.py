def enseigne(text_list):
    n_list = text_list[:3]
    Prestataire = []
    Adresse = []
    ens = []
    Prestataire.append(n_list[0])
    Adresse.extend(n_list[1:3])

    P = ' '.join(Prestataire)
    A = ' '.join(Adresse)
    
    return P,A
