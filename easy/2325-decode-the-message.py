class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        chars_map = {}
        char_index = 0
        for ch in key:
            if len(chars_map.keys()) == 26:
                break
            if ch not in chars_map and ch != " ":
                chars_map[ch] = char_index
                char_index += 1
            
        result = []
        for ch in message:
            if ch == " ":
                result.append(ch)
                continue
            result.append(chr(97 + chars_map[ch]))
        return "".join(result)
