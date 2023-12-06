import unittest

data = ((1, 100, 9), (1200, 1230, 4))


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = 0
        for num in range(low, high + 1):
            num_as_str = str(num)
            num_len = len(num_as_str)

            if num_len % 2 != 0:
                continue

            sum1 = 0
            sum2 = 0
            index_left = 0
            index_right = num_len - 1
            while index_left < index_right:
                sum1 += int(num_as_str[index_left])
                sum2 += int(num_as_str[index_right])
                index_left += 1
                index_right -= 1
                
            if sum1 == sum2:
                result += 1

        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for low, high, expected in data:
            self.assertEqual(expected, s.countSymmetricIntegers(low, high))


if __name__ == "__main__":
    unittest.main()
