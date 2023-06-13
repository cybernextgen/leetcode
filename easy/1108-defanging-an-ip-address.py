import unittest

data = (("1.1.1.1", "1[.]1[.]1[.]1"), ("255.100.50.0", "255[.]100[.]50[.]0"))


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.defangIPaddr(input_data), expected)


if __name__ == "__main__":
    unittest.main()
