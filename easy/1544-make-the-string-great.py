import unittest

data = (("leEeetcode", "leetcode"), ("abBAcC", ""))


class Solution:
    def makeGood(self, s: str) -> str:
        result = s
        pointer = 0
        while result and pointer < len(result) - 1:
            if abs(ord(result[pointer]) - ord(result[pointer + 1])) == 32:
                if pointer > 0:
                    result = result[:pointer] + result[pointer + 2 :]
                    pointer -= 1
                else:
                    result = result[pointer + 2 :]
            else:
                pointer += 1
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.makeGood(input_data), expected)


if __name__ == "__main__":
    unittest.main()
