import unittest
from typing import List

data = (
    (["5", "2", "C", "D", "+"], 30),
    (["5", "-2", "4", "C", "D", "9", "+", "+"], 27),
    (["1", "C"], 0),
)


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.calPoints(input_data), input_data)


if __name__ == "__main__":
    unittest.main()
