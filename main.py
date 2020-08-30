from utils import return_text_cleaned, transform_mot_to_phonetique, find_voyelle_and_consonne_in_phonetique
import os
import pandas as pd
import random

NOMBRE_DE_LETTRE = 15


def return_structure_de_phrase(structure_de_phrase_df, nombre_de_mot=None):
    if nombre_de_mot is not None:
        structure_de_phrase_df_function = structure_de_phrase_df[
            ~structure_de_phrase_df[nombre_de_mot - 1].isna()].copy()

    else:
        structure_de_phrase_df_function = structure_de_phrase_df.copy()

    random_int = random.randint(0, structure_de_phrase_df_function.shape[0] - 1)
    tab_type_mot = []
    for type_mot in structure_de_phrase_df_function.iloc[random_int].values:
        if type_mot is None:
            break
        else:
            tab_type_mot.append(type_mot)

    return tab_type_mot


def retourne_list_frequence_des_mots(type_mot_df, type_mot):
    tab_all_mot = ""
    for list_mot in type_mot_df[type_mot] * (type_mot_df["mot"] + " "):
        tab_all_mot += " " + list_mot.strip()
    tab_all_mot = tab_all_mot.strip()
    tab_all_mot = tab_all_mot.split()
    return tab_all_mot


def retourne_random_choice_from_list(list_frequence_mot):
    return random.choice(list_frequence_mot)


def retourner_phrases_en_fonction_de_la_structure(list_type_mot, general_df):
    list_mot = []
    for type_mot in list_type_mot:
        type_mot_df = general_df[general_df[type_mot] != 0].copy()

        list_frequence_type_mot = retourne_list_frequence_des_mots(type_mot_df, type_mot)
        nouveau_mot = retourne_random_choice_from_list(list_frequence_type_mot)
        list_mot.append(nouveau_mot)

    return list_mot


def mettre_deux_tables_a_la_même_longueur(list_mot_phrase, list_structure_de_phrase):
    if len(list_mot_phrase) == len(list_structure_de_phrase):
        return list_mot_phrase, list_structure_de_phrase

    if len(list_structure_de_phrase) < len(list_mot_phrase):
        list_structure_de_phrase_to_return = list_structure_de_phrase
        for none_a_ajoute in range(len(list_mot_phrase) - len(list_structure_de_phrase)):
            list_structure_de_phrase_to_return = [None] + list_structure_de_phrase_to_return
        return list_mot_phrase, list_structure_de_phrase_to_return

    if len(list_structure_de_phrase) > len(list_mot_phrase):
        list_mot_phrase_to_return = list_mot_phrase
        for none_a_ajoute in range(len(list_structure_de_phrase) - len(list_mot_phrase)):
            list_mot_phrase_to_return = [None] + list_mot_phrase_to_return
        return list_mot_phrase_to_return, list_structure_de_phrase


def retourne_mot_qui_rime(df, mot_qui_rime, type_mot, nombre_de_rime=None):
    nb_syllabes = df[df["mot"] == mot_qui_rime]['nb_syllabes'].values[0]
    df_qui_rime = df[df[type_mot] > 1]
    df_qui_rime = df_qui_rime[df_qui_rime["mot"] != mot_qui_rime]

    if nb_syllabes >= 1:
        for numero_de_lettre in reversed(range(1, NOMBRE_DE_LETTRE)):
            lettre_qui_rime = df[df["mot"] == mot_qui_rime]['lettre_{}'.format(numero_de_lettre)].values[0]
            df_qui_rime = df_qui_rime[df_qui_rime['lettre_{}'.format(numero_de_lettre)] == lettre_qui_rime]

            if df_qui_rime.empty:
                list_frequence_type_mot = retourne_list_frequence_des_mots(df, type_mot)
                nouveau_mot = retourne_random_choice_from_list(list_frequence_type_mot)
                return nouveau_mot
            if df_qui_rime.shape[0] < 100:
                list_frequence_type_mot = retourne_list_frequence_des_mots(df_qui_rime, type_mot)
                return retourne_random_choice_from_list(list_frequence_type_mot)

    else:
        list_frequence_type_mot = retourne_list_frequence_des_mots(df, type_mot)
        nouveau_mot = retourne_random_choice_from_list(list_frequence_type_mot)

        return nouveau_mot


def rime_phrase(list_mot_phrase, list_structure_de_phrase, general_df):
    list_mot_phrase_refactor, list_structure_de_phrase_refactor = mettre_deux_tables_a_la_même_longueur(
        list_mot_phrase, list_structure_de_phrase)

    list_mot = []
    for mot_qui_rime, type_mot in zip(list_mot_phrase_refactor, list_structure_de_phrase_refactor):

        if type_mot is None:
            pass
        elif mot_qui_rime is None:
            type_mot_df = general_df[general_df[type_mot] != 0].copy()

            list_frequence_type_mot = retourne_list_frequence_des_mots(type_mot_df, type_mot)

            nouveau_mot = retourne_random_choice_from_list(list_frequence_type_mot)
            list_mot.append(nouveau_mot)

        else:

            nouveau_mot = retourne_mot_qui_rime(general_df, mot_qui_rime, type_mot, nombre_de_rime=None)

            list_mot.append(nouveau_mot)

    return list_mot


if __name__ == "__main__":

    general_df = pd.read_pickle("./pickles_csv/phonetique_type_of_word_nb_syllabe_df_rappeur.pkl")
    structure_de_phrase = pd.read_pickle("./pickles_csv/dataframe_structure_de_phrases_rappeur.pkl")
    NOMBRE_DE_LIGNE_A_GENERER = 20

    for numero_ligne in range(NOMBRE_DE_LIGNE_A_GENERER):

        if numero_ligne % 2 == 0:
            list_structure_de_phrase = return_structure_de_phrase(structure_de_phrase)
            list_mot_premier_phrase = retourner_phrases_en_fonction_de_la_structure(list_structure_de_phrase,
                                                                                    general_df)
            print(" ".join(list_mot_premier_phrase))
        else:
            list_structure_de_phrase_deuxieme = return_structure_de_phrase(structure_de_phrase)

            list_mot_deuxieme_phrase = rime_phrase(list_mot_premier_phrase, list_structure_de_phrase_deuxieme,
                                                   general_df)
            print(" ".join(list_mot_deuxieme_phrase))


# retourne_mot_qui_rime(df=general_df, mot_qui_rime="abaisse", type_mot="VERB")


def test_2_list_de_la_même_taille():
    given_list_mot_phrase = ["bonjour", "monsieur", "sable"]
    given_list_structure_de_phrase = ["PRON", "VERB", "ADJ"]

    expected_list_mot_phrase = ["bonjour", "monsieur", "sable"]
    expected_list_structure_de_phrase = ["PRON", "VERB", "ADJ"]

    result_list_mot_phrase, result_list_structure_de_phrase = mettre_deux_tables_a_la_même_longueur(
        given_list_mot_phrase, given_list_structure_de_phrase)

    assert expected_list_mot_phrase == result_list_mot_phrase
    assert expected_list_structure_de_phrase == result_list_structure_de_phrase


def test_list_structure_de_phrase_plus_courte():
    given_list_mot_phrase = ["bonjour", "monsieur", "sable"]
    given_list_structure_de_phrase = ["VERB", "ADJ"]

    expected_list_mot_phrase = ["bonjour", "monsieur", "sable"]
    expected_list_structure_de_phrase = [None, "VERB", "ADJ"]

    result_list_mot_phrase, result_list_structure_de_phrase = mettre_deux_tables_a_la_même_longueur(
        given_list_mot_phrase, given_list_structure_de_phrase)

    assert expected_list_mot_phrase == result_list_mot_phrase
    assert expected_list_structure_de_phrase == result_list_structure_de_phrase


def test_list_structure_de_phrase_2_plus_courte():
    given_list_mot_phrase = ["bonjour", "monsieur", "sable"]
    given_list_structure_de_phrase = ["ADJ"]

    expected_list_mot_phrase = ["bonjour", "monsieur", "sable"]
    expected_list_structure_de_phrase = [None, None, "ADJ"]

    result_list_mot_phrase, result_list_structure_de_phrase = mettre_deux_tables_a_la_même_longueur(
        given_list_mot_phrase, given_list_structure_de_phrase)

    assert expected_list_mot_phrase == result_list_mot_phrase
    assert expected_list_structure_de_phrase == result_list_structure_de_phrase


def test_list_mot_phrase_plus_courte():
    given_list_mot_phrase = ["monsieur", "sable"]
    given_list_structure_de_phrase = ["PRON", "VERB", "ADJ"]

    expected_list_mot_phrase = [None, "monsieur", "sable"]
    expected_list_structure_de_phrase = ["PRON", "VERB", "ADJ"]

    result_list_mot_phrase, result_list_structure_de_phrase = mettre_deux_tables_a_la_même_longueur(
        given_list_mot_phrase, given_list_structure_de_phrase)

    assert expected_list_mot_phrase == result_list_mot_phrase
    assert expected_list_structure_de_phrase == result_list_structure_de_phrase


def test_list_mot_phrase_plus_courte_2():
    given_list_mot_phrase = ["sable"]
    given_list_structure_de_phrase = ["PRON", "VERB", "ADJ"]

    expected_list_mot_phrase = [None, None, "sable"]
    expected_list_structure_de_phrase = ["PRON", "VERB", "ADJ"]

    result_list_mot_phrase, result_list_structure_de_phrase = mettre_deux_tables_a_la_même_longueur(
        given_list_mot_phrase, given_list_structure_de_phrase)

    assert expected_list_mot_phrase == result_list_mot_phrase
    assert expected_list_structure_de_phrase == result_list_structure_de_phrase


test_2_list_de_la_même_taille()
test_list_structure_de_phrase_plus_courte()
test_list_structure_de_phrase_2_plus_courte()
test_list_mot_phrase_plus_courte()
test_list_mot_phrase_plus_courte_2()
