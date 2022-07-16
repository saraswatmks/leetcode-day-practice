"""
Count the subdomain visits.
https://leetcode.com/problems/subdomain-visit-count/

Input: cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output: ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]

"""

from typing import List
from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_map = defaultdict(int)
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            domains = domain.split(".")
            for i in range(len(domains)):
                domain_map[".".join(domains[i:])] += count

        return ["{} {}".format(ct, dom) for dom, ct in domain_map.items()]


if __name__ == "__main__":
    cpdomains = [
        "900 google.mail.com",
        "50 yahoo.com",
        "1 intel.mail.com",
        "5 wiki.org",
    ]
    sol = Solution().subdomainVisits(cpdomains)
    print(sol)
