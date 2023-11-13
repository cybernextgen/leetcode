class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        found_vowels = []
        for ch in s:
            if ch.lower() in vowels:
                found_vowels.append(ch)
        
        result = []
        found_vowels.sort(reverse=True)
        for ch in s:
            if ch.lower() in vowels:
                result.append(found_vowels.pop())
                continue
            result.append(ch)
        return "".join(result)
