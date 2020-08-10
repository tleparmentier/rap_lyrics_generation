import pandas as pd
import random
import sys
from os import path
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Erreur : Arguments invalides : ')
        print('\t python creation_du_df_de_structure_de_phrase.py structure_phrase_refactor_nekfeu.pickle')
        sys.exit(1)

    file_name_pkl = sys.argv[1]
    path_to_tab_mot_phrase = "./pickles_csv/{}".format(file_name_pkl)
    assert path.exists(path_to_tab_mot_phrase)

    tab_mot_phrase = pd.read_pickle(path_to_tab_mot_phrase)
    print(tab_mot_phrase)
    tab_structure_phrase = []
    for phrase in tab_mot_phrase:
        if len(phrase) < 3:
            pass
        else:
            is_clean = True
            tab_pronom = []
            for mot in phrase:
                if mot[1] == 'X':
                    is_clean = False
                    break
                tab_pronom.append(mot[1])
            if is_clean:
                tab_structure_phrase.append(tab_pronom)

    structure_phrase_df = pd.DataFrame(tab_structure_phrase)

    dict_type_word_to_list = {}

    for phrase in tab_mot_phrase:
        for mot in phrase:
            key = mot[1]
            value = mot[0]

            if key not in dict_type_word_to_list.keys():
                dict_type_word_to_list[key] = []
                dict_type_word_to_list[key].append(value.lower())
            else:
                dict_type_word_to_list[key].append(value.lower())

    dict_type_word_to_set = {}

    for phrase in tab_mot_phrase:
        for mot in phrase:
            key = mot[1]
            value = mot[0]

            if key not in dict_type_word_to_set.keys():
                dict_type_word_to_set[key] = set()
                dict_type_word_to_set[key].add(value.lower())
            else:
                dict_type_word_to_set[key].add(value.lower())

    print(dict_type_word_to_set)
    print(dict_type_word_to_list)

    for ll in range(20):
        random.randint(0, structure_phrase_df.shape[0])

        structure_df = structure_phrase_df.copy()
        tab_type_mot = []
        for i in range(structure_phrase_df.shape[1]):
            rand_int = random.randint(0, structure_df.shape[0]-1)
            type_mot = structure_df.iloc[rand_int, i]

            structure_df = structure_df[structure_df[i] == type_mot]
            if type_mot is None:
                break
            tab_type_mot.append(type_mot)
        phrase_construite = []
        for mot_type in tab_type_mot:
            phrase_construite.append(random.choice(dict_type_word_to_list[mot_type]))
        print(" ".join(phrase_construite))
