import unittest


def check_permutations(str1, str2):
    char_hash = {}
    if len(str1) != len(str2):
        return False

    for char in str1:
        if char not in char_hash:
            char_hash[char] = 1
        else:
            char_hash[char] += 1

    for char in str2:
        if char not in char_hash:
            return False
        else:
            char_hash[char] -= 1
            if char_hash[char] == 0:
                del char_hash[char]
    return True


class TestCheckPermutations(unittest.TestCase):

    def test_returns_true_if_str1_is_permutation_of_str2(self):
        str1 = "hello"
        str2 = "holel"

        result = check_permutations(str1, str2)
        self.assertTrue(result)

    def test_returns_false_if_str1_is_not_a_permutation_of_str2(self):
        str1 = "hello"
        str2 = "holll"

        result = check_permutations(str1, str2)
        self.assertFalse(result)

    def test_returns_false_if_str1_is_not_same_length_as_str2(self):
        str1 = "oneword"
        str2 = "oneword2"

        result = check_permutations(str1, str2)
        self.assertFalse(result)
