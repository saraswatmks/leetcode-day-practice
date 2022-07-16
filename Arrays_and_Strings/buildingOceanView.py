"""
Building with an ocean view.
https://leetcode.com/problems/buildings-with-an-ocean-view/

Input: heights = [4,2,3,1]
Output: [0,2,3]

"""


class Solution:
    def findBuildings(self, heights):
        """
        Time Complexity: O(n)
        Space Complexity: O(k) k -> no. of indices
        """
        view = [len(heights) - 1]
        max_h = heights[-1]

        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > max_h:
                max_h = heights[i]
                view.append(i)

        return view[::-1]


if __name__ == "__main__":
    heights = [4, 2, 3, 1]
    sol = Solution().findBuildings(heights)
    print(sol)
    heights = [1, 3, 2, 4]
    sol = Solution().findBuildings(heights)
    print(sol)
