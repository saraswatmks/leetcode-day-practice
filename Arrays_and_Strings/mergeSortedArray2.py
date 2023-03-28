"""
Merge two sorted arrays into a new array.

Input: arr1 = [1,3,7,10,12]; arr2= [4,5,6,8,9,11]
Output: [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
"""


class Solution:
    def merge_arrays(self, arr1, arr2):
        """
        Using two pointer approach.

        Time Complexity: O(n+m) n,m are length of respective arrays.
        Space Complexity: O(n+m)
        """
        i = j = 0
        i_len = len(arr1)
        j_len = len(arr2)
        res = []
        while i < i_len and j < j_len:
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1

        res += arr1[i:] or arr2[j:]

        return res


if __name__ == "__main__":
    arr1 = [1, 3, 7, 10, 12]
    arr2 = [4, 5, 6, 8, 9, 11]
    s = Solution().merge_arrays(arr1, arr2)
    print(s)
