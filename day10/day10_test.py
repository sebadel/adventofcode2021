#!/usr/bin/env python

import unittest
import day10


class TestLine(unittest.TestCase):
    def test_validity(self):
        self.assertEqual(day10._first_illegal_character('{}[<>[]}>{[]{[(<()>'), '}')
        self.assertEqual(day10._first_illegal_character('[[<[([]))<([[{}[[()]]]'), ')')


if __name__ == '__main__':
    unittest.main()