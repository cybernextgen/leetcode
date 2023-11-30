import unittest

data = ((15, 5, 20), (13, 11, 0))


class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for arrivalTime, delayedTime, expected in data:
            self.assertEqual(
                expected, s.findDelayedArrivalTime(arrivalTime, delayedTime)
            )


if __name__ == "__main__":
    unittest.main()
