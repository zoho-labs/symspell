from typing import List

class SymspellPy():
    """ SymspellPy class 
    SymspellPy is used for loading dictionaries, looking up words & sentences and word_segmentation.
    """
    @staticmethod
    def __init__(self, max_distance:int = 2, prefix_length:int = 7, count_threshold:int = 1, algorithm:str = 'DAMERAU') -> SymspellPy:
        """ Instantiate a new SymspellPy Class with given options. 
        Args:
            max_distance: int:
                Maximum Edit Distance
            prefix: str:
                The length of word prefixes used for spell checking.
            count_threshold: int:
                The minimum frequency count for dictionary words to be considered correct spellings
        """
        pass

    def load_dictionary(self, file:str, term_index:int, count_index:int, seperator:str) -> bool:

        """ Load single dictionary entry from word/frequency count pair.
        Args:
            file:str:
                Path of dictionary file
            term_index:int, 
                The Column Position of the word
            count_index:int,
                The Column Position of the frequency_count
            Seperator:str,
                Seperator between word and frequency_count
        """
        pass

    def load_bigram_dictionary(self, file:str, term_index:int, count_index:int, seperator:str) -> bool:

        """ Load multiple bigram entries from a file of bigram/frequency count pairs.
        Args:
            file:str:
                Path of dictionary file
            term_index:int, 
                The Column Position of the word
            count_index:int,
                The Column Position of the frequency_count
            Seperator:str,
                Seperator between word and frequency_count
        """
        pass

    def lookup(self, input:str, verbosity:int, max_edit_distance:int = 2) -> List[PySuggestion]:

        """ Find suggested spellings for a given input word, using the maximum
            edit distance specified during construction of the SymSpell dictionary.
        
        Args:
            input:str:
                The word beigng spellchecked
            verbosity: int:
                The value controlling the quantity/closeness of the returned suggestions.
           max_edit_distance: int:
                The maximum edit distance between input and suggested words.
        
        """
        pass

    def lookup_compound(self, input:str, max_edit_distance:int = 2) -> List[PySuggestion]:
        """
        Find suggested spellings for a given input sentence, using the maximum
        edit distance specified during construction of the SymSpell dictionary.
        
        # Args
        input:str
            The sentence being spell checked.
        max_edit_distance:int
            The maximum edit distance between input and suggested words.
        """
        pass
    
    def word_segmentation(self, input:str, max_edit_distance: int = 2) -> PyComposition:
        """
        Divides a string into words by inserting missing spaces at the appropriate positions

        # Args
        input:str
            The word being segmented
        max_edit_distance:int
            The maximum edit distance betweem input and suggested words.
        """
        pass