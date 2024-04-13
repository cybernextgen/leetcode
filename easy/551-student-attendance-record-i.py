import unittest

data = (("PPALLP", True), ("PPALLL", False), ("LALL", True))


class Solution:
    def checkRecord(self, s: str) -> bool:
        absent_count = 0
        late_count = 0
        for ch in s:
            if ch == "L":
                late_count += 1
            else:
                if ch == "A":
                    absent_count += 1
                late_count = 0

            if absent_count >= 2 or late_count >= 3:
                return False
        return True


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.checkRecord(input_data), expected)


if __name__ == "__main__":
    unittest.main()
