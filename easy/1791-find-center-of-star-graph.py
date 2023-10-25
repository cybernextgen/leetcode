class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        p1 = edges[0]
        p2 = edges[1]
        if p1[0] == p2[0] or p1[0] == p2[1]:
            return p1[0]
        return p1[1]
