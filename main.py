LONG_TEXT = """asdlknfasldkmfasdfasdf"""
arr = []


def add_word(word):
    arr.append(word)
    return arr


def get_words(chars):
    vocab = []
    arr.sort()
    for i in range(len(arr)):
        if arr[i].startswith(chars) is True and len(vocab) < 5:
            vocab.append(arr[i])
    return vocab


def crop_text(length):
    i = 0
    while i * length < len(LONG_TEXT):
        yield LONG_TEXT[i * length:(i+1) * length]
        i += 1


if __name__ == '__main__':
    assert get_words('') == []

    add_word('bat')
    add_word('batman')

    assert get_words('') == ['bat', 'batman']
    assert get_words('bat') == ['bat', 'batman']
    assert get_words('batm') == ['batman']
    assert get_words('x') == []

    add_word('bar')
    add_word('bartender')
    add_word('basket')
    add_word('band')

    assert get_words('ba') == ['band', 'bar', 'bartender', 'basket', 'bat']

    text_generator = crop_text(10)
    assert next(text_generator) == "asdlknfasl"
    assert next(text_generator) == "dkmfasdfas"
    assert next(text_generator) == "df"
