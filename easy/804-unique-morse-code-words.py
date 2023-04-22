import unittest
from typing import List


data = ((["gin", "zen", "gig", "msg"], 2), (["a"], 1))


class Solution:
    def __get_word_code(self, word: str) -> str:
        chars_codes = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        result = []
        for char in word.lower():
            index = ord(char) - 97
            result.append(chars_codes[index])
        return "".join(result)

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        transformations = set()
        for word in words:
            word_code = self.__get_word_code(word)
            transformations.add(word_code)
        return len(transformations)


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.uniqueMorseRepresentations(input_data), expected)


if __name__ == "__main__":
    unittest.main()
