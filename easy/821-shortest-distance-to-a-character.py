import unittest
from typing import List

data = (
    ("loveleetcode", "e", [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]),
    ("aaab", "b", [3, 2, 1, 0]),
)


class Solution:
    def shortestToChar(self, input_str: str, target_char: str) -> List[int]:
        result = []
        # forward pass
        distance = None
        for current_char in input_str:
            if distance is not None:
                distance += 1
            if current_char == target_char:
                distance = 0
            result.append(distance)
        # backward pass
        distance = None
        for index in range(len(input_str) - 1, -1, -1):
            if distance is not None:
                distance += 1
            current_char = input_str[index]
            if current_char == target_char:
                distance = 0
            current_result = result[index]

            if current_result is not None:
                if distance is None:
                    continue
                result[index] = min([current_result, distance])
            else:
                result[index] = distance
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_str, ch, expected in data:
            self.assertEqual(expected, s.shortestToChar(input_str, ch))


if __name__ == "__main__":
    unittest.main()
