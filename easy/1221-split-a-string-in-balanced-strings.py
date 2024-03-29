import unittest

data = (("RLRRLLRLRL", 4), ("RLRRRLLRLL", 2), ("LLLLRRRR", 1))


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        balance = 0
        for char in s:
            if char == "R":
                balance += 1
            else:
                balance -= 1
            if not balance:
                result += 1
                balance = 0
        return result


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()
        for input_data, result in data:
            self.assertEqual(s.balancedStringSplit(input_data), result)


if __name__ == "__main__":
    unittest.main()
