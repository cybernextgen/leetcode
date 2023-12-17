class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        seen = []
        seen_index = 0
        result = []
        for word in words:
            if word == "prev":
                current_num = -1
                if abs(seen_index) < len(seen):
                    seen_index -= 1
                    current_num = seen[seen_index]                    
                result.append(current_num)
            else:
                seen.append(int(word))
                seen_index = 0
        return result
