"""

Calculate the minimum number of platforms to accomodate all trains.
https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/

Input: arr = [9:00, 9:40, 9:50, 11:00, 15:00, 18:00]
       dep = [9:10, 12:00, 11:20, 11:30, 19:00, 20:00]
Output: 3

"""
import heapq


class Solution:
    def minStationsOne(self, arr, dep):
        """

        Here the idea is to sort both arrays and count the overlaps.

        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """

        arr.sort()
        dep.sort()

        i = j = 0
        platform = count = 0

        while i < len(arr) and j < len(arr):
            if arr[i] <= dep[j]:
                i += 1
                count += 1
            elif arr[i] > dep[j]:
                j += 1
                count -= 1
            platform = max(platform, count)

        return platform

    def minStationsTwo(self, arr, dep):
        """
        Using heap.

        Time Complexity: O(n log n)
        Space Complexity: O(k)
        """

        timing = [(a, d) for a, d in zip(arr, dep)]
        # sort by arrival
        timing.sort()

        h = []
        # push the departure time of first train
        heapq.heappush(h, timing[0][1])
        count = platform = 0
        # start from second train and compare with previous
        for i in range(1, len(timing)):
            if timing[i][0] <= h[0]:
                count += 1
            else:
                heapq.heappop(h)
            heapq.heappush(h, timing[i][1])

    def minStationsThree(self, arr, dep):
        pass


if __name__ == "__main__":
    arr = [9.00, 9.40, 9.50, 11.00, 15.00, 18.00]
    dep = [9.10, 12.00, 11.20, 11.30, 19.00, 20.00]
    sol = Solution().minStationsOne(arr, dep)
    print(sol)
