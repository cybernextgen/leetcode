import unittest
from typing import List
import itertools

data = (
    ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    ("", []),
    ("2", ["a", "b", "c"]),
)


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        buttons_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        return [
            "".join(c) for c in itertools.product(*[buttons_map[d] for d in digits])
        ]


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.letterCombinations(input_data))


if __name__ == "__main__":
    unittest.main()
