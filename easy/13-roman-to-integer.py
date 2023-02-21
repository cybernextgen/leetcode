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
import itertools
import re

data = (("III", 3), ("LVIII", 58), ("MCMXCIV", 1994))


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_signs_mapping = {
            "I": 1,
            "IV": 3,
            "V": 5,
            "IX": 8,
            "X": 10,
            "XL": 30,
            "L": 50,
            "XC": 80,
            "C": 100,
            "CD": 300,
            "D": 500,
            "CM": 800,
            "M": 1000,
        }
        prev_char = ""
        result = 0
        for char in s:
            intVal = roman_signs_mapping.get(prev_char + char, 0)
            if not intVal:
                intVal = roman_signs_mapping.get(char, 0)
            result += intVal
            prev_char = char
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, result in data:
            self.assertEqual(result, s.romanToInt(input_data))


if __name__ == "__main__":
    unittest.main()
