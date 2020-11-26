import unittest


def has_unique_characters(string):
    letters = {}
    for letter in string:
        if letter in letters:
            return False
        letters[letter] = True
    return True


class TestHasUniqueCharacters(unittest.TestCase):

    def test_returns_true_if_unique(self):
        string = "abcdefg"

        result = has_unique_characters(string)
        self.assertTrue(result)
