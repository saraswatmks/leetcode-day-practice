"""
Asked in Bloomberg.

Another example would be [6,4,9,10,34,56,54] and output is 68. 
to explain it in a bit more detail 4 is the smallest weight, 
so we add 4 to the sum and remove it's adjacent numbers 6 and 9 from the list, 
in the next iteration we look at numbers 10, 
34 and 10 is thhe smallest so we add 10 to the sum and remove 34 and next iteration 
we look at 56 and 54 and 54 is the smaller number so we add 54 to the sum and remove 56 
so the total sum = 68

Input: [6,4,9,10,34,56,54]
Output: 68

Input: [4,3,2,1]
Output: 4

"""


class Solution:
    def solutionOne(self, nums):
        """
        Idea is to create a sorted list of weights. Then, using indexes from sorted list modify the original list.

        Time Complexity: O(nlogn)
        Space Complexity: O(n)
        """
        # track original index of the value
        items = [(val, idx) for idx, val in enumerate(nums)]
        items.sort()
        res = 0

        for val, idx in items:
            if nums[idx] == 0:
                continue
            res += val
            # set adjacents items for 0
            if idx - 1 >= 0 and nums[idx - 1]:
                nums[idx - 1] = 0
            if idx + 1 < len(nums) and nums[idx + 1]:
                nums[idx + 1] = 0

        return res


if __name__ == "__main__":
    s = [4, 3, 2, 1]
    print(Solution().solutionOne(s))
