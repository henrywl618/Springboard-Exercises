"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    """ Returns random words from a given text file.

    >>> words = WordFinder('words.txt')
    235886 words read.

    >>> isinstance(words.create_list('words.txt'),list)
    True

    >>> len(words.words_list)
    235886

    >>> words.random() in words.words_list
    True
    """
    
    def __init__(self,file_dir):
        "Makes a list of words from a given text file and can return a random word."
        self.words_list = self.create_list(file_dir)
        self.print_wordsread()
    
    def create_list(self,file_dir):
        "Reads the given text file and parses each line as elements in a list"
        text_file = open(file_dir,'r')
        words_list = [line.strip() for line in text_file]
        text_file.close()
        return words_list

    def print_wordsread(self):
        "Prints the total number of words read from the text file."
        print(f'{len(self.words_list)} words read.')
    
    def random(self):
        "Returns a random word in the words list"
        return choice(self.words_list)

class SpecialWordFinder(WordFinder):

    def __init__(self,file_dir):
        "Makes a list of words from a given text file and can return a random word. Excludes comments and empty lines"
        super().__init__(file_dir)

    def create_list(self,file_dir):
        "Reads the given text file and parses each line as elements in a list. Removes comments and empty lines."
        text_file = open(file_dir,'r')
        words_list = [line.strip() for line in text_file if '#' not in line and line.strip() != '']
        text_file.close()
        return words_list


