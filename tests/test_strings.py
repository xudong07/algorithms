from strings.add_binary import add_binary
from strings.breaking_bad import match_symbol, match_symbol_1, bracket
from strings.decode_string import decode_string
from strings.delete_reoccurring import delete_reoccurring_characters
from strings.domain_extractor import domain_name_1, domain_name_2
from strings.encode_decode import encode, decode
from strings.group_anagrams import group_anagrams
from strings.int_to_roman import int_to_roman
from strings.is_palindrome import is_palindrome, is_palindrome_reverse, \
is_palindrome_two_pointer, is_palindrome_stack
from strings.license_number import license_number
from strings.make_sentence import make_sentence
from strings.merge_string_checker import is_merge_recursive, is_merge_iterative
from strings.multiply_strings import multiply
from strings.one_edit_distance import is_one_edit, is_one_edit2
from strings.rabin_karp import rabin_karp
from strings.reverse_string import *
from strings.reverse_vowel import reverse_vowel
from strings.reverse_words import reverse_words
from strings.roman_to_int import roman_to_int
from strings.strip_url_params import *
from strings.validate_coordinates import *
from strings.word_squares import word_squares

import unittest


class TestAddBinary(unittest.TestCase):
    """[summary]
    Test for the file add_binary.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_add_binary(self):
        self.assertEqual("100", add_binary("11", "1"))
        self.assertEqual("101", add_binary("100", "1"))
        self.assertEqual("10", add_binary("1", "1"))


class TestBreakingBad(unittest.TestCase):
    """[summary]
    Test for the file breaking_bad.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def setUp(self):
        self.words = ['Amazon', 'Microsoft', 'Google']
        self.symbols = ['i', 'Am', 'cro', 'le', 'abc']
        self.result = ['M[i]crosoft', '[Am]azon', 'Mi[cro]soft', 'Goog[le]']
    def test_match_symbol(self):
        self.assertEqual(self.result, match_symbol(self.words,self.symbols))
    def test_match_symbol_1(self):
        self.assertEqual(['[Am]azon', 'Mi[cro]soft', 'Goog[le]'], match_symbol_1(self.words,self.symbols))
    def test_bracket(self):
        self.assertEqual(('[Am]azon', 'Mi[cro]soft', 'Goog[le]'), bracket(self.words, self.symbols))


class TestDecodeString(unittest.TestCase):
    """[summary]
    Test for the file decode_string.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_decode_string(self):
        self.assertEqual("aaabcbc", decode_string("3[a]2[bc]"))
        self.assertEqual("accaccacc", decode_string("3[a2[c]]"))


class TestDeleteReoccurring(unittest.TestCase):
    """[summary]
    Test for the file delete_reoccurring.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_delete_reoccurring_characters(self):
        self.assertEqual("abc", delete_reoccurring_characters("aaabcccc"))


class TestDomainExtractor(unittest.TestCase):
    """[summary]
    Test for the file domain_extractor.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_valid(self):
        self.assertEqual(domain_name_1("https://github.com/SaadBenn"), "github")
    def test_invalid(self):
        self.assertEqual(domain_name_2("http://google.com"), "google")


class TestEncodeDecode(unittest.TestCase):
    """[summary]
    Test for the file encode_decode.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_encode(self):
        self.assertEqual("4:keon2:is7:awesome", encode("keon is awesome"))
    def test_decode(self):
        self.assertEqual(['keon', 'is', 'awesome'], decode("4:keon2:is7:awesome"))


class TestGroupAnagrams(unittest.TestCase):
    """[summary]
    Test for the file group_anagrams.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_group_anagrams(self):
        self.assertEqual([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']], \
        group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


class TestIntToRoman(unittest.TestCase):
    """[summary]
    Test for the file int_to_roman.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_int_to_roman(self):
        self.assertEqual("DCXLIV", int_to_roman(644))
        self.assertEqual("I", int_to_roman(1))
        self.assertEqual("MMMCMXCIX", int_to_roman(3999))


class TestIsPalindrome(unittest.TestCase):
    """[summary]
    Test for the file is_palindrome.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_is_palindrome(self):
        # 'Otto' is a old german name.
        self.assertTrue(is_palindrome("Otto"))
        self.assertFalse(is_palindrome("house"))
    def test_is_palindrome_reverse(self):
        # 'Otto' is a old german name.
        self.assertTrue(is_palindrome_reverse("Otto"))
        self.assertFalse(is_palindrome_reverse("house"))
    def test_is_palindrome_two_pointer(self):
        # 'Otto' is a old german name.
        self.assertTrue(is_palindrome_two_pointer("Otto"))
        self.assertFalse(is_palindrome_two_pointer("house"))
    def test_is_palindrome_stack(self):
        # 'Otto' is a old german name.
        self.assertTrue(is_palindrome_stack("Otto"))
        self.assertFalse(is_palindrome_stack("house"))


class TestLicenseNumber(unittest.TestCase):
    """[summary]
    Test for the file license_number.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_license_number(self):
        self.assertEqual("a-b-c-d-f-d-d-f", license_number("a-bc-dfd-df", 1))
        self.assertEqual("ab-cd-fd-df", license_number("a-bc-dfd-df", 2))
        self.assertEqual("ab-cdf-ddf", license_number("a-bc-dfd-df", 3))
        self.assertEqual("abcd-fddf", license_number("a-bc-dfd-df", 4))
        self.assertEqual("abc-dfddf", license_number("a-bc-dfd-df", 5))


class TestMakeSentence(unittest.TestCase):
    """[summary]
    Test for the file make_sentence.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_make_sentence(self):
        dictionarys = ["", "app", "let", "t", "apple", "applet"]
        word = "applet"
        self.assertTrue(make_sentence(word, dictionarys))


class TestMergeStringChecker(unittest.TestCase):
    """[summary]
    Test for the file merge_string_checker.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_is_merge_recursive(self):
        self.assertTrue(is_merge_recursive("codewars", "cdw", "oears"))
    def test_is_merge_iterative(self):
        self.assertTrue(is_merge_iterative("codewars", "cdw", "oears"))


class TestMultiplyStrings(unittest.TestCase):
    """[summary]
    Test for the file multiply_strings.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_multiply(self):
        self.assertEqual("23", multiply("1", "23"))
        self.assertEqual("529", multiply("23", "23"))
        self.assertEqual("0", multiply("0", "23"))
        self.assertEqual("1000000", multiply("100", "10000"))


class TestOneEditDistance(unittest.TestCase):
    """[summary]
    Test for the file one_edit_distance.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_is_one_edit(self):
        self.assertTrue(is_one_edit("abc", "abd"))
        self.assertFalse(is_one_edit("abc", "aed"))
        self.assertFalse(is_one_edit("abcd", "abcd"))
    def test_is_one_edit2(self):
        self.assertTrue(is_one_edit2("abc", "abd"))
        self.assertFalse(is_one_edit2("abc", "aed"))
        self.assertFalse(is_one_edit2("abcd", "abcd"))


class TestRabinKarp(unittest.TestCase):
    """[summary]
    Test for the file rabin_karp.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_rabin_karp(self):
        self.assertEqual(3, rabin_karp("abc", "zsnabckfkd"))
        self.assertEqual(None, rabin_karp("abc", "zsnajkskfkd"))


class TestReverseString(unittest.TestCase):
    """[summary]
    Test for the file reverse_string.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_recursive(self):
        self.assertEqual("ereht olleh", recursive("hello there"))
    def test_iterative(self):
        self.assertEqual("ereht olleh", iterative("hello there"))
    def test_pythonic(self):
        self.assertEqual("ereht olleh", pythonic("hello there"))
    def test_ultra_pythonic(self):
        self.assertEqual("ereht olleh", ultra_pythonic("hello there"))
    

class TestReverseVowel(unittest.TestCase):
    """[summary]
    Test for the file reverse_vowel.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_reverse_vowel(self):
        self.assertEqual("holle", reverse_vowel("hello"))


class TestReverseWords(unittest.TestCase):
    """[summary]
    Test for the file reverse_words.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_reverse_words(self):
        self.assertEqual("pizza like I and kim keon am I", \
        reverse_words("I am keon kim and I like pizza"))


class TestRomanToInt(unittest.TestCase):
    """[summary]
    Test for the file roman_to_int.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_roman_to_int(self):
        self.assertEqual(621, roman_to_int("DCXXI"))
        self.assertEqual(1, roman_to_int("I"))
        self.assertEqual(3999, roman_to_int("MMMCMXCIX"))


# class TestStripUrlParams(unittest.TestCase):
#     """[summary]
#     Test for the file strip_urls_params.py

#     Arguments:
#         unittest {[type]} -- [description]
#     """

#     def test_strip_url_params1(self):
#         self.assertEqual(strip_url_params1("www.saadbenn.com?a=1&b=2&a=2"), "www.saadbenn.com?a=1&b=2")
#         self.assertEqual(strip_url_params1("www.saadbenn.com?a=1&b=2", ['b']), "www.saadbenn.com?a=1")
#     def test_strip_url_params2(self):
#         self.assertEqual(strip_url_params2("www.saadbenn.com?a=1&b=2&a=2"), "www.saadbenn.com?a=1&b=2")
#         self.assertEqual(strip_url_params2("www.saadbenn.com?a=1&b=2", ['b']), "www.saadbenn.com?a=1")
#     def test_strip_url_params3(self):
#         self.assertEqual(strip_url_params3("www.saadbenn.com?a=1&b=2&a=2"), "www.saadbenn.com?a=1&b=2")
#         self.assertEqual(strip_url_params3("www.saadbenn.com?a=1&b=2", ['b']), "www.saadbenn.com?a=1")


class TestValidateCoordinates(unittest.TestCase):
    """[summary]
    Test for the file validate_coordinates.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_valid(self):
        valid_coordinates = ["-23, 25","4, -3","90, 180","-90, -180"]
        for coordinate in valid_coordinates:
            self.assertTrue(is_valid_coordinates_0(coordinate))
    def test_invalid(self):
        invalid_coordinates = ["23.234, - 23.4234","99.234, 12.324","6.325624, 43.34345.345","0, 1,2","23.245, 1e1"]
        for coordinate in invalid_coordinates:
            self.assertFalse(is_valid_coordinates_0(coordinate))


class TestWordSquares(unittest.TestCase):
    """[summary]
    Test for the file word_squares.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_word_squares(self):
        self.assertEqual([['wall', 'area', 'lead', 'lady'], ['ball', 'area', 'lead', 'lady']], \
        word_squares(["area","lead","wall","lady","ball"]))


if __name__ == "__main__":
    unittest.main()