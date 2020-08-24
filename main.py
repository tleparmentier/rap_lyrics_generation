from utils import return_text_cleaned, transform_mot_to_phonetique, find_voyelle_and_consonne_in_phonetique
import os
path_texts = './french_lyrics'
text_all_rappeur = ""
for file_name_text_rap in os.listdir(path_texts):

    with open(path_texts+'/{}'.format(file_name_text_rap), encoding='UTF-8') as f:
        text = f.read()
    text_all_rappeur += text



text_all_rappeur = text_all_rappeur.lower()
text_all_rappeur = return_text_cleaned(text_all_rappeur)
list_mot = text_all_rappeur.split()

# tab avec toutes les phonétiques
# tab avec toutes les les 7 dernières syllabes
#                         7 dernière consonne
# Nombre d'apparition
# Type de mot


set_mot_unique = set()
for mot in list_mot:
    set_mot_unique.add(mot)

print(len(set_mot_unique))

dict_mot_phonetique = {}
for mot in set_mot_unique:
    dict_mot_phonetique[mot] = transform_mot_to_phonetique(mot)


dict_mot_frequence_dapparition = {}
for mot in list_mot:
    if mot not in dict_mot_frequence_dapparition.keys():
        dict_mot_frequence_dapparition[mot] = 1
    else:
        dict_mot_frequence_dapparition[mot] += 1


#print(dict_mot_frequence_dapparition)



max_syll = 0
for key, values in dict_mot_phonetique.items():
    tab_voyelles, tab_consonnes = find_voyelle_and_consonne_in_phonetique(values)
    nombre_syllabes = len(tab_consonnes)
    #print(nombre_syllabes)
    if max_syll < nombre_syllabes:
        max_syll = nombre_syllabes
        print(key , values)

#print(key, ":", values, ":",)