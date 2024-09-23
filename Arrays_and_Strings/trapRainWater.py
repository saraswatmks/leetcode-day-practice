"""
Calculate how much rain water can be trapped.
https://leetcode.com/problems/trapping-rain-water/solution/

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Input: height = [4,2,0,3,2,5]
Output: 9

"""


class Solution:
    def trapWaterOne(self, height: list):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        left = [height[0]] * len(height)
        right = [0] * len(height)
        right[-1] = height[-1]

        for i in range(1, len(height)):
            left[i] = max(height[i], left[i - 1])

        for i in range(len(height) - 2, -1, -1):
            right[i] = max(height[i], right[i + 1])

        max_water = 0
        for i in range(len(height)):
            max_water += min(left[i], right[i]) - height[i]

        return max_water

    def trapWaterTwo(self, height: list):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left = 0
        right = len(height) - 1
        volume = 0
        l_max, r_max = height[left], height[right]

        while left < right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])

            if l_max <= r_max:
                volume += l_max - height[left]
                left += 1
            else:
                volume += r_max - height[right]
                right -= 1

        return volume

    def trapThree(self, heights):
        pass  # j- i * min(heights[i], heights[j])


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    sol = Solution().trapWaterTwo(height)
    # print(sol)
    # height = [4, 2, 8, 0, 7, 3, 2, 5]
    # height = [4, 2, 0, 3, 2, 5]
    # sol = Solution().trapWaterTwo(height)
    print(sol)
