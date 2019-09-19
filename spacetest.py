
import unittest
from Spaceman import is_word_guessed, is_guess_in_word, load_word


class spacemanTests(unittest.TestCase):

    def test_word_gen(self):
        f = open('words.txt', 'r')
        words_list = f.readlines()
        f.close()
        words_list = words_list[0].split(' ')
        word = load_word()
        self.assertTrue(word.lower() in words_list)

    def test_word_guessed(self):
        self.assertTrue(is_word_guessed('demon', ['d', 'e', 'm', 'o', 'n']))
        self.assertTrue(is_word_guessed('demon', ['s', 'c', 'h', 'M', 'o', 'n','e', 'y']))
        self.assertFalse(is_word_guessed('demon', ['c', 'e', 'm', 'o', 'n']))
        self.assertFalse(is_word_guessed('demon', ['<', '*', 'm', 4, 'e']))

    def test_guess_in_word(self):
        self.assertTrue(is_guess_in_word("o", "moth"))
        self.assertFalse(is_guess_in_word("O", "moth"))
        self.assertFalse(is_guess_in_word("0", "moth"))


if __name__ == '__main__':
    unittest.main()
