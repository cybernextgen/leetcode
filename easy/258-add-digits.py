import unittest

data = ((38, 2), (11, 2))


class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num

        while num > 9:
            num = self.__get_digits_sum(num)
        return num

    def __get_digits_sum(self, num: int) -> int:
        d, result = divmod(num, 10)
        if d > 9:
            result += self.addDigits(d)
            return result
        result += d
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, result in data:
            self.assertEqual(result, s.addDigits(input_data))


if __name__ == "__main__":
    unittest.main()
