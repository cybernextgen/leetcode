class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        result = 0
        key_index = {"type": 0, "color": 1, "name": 2}[ruleKey]
        for item in items:
            if item[key_index] == ruleValue:
                result += 1
        return result
