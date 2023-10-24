import unittest
from typing import List

data = ((17, [2, 0]), (2, [0, 1]))


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0
        odd = 0
        for index, bit in enumerate(reversed(f"{n:b}")):
            if bit == "1":
                if not index % 2:
                    even += 1
                else:
                    odd += 1
        return [even, odd]


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.evenOddBit(input_data))


if __name__ == "__main__":
    unittest.main()
