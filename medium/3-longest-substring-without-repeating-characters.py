import unittest
import collections

data = (("pwwkew", 3), ("abcabcbb", 3), ("bbbbb", 1))


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        if len(s) == 1:
            return 1

        chars = set()
        dq = collections.deque()
        max_length = 0

        for ch in s:
            if ch in chars:
                while True:
                    ch_from_dq = dq.popleft()
                    if ch_from_dq == ch:
                        break
                    chars.remove(ch_from_dq)
            else:
                chars.add(ch)
                max_length = max(max_length, len(chars))
            dq.append(ch)
        return max_length


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.lengthOfLongestSubstring(input_data), expected)


if __name__ == "__main__":
    unittest.main()
