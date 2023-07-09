import unittest
from typing import List

data = (
    (["Hello", "Alaska", "Dad", "Peace"], ["Alaska", "Dad"]),
    (["omk"], []),
    (["adsdf", "sfd"], ["adsdf", "sfd"]),
)


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        result = []
        for word in words:
            letters = set(word.lower())
            for row in rows:
                if row.issuperset(letters):
                    result.append(word)
                    break
        return result


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.findWords(input_data), expected)


if __name__ == "__main__":
    unittest.main()
