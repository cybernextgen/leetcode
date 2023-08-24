import unittest

data = (
    ("i love eating burger", "burg", 4),
    ("this problem is an easy problem", "pro", 2),
    ("i am tired", "you", -1),
)


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for index, word in enumerate(sentence.split()):
            if word.startswith(searchWord):
                return index + 1
        return -1


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, prefix, expected in data:
            self.assertEqual(expected, s.isPrefixOfWord(input_data, prefix))


if __name__ == "__main__":
    unittest.main()
