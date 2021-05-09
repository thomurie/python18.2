def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    phrase_array = list(phrase)

    first_word = phrase_array.pop(0).title()

    phrase_array.insert(0, first_word)

    return ''.join(phrase_array)

print(capitalize('only first word'))