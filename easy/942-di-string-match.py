import unittest
import collections
from typing import List

data = (("IDID", [0, 4, 1, 3, 2]), ("III", [0, 1, 2, 3]), ("DDI", [3, 2, 0, 1]))


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        dq = collections.deque(range(0, len(s) + 1))
        result = []
        for ch in s:
            if ch == "I":
                result.append(dq.popleft())
            else:
                result.append(dq.pop())
        result.append(dq.pop())
        return result


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, expected in data:
            self.assertListEqual(s.diStringMatch(input_data), expected)


if __name__ == "__main__":
    unittest.main()
