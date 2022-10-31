from hash_table import LinearProbeHashTable
from dictionary import Dictionary
from list_adt import ArrayList
from enum import Enum
from string import punctuation
import sys

class Rarity(Enum):
    COMMON = 0
    UNCOMMON = 1
    RARE = 2
    MISSPELT = 3

class Frequency:
    """
    A Frequency class, which defines multiple useful methods
    """
    DEFAULT_ENCODING = 'utf-8'
    DEFAULT_TABLE_SIZE = 250727
    DEFAULT_HASH_BASE = 31
    DEFAULT_TIME = 4
    MAX_CAPACITY = 2599999
    RECURSION_LIMIT = 2000

    def __init__(self) -> None:
        """
        A constructor which initialises a new Hash Table, as well as an instance of Dictionary which
        was read in english_large.txt.
        :parameters and output: None
        :complexity: O(N) where N is the number of lines in english_large.txt
        """
        self.hash_table = LinearProbeHashTable()  # create new hash table
        self.dictionary = Dictionary(self.DEFAULT_HASH_BASE, self.DEFAULT_TABLE_SIZE)  # new instance of dictionary
        self.dictionary.load_dictionary("english_large.txt", self.DEFAULT_TIME)
        self.max_word = ("", 0)  # set tuple max_word to default value

    def add_file(self, filename: str) -> None:
        """
        This reads each word from filename into the hash table, 
        and its data is the number of times the word has been read into the hash table.
        parameter: filename is a string representing the filename
        returns: None
        :complexity: O(N) where N is the number of words stripped in the given file
        """
        with open(filename, 'r', encoding=self.DEFAULT_ENCODING) as file:
            # referred to:
            # https://stackoverflow.com/questions/37221307/how-do-i-strip-all-leading-and-trailing-punctuation-in-python
            # for strippling leading and trailing punctuation
            line = file.readline()
            while line:  # for each line
                line = line.strip()
                for word in line.split():  # for each word in line
                    word = word.lower()  # convert to lowercase
                    word = word.strip(punctuation)  # strip punctuation
                    if not self.dictionary.hash_table.__contains__(word):  # if word not in dictionary, go on to next iteration
                        continue
                    if not self.hash_table.__contains__(word):  # if first time seeing, set it as data 1
                        self.hash_table[word] = 1
                    else:  # If the word is input previously already,
                        frequency = self.hash_table[word]  # obtain frequency, data
                        frequency += 1 
                        self.hash_table[word] = frequency  # set incremented frequency
                        if self.max_word[1] < frequency:
                            self.max_word = (word, frequency)  # update max_word if necessary
                line = file.readline()
    
    def rarity(self, word: str) -> Rarity:
        """
        Given a word, it returns its rarity score as an enumerated value, it takes in word: string as a paramter
        <del>:complexity: O(N) where N is the length of self.hash_table. Because the dominant
        factor is the part where it searches through __contains__(word), whose complexity is N.</del>
        :complexity: O(1). I have looked at the complexity in the hash_table.py, and its structure 
        leads to O(1), which is the benefit of using hash.
        """
        if not self.hash_table.__contains__(word):
            return Rarity.MISSPELT  # output MISSPELT enum if not found in hash
        frequency = self.hash_table[word]
        maximum = self.max_word[1]
        if frequency >= maximum / 100:
            return Rarity.COMMON
        elif frequency < maximum / 1000:
            return Rarity.RARE
        elif frequency < maximum / 100 and frequency >= maximum / 1000:
            return Rarity.UNCOMMON
            # for these 3, I followed conditions in the Background

    def ranking(self) -> ArrayList[tuple]:
        sys.setrecursionlimit(Frequency.RECURSION_LIMIT)
        freq_array = ArrayList(self.MAX_CAPACITY)
        for item in self.hash_table.table:
            if item is not None:
                key, value = item
                freq_array.append((key, value))
        return quick_sort(freq_array)


def quick_sort(array: ArrayList[tuple]) -> ArrayList[tuple]:
    if len(array) <= 1:
        return array
    else:
        greater = ArrayList(Frequency.MAX_CAPACITY)
        equal = ArrayList(Frequency.MAX_CAPACITY)
        less = ArrayList(Frequency.MAX_CAPACITY)
        pivot = array.__getitem__(0)
        print(pivot)

        for i in range(len(array)):
            key, value = array.__getitem__(i)
            if pivot[1] < value:
                less.append((key, value))
            elif pivot[1] > value:
                greater.append((key, value))
            else:
                equal.append((key, value))
        ret_array = ArrayList(Frequency.MAX_CAPACITY)
        greater = quick_sort(greater)
        less = quick_sort(less)
        for item in greater:
            ret_array.append(item)
        for item in equal:
            ret_array.append(item)
        for item in less:
            ret_array.append(item)
        return ret_array

def frequency_analysis() -> None:
    """
    This creates an instance of class Frequency, adds 215-0.txt to it and generates the ranking list
    """
    prompt = int(input("Please enter the number of rankings to show: "))
    freq = Frequency()
    freq.add_file("215-0.txt")
    ranking = freq.ranking()
    print("Here are the results, from higher ranking: \n")
    for x in range(prompt):
        rank = x + 1
        word, frequency = ranking.__getitem__(x)
        rarity = freq.rarity(word)
        print("Ranking: {}, word: {}, frequency: {}, rarity: {}\n".format(rank, word, frequency, rarity))


if __name__ == '__main__':
    frequency_analysis()
