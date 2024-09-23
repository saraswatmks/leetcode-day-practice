"""
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].
You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.


https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/

Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

"""
import heapq

class Solution:
    def solutionOne(self, startTime, endTime, profit):
        """
        Time Complexity: O(nlogn)
        Space Complexity: O(n)
        """
        jobs = sorted([(startTime[i], endTime[i], profit[i])for i in range(len(startTime))])
        heap = []
        curr_profit = 0
        max_profit = 0
        for s, e, p in jobs:
            while heap and heap[0][0] <= s:
                _, tmp = heapq.heappop(heap)
                curr_profit = max(curr_profit, tmp)
            heapq.heappush(heap, (e, curr_profit + p))
            max_profit = max(max_profit, curr_profit + p)
        return max_profit

if __name__ == "__main__":
    startTime = [1,2,3,3]; endTime = [3,4,5,6]; profit = [50,10,40,70]
    sol = Solution()
    print(sol.solutionOne(startTime, endTime, profit)) # 120

