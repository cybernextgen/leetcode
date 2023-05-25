import unittest
from typing import List
import re

data = (
    (
        [
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com",
        ],
        2,
    ),
    (["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"], 3),
)


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        if not emails:
            return 0
        unique_emails = set()
        regex = re.compile(r"(?P<local_name>[^\+]*)(\+.*)?(?P<domain_name>@.*)")
        for email in emails:
            m = regex.search(email)
            if m:
                local_name = m.group("local_name").replace(".", "")
                domain_name = m.group("domain_name")
                unique_emails.add(local_name + domain_name)
        return len(unique_emails)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.numUniqueEmails(input_data), expected)


if __name__ == "__main__":
    unittest.main()
