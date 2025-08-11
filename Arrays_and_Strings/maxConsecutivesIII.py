"""
This is a sliding window based question. 

Return max consecutive ones, when we can flip max k 0s.
https://leetcode.com/problems/max-consecutive-ones-iii/

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6

"""


class Solution:
    def longestOnes(self, nums: list, K: int):
        """
        Sliding window approach.
        Visual explanation: https://leetcode.com/problems/max-consecutive-ones-iii/discuss/719833/Python3-sliding-window-with-clear-example-explains-why-the-soln-works

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left = right = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                K -= 1

            if K < 0:
                if nums[left] == 0:
                    K += 1
                left += 1

        return right - left + 1

    def variantOne(self, days, pto):
        """
        Take from: https://www.youtube.com/watch?v=moTN6h5QkP8&list=PLtVcREFQDb6ZykTpgFhkQiPjLyrX1Y96D&index=14
        Worded around given W wordday and H holidays, determine max vacations you can take given k days off. 
        K can be in deciaml. Sliding window with a twist
        TC: O(n)
        SC: O(1)

        example:
        days = [H, W, W, H, W]
        pto = 2.78
        """
        max_vacation = 0
        # separate a decimal into int and float 
        whole_pto, partial_pto = int(pto), k - int(pto)
        left = 0

        for right in range(len(days)):
            if days[right] == 'W':
                pto -= 1
            while pto < 0:
                if days[left] == 'W':
                    pto+=1
                left += 1
            
            extension = 0.0
            # check extension only if either one before or after are W days
            if left>0 and days[left-1] == 'W' or right < len(days) and days[right+1] == 'W':
                extension=partial_pto
            
            max_vacation = max(max_vacation, right - left + 1 + extension)

        return max_vacation
                
                
        
        


if __name__ == "__main__":
    # nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    nums = [1, 1, 1, 0, 0, 0, 1]
    k = 2
    sol = Solution().longestOnes(nums, k)
    print(sol)
