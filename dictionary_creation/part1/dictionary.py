from hash_table import LinearProbeHashTable
from typing import Tuple
import timeit




class Statistics:
    """
	Statistics class
	No class constants
	"""

    def load_statistics(self, hash_base: int, table_size: int, filename: str, max_time: int) -> Tuple:
        """
		This method returns a set of tuple of values:
			words: the number of words added to the table
			time: the time taken for load_dictionary to complete if <= max_time and max_time otherwise
			conflict_count, probe_total, probe_max, rehash_count: are the same as in Dictionary.statistics()
		:complexity: O(N) where N is the table size
		statistics() has complexity of O(1), as done in the previous part, and constructor has
		N where N is the table size, and load_dictionary has O(N) where N is number of keys in the file
		since N for table size is larger and dominant factor, O(N) is the complexity
		"""
        dic = Dictionary(hash_base, table_size)

        # for time
        start_time = timeit.default_timer()
        try:
            dic.load_dictionary(filename, max_time)
        except TimeoutError:
            time = max_time
        else:
            time = timeit.default_timer() - start_time

        # for words
        words = len(dic.hash_table)
        return (words, time) + dic.hash_table.statistics()

    def table_load_statistics(self, max_time: int) -> None:
        """
		It prints out set of data for 27 different types of combinations.
		It uses load_statistics to time how long it takes for load_dictionary to run
		:complexity: O(N^3), where N is the number of inputs in the text file
		"""
        b_list = [1, 27183, 250726]
        tablesize_list = [250727, 402221, 1000081]
        filename_list = ["english_large.txt", "english_small.txt", "french.txt"]
        for b in b_list:
            for t in tablesize_list:
                for f in filename_list:
                    hashed_b = hash(b)
                    hashed_t = hash(t)  # apply universal hash function to both b and t

                    wo, ti, cc, pt, pm, rc = self.load_statistics(hashed_b, hashed_t, f, max_time)
                    # these 2 characters represent each returned component
                    print("{}, {}, {}, {}, {}, {}, {}, {}, {}".format(b, t, f, wo, ti, cc, pt, pm, rc))
            # order of these are as found in Graphing Tutorial


class Dictionary:
    """
	Dictionary class
	constants:
		INTEGER: one in this case. A default value to set to the hash table as the associate data.
	"""
    INTEGER = 1

    def __init__(self, hash_base: int, table_size: int) -> None:
        """
		A constructor for Dictionary class
        :complexity: O(N) where N is the table_size
		"""
        self.hash_table = LinearProbeHashTable(hash_base, table_size)

    def load_dictionary(self, filename: str, time_limit: int = None) -> int:
        """
		It loads dictionary from given filename
		:raises TimeoutError: when loading dictionary takes more than time_limit, if given
		:complexity: O(N) where N is the number of lines in filename file
		"""
        if time_limit:  # if time limit is given, check time
            start_time = timeit.default_timer()
            with open(filename, encoding='UTF-8') as f:  # I am reusing some of the formats from Collab prac 2.
                for line in f:
                    self.hash_table.__setitem__(line.rstrip(), self.INTEGER)
                    if timeit.default_timer() - start_time > time_limit:
                        raise TimeoutError('Loading took too much time')
                f.close()
            return len(self.hash_table)
        # I made this change because in Task 2, I had a problem with open
        # Encoding taking too much time. I wanted to reduce complexity as much as possible

        # I am using timeit to measure time. statement is a function to check time on.
        # Referred to: https://docs.python.org/3/library/timeit.html, and an answer from Dr. Alexey on Ed

        else:
            with open(filename, encoding='UTF-8') as f:  # I am reusing some of the formats from Collab prac 2.
                for line in f:
                    self.hash_table.__setitem__(line.rstrip(), self.INTEGER)
                # counter += 1, but decided to not use counter as it takes time
                f.close()
            return len(self.hash_table)

    def add_word(self, word: str) -> None:
        """
		Adds the given word to the hash table with INTEGER(1) as the associated data
		:complexity: O(1), it only deals with adding an element, which is O(1), and conversion to lowercase and error check
		:raises Exception: when word is an empty string
		"""
        if not word:  # raises exception for empty word
            raise Exception("A word cannot be empty")
        word = word.lower()
        self.hash_table.__setitem__(word, self.INTEGER)

    def find_word(self, word: str) -> bool:
        """
		Returns boolean True if the word is in the hash table and False otherwise
		:complexity: O(1). Although it might look as a linear search, in this hash table it simply checks whether
		a key returns associated data or not - one of the benefits of this data structure.

		I am not supposed to raise exception, so changing the raise Exception to return false
		"""
        if not word:
            return False
        # raise Exception("A word cannot be empty")
        word = word.lower()  # raises exception for empty word, and converts to lowercase
        return self.hash_table.__contains__(word)

    def delete_word(self, word: str) -> None:
        """
		Deletes the given word from the hash table
		I am referring to __delitem__ from hash_table, and since most execution of delete_word lies there,
		the complexity is similar to that. Since convertion to lowercase and exception checks are O(1), they are insignificant
        :complexity best: O(K) finds the position straight away and doesn't have to rehash
                          where K is the size of the key
        :complexity worst: O(K + N) when it has to rehash all items in the hash table
                          where N is the table size
		By Constraints and assumptions:
		Exception must not be raised, so I am using return None instead
		"""
        if not word:
            return None
        # raise Exception("A word cannot be empty")
        """
		# I must make sure it does not raise KeyError when the key doesn't exist
		if not self.find_word(word):
			return None # Do nothing if the key doesn't exist
		I was thinking of adding this part, however, it was not necessary after referring to test cases
		"""
        word = word.lower()
        self.hash_table.__delitem__(word)


def process_option(dictionary: Dictionary, method_name: str) -> None:
    """ Helper code for processing menu options."""
    if method_name == 'read_file':
        filename = input('Enter filename: ')
        try:
            dictionary.load_dictionary(filename)
            print('Successfully read file')
        except FileNotFoundError as e:
            print(e)
    else:
        word = input('Enter word: ')
        if method_name == 'add_word':
            dictionary.add_word(word)
            try:
                dictionary.add_word(word)
                print('[{}] {}'.format(word, 'Successfully added'))
            except IndexError as e:
                print('[{}] {}'.format(word, e))
        elif method_name == 'find_word':
            if dictionary.find_word(word):
                print('[{}] {}'.format(word, 'Found in dictionary'))
            else:
                print('[{}] {}'.format(word, 'Not found in dictionary'))
        elif method_name == 'delete_word':
            try:
                dictionary.delete_word(word)
                print('[{}] {}'.format(word, 'Deleted from dictionary'))
            except KeyError:
                print('[{}] {}'.format(word, 'Not found in dictionary'))


def menu(dictionary: Dictionary):
    """ Wrapper for using the dictionary. """
    option = None
    menu_options = {'read_file': 'Read File',
                    'add_word': 'Add Word',
                    'find_word': 'Find Word',
                    'delete_word': 'Delete Word',
                    'exit': 'Exit'}

    exit_option = list(menu_options.keys()).index('exit') + 1

    while option != exit_option:
        print('---------------------')
        opt = 1
        for menu_option in menu_options.values():
            print('{}. {}'.format(opt, menu_option))
            opt += 1
        print('---------------------')
        try:
            option = int(input("Enter option: "))
            if option < 1 or option > exit_option:
                raise ValueError('Option must be between 1 and ' + str(exit_option))
        except ValueError as e:
            print('[{}] {}'.format('menu', e))
        else:
            if option != exit_option:
                process_option(dictionary, list(menu_options.keys())[option - 1])
    print("---------------------")


if __name__ == '__main__':
    """
    statistics = Statistics()
    statistics.table_load_statistics(3)

    dictionary = Dictionary(31, 250727)
    menu(dictionary)
	"""
    # I will export printed data to csv file
    execution = Statistics()
    execution.table_load_statistics(10)

