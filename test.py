from main import wybierz_sowe_zwroc_koszt

def test_wybierz_sowe_zwroc_koszt():
    assert wybierz_sowe_zwroc_koszt(True, 'krajowa',
                                'list', 'wyjec') == {'galeony' : 0, 'sykle': 0, 'knuty' : 23}

    assert wybierz_sowe_zwroc_koszt(True, 'dalekobiezna',
                                'paczka', 'wyjec') == {'galeony' : 0, 'sykle': 2, 'knuty' : 12}


test_wybierz_sowe_zwroc_koszt()