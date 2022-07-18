"""
Given an array, return the rank of array. Highest score, highest rank. 

https://leetcode.com/problems/rank-transform-of-an-array/

Input: arr = [40,10,20,30]
Output: [4,1,2,3]

"""

class Solution:
    def arrayRank(self, arr: list) -> list:
        d = {}
        for a in sorted(arr):
            if a in d:
                continue
            d[a] = len(d) + 1
        return list(map(d.get, arr))

if __name__ == "__main__":
    arr = [37,12,28,9,100,56,80,5,12]
    # [5,3,4,2,8,6,7,1,3]
    sol = Solution().arrayRank(arr)
    print(sol)