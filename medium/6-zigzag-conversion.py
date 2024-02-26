import unittest

data = (
    ("ABC", 1, "ABC"),
    ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
    ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
    ("A", 1, "A"),
)


class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s
        
        counter = 0
        delta = 1
        result = [list() for _ in range(num_rows)]
        for ch in s:
            result[counter].append(ch)
            counter += delta
            if counter == num_rows:
                counter -= 2
                delta = -1
            elif counter < 0:
                counter = 1
                delta = 1
        return "".join("".join(l) for l in result)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_str, num_rows, expected in data:
            self.assertEqual(s.convert(input_str, num_rows), expected)


if __name__ == "__main__":
    unittest.main()
