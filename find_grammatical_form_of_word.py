from utils import return_text_cleaned
from nltk.tag import StanfordPOSTagger
import pickle
from os import path
import sys


def tab_of_phonetique_for_each_sentence_return_phonetique(sentences):
    tab_structure_gramaticale_par_phrase = []
    index = 0
    for phrase in sentences:
        tab_structure_gramaticale_par_phrase.append(pos_tagger.tag(phrase.split()))
        index += 1

    return tab_structure_gramaticale_par_phrase


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Erreur : Arguments invalides : ')
        print('\t python find_grammatical_form_of_word.py nekfeu.txt')
        sys.exit(1)
    file_name_txt = sys.argv[1]
    file_name = file_name_txt.split(".txt")[0]

    path_to_lyrics = "./french_lyrics/{}".format(file_name_txt)
    assert path.exists(path_to_lyrics)

    with open(path_to_lyrics, encoding='UTF-8') as f:
        text = f.read()

    jar = 'stanford_postagger/stanford-postagger-4.0.0.jar'
    model = 'stanford_postagger/french-ud.tagger'
    pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8')

    text_cleaned = return_text_cleaned(text)

    phrases = text_cleaned.split('\n')

    path_to_pickle_phonetique = './pickles_csv/structure_phrase_refactor_{}.pickle'.format(file_name)
    if path.exists(path_to_pickle_phonetique):
        print('Interruption: Le fichier de phonetique existe déja:{} '.format(path_to_pickle_phonetique))
    else:
        print("Création: Le fichier de phonetique n'existe pas:{} ".format(path_to_pickle_phonetique))
        tab_mot_phrase = tab_of_phonetique_for_each_sentence_return_phonetique(phrases)
        with open(path_to_pickle_phonetique, 'wb') as handle:
            pickle.dump(tab_mot_phrase, handle, protocol=pickle.HIGHEST_PROTOCOL)
