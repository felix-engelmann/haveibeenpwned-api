import uuid
import string
import unittest
from random import choice
import os
from . import app, Pwned


def get_random_string(length):
    return "".join(
        choice(string.ascii_letters) for _ in range(length)
    )


class PwnedTestCase(unittest.TestCase):

    def setUp(self):
        testfile = os.path.join(os.path.dirname(__file__), "first10k.txt")
        self.pwnd = Pwned(testfile)

    def test_lookup(self):
        ret = self.pwnd.lookup("00001")

        self.assertEqual(ret[0][:35],'0005DE2A9668A41F6A508AFB6A6FC4A5610')
        self.assertEqual(ret[-1][:35],'FDE50C816E371829CFBD439F00ED2FE0891')
        self.assertEqual(len(ret), 571)

    def test_lookup_first(self):
        ret = self.pwnd.lookup("00000")

        self.assertEqual(ret[0][:35],'0005AD76BD555C1D6D771DE417A4B87E4B4')
        self.assertEqual(ret[-1][:35],'FFF5C4A486B528DD84D1F1D3F41A06E9256')
        self.assertEqual(len(ret), 632)

    def test_lookup_varlen(self):
        ret = self.pwnd.lookup("0000C39")

        self.assertEqual(ret, ['0969D683FF1FE58626C8FEF9DCB0F1418:3',
                               '62B6D813BACABDA9B6A054F0718E6EB41:6',
                               'D0103D6A7F36AD71FE57222568228F70B:1',
                               'F6F9DD8DDB9A0D374B623A4E34658D396:1'])