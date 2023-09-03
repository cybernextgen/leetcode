import unittest
from typing import List

data = (
    (["--X", "X++", "X++"], 1),
    (["++X", "++X", "X++"], 3),
    (["X++", "++X", "--X", "X--"], 0),
)


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for op in operations:
            if op.find("++") >= 0:
                result += 1
                continue
            result -= 1
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for operations, expected in data:
            self.assertEqual(expected, s.finalValueAfterOperations(operations))


if __name__ == "__main__":
    unittest.main()
