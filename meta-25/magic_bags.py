# You have N bags of candy. The ith bag contains arr[i] pieces of candy, and each of the bags is magical!
# It takes you 1 minute to eat all of the pieces of candy in a bag (irrespective of how many pieces of candy are inside), and as soon as you finish, the bag mysteriously refills. If there were x pieces of candy in the bag at the beginning of the minute, then after you've finished you'll find that floor(x/2) pieces are now inside.
# You have k minutes to eat as much candy as possible. How many pieces of candy can you eat?

# Examples

# N = 5 
# k = 3
# arr = [2, 1, 7, 4, 2]
# output = 14
# In the first minute you can eat 7 pieces of candy. That bag will refill with floor(7/2) = 3 pieces.
# In the second minute you can eat 4 pieces of candy from another bag. That bag will refill with floor(4/2) = 2 pieces.
# In the third minute you can eat the 3 pieces of candy that have appeared in the first bag that you ate.
# In total you can eat 7 + 4 + 3 = 14 pieces of candy.

import heapq

class Solution:
  def solutionOne(self, arr, k):
    """
    Heap Solution
    TC: (N log k)
    SC: O(k)
    """

    top_k_candies = []
    for num in arr:
      if len(top_k_candies) < k:
        heapq.heappush(top_k_candies, num)
      else:
        heapq.heappushpop(top_k_candies, num)

    # convert min_heap to max_heap
    top_k_candies = [-x for x in top_k_candies]
    heapq.heapify(top_k_candies)

    cnt = 0
    for _ in range(k):
      # fetch the highest number
      candies = -heapq.heappop(top_k_candies)
      cnt += candies
      # push the candies //2 value in the heap
      heapq.heappush(top_k_candies, -1 * (candies // 2))

    return cnt


if __name__ == "__main__":
  arr = [2, 1, 7, 4, 2]
  k = 3
  sol = Solution().solutionOne(arr, k)
  print(sol)
      
