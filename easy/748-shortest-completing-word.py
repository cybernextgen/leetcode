import unittest
from typing import List
import re
import collections

data = (
    ("1s3 456", ["looks", "pest", "stew", "show"], "pest"),
    ("1s3 PSt", ["step", "steps", "stripe", "stepple"], "steps"),
    ("1s3 456", ["looks", "pest", "stew", "show"], "pest"),
)


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        license_plate_letters = re.sub(r"\d|\s", "", licensePlate).lower()
        licence_plate_letters_counts = collections.Counter(license_plate_letters)

        min_len = None
        result = ""
        for word in words:
            word_counts = collections.Counter(word)
            if licence_plate_letters_counts - word_counts:
                continue

            len_word = len(word)
            if min_len and len_word >= min_len:
                continue

            min_len = len_word
            result = word

        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for licensePlate, words, expected in data:
            self.assertEqual(expected, s.shortestCompletingWord(licensePlate, words))


if __name__ == "__main__":
    unittest.main()
