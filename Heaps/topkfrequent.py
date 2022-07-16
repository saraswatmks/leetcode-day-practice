"""
Find the top K most frequent elements.
https://leetcode.com/problems/top-k-frequent-elements/solution/

input: nums = [1,1,1,2,2,3], k = 2
output: [1,2]
"""

import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        """
        Using bucket sort approach.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        buckets = [[] for _ in range(len(nums))]
        counts = Counter(nums)
        ans = []

        for num, freq in counts.items():
            buckets[freq].append(num)

        # traverse from back
        for i in range(len(buckets) - 1, -1, -1):
            bucket = buckets[i]
            if bucket:
                for num in bucket:
                    ans.append(num)
        return ans[:k]
    
    def usingMaxHeap(self, nums, k):
        """
        Time Complexity: O(n) + O(k log N)
        Space: O(n)
        """
        count = Counter(nums)
        s = [(-val, num) for num, val in count.items()]
        res= []
        heapq.heapify(s)
        for i in range(k):
            res.append(heapq.heappop(s)[1])
        return res


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 3, 3, 5, 5, 5, 5, 5]
    print(Solution().topKFrequent(nums, 2))
