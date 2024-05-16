from main import waluta_dict_na_str,waluta_str_na_dict

def test_waluta_dict_na_str():
    assert waluta_dict_na_str({}) == ""
    assert waluta_dict_na_str({1:50,2:13,3:20}) == "50 galeon, 13 sykl, 20 knut"
    assert waluta_dict_na_str({1:0,2:0,3:0.9}) == ""
    assert waluta_dict_na_str({1: Null, 2: Null, 3: Null}) == Null
def test_waluta_str_na_dict():
    assert waluta_str_na_dict("") == {'galeon': 0, 'sykl': 0, 'knut': 0}
    assert waluta_str_na_dict("10 g 8 s 99 k") == {'galeon': 10, 'sykl': 8, 'knut': 99}
    assert waluta_dict_na_dict({1: 100, 2: 5, 3: 8.19}) == {'galeon': 100, 'sykl': 5, 'knut': 8.19}
    assert waluta_dict_na_dist({1: Null, 2: Null, 3: 8}) == Null

test_waluta_dict_na_str()
test_waluta_str_na_dict()
