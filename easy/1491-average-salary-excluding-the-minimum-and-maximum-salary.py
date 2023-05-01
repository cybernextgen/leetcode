import unittest
from typing import List
from collections import Counter

data = (([4000, 3000, 1000, 2000], 2500), ([1000, 2000, 3000], 2000))


class Solution1:
    def average(self, salary: List[int]) -> float:
        if not salary:
            return 0
        salary_counts = Counter(salary)
        min_salary = salary[0]
        max_salary = min_salary
        for s in salary_counts.keys():
            if s < min_salary:
                min_salary = s
                continue
            if s > max_salary:
                max_salary = s
        numerator = 0
        denominator = 0
        for s in salary_counts.keys():
            if s != min_salary and s != max_salary:
                count = salary_counts[s]
                numerator += s * count
                denominator += count
        if not numerator:
            return 0
        return numerator / denominator


class Solution2:
    def average(self, salary: List[int]) -> float:
        if not salary:
            return 0
        min_salary = salary[0]
        max_salary = min_salary
        numerator = 0
        denominator = 0
        for s in salary:
            numerator += s
            if s < min_salary:
                min_salary = s
                continue
            if s > max_salary:
                max_salary = s
        numerator -= max_salary + min_salary
        salary_len = len(salary) - 2
        if salary_len == 0:
            return 0
        return numerator / salary_len


class Solution3:
    def average(self, salary: List[int]) -> float:
        if not salary:
            return 0
        numerator = sum(salary)
        min_salary = min(salary)
        max_salary = max(salary)
        numerator -= min_salary + max_salary
        if len(salary) <= 2:
            return 0
        return numerator / (len(salary) - 2)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution3()

        for input_data, expected in data:
            self.assertEqual(s.average(input_data), expected)


if __name__ == "__main__":
    unittest.main()
