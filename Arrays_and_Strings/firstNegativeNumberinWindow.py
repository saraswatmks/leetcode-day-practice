"""
Given an array, window size, find the first negative number in every window.

Input : arr[] = {12, -1, -7, 8, -15, 30, 16, 28} , k = 3
Output : -1 -1 -7 -15 -15 0

"""


class Solution:
    def firstNegative(self, nums, k):
        """
        This is a sliding window question of fixed length.

        Time Complexity: O(n)
        Space Complexity: O(n - k)
        """

        i = j = 0
        res = []
        temp = []

        while j < len(nums):
            if nums[j] < 0:
                temp.append(nums[j])
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                # if temp is empty
                if not temp:
                    # send zero, no neg found
                    res.append(0)
                else:
                    res.append(temp[0])
                    # remove the first element

                # slide the window
                # increase only if the negative number is found
                # nothing to do for positive numbers since they wont show up in temp.
                if nums[i] in temp:
                    temp = temp[1:]  # pop front
                i += 1
                j += 1
        return res


if __name__ == "__main__":
    arr = [12, -1, -7, 8, -15, 30, 16, 28]
    k = 3
    sol = Solution().firstNegative(arr, k)
    print(sol)
