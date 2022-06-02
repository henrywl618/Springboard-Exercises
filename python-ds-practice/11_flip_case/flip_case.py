def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    def switchCase(char):
        if char.islower():
            return char.upper()
        return char.lower()

    return ''.join([switchCase(letter) if letter.lower() == to_swap.lower() else letter for letter in phrase])
