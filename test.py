from main import licz_sume

def test_licz_sume():
    # Test 1: Sprawdzenie poprawności obliczeń dla podanych danych
    slownik = {
        "galeon": [1, 3, 5],
        "sykl": [18, 20, 10],
        "knut": [30, 40, 7]
    }
    expected_result = {"galeon": 4, "sykl": 19, "knut": 11}
    assert licz_sume(slownik) == expected_result

    # Test 2: Sprawdzenie poprawności obliczeń dla pustego słownika
    slownik_pusty = {"galeon": [], "sykl": [], "knut": []}
    expected_result_pusty = {"galeon": 0, "sykl": 0, "knut": 0}
    assert licz_sume(slownik_pusty) == expected_result_pusty

    # Test 3: Sprawdzenie poprawności obliczeń dla wartości ujemnych
    slownik_ujemny = {"galeon": [-1, -3, -5], "sykl": [-18, -20, -10], "knut": [-30, -40, -7]}
    expected_result_ujemny = {"galeon": -4, "sykl": -19, "knut": -11}
    assert licz_sume(slownik_ujemny) == expected_result_ujemny

    # Test 4: Sprawdzenie poprawności obliczeń dla wartości zerowych
    slownik_zero = {"galeon": [0, 0, 0], "sykl": [0, 0, 0], "knut": [0, 0, 0]}
    expected_result_zero = {"galeon": 0, "sykl": 0, "knut": 0}
    assert licz_sume(slownik_zero) == expected_result_zero

    # Test 5: Sprawdzenie poprawności obliczeń dla dużych wartości
    slownik_duze = {"galeon": [1000000, 2000000, 3000000], "sykl": [4000000, 5000000, 6000000], "knut": [7000000, 8000000, 9000000]}
    expected_result_duze = {"galeon": 611764, "sykl": 0, "knut": 0}
    assert licz_sume(slownik_duze) == expected_result_duze

    print("Wszystkie testy zakończone powodzeniem!")

# Wywołanie testów
test_licz_sume()