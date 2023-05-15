import unittest

data = (("ab#c", "ad#c", True), ("ab##", "c#d#", True), ("a#c", "b", False))


class Solution:
    def __handle_backspace(self, s: str) -> str:
        result = ""
        skip_chars = 0
        for char in reversed(s):
            if char == "#":
                skip_chars += 1
                continue
            if skip_chars:
                skip_chars -= 1
                continue
            result = char + result
        return result

    def backspaceCompare(self, s: str, t: str) -> bool:
        result_s = self.__handle_backspace(s)
        result_t = self.__handle_backspace(t)
        return result_s == result_t


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for str1, str2, expected in data:
            self.assertEqual(s.backspaceCompare(str1, str2), expected)


if __name__ == "__main__":
    unittest.main()
