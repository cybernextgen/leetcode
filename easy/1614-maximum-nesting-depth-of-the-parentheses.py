import unittest

data = (("(1+(2*3)+((8)/4))+1", 3), ("(1)+((2))+(((3)))", 3))


class Solution:
    def maxDepth(self, s: str) -> int:
        current_depth = 0
        max_depth = 0
        for ch in s:
            if ch == "(":
                current_depth += 1
            if ch == ")":
                current_depth -= 1
            if current_depth > max_depth:
                max_depth = current_depth
        return max_depth


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.maxDepth(input_data))


if __name__ == "__main__":
    unittest.main()
