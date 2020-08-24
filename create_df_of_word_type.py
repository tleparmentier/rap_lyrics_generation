import pandas as pd

structure_phrase = pd.read_pickle("pickles_csv/structure_phrase_refactor_booba_nekfeu.pickle")

general_df = pd.read_pickle("pickles_csv/phonetique_df.pkl")

dict_mot_to_type = {}
set_mot_type = set()

for phrase in structure_phrase:
    for mot, mot_type in phrase:
        set_mot_type.add(mot_type)
        if mot not in dict_mot_to_type.keys():
            dict_mot_to_type[mot] = {mot_type: 1}

        elif mot_type not in dict_mot_to_type[mot].keys():
            dict_mot_to_type[mot][mot_type] = 1

        else:
            dict_mot_to_type[mot][mot_type] += 1


for type_mot in set_mot_type:
    general_df[type_mot] = general_df['mot'].map(
        lambda x: 0 if (x not in dict_mot_to_type.keys()) or (type_mot not in dict_mot_to_type[x].keys()) else
        dict_mot_to_type[x][type_mot])


general_df.to_pickle("./pickles_csv/phonetique_type_of_word_df.pkl")

