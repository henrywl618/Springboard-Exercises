def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    if parens[0] == ')':
        return False
    if parens.count('(') != parens.count(')'):
        return False

    count = 0
    for char in parens:
        if count < 0:
            return False
        if char =='(':
            count+=1
        elif char ==')':
            count-=1
    return True

