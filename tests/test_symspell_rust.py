import os.path
import pickle
import sys
import unittest

import pytest
from symspell_rust import SymspellPy

class TestSymspellRust(unittest.TestCase):

    dictionary_path = "data/frequency_dictionary_en_82_765.txt"
    bigram_dict_path = "data/frequency_bigramdictionary_en_243_342.txt"
    
    def test_lookup(self):
        max_edit_distance = 2
        prefix_length = 7
        sym_spell = SymspellPy(max_edit_distance, prefix_length)
        sym_spell.load_dictionary(self.dictionary_path, 0, 1, " ")
        typo = "inspirede"
        correction = "inspired"
        results = sym_spell.lookup(typo,0,max_edit_distance)
        self.assertEqual(1, len(results))
        self.assertEqual(correction,results[0].term)
        self.assertEqual(1, results[0].distance)
        self.assertEqual(11531233,results[0].count)

    def test_lookup_compound(self):
        max_edit_distance = 2
        prefix_length = 7
        sym_spell = SymspellPy(max_edit_distance, prefix_length)
        sym_spell.load_dictionary(self.dictionary_path, 0, 1, " ")
        sym_spell.load_bigram_dictionary(self.bigram_dict_path, 0, 2, " ")

        typo = "whereis th elove"
        correction = "where is the love"
        results = sym_spell.lookup_compound(typo, max_edit_distance)
        self.assertEqual(1, len(results))
        self.assertEqual(correction, results[0].term)
        self.assertEqual(2, results[0].distance)
        self.assertEqual(12339616, results[0].count)

        typo = "the bigjest playrs"
        correction = "the biggest players"
        results = sym_spell.lookup_compound(typo, max_edit_distance)
        self.assertEqual(1, len(results))
        self.assertEqual(correction, results[0].term)
        self.assertEqual(2, results[0].distance)
        self.assertEqual(217252, results[0].count)

        typo = "Can yu readthis"
        correction = "can you read this"
        results = sym_spell.lookup_compound(typo, max_edit_distance)
        self.assertEqual(1, len(results))
        self.assertEqual(correction, results[0].term)
        self.assertEqual(3, results[0].distance)
        self.assertEqual(7457739, results[0].count)


    def test_word_segmentation(self):
        max_edit_distance = 0
        prefix_length = 7
        sym_spell = SymspellPy(max_edit_distance, prefix_length)
        sym_spell.load_dictionary(self.dictionary_path, 0, 1, " ")

        typo = "thequickbrownfoxjumpsoverthelazydog"
        correction = "the quick brown fox jumps over the lazy dog"
        result = sym_spell.word_segmentation(typo, max_edit_distance)
        self.assertEqual(correction, result.segmented_string)
        self.assertEqual(8, result.distance_sum)
        self.assertEqual(-34.49116897583008, result.prob_log_sum)

        typo = "itwasabrightcolddayinaprilandtheclockswerestrikingthirteen"
        correction = ("it was a bright cold day in april and the clocks "
                      "were striking thirteen")
        result = sym_spell.word_segmentation(typo, max_edit_distance)
        self.assertEqual(correction, result.segmented_string)
        self.assertEqual(13, result.distance_sum)
        self.assertEqual(-48.45243835449219, result.prob_log_sum)

        typo = ("itwasthebestoftimesitwastheworstoftimesitwastheageofwisdom"
                "itwastheageoffoolishness")
        correction = ("it was the best of times it was the worst of times "
                      "it was the age of wisdom it was the age of foolishness")
        result = sym_spell.word_segmentation(typo, max_edit_distance)
        self.assertEqual(correction, result.segmented_string)
        self.assertEqual(23, result.distance_sum)
        self.assertEqual(-70.51303100585938, result.prob_log_sum)

