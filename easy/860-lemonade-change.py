import unittest
from typing import List

data = (
    ([5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5], True),
    ([5, 5, 5, 10, 20], True),
    ([5, 5, 10, 10, 20], False),
)


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = {5: 0, 10: 0, 20: 0}
        for b in bills:
            change_required = b - 5
            if change_required:
                if change_required > 5 and cash[10] > 0:
                    cash[10] -= 1
                    change_required -= 10
                while change_required > 0 and cash[5] > 0:
                    cash[5] -= 1
                    change_required -= 5
                if change_required > 0:
                    return False
            cash[b] += 1
        return True


class Solution1:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        for b in bills:
            if b == 5:
                fives += 1
            elif b == 10:
                tens += 1
                fives -= 1
            elif tens > 0:
                tens -= 1
                fives -= 1
            else:
                fives -= 3
            if fives < 0:
                return False
        return True


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution1()

        for bills, expected in data:
            self.assertEqual(s.lemonadeChange(bills), expected)


if __name__ == "__main__":
    unittest.main()
