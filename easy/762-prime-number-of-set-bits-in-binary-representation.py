import unittest
import math

data = ((6, 10, 4), (10, 15, 5))


def is_prime(n: int) -> bool:
    if n == 1:
        return False

    max_div = int(math.sqrt(n) + 1)

    for d in range(2, max_div):
        if n % d == 0:
            return False
    return True


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        result = 0
        for n in range(left, right + 1):
            set_bits_count = f"{n:b}".count("1")
            if is_prime(set_bits_count):
                result += 1
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for left, right, expected in data:
            self.assertEqual(expected, s.countPrimeSetBits(left, right), expected)


if __name__ == "__main__":
    unittest.main()
