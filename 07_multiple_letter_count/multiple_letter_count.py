def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letters = list(phrase)
    letters_dictionary = {letter:letters.count(letter) for letter in phrase}

    return letters_dictionary
    

print(multiple_letter_count('yay'))