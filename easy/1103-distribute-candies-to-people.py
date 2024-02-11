import unittest
from typing import List

data = (
    (7, 4, [1, 2, 3, 1]),
    (10, 3, [5, 2, 3]),
)


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        iteration = 0
        index = 0
        while candies > 0:
            required_candies = min(num_people * iteration + index + 1, candies)
            candies -= required_candies
            result[index] += required_candies
            index += 1

            if index == num_people:
                iteration += 1
                index = 0

        return result


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for candies, num_people, expected in data:
            self.assertListEqual(s.distributeCandies(candies, num_people), expected)


if __name__ == "__main__":
    unittest.main()
