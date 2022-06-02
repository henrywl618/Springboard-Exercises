def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = set('aeiou')
    char_dict = dict(enumerate(s))
    vowels_dict = {key:value for (key,value) in char_dict.items() if value in vowels}
    key_list = list(vowels_dict.keys())
    values_list = list(vowels_dict.values())
   
    i=0

    for key in key_list[::-1]:
        char_dict[key] = values_list[i]
        i+=1
        
    return "".join(list(char_dict.values()))
