import uuid
import string
import unittest
from random import choice
import os
from . import app, Pwnd


def get_random_string(length):
    return "".join(
        choice(string.ascii_letters) for _ in range(length)
    )


class PwnedTestCase(unittest.TestCase):

    def test_init(self):
        testfile=os.path.join(os.path.dirname(__file__),"first10k.txt")
        a=Pwnd(testfile)
