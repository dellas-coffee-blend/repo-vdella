# coding=utf-8
import unittest
from src.people.giulia.strings import *


class TestStrings(unittest.TestCase):

    def test_inverted_text(self):
        self.assertFalse(inverted_text("Meu nome é Julia."), "Meu nome é Julia.")
        movie = "Like a movie, you are the leading role, just like me."
        self.assertTrue(inverted_text(movie), movie[::-1])

    def test_palindrome(self):
        self.assertFalse(palindrome("Bees"))
        self.assertTrue(palindrome("ababa"))
        self.assertTrue(palindrome("uau"))
        self.assertFalse(palindrome("Tin man"))
