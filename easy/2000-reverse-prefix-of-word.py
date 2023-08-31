import unittest

data = (("abcdefd", "d", "dcbaefd"), ("xyxzxe", "z", "zxyxxe"), ("abcd", "z", "abcd"))


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)
        if index >= 0:
            return word[index::-1] + word[index + 1 :]
        return word


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for word, ch, expected in data:
            self.assertEqual(expected, s.reversePrefix(word, ch))


if __name__ == "__main__":
    unittest.main()
