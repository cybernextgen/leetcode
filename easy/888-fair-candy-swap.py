import unittest
from typing import List


data = (([1, 1], [2, 2], [1, 2]), ([1, 2], [2, 3], [1, 2]), ([2], [1, 3], [2, 3]))


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_set = set(aliceSizes)
        bob_set = set(bobSizes)
        delta = (sum(bobSizes) - sum(aliceSizes)) / 2
        for s in alice_set:
            need = delta + s
            if need in bob_set:
                return [s, need]
        return []


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for aliceSizes, bobSizes, expected in data:
            self.assertEqual(s.fairCandySwap(aliceSizes, bobSizes), expected)


if __name__ == "__main__":
    unittest.main()
