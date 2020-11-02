def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

    >>> same_frequency(551122, 221515)
    True

    >>> same_frequency(321142, 3212215)
    False

    >>> same_frequency(1212, 2211)
    True
    """
    msg = f"num1: {num1} \nnum2: {num2}"

    if len(str(num1)) == len(str(num2)):
        print(msg)
        return True
    elif len(str(num1)) != len(str(num2)):
        print(msg)
        return False
