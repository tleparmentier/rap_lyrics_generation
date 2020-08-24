from utils import return_text_cleaned, transform_mot_to_phonetique, find_voyelle_and_consonne_in_phonetique
import os
import pandas as pd


path_texts = './french_lyrics'
text_all_rappeur = ""
for file_name_text_rap in os.listdir(path_texts):
    with open(path_texts+'/{}'.format(file_name_text_rap), encoding='UTF-8') as f:
        text = f.read()
    text_all_rappeur += text


text_all_rappeur = text_all_rappeur.lower()
text_all_rappeur = return_text_cleaned(text_all_rappeur)
list_mot = text_all_rappeur.split()

set_mot_unique = set()
for mot in list_mot:
    set_mot_unique.add(mot)

NOMBRE_VOYELLE = 7
NOMBRE_CONSONNE = 7
NOMBRE_LETTRE = 14

tab_columns = ['mot', 'mot_phonetique']
tab_columns_voyelles = []
tab_columns_consonnes = []
for i in range(1, NOMBRE_VOYELLE+1):
    tab_columns_voyelles.append("voyelle_{}".format(i))
    tab_columns_consonnes.append("consonne_{}".format(i))

tab_columns_lettre= []
for i in range(1, NOMBRE_LETTRE + 1):
    tab_columns_lettre.append("lettre_{}".format(i))


text_all_rappeur_phonetique = transform_mot_to_phonetique(text_all_rappeur)
list_mot_phonetique = text_all_rappeur_phonetique.split()
set_phonetique = set()
for mot in list_mot_phonetique:
    for son in mot:
        set_phonetique.add(son)

list_unique_phonetique = sorted(list(set_phonetique))

tab_columns_is_phonetique = []
for phonetique in list_unique_phonetique:
    tab_columns_is_phonetique.append("{}".format(phonetique))

tab_columns += tab_columns_voyelles + tab_columns_consonnes + tab_columns_is_phonetique + tab_columns_lettre


phonetique_df = pd.DataFrame(columns=tab_columns)


dict_mot_phonetique = {}
for mot in set_mot_unique:
    dict_mot_phonetique[mot] = transform_mot_to_phonetique(mot)


list_mot_unique = sorted(list(set_mot_unique))
mot_df = pd.DataFrame(columns=["mot"])
mot_df['mot'] = list_mot_unique
mot_df['mot_phonetique'] = mot_df['mot'].map(lambda x: transform_mot_to_phonetique(x))

list_mot_phonetique = mot_df['mot_phonetique'].values

tab_all_voyelle = []
tab_all_consonne = []
tab_all_lettre = []
tab_all_nb_phonetique = []
for mot in list_mot_phonetique:
    list_voyelle_mot = [None] * NOMBRE_VOYELLE
    tab_voyelle, tab_consonne = find_voyelle_and_consonne_in_phonetique(mot)

    # Voyelle
    tab_voyelle.reverse()
    nombre_de_voyelle = NOMBRE_VOYELLE - 1
    for lettre in tab_voyelle:
        list_voyelle_mot[nombre_de_voyelle] = lettre
        nombre_de_voyelle -= 1

    tab_all_voyelle.append(list_voyelle_mot)

    # Consonne
    list_consonne_mot = [None] * NOMBRE_CONSONNE
    tab_consonne.reverse()
    nombre_de_consonne = NOMBRE_CONSONNE - 1
    for lettre in tab_consonne:
        list_consonne_mot[nombre_de_consonne] = lettre
        nombre_de_consonne -= 1
    tab_all_consonne.append(list_consonne_mot)

    # Lettre
    mot_phonetique_reversed = mot[::-1]
    list_lettre_mot = [None] * NOMBRE_LETTRE
    nombre_de_lettre = NOMBRE_LETTRE - 1
    for lettre in mot_phonetique_reversed:
        list_lettre_mot[nombre_de_lettre] = lettre
        nombre_de_lettre -= 1
    tab_all_lettre.append(list_lettre_mot)

    # Nb phonetique
    nb_phonetique = len(list_unique_phonetique)
    list_nb_phonetique_mot = [0] * nb_phonetique
    for index, son in enumerate(list_unique_phonetique):
        list_nb_phonetique_mot[index] = mot.count(son)

    tab_all_nb_phonetique.append(list_nb_phonetique_mot)


consonne_df = pd.DataFrame(tab_all_consonne,  columns=tab_columns_consonnes)
voyelle_df = pd.DataFrame(tab_all_voyelle,  columns=tab_columns_voyelles)
lettre_df = pd.DataFrame(tab_all_lettre,  columns=tab_columns_lettre)
nb_phonetique_df = pd.DataFrame(tab_all_nb_phonetique, columns=tab_columns_is_phonetique)


phonetique_df = pd.concat([mot_df, voyelle_df, consonne_df, lettre_df, nb_phonetique_df], axis=1)

phonetique_df.to_pickle("./pickles_csv/phonetique_df.pkl")

print(phonetique_df)
print(phonetique_df.shape)
print(len(set_mot_unique))