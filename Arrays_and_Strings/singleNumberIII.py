###
Single Number III

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
Example 2:

Input: nums = [-1,0]
Output: [-1,0]
###

class Solution:
  ###
  Key idea is to create groups based on the right most set bit, which means on the right which bit is 1.
  ###

  def solutionone(nums):
    res = 0
    # do a xor of all nums in the list
    for num in nums:
      res = res ^ num

    # find the right most bit
    rb = res & -res

    ans = []
    a, b = 0, 0
    for num in nums:
      if num & rb:
          a = a ^ num
      else:
          b = b ^ num

    return [a, b]

if __name__ == "__main__":
  nums=[1,2,3,1,8,2]
  s = Solution().solutionone(nums)
  print(s)

  
