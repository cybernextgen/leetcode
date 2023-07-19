import unittest

data = (
    # ("USA", True),
    # ("leetcode", True),
    # ("Google", True),
    # ("FlaG", False),
    ("usa", True),
)


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        all_capitals = all_not_capitals = only_first_capital = True
        is_first_char = True
        for char in word:
            is_capital = ord(char) < 97
            if not is_capital:
                all_capitals = False
            else:
                all_not_capitals = False

            if (is_first_char and not is_capital) or (not is_first_char and is_capital):
                only_first_capital = False

            if not (all_capitals or all_not_capitals or only_first_capital):
                return False

            is_first_char = False

        return True


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.detectCapitalUse(input_data), expected)


if __name__ == "__main__":
    unittest.main()
