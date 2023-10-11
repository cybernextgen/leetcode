import unittest


data = (("51230100", "512301"), ("123", "123"))


class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.strip("0")


class Solution2:
    def removeTrailingZeros(self, num: str) -> str:
        if not num:
            return num

        left_index = 0
        right_index = len(num) - 1
        while True:
            strip_left = num[left_index] == "0"
            strip_right = num[right_index] == "0"

            if strip_left:
                left_index += 1

            if strip_right:
                right_index -= 1

            if not strip_left and not strip_right:
                break
        return num[left_index : right_index + 1]


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution2()

        for input_data, expected in data:
            self.assertEqual(expected, s.removeTrailingZeros(input_data))


if __name__ == "__main__":
    unittest.main()
