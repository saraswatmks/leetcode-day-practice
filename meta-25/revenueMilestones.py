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
    N = len(revenues)
    cum_revenue = revenues[:]
    for i in range(1, len(revenues)):
      cum_revenue[i] += cum_revenue[i-1]

    def search(arr, target):
      l = 0
      r = len(arr) - 1

      while l < r:
        mid = (l+r)//2
        if arr[mid] >= target:
          r = mid
        else:
          l = mid+1
      return l

    ans = []
    # for each milestone for a binary search M log N
    for m in milestones:
      idx = search(revenues, m)
      ans.append(idx+1 if idx != N else -1)
      
    return ans

  def solutionTwo(self, revenues, milestones):
    """
    Hashmap
    TC: O(N + MlogM), N <- length of revenue, M <- length of milestones
    SC: O(N)
    """
    M= len(milestones)
    res = [0] * M
    hashmap = {c:i for i, c in enumerate(milestones)}
    
    k = 0
    for i, r in enumerate(revenues):
      total_revenue += r
      while k < M and total_revenue <= milestones[k]:
        res[hashmap[milestones[k]]] = i + 1
        k += 1
    return res
    

if __name__ == "__main__":
  revenues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
  milestones = [100, 200, 500]
  s = Solution().solutionOne(revenues, milestones)
  print(f'{s=}')
  s = Solution().solutionTwo(revenues, milestones)
  print(f'{s=}')
