import unittest

data = (("abc", "pqr", "apbqcr"), ("ab", "pqrs", "apbqrs"), ("abcd", "pq", "apbqcd"))


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1:
            return word2
        if not word2:
            return word1
        word1_len = len(word1)
        word2_len = len(word2)
        min_len = word1_len
        if word1_len != word2_len:
            if word1_len > word2_len:
                min_len = word2_len
            else:
                min_len = word1_len
        res = ""
        for index in range(min_len):
            res = f"{res}{word1[index]}{word2[index]}"
        return f"{res}{word1[min_len:]}{word2[min_len:]}"


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for word1, word2, expected in data:
            self.assertEqual(s.mergeAlternately(word1, word2), expected)


if __name__ == "__main__":
    unittest.main()
