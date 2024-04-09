import unittest
from typing import List

data = (([2, 3, 2], 2, 6), ([5, 1, 1, 1], 0, 8))


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        result = 0
        target_ticket_count = tickets[k]
        for index, ticket_count in enumerate(tickets):
            result += (
                min(ticket_count, target_ticket_count)
                if index <= k
                else min(ticket_count, target_ticket_count - 1)
            )
        return result        


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for tickets, k, expected in data:
            self.assertEqual(s.timeRequiredToBuy(tickets, k), expected)


if __name__ == "__main__":
    unittest.main()
