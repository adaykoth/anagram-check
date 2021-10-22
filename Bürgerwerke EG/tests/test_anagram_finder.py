import pytest
from code.anagram_finder import is_anagram

class TestAnagramCheck():

    def test_on_anagram(self):
        """
        Check if anagrams are correctly identified as such.
        """

        test_string = "anagram"
        test_anagram = "gramana"
        actual = is_anagram(test_string, test_anagram)
        assert actual == True

    def test_on_no_anagram(self):
        """
        Check if words which are not anagrams are correctly identified as such.
        """

        test_string = "anagram"
        test_anagram = "granada"
        actual = is_anagram(test_string, test_anagram)
        assert actual == False

    def test_with_whitespace(self):
        """
        Check for handling of whitespaces.

        Depending on the definition of anagram,
        whitespaces might render two words with the same letters NOT an anagram of each other.
        Here it is treated as still being an anagram.
        """

        test_string = "annagram"
        test_anagram_w_withspace = "gram anna"
        actual = is_anagram(test_string, test_anagram_w_withspace)
        assert actual == True

    def test_wrong_input(self):
        """
        Function should only accepts words without numbers (per convention).

        Currently unnecessary in the global scope of the script,
        as input() function converts everything to strings anyway.
        """

        test_float = 2954.02
        test_list = ["anagram", "gramana"]
        with pytest.raises(AttributeError) as exc_info:
            is_anagram(test_float, test_list)
        expected_error_msg = "Words must be strings!"
        assert exc_info.match(expected_error_msg)

    def test_words_with_numbers(self):
        """
        Function should only accepts words without numbers (per convention).

        Currently unnecessary in the global scope of the script,
        as input() function converts everything to strings anyway.
        """

        test_string = "1. FC Köln"
        test_anagram = "anagram"
        with pytest.raises(ValueError) as exc_info:
            is_anagram(test_string, test_anagram)
        expected_error_msg = "should only contain letters!"
        assert exc_info.match(expected_error_msg)

if __name__ == '__main__':
    pytest.main()