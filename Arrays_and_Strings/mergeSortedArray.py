"""
Given two sorted arrays, merge them.
https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/309/

input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3, m = 3
output: [1,2,2,3,5,6]

"""


class Solution:
    def mergeSorted(self, arr1: list, arr2: list, m: int, n: int):
        """
        Time Complexity: O(k) where k is max length among both array.
        Space Complexity: O(1) because we are reusing space from arr1.
        """
        # zero index
        last = m + n - 1
        while m > 0 and n > 0:
            if arr1[m - 1] > arr2[n - 1]:
                arr1[last] = arr1[m - 1]
                m -= 1
            else:
                arr1[last] = arr2[n - 1]
                n -= 1
            last -= 1
        return arr1


if __name__ == "__main__":
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    ans = Solution().mergeSorted(arr1=nums1, arr2=nums2, m=m, n=n)
    print(ans)
