class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels_set = {'a', 'e', 'i', 'o', 'u'}
        result = 0
        for word in words[left:right + 1]:
            if word[0] in vowels_set and word[-1] in vowels_set:
                result += 1
        return result
        
