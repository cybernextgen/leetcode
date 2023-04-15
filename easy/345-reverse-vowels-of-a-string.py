import unittest

data = (
    ("hello", "holle"),
    ("leetcode", "leotcede")
)


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels_set = set('aeiouAEIOU')
        left_index = 0
        right_index = len(s) - 1
        chars = list(s)
        while right_index > left_index:
            left_char = chars[left_index]
            right_char = chars[right_index]

            left_char_is_vowel = left_char in vowels_set
            right_char_is_vowel = right_char in vowels_set
            
            if left_char_is_vowel and right_char_is_vowel:
                chars[left_index], chars[right_index] = right_char, left_char
                left_index += 1
                right_index -= 1
                continue
                
            left_index += not left_char_is_vowel
            right_index -= not right_char_is_vowel
        return "".join(chars)
   

class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.reverseVowels(input_data), expected)

if __name__ == "__main__":
    unittest.main()