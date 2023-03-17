import unittest

data = ((43261596, 964176192), (4294967293, 3221225471))


class Solution:
    def reverseBits(self, n: int) -> int:
        return int(f"{n:>032b}"[::-1], 2)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.reverseBits(input_data))


if __name__ == "__main__":
    unittest.main()
