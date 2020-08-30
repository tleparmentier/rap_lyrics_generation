import pandas as pd
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Erreur : Arguments invalides : ')
        print('\t python create_structure_de_phrase_df.py rappeur.txt')
        sys.exit(1)
    file_name_txt = sys.argv[1]
    file_name = file_name_txt.split('.txt')[0]

    path_to_tab_mot_phrase = "./pickles_csv/structure_phrase_refactor_{}.pickle".format(file_name)
    tab_mot_phrase = pd.read_pickle(path_to_tab_mot_phrase)

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
    structure_phrase_df.to_pickle("./pickles_csv/dataframe_structure_de_phrases_{}.pkl".format(file_name))
