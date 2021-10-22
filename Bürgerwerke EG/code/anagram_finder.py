
def is_anagram(word1, word2):
    """
    Checks for two given words if they are anagrams of each other.
        This is done by leveraging pythons runtime type conversion and checking if the characters in both words match.

    Parameters
    ----------
    word1 : str
        First word
    word2 : str
        Second word

    Returns
    -------
    bool
        True if words are anagrams of each other, False otherwise.
        
    """
    # unnecessary with current implementation, as we only pass strings to function
    try:
        # strip whitespace from strings
        w1, w2 = [w.replace(" ", "") for w in (word1,word2)]
    except AttributeError:
        raise AttributeError("Words must be strings!")

    # check if strings contain numbers
    if not w1.isalpha():
        raise ValueError(f"{w1} should only contain letters!")
    elif not w2.isalpha():
        raise ValueError(f"{w2} should only contain letters!")

    return sorted(w1) == sorted(w2)


if __name__ == '__main__':

    first_word = input("Enter the first word: ")
    second_word = input("Enter the second word: ")

    if is_anagram(first_word,second_word):
        print(f"{second_word} is an anagram of {first_word}.")
    else:
        print(f"{second_word} is NO anagram of {first_word}.")


