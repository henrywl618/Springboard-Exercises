def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    n1 = str(num1)
    n2 = str(num2)

    if len(n1) != len(n2):
        return False

    set1=set(n1)

    for digit in set1:
        if n2.count(digit) != n1.count(digit):
            return False
    
    return True
