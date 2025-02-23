### https://leetcode.com/discuss/interview-question/1188322/facebook-recruiting-portal-revenue-milestones

# Output
# Return a length-K array where K_i is the day on which company first had milestones[i] total revenue. If the milestone is never met, return -1.

# Example
# revenues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# milestones = [100, 200, 500]
# output = [4, 6, 10]

class Solution:

  def solutionOne(self, revenues, milestones):
    """
    Binary Search
    TC: O(N + MlogN) N <- length of revenue, M <- length of milestones
    SC: O(N + M)
    """
    pass

  def solutionTwo(self, revenues, milestones):
    """
    Hashmap
    TC: O(N + MlogM), N <- length of revenue, M <- length of milestones
    SC: O(N)
    """
    pass


if __name__ == "__main__":
  revenues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
  milestones = [100, 200, 500]
  s = Solution().solutionOne(revenues, milestones)
  print(f'{s=}')
  s = Solution().solutionTwo(revenues, milestones)
  print(f'{s=}')
