import unittest
import time
from main import countWellFormedParenthesis

class TestPerformance(unittest.TestCase):
    def test_performance_n10(self):
        max_duration = 0.05
        start = time.time()
        countWellFormedParenthesis(6)
        end = time.time()
        duration = end - start
        self.assertLessEqual(duration, max_duration, f"Execution time exceeds limit: {duration:.6f} seconds")