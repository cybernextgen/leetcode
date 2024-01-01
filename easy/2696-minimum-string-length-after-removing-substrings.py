import unittest
import re

data = (("ABFCACDB", 2), ("ACBBD", 5))


class Solution2:
    def minLength(self, s: str) -> int:
        index = 0
        while len(s) > 0 and index < len(s) - 1:
            current_substring = s[index : index + 2]
            if current_substring == "AB" or current_substring == "CD":
                s = f"{s[0:index]}{s[index + 2 : len(s)]}"
                if index:
                    index -= 1
            else:
                index += 1
        return len(s)


class Solution1:
    def minLength(self, s: str) -> int:
        while True:
            new_s = re.sub(r"AB|CD|AABB|ACDB|CABD|CCDD", "", s)
            if s == new_s:
                return len(s)
            else:
                s = new_s


class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for ch in s:
            if stack and f"{stack[-1]}{ch}" in ("AB", "CD"):
                stack.pop()
            else:
                stack.append(ch)
        return len(stack)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.minLength(input_data))


if __name__ == "__main__":
    unittest.main()
