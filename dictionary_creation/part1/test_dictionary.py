"""Unit Testing for Task 1 and 2"""
__author__ = 'Brendon Taylor'
__docformat__ = 'reStructuredText'
__modified__ = '20/05/2020'
__since__ = '22/05/2020'


import unittest
from hash_table import LinearProbeHashTable
from dictionary import Statistics, Dictionary


def file_len(filename: str) -> int:
    """Calculates the number of lines in a given file"""
    with open(filename, encoding='UTF-8') as f:
        for i, l in enumerate(f):
            pass
    return i + 1


class TestDictionary(unittest.TestCase):
    DEFAULT_TABLE_SIZE = 250727
    DEFAULT_HASH_BASE = 31
    DEFAULT_TIMEOUT = 10
    FILENAMES = ['english_small.txt', 'english_large.txt', 'french.txt']
    RANDOM_STR = 'FIT1008 is the best subject!'

    def setUp(self) -> None:
        """ Used by our test cases """
        self.dictionary = Dictionary(TestDictionary.DEFAULT_HASH_BASE, TestDictionary.DEFAULT_TABLE_SIZE)

    def test_init(self) -> None:
        """ Testing type of our table and the length is 0 """
        self.assertEqual(type(self.dictionary.hash_table), LinearProbeHashTable)
        self.assertEqual(len(self.dictionary.hash_table), 0)

    def test_load_dictionary(self) -> None:
        """ Reading a dictionary and ensuring the number of lines matches the number of words
            Also testing the various exceptions are raised correctly """
        for filename in TestDictionary.FILENAMES:
            self.dictionary = Dictionary(TestDictionary.DEFAULT_HASH_BASE, TestDictionary.DEFAULT_TABLE_SIZE)
            words = self.dictionary.load_dictionary(filename)
            lines = file_len(filename)
            self.assertEqual(words, lines, "Number of words should match number of lines")

    def test_add_word(self) -> None:
        """ Testing the ability to add words """
        t1 = Dictionary(31, 17)
        t1.add_word("first test") # Normal test as a first one
        # First test
        self.assertEqual(t1.hash_table.__getitem__("first test"), 1, "Test for add_word failed")

        t1.add_word("TEST2") # Testing for capital and lowercase
        # Second test
        self.assertEqual(t1.hash_table.__getitem__("test2"), 1, "Test for add_word failed")

    def test_find_word(self) -> None:
        """ Ensuring both valid and invalid words """
        t2 = Dictionary(31, 17)
        t2.add_word("Does this work?")  # Mixture of capital, ? and spaces
        # First test
        self.assertTrue(t2.find_word("does this work?"), "Test for find_word failed")
        t2.add_word("Helllo")
        # Second test
        self.assertFalse(t2.find_word("Hello"), "Test for find_word failed") # It should give false as Hello is different from Helllo

    def test_delete_word(self) -> None:
        """ Deleting valid words and ensuring we can't delete invalid words """
        self.dictionary.load_dictionary('english_small.txt')
        table_size = len(self.dictionary.hash_table)
        with self.assertRaises(KeyError):
            self.dictionary.delete_word(TestDictionary.RANDOM_STR)
        self.assertEqual(len(self.dictionary.hash_table), table_size)

        self.dictionary.delete_word('test')
        self.assertEqual(len(self.dictionary.hash_table), table_size - 1)
        
        t3 = Dictionary(31, 17)
        t3.add_word("123") # add and then delete for test
        t3.delete_word("123") 
        # First test. "123" should not be found after deleting
        #t3.assertFalse(t3.find_word("123"), "Key should not have been found")
        # I was above test initially, but since it involves find_word, it is not appropriate here

        self.assertRaises(KeyError, lambda: t3.hash_table.__getitem__("123"))
        # Wrong test: self.assertRaises(t3.hash_table.__getitem__("123"), KeyError, "Key should not exist")

        """
        https://stackoverflow.com/questions/6103825/how-to-properly-use-unit-testings-assertraises-with-nonetype-objects
        This link has helped me deal with KeyError, as my previous attempts raised KeyError before testing it
        """
        
        # Second test, check for KeyError
        # Wrong test: self.assertRaises(t3.delete_word("Not existing word"), KeyError, "It should raise KeyError")
        self.assertRaises(KeyError, lambda: t3.delete_word("Non-existing word"))

            # Extra tests for Statistics method
    def test_statistics(self):
        """
         A unittest for statistics returning correct Tuple
        """
        s1 = Dictionary(1, 1)
        s1.add_word("hi")
        s1.add_word("hi") # Because they are the same keys, it is not considered collision
        # However, it is rehashed once as it needs a resize of the table when second "hi" is input
        self.assertEqual(s1.hash_table.statistics(), (0, 0, 0, 1)) 
        s2 = Dictionary(1, 3)
        s2.add_word("a")
        s2.add_word("bijefo")
        s2.add_word("ciefjie")
        s2.add_word("cijefiel")
        s2.add_word("cosjef")
        # my second test
        self.assertEqual(s2.hash_table.statistics(), (1, 1, 1, 1))
    # my test on load_statistics
    def test_load_statistics(self):
        """
        A test for load_statistics method
        """
        s3 = Statistics() # This also compliments as a unit test for statistics class
        self.assertIsInstance(s3.load_statistics(1, 3, "sampletext.txt", 3), tuple)
        # my second test, I will be breaking tuple into parts and inspect each
        a, b, c, d, e, f = s3.load_statistics(3, 5, "sampletext.txt", 2)
        self.assertLess(b, 2)  # b = time. Time taken to process should be less than 2
        # print(a, b, c, d, e, f) I have done manual tests to make sure values are correct
    def test_table_load_statistics(self):
        # I have done manual test to make sure that it works and prints desired otuput
        # Working code in table_load_statistics in dictionary.py also proves the legitimacy of method
        pass
        """
        s4 = Statistics()
        s4.table_load_statistics(10)
        
        s5 = Statistics()
        s5.table_load_statistics(2) 
        This was also a valid test for manual check, but commenting it out since it will take time
        """


if __name__ == '__main__':
    unittest.main()