def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swap = to_swap.lower()
    swapped_phrase = ''

    for letter in phrase:
        print(letter, swap)
        if letter.lower() == swap:
            swapped_phrase+=letter.swapcase()
        else:
            swapped_phrase+=letter

    return swapped_phrase