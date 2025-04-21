import unittest
from main import countWellFormedParenthesis

class TestBracketCount(unittest.TestCase):

    def test_n1(self):
        self.assertEqual(countWellFormedParenthesis(1), 1)

    def test_n2(self):
        self.assertEqual(countWellFormedParenthesis(2), 2)

    def test_n3(self):
        self.assertEqual(countWellFormedParenthesis(3), 5)

    def test_n4(self):
        self.assertEqual(countWellFormedParenthesis(4), 14)

    def test_n5(self):
        self.assertEqual(countWellFormedParenthesis(5), 42)

    def test_n6(self):
        self.assertEqual(countWellFormedParenthesis(6), 132)

if __name__ == "__main__":
    unittest.main()
