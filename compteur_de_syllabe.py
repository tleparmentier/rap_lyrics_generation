from utils import return_text_cleaned, transform_mot_to_phonetique, find_voyelle_and_consonne_in_phonetique
import pandas as pd
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Erreur : Arguments invalides : ')
        print('\t python compteur_de_syllabe.py rappeur.txt')
        sys.exit(1)
    file_name_txt = sys.argv[1]
    file_name = file_name_txt.split('.txt')[0]

    general_df = pd.read_pickle("./pickles_csv/phonetique_type_of_word_df_{}.pkl".format(file_name))

    general_df['nb_syllabes'] = general_df['mot_phonetique'].map(lambda x: len(find_voyelle_and_consonne_in_phonetique(x)[0]))

    general_df.to_pickle("./pickles_csv/phonetique_type_of_word_nb_syllabe_df_{}.pkl".format(file_name))



