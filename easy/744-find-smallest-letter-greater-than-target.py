import unittest
from typing import List
import bisect

data = (
    (["c", "f", "j"], "a", "c"),
    (["c", "f", "j"], "c", "f"),
    (["x", "x", "y", "y"], "z", "x"),
)


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1] <= target:
            return letters[0]
        index = bisect.bisect_right(letters, target)
        return letters[index]


class Solution2:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1] <= target:
            return letters[0]
        for ch in letters:
            if ch > target:
                return ch
        return letters[0]


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for letters, target, expected in data:
            self.assertEqual(s.nextGreatestLetter(letters, target), expected)


if __name__ == "__main__":
    unittest.main()
