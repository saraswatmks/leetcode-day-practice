"""
Verify preorder sequence.
https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/

Input: preorder = [5,2,1,3,6]
Output: true
"""
import math
class Solution:
    def verifySequence(self, preorder: list):
        """
        Idea is to find the numbers where we observe an increase (low->high) variation. That is the left -> right child transition.
        We then go back to find the parent of the node. 

        Taken from: https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/discuss/68149/Python-solution-with-detailed-explanation

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        low = -math.inf
        ans = []
        for x in preorder:
            if x < low:
                False
            while ans and ans[-1] < x:
                low = ans.pop()
            ans.append(x)
        return True

if __name__ == "__main__":
    preorder = [5,2,1,3,6]
    sol = Solution().verifySequence(preorder)
    print(sol)
