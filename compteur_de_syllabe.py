from utils import return_text_cleaned, transform_mot_to_phonetique, find_voyelle_and_consonne_in_phonetique
import pandas as pd


general_df = pd.read_pickle("./pickles_csv/phonetique_type_of_word_df.pkl")

general_df['nb_syllabes'] = general_df['mot_phonetique'].map(lambda x: len(find_voyelle_and_consonne_in_phonetique(x)[0]))

general_df.to_pickle("./pickles_csv/phonetique_type_of_word_nb_syllabe_df.pkl")



