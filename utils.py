def return_text_cleaned(text: str):
    text = text.replace("\t", "")
    text = text.replace("\n\n", "\n")
    text = text.replace("\n\n", "\n")
    text = text.replace("\n\n", "\n")
    text = text.replace("\n\n", "\n")
    text = text.replace("NEW_SONG_123", " ")
    text = text.replace("\'", " ")
    text = text.replace("眼", "")
    text = text.replace("着", "")
    text = text.replace("空", "")
    text = text.replace("紧", "")
    text = text.replace("躲", "")

    text = text.replace("都", "")
    text = text.replace("门", "")
    text = text.replace("间", "")
    text = text.replace("饰", "")
    text = text.replace("ﬀ", "")
    text = text.replace("ﬁ", "")

    text = text.replace('🖖🏾', "")
    text = text.replace("(", " ")
    text = text.replace(")", " ")
    text = text.replace("?", " ")
    text = text.replace("[", " ")
    text = text.replace("]", " ")
    text = text.replace(")", " ")
    text = text.replace('"', " ")
    text = text.replace("_", " ")
    text = text.replace(".", " ")
    text = text.replace("!", " ")
    text = text.replace("=", " égal ")
    text = text.replace("n°", "numéro ")
    text = text.replace("%", " pourcent")
    text = text.replace("€", " euros")
    text = text.replace("ë", "è")
    text = text.replace("ü", "u")
    text = text.replace('\\', " ")
    text = text.replace("  ", " ")
    text = text.replace("  ", " ")
    text = text.replace("§", " ")
    text = text.replace(",", " ")
    text = text.replace("-", " ")
    text = text.replace("  ", " ")
    text = text.replace(".", " ")
    text = text.replace("!", " ")
    text = text.replace('’', " ")
    text = text.replace(";", " ")
    text = text.replace("1", " un ")
    text = text.replace("0", " zéro ")
    text = text.replace("3", " trois ")
    text = text.replace("2", " deux ")
    text = text.replace(":", " ")
    text = text.replace("7", " sept ")
    text = text.replace("&", "et")
    text = text.replace("6", " six ")
    text = text.replace("×", " ")
    text = text.replace("4", " quatre ")
    text = text.replace("9", " neuf ")
    text = text.replace("#", " ")
    text = text.replace("*", " ")
    text = text.replace("5", " cinq ")
    text = text.replace("«", " ")
    text = text.replace("»", " ")
    text = text.replace("…", " ")
    text = text.replace("í", "i")
    text = text.replace("ó", "o")
    text = text.replace("‘", " ")
    text = text.replace("/", " ")
    text = text.replace("–", " ")
    text = text.replace("“", " ")
    text = text.replace("+", " ")
    text = text.replace("ñ", " ")
    text = text.replace("”", " ")
    text = text.replace("$", " ")
    text = text.replace("\xa0", " ")
    text = text.replace("8", " huit ")
    text = text.replace("¡", " ")
    text = text.replace("æ", "ae")
    for lettre in ['ā', 'ą', 'ć', 'č', 'ē', 'ę', 'ğ', 'ī', 'ķ', 'ļ', 'ł', 'ń', 'ņ', 'ō', 'œ', 'ś', 'ş', 'š', 'ū', 'ź',
                   'ż',
                   'ž', 'ș', 'ɑ', 'ɛ', 'ʒ', 'ʻ', 'ʼ', '̀', '́', '̂', '̧', 'α', 'β', 'γ', 'δ', 'ε', 'θ', 'ι', 'κ', 'λ',
                   'ν', 'ο',
                   'π', 'ρ', 'ς', 'σ', 'τ', 'υ', 'φ', 'χ', 'ω', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к',
                   'л',
                   'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я', 'ё',
                   'א', 'ב',
                   'ג', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'ך', 'כ', 'ל', 'ם', 'מ', 'ן', 'נ', 'ס', 'ע', 'ף', 'פ', 'צ', 'ק',
                   'ר', 'ש', 'ת',
                   'ئ', 'ا', 'ر', 'ز', 'ع', 'ل', 'ی', 'ḥ', 'ṭ', '\u2005', '\u2009', '\u200a', '\u200b', '\u200c',
                   '\u200e', '–', '—', '‘',
                   '’', '‚', '“', '”', '„', '…', '\u2028', '\u202a', '\u202c', '\u205f', '₂', '€', '♪', '♫', 'か', 'だ',
                   'で', 'と', 'ひ',
                   'る', 'テ', 'ホ', 'ル', '上', '不', '京', '伤', '关', '内', '再', '在', '已', '当', '我', '房', '掩', '東', '泪', '洞',
                   '流', '然',
                   '用', '痕', '眼', '着', '空', 'ﬀ', 'ﬁ', '\ufeff', '🏾', '🖖']:
        text = text.replace(lettre, " ")

    for lettre in ['{', '}', '\x80', '\x81', '\x85', '\x8c', '\x91', '\x92', '\x93',
                   '\x94', '\x9c', '¥', '\xad', '°', '²', '³', '´', '¾', '¿', 'ß', 'ì', '<', '>', '@', '`', 'の']:
        text = text.replace(lettre, " ")

    for lettre in ['à', 'á', 'â', 'ã', 'ä']:
        text = text.replace(lettre, "a")

    for lettre in ['ì', 'î', 'ï']:
        text = text.replace(lettre, "i")

    for lettre in ['ò', 'ô', 'õ', 'ö']:
        text = text.replace(lettre, "o")

    for lettre in ['ù', 'ú', 'û']:
        text = text.replace(lettre, "u")

    text = text.replace("  ", " ")
    text = text.replace("  ", " ")
    text = text.replace("  ", " ")
    text = text.replace("  ", " ")
    text = text.replace("  ", " ")
    text = text.replace("  ", " ")
    text = text.replace("  ", " ")
    text = text.replace("  ", " ")
    text = text.replace("  ", " ")
    text = text.replace("  ", " ")

    return text.strip()


def return_syllabes(mot):
    tab_syllabes_to_return = []
    syllabe = ""
    list_voyelles = ["a", "ä", "à", 'á', "e", "ê", "è", "i", "î", "o", "ô", "u", "ù", "é", "ï"]
    list_voyelles_non_phonetique = ["a", "ä", "à", 'á', "e", "ê", "è", "i", "î", "o", "ô", "u", "ù"]
    list_voyelles_phonetique = ["é", "ï"]
    len_mot = len(mot)
    num_syllabe = 0
    last_lettre_type = None
    for index, lettre in enumerate(mot):

        # On s'occupe de la dernière lettre
        if index == len_mot - 1:
            if lettre in list_voyelles_phonetique:
                if last_lettre_type == "consonne":
                    syllabe += lettre
                    tab_syllabes_to_return.append(syllabe)
                    syllabe = ""
                else:
                    tab_syllabes_to_return.append(syllabe)
                    syllabe = lettre
            else:
                syllabe = syllabe + lettre
        else:
            if lettre in list_voyelles_non_phonetique:
                syllabe = syllabe + lettre
                last_lettre_type = "voyelle"

            elif lettre not in list_voyelles_phonetique:
                if syllabe != "":
                    if len(syllabe) == 1 and num_syllabe > 0 and syllabe not in list_voyelles:

                        tab_syllabes_to_return[num_syllabe - 1] += syllabe

                    elif len(syllabe) == 1 and num_syllabe == 0 and syllabe not in list_voyelles_non_phonetique:

                        lettre = syllabe + lettre
                    else:

                        tab_syllabes_to_return.append(syllabe)
                        num_syllabe += 1
                syllabe = lettre
                last_lettre_type = "consonne"

            else:

                if last_lettre_type == "consonne":
                    syllabe += lettre

                    tab_syllabes_to_return.append(syllabe)
                    num_syllabe += 1
                    syllabe = ""
                else:

                    tab_syllabes_to_return.append(syllabe)
                    num_syllabe += 1
                    syllabe = lettre

                last_lettre_type = "voyelle_phonetique"

        if len_mot == index + 1:
            is_voyelle_in_last_syllabe = False
            for lettre_derniere_syllabe in syllabe:
                if lettre_derniere_syllabe in list_voyelles:
                    is_voyelle_in_last_syllabe = True
            if is_voyelle_in_last_syllabe:
                tab_syllabes_to_return.append(syllabe)

            elif num_syllabe >= 1:
                tab_syllabes_to_return[-1] += syllabe
    return tab_syllabes_to_return


def return_voyelles_a_la_suite(mot):
    list_voyelles_dans_le_mot = []
    list_voyelles = ["a", "ä", "à", 'á', "e", "ê", "è", "i", "î", "o", "ô", "u", "ù", "é", "ï"]
    list_voyelles_non_phonetique = ["a", "ä", "à", 'á', "e", "ê", "è", "i", "î", "o", "ô", "u", "ù"]
    list_voyelles_phonetique = ["é", "ï"]
    serie_de_voyelle = ""
    for lettre in mot:
        if lettre in list_voyelles:
            serie_de_voyelle += lettre
        else:
            if serie_de_voyelle != "":
                list_voyelles_dans_le_mot.append(serie_de_voyelle)
            serie_de_voyelle = ""
    if serie_de_voyelle != "":
        list_voyelles_dans_le_mot.append(serie_de_voyelle)

    return list_voyelles_dans_le_mot


def remplace_x(mot):
    mot = mot.replace("eaux", "o")
    mot = mot.replace("eux", "ê")
    mot = mot.replace("aux", "o")
    mot = mot.replace("oix", "wä")
    mot = mot.replace("ex", "èx")
    mot = mot.replace("aix", "è")
    mot = mot.replace("prix", "pri")
    mot = mot.replace("oux", "û")

    mot = mot.replace("x", "ks")
    return mot


def replace_s(mot):
    mot = mot.replace("mesd", "mèd")
    mot = mot.replace("mess", "mès")
    if mot == 'mes':
        mot = "mé"
    elif mot == 'tes':
        mot = "té"
    elif mot == 'ses':
        mot = "sé"
    elif mot == 'ces':
        mot = "sé"
    elif mot == 'les':
        mot = "lé"
    elif mot == 'des':
        mot = "dé"

    mot = mot.replace("ssass", "sas")
    mot = mot.replace("ressem", "resâ")
    mot = mot.replace("ressen", "resâ")
    mot = mot.replace("ess", "ès")
    mot = mot.replace("isi", "izi")
    mot = mot.replace("asi", "azi")
    mot = mot.replace("osi", "ozi")
    mot = mot.replace("iso", "izo")
    mot = mot.replace("isa", "iza")

    mot = mot.replace("ise", "ize")
    mot = mot.replace("osa", "oza")
    mot = mot.replace("esa", "eza")
    mot = mot.replace("usa", "uza")
    mot = mot.replace("use", "uze")
    mot = mot.replace("usi", "uzi")
    mot = mot.replace("ase", "aze")
    mot = mot.replace("ose", "oze")

    if mot[-1] == "s":
        mot = mot[:-1]
    mot = mot.replace("es", "ès")
    mot = mot.replace("ss", "s")
    return mot


def replace_er(mot):
    if len(mot) >= 2:
        if "er" in mot[-2:]:
            mot = mot[:-1]
            mot = list(mot)
            mot[-1] = "é"
            mot = ''.join(mot)
    return mot


def transform_mot_to_phonetique(mot):
    mot = mot.replace('û', 'u')
    mot = mot.replace('ô', 'o')
    mot = mot.replace('â', 'a')
    mot = mot.replace("ê", "è")
    mot = mot.replace("œ", "oe")
    mot = mot.replace("î", "i")
    mot = mot.replace("á", "a")

    if mot == "où":
        mot = "û"
    if mot == 'bbc':
        mot = "barbêciû"
    if mot == "est":
        mot = "è"

    if mot == "de":
        mot = "dê"
    if mot == "se":
        mot = "sê"
    if mot == "le":
        mot = "lê"
    mot = mot.replace("tech", "tèk")

    mot = mot.replace("schy", "ski")
    mot = mot.replace("sch", "ch")
    mot = mot.replace("ch", "<")

    mot = mot.replace("ccé", "ksé")
    mot = mot.replace("cce", "kse")
    mot = mot.replace("ccè", "ksè")
    mot = mot.replace("cci", "ksi")
    mot = mot.replace("cc", "k")

    if 'x' in mot:
        mot = remplace_x(mot)

    mot = mot.replace("aine", 'ène')
    mot = mot.replace("ainé", 'èné')
    mot = mot.replace("aina", 'èna')
    mot = mot.replace("aini", 'èni')

    mot = mot.replace("ouill", 'ûy')
    mot = mot.replace("ouil", "ûy")
    mot = mot.replace("ou", "û")
    mot = mot.replace("oin", 'w1')
    mot = mot.replace("oi", 'wä')
    mot = mot.replace('ement', 'emâ')
    mot = mot.replace("elle", 'èle')

    mot = mot.replace("euille", 'êye')
    mot = mot.replace("ueill", 'êy')
    mot = mot.replace("eill", 'èy')
    mot = mot.replace("aill", 'ay')
    mot = mot.replace("illi", "ili")
    mot = mot.replace("ille", 'iye')
    mot = mot.replace("illé", 'iyé')
    mot = mot.replace("ell", 'èl')
    mot = mot.replace("ll", 'l')
    mot.replace("aint", "1")
    mot = mot.replace("ain", '1')

    for voyelle in ["a", "e", "i", "o", "u", "è", "é", "ô", "ö", "û", "h", "y"]:
        mot = mot.replace("in" + voyelle, "*" + voyelle)

    mot = mot.replace("ein", "1")
    mot = mot.replace("in", "1")
    mot = mot.replace("*", "in")
    mot = mot.replace("ein", "èn")

    mot = mot.replace('iment', 'imâ')
    mot = mot.replace('mment', 'mâ')
    mot = mot.replace('ément', 'émâ')
    mot = mot.replace('aient', 'è')
    terminaison_not_removed = True
    if mot[-2:] == "ez" and terminaison_not_removed:
        mot = mot[:-1]
        mot = list(mot)
        mot[-1] = "é"
        mot = ''.join(mot)
        terminaison_not_removed = False
    if "s" in mot and len(mot) > 1:
        mot = replace_s(mot)

    mot = mot.replace('ce', 'se')
    mot = mot.replace('c1', 's1')
    mot = mot.replace('ci', 'si')
    mot = mot.replace('cé', 'sé')
    mot = mot.replace('cè', 'sè')
    mot = mot.replace('cê', 'sê')

    mot = replace_er(mot)

    if mot[-3:] == "ait":
        mot = mot[:-2]
        mot = list(mot)
        mot[-1] = "è"
        mot = ''.join(mot)
        terminaison_not_removed = False

    mot = mot.replace('ai', 'è')

    mot = mot.replace('eau', 'o')
    mot = mot.replace('au', 'o')
    mot = mot.replace('tent', 't')

    if mot[-3:] == "ent" and terminaison_not_removed:
        mot = mot[:-2]
        terminaison_not_removed = False

    if mot[-3:] == "end" and terminaison_not_removed:
        mot = mot[:-2]
        mot = list(mot)
        mot[-1] = "â"
        mot = ''.join(mot)
        terminaison_not_removed = False
    mot = mot.replace('enn', 'èn')
    mot = mot.replace('erre', 'ère')
    mot = mot.replace('err', 'èr')
    mot = mot.replace('oeu', 'ê')
    mot = mot.replace('eu', 'ê')

    if mot[-3:] == "ant" and terminaison_not_removed:
        mot = mot[:-2]
        mot = list(mot)
        mot[-1] = "â"
        mot = ''.join(mot)
        terminaison_not_removed = False

    mot = mot.replace("ant", "ât")

    mot = mot.replace('enn', 'èn')

    mot = mot.replace('nn', 'n')
    mot = mot.replace('qu', 'k')
    mot = mot.replace('ienci', 'iâsi')
    mot = mot.replace('ienc', 'iâs')
    mot = mot.replace('ient', 'iât')
    mot = mot.replace('ien', 'i1')

    if mot == "un":
        mot = "1"

    if mot == "chacun":
        mot = "chac1"

    if mot[-3:] == "ont" and terminaison_not_removed:
        mot = mot[:-2]
        mot = list(mot)
        mot[-1] = "ö"
        mot = ''.join(mot)
        terminaison_not_removed = False

    mot = mot.replace("ont", "öt")

    for voyelle in ["a", "e", "i", "o", "u", "è", "é", "ô", "ö", "û", "h", "y", "n"]:
        mot = mot.replace("on" + voyelle, "øn" + voyelle)

    mot = mot.replace("on", "ö")
    mot = mot.replace("ø", "o")

    for voyelle in ["a", "e", "i", "o", "u", "è", "é", "ô", "ö", "û", "h", "y", "œ", "ê", "n"]:
        mot = mot.replace("an" + voyelle, "ãn" + voyelle)
    mot = mot.replace("an", "â")
    mot = mot.replace("ã", "a")

    for voyelle in ["a", "e", "i", "o", "u", "è", "é", "ô", "ö", "û", "h", "y", "n"]:
        mot = mot.replace("am" + voyelle, "ãm" + voyelle)

    mot = mot.replace("am", "â")
    mot = mot.replace("ã", "a")

    for voyelle in ["a", "e", "i", "o", "u", "è", "é", "ô", "ö", "û", "h", "y"]:
        mot = mot.replace("ein" + voyelle, "*" + voyelle)

    mot = mot.replace("ein", "1")
    mot = mot.replace("*", "ein")

    for voyelle in ["a", "e", "i", "o", "u", "è", "é", "ô", "ö", "û", "h", "y", "m"]:
        mot = mot.replace("om" + voyelle, "*" + voyelle)

    mot = mot.replace("om", "ö")
    mot = mot.replace("*", "om")

    mot = mot.replace("mm", "m")
    mot = mot.replace("bb", "b")
    mot = mot.replace("rr", "r")
    mot = mot.replace("ett", "èt")
    mot = mot.replace("ge", "je")
    mot = mot.replace("gé", "jé")
    mot = mot.replace("gu", "g")
    mot = mot.replace('cy', 'si')
    mot = mot.replace('ce', 'se')
    mot = mot.replace('ci', 'si')
    mot = mot.replace('c', 'k')

    for voyelle in ["a", 'â', "e", "i", "o", "u", "è", "é", "ô", "ö", "û", "h", "y"]:
        mot = mot.replace("en" + voyelle, "*" + voyelle)
    mot = mot.replace('en', 'â')
    mot = mot.replace('*', 'en')
    mot = mot.replace('tt', 't')
    mot = mot.replace('kk', 'k')
    mot = mot.replace('pp', 'p')

    for voyelle in ["a", 'â', "e", "i", "o", "u", "è", "é", "ô", "ö", "û", "h", "y"]:
        mot = mot.replace("im" + voyelle, "*" + voyelle)
    mot = mot.replace('im', '1')
    mot = mot.replace('*', 'im')

    mot = mot.replace('ç', 's')
    mot = mot.replace('ï', 'i')

    mot = mot.replace('à', 'a')
    mot = mot.replace("q", "k")
    mot = mot.replace("ff", "f")
    mot = mot.replace("sêy", "kêy")
    mot = mot.replace("oeil", "êy")
    mot = mot.replace("zooooooooo", "zo")
    mot = mot.replace("oooohooohooo", "o")
    mot = mot.replace("ohhhhooohhhhoooo", "o")
    mot = mot.replace("oooohooohooo", "o")
    mot = mot.replace("oooohooohooo", "o")
    mot = mot.replace("oooohooohooo", "o")
    mot = mot.replace("oooohooohooo", "o")

    mot = mot.replace("aaaaaaaaaaaaaaaaaaaa", "a")
    mot = mot.replace("aaaaaaaaaaaaaaaah", "a")
    mot = mot.replace('eeeaaaaheehaaeeaae', "éa")
    mot = mot.replace("haaaaanhaaaaaanhaaaaâ", "hâ")
    mot = mot.replace('lalalalalalalalalalalalalalalala', "lala")
    mot = mot.replace('jênedemwäsèlere<er<e@hotmèl', "hotmèl")

    if len(mot) > 1:
        if mot[-1] == "e":
            mot = mot[:-1]

    return mot


def find_voyelle_and_consonne_in_phonetique(mot):
    voyelles_in_word = []
    consonnes_in_word = []
    for lettre in mot:
        if lettre in ["a", 'â', "e", "i", "o", "u", "è", "é", "ô", "ö", "û", "ê", "ä", "1"]:
            voyelles_in_word.append(lettre)
        else:
            consonnes_in_word.append(lettre)

    return voyelles_in_word, consonnes_in_word
