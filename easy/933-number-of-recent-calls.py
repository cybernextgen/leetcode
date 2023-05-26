import unittest
import collections

data = ()


class RecentCounter:
    def __init__(self):
        self.calls_list = collections.deque()
        self.interval = 3000

    def ping(self, t: int) -> int:
        self.calls_list.append(t)
        limit = t - 3000
        while self.calls_list[0] < limit:
            self.calls_list.popleft()
        return len(self.calls_list)


# class TestCase(unittest.TestCase):
#     def test_solution(self):
#         s = Solution()

#         for input_data, expected in data:
#             self.assertEqual(s.numUniqueEmails(input_data), expected)

if __name__ == "__main__":
    unittest.main()
