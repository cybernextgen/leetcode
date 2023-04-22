import unittest

data = (
    # ("abcde", "cdeab", True),
    # ("abcde", "abced", False),
    ("gcmbf", "fgcmb", True),
)


class Solution:
    def __shift(self, str) -> str:
        if len(str) <= 1:
            return str
        return f"{str[1:]}{str[0]}"

    def rotateString(self, s: str, goal: str) -> bool:
        if not s and goal or (s and not goal):
            return False

        if not s and not goal:
            return True

        shifts_remain = len(s) - 1
        while shifts_remain >= 0:
            if s == goal:
                return True
            s = self.__shift(s)
            shifts_remain -= 1

        return False


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for str1, str2, expected in data:
            self.assertEqual(s.rotateString(str1, str2), expected)


if __name__ == "__main__":
    unittest.main()
