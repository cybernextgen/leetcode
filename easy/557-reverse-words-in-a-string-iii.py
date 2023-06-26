import unittest

data = (
    ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
    ("God Ding", "doG gniD"),
)


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(["".join(reversed(w)) for w in s.split()])


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.reverseWords(input_data), expected)


if __name__ == "__main__":
    unittest.main()
