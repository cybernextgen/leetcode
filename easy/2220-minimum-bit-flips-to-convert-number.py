class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_binary_repr = f"{start:b}"
        goal_binary_repr = f"{goal:b}"

        if len(start_binary_repr) < len(goal_binary_repr):
            start_binary_repr, goal_binary_repr = goal_binary_repr, start_binary_repr

        max_len = len(start_binary_repr)
        goal_binary_repr = (
            "".join(["0"] * (max_len - len(goal_binary_repr))) + goal_binary_repr
        )

        result = 0
        for index in range(max_len):
            if goal_binary_repr[index] != start_binary_repr[index]:
                result += 1
        return result


if __name__ == "__main__":
    for start, goal, expected in ((10, 7, 3), (3, 4, 3)):
        assert Solution().minBitFlips(start, goal) == expected
