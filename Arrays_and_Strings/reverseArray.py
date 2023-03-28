"""
Given an array, reverse it without using extra space.

Input: arr = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""


class Solution:
    def solution(self, arr):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if len(arr) < 1:
            # nothing to reverse
            return arr
        
        s, e = 0, len(arr)-1

        while s<e:
            arr[s], arr[e] = arr[e], arr[s]
            s+=1
            e-=1
        return arr


if __name__ == "__main__":
    n = [1,2,3,4,5]
    s = Solution().solution(n)
    print(s)
