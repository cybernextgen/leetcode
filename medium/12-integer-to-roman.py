"""
I 1
V 5
X 10
L 50
C 100
D 500
M 1000

I can be placed before V (5) and X (10) to make 4 and 9
X can be placed before L (50) and C (100) to make 40 and 90
C can be placed before D (500) and M (1000) to make 400 and 900
"""
import unittest

data = ((3, "III"), (58, "LVIII"), (1994, "MCMXCIV"))


class Solution:
    def intToRoman(self, num: int) -> str:
        divisors = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        roman_signs = [
            "I",
            "IV",
            "V",
            "IX",
            "X",
            "XL",
            "L",
            "XC",
            "C",
            "CD",
            "D",
            "CM",
            "M",
        ]
        result = ""
        current_divisor_pos = len(divisors)
        while num > 0:
            current_divisor_pos -= 1
            while True:
                current_divisor = divisors[current_divisor_pos]
                if current_divisor > num:
                    current_divisor_pos -= 1
                    continue
                break
            count, num = divmod(num, current_divisor)
            result += roman_signs[current_divisor_pos] * count
        return result


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, result in data:
            self.assertEqual(s.intToRoman(input_data), result)


if __name__ == "__main__":
    unittest.main()
