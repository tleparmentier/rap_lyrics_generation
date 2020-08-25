import pandas as pd

path_to_tab_mot_phrase = "./pickles_csv/structure_phrase_refactor_booba_nekfeu.pickle"
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
structure_phrase_df.to_pickle("./pickles_csv/dataframe_structure_de_phrases.pkl")