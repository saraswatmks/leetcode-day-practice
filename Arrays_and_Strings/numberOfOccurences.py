"""
Find occurences of a number in a sorted array.

https://leetcode.com/discuss/interview-question/124724/

Input: arr = [4, 4, 8, 8, 8, 15, 16, 23, 23, 42], target = 8
Output: 3

"""


class Solution:
    def count(self, arr: list, target: int):
        """
        Time complexity: O(log n)
        """
        left = self.binary_search(arr, target, True)
        if left < 0:
            return 0
        right = self.binary_search(arr, target, False)
        return right - left + 1

    def binary_search(self, arr: list, target: int, leftmost: bool):
        lo = 0
        hi = len(arr) - 1
        idx = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target > arr[mid]:
                lo = mid + 1
            elif target < arr[mid]:
                hi = mid - 1
            else:
                idx = mid
                if leftmost:
                    hi = mid - 1
                else:
                    lo = mid + 1
        return idx


if __name__ == "__main__":
    arr = [4, 4, 8, 8, 8, 15, 16, 23, 23, 42]
    target = 8
    s = Solution().count(arr, target)
    print(s)
