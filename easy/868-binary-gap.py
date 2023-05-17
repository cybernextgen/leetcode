import unittest

data = ((22, 2), (8, 0), (5, 2))


class Solution:
    def binaryGap(self, n: int) -> int:
        binary_repr = f"{n:b}"
        result = 0
        current_distance = 0
        for index, char in enumerate(binary_repr):
            if char != "1":
                current_distance += 1
                continue
            if current_distance > result:
                result = current_distance
            current_distance = 1
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.binaryGap(input_data), expected)


if __name__ == "__main__":
    unittest.main()
