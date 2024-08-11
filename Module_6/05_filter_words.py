def filater_words(text: str) -> set:
    pass


def test_filter_words():
    assert filater_words("Ala ma kota") == {'ma', 'kota'}
    assert filater_words("Ala MA KOTA") == {'MA', 'KOTA'}
    assert filater_words("Ala Ma kotA") == {'Ma', 'kotA'}
    assert filater_words("tygrys") == set()