def count_word(text: str, search_word: str) -> int:
    counter = 0
    for i in text.split(' '):
        if i == search_word:
            counter += 1

    return counter


def test_word_count():
    assert count_word('Python i Python', 'Python') == 2
    assert count_word('Python i Python', 'python') == 0
    assert count_word('Python i python', 'python') == 1
    assert count_word('Java i PHP', 'Python') == 0
