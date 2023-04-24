import unittest

data = (("aA", "aAAbbbb", 3), ("z", "ZZ", 0))


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        jewels_count = 0
        for s in stones:
            if s in jewels_set:
                jewels_count += 1
        return jewels_count


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for jewels, stones, expected in data:
            self.assertEqual(s.numJewelsInStones(jewels, stones), expected)


if __name__ == "__main__":
    unittest.main()
