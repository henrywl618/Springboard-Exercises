def print_upper_words(strings,must_start_with):
    """Prints words that start with a given set of letters

    For example:
    print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})

    Should print: "HELLO", "HEY", "YO", and "YES"

    """
    for string in strings:
        first_letter = string[0]
        if first_letter in must_start_with: 
            print(string.upper()) 


# this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})