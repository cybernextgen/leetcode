import unittest

data = (("cc", 2), ("j", 1), ("leetcode", 2), ("abbcccddddeeeeedcba", 5))


class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 1:
            return 1

        max_power = 0
        current_power = 1
        prev_char = s[0]
        for current_char in s[1:]:
            if current_char != prev_char:
                max_power = max(max_power, current_power)
                prev_char = current_char
                current_power = 1
            else:
                current_power += 1
        
        max_power = max(max_power, current_power)

        return max_power


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.maxPower(input_data))


if __name__ == "__main__":
    unittest.main()
