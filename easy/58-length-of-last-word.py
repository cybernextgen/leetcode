import unittest

data = (
    ("Hello World", 5),
    ("   fly me   to   the moon  ", 4),
    ("luffy is still joyboy", 6),
)


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().rsplit(maxsplit=1)
        if words:
            return len(words[-1])
        return 0


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, result in data:
            self.assertEqual(result, s.lengthOfLastWord(input_data))


if __name__ == "__main__":
    unittest.main()
