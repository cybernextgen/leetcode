import unittest

data = (("011101", 5), ("00111", 5), ("1111", 3), ("00", 1))


class Solution:
    def maxScore(self, s: str) -> int:
        last_index = len(s) - 1
        left_score = 1 if s[0] == "0" else 0
        right_score = s[1:].count("1")
        max_score = left_score + right_score

        for ch in s[1:last_index]:
            if ch == "0":
                left_score += 1
            else:
                right_score -= 1
            if (m := left_score + right_score) > max_score:
                max_score = m
        return max_score


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.maxScore(input_data), expected)


if __name__ == "__main__":
    unittest.main()
