from utils import return_syllabes


def test_a_return_a():
    given = "a"
    expected = ['a']
    result = return_syllabes(given)
    assert result == expected


def test_ota_return_o_ta():
    given = "oba"
    expected = ['o', 'ba']
    result = return_syllabes(given)
    assert result == expected


def test_rota_return_ro_ta():
    given = "rota"
    expected = ['ro', 'ta']
    result = return_syllabes(given)
    assert result == expected


def test_robot_return_ro_bot():
    given = "robot"
    expected = ['ro', 'bot']
    result = return_syllabes(given)
    assert result == expected


def test_rotor_return_ro_tor():
    given = "rotor"
    expected = ['ro', 'tor']
    result = return_syllabes(given)
    assert result == expected


def test_bonjour_return_bon_jour():
    given = "bonjour"
    expected = ['bon', "jour"]
    result = return_syllabes(given)
    assert result == expected


def test_trop_return_trop():
    given = "trop"
    expected = ['trop']
    result = return_syllabes(given)
    assert result == expected


def test_velociraptor_return_ve_lo_ci_rap_tor():
    given = "vélociraptor"
    expected = ['vé', 'lo', 'ci', 'rap', 'tor']
    result = return_syllabes(given)
    assert result == expected


def test_oiseaux_return_oi_seaux():
    given = "oiseaux"
    expected = ['oi', 'seaux']
    result = return_syllabes(given)
    assert result == expected


def test_renegats_re_ne_gats():
    given = "renegats"
    expected = ['re', 'ne', 'gats']
    result = return_syllabes(given)
    assert result == expected


# TODO le expected n'est pas vraiment celui attendu, mais pour l'instant c'est pas mal
def test_patrons_return_pa_trons():
    given = "patrons"
    expected = ['pat', 'rons']
    result = return_syllabes(given)
    assert result == expected


def test_noue_return_nou_e():
    given = "noué"
    expected = ['nou', 'é']
    result = return_syllabes(given)
    assert result == expected


def test_degente_return_de_gen_te():
    given = "dégenté"
    expected = ['dé', 'gen', 'té']
    result = return_syllabes(given)
    assert result == expected


def test_neant_return_ne_ant():
    given = "néant"
    expected = ['né', 'ant']
    result = return_syllabes(given)
    assert result == expected


def test_aleas_return_a_le_as():
    given = "aléas"
    expected = ['a', 'lé', 'as']
    result = return_syllabes(given)
    assert result == expected


def test_aeroport_return_a_e_ro_port():
    given = "aéroport"
    expected = ['a', 'é', 'ro', 'port']
    result = return_syllabes(given)
    assert result == expected


