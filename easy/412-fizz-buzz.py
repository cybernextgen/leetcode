import unittest
from typing import List

data = (
    (3, ["1", "2", "Fizz"]),
    (5, ["1", "2", "Fizz", "4", "Buzz"]),
    (
        15,
        [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz",
        ],
    ),
)


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for current_number in range(1, n + 1):
            s = ""
            if not current_number % 3:
                s += "Fizz"
            if not current_number % 5:
                s += "Buzz"
            if not s:
                s = str(current_number)
            result.append(s)
        return result


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, result in data:
            self.assertListEqual(s.fizzBuzz(input_data), result)


if __name__ == "__main__":
    unittest.main()
