def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

    >>> vowel_count('rithm school')
    {'i': 1, 'o': 2}

    >>> vowel_count('HOW ARE YOU? i am great!')
    {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    vowels = set("aeiou")
    count = {}.fromkeys(vowels, 0)
    phrase = phrase.lower()

    for char in phrase:
        if char in count:
            count[char] += 1

    return count
