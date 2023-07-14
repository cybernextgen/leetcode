import unittest
from typing import List

data = (
    ([5, 4, 3, 2, 1], ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]),
    ([10, 3, 8, 9, 4], ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]),
)


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        result_table = {}

        for index, result in enumerate(sorted(score, reverse=True)):
            if not index:
                result_table[result] = "Gold Medal"
            elif index == 1:
                result_table[result] = "Silver Medal"
            elif index == 2:
                result_table[result] = "Bronze Medal"
            else:
                result_table[result] = f"{index + 1}"

        for index, result in enumerate(score):
            score[index] = result_table[result]

        return score  # type: ignore


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, expected in data:
            self.assertListEqual(s.findRelativeRanks(input_data), expected)


if __name__ == "__main__":
    unittest.main()
