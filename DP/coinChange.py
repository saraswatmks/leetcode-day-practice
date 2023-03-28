"""
Given infinite coins, find the minimum coins can sum to a target value.
https://leetcode.com/problems/coin-change/

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

"""
import sys


class Solution:
    def countCoins(self, amount, coins):
        """
        Using brute force approach (recursion)

        Time Complexity: O(m ^ n)
        m -> array length
        n -> depth of tree (in this case, the amount)

        Space Complexity: O(m ^ n)
        """
        if amount == 0:
            return 0

        ans = sys.maxsize

        for coin in coins:
            diff = amount - coin
            if diff >= 0:
                subAns = self.countCoins(diff, coins)
                if subAns + 1 < ans and subAns != sys.maxsize:
                    ans = subAns + 1
        return ans

    def countCountWithdp(self, amount, coins):
        """
        Time Complexity: O(amount * coins.length);
        Space Complexity: O(amount)
        """

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)

        if dp[-1] == float("inf"):
            return -1

        return dp[-1]

    def countCoinsBFS(self, amount, coins):
        """
        Taken from: https://leetcode.com/problems/coin-change/discuss/77361/Fast-Python-BFS-Solution

        Logic when to use BFS vs DFS:
        As a rule of thumbs, When you expect your solution closer to root of the search Tree then BFS is a good choice.
        But when you do expect your solution far from the root DFS is more efficient than BFS.

        The question requires the minimum number of coins, so you need to find a shortest path, hence you need to use BFS.

        Time Complexity: O(len(coins) * amount)
        Space Complexity: O(amount)

        """
        if amount == 0:
            return 0

        # [amount, number of coins (depth)]
        queue = [[0, 0]]
        visited = {0}
        step = 0
        for node, step in queue:
            for coin in coins:
                if node + coin in visited:
                    continue
                if node + coin == amount:
                    return step + 1
                elif node + coin < amount:
                    queue.append([node + coin, step + 1])
                    visited.add(node + coin)

        return -1

    def countCoinsBFS2(self, amount, coins):
        """
        This is same as countCoinsBFS but written differently.
        """
        q = [[0, 0]]  # amt so far, cnt
        visited = {0}

        while q:
            amt, cnt = q.pop(0)
            cnt += 1
            for i in range(len(coins)):
                tmp = amt + coins[i]
                if tmp in visited:
                    continue
                if tmp == amount:
                    return cnt
                elif tmp < amount:
                    q.append([tmp, cnt])
                    visited.add(tmp)
        return -1


if __name__ == "__main__":
    # coins = [1, 2, 5]
    coins = [7, 5, 3]
    amount = 18
    # sol = Solution().countCoins(amount, coins)
    # print(sol)
    sol = Solution().countCountWithdp(amount, coins)
    print(sol)
    # sol = Solution().countCoinsBFS(amount, coins)
    # print(sol)
