import unittest

data = (("bbbbbbbbbbbbbbbbbbb", 0), ("aabccabba", 3), ("cabaabac", 0), ("ca", 2))


class Solution:
    def minimumLength(self, s: str) -> int:

        left_index = 0
        right_index = len(s) - 1
        while True:
            current_left_index = left_index
            current_right_index = right_index

            left_ch = s[left_index]
            right_ch = s[right_index]

            if left_ch != right_ch or left_index >= right_index:
                break

            while (
                current_left_index < current_right_index
                and s[current_left_index + 1] == left_ch
            ):
                current_left_index += 1

            while (
                current_right_index > current_left_index
                and s[current_right_index - 1] == left_ch
            ):
                current_right_index -= 1

            if current_left_index >= current_right_index:
                return 0

            left_index = current_left_index + 1
            right_index = current_right_index - 1

        return right_index - left_index + 1


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, result in data:
            self.assertEqual(s.minimumLength(input_data), result)


if __name__ == "__main__":
    unittest.main()
