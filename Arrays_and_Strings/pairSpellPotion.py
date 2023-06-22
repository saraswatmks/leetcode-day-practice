"""
You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.
You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.
Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description

Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.

"""


class Solution:
    """The trick is to sort potions and use binary search."""

    def solutionOne(self, spells, potions, success):
        """
        This gives TLE.
        Time Complexity: O(n*m)
        Space Complexity: O(n)
        """

        ans = []
        for s in spells:
            tmp = 0
            for p in potions:
                if s * p >= success:
                    tmp += 1
            ans.append(tmp)
        return ans

    def solutionTwo(self, spells, potions, success):
        """
        Time Complexity: O(n log n + n) ~ O(n log n)
        Space Complexity: O(n)
        """

        def _binarysearch(potions, spell, success):
            n = len(potions)
            low = 0
            high = n - 1
            bestIdx = n

            while low <= high:
                mid = (low + high) // 2
                prod = spell * potions[mid]

                if prod < success:
                    low = mid + 1
                # means all these numbers are of interest, we need to pick the lowest num from these to get number of elements
                elif prod >= success:
                    bestIdx = mid
                    high = mid - 1

            return (
                n - bestIdx
            )  # these many potions * mid values are above success

        n = len(spells)
        ans = [0] * n
        potions.sort()
        for i in range(n):
            ans[i] = _binarysearch(potions, spells[i], success)
        return ans


if __name__ == "__main__":
    spells = [5, 1, 3]
    potions = [1, 2, 3, 4, 5]
    success = 7
    s = Solution().solutionTwo(spells, potions, success)
    print(s)
