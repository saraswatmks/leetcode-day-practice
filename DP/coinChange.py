"""
Given infinite coins, find the minimum coins can sum to a target value.
https://leetcode.com/problems/coin-change/

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
        Time Complexity: O(m * n);
        m -> array length
        n -> amount/depth of tree
        """

        def _minCount(amount, coins, dp):
            if amount == 0:
                return 0

            ans = sys.maxsize

            for coin in coins:
                diff = amount - coin
                if diff >= 0:
                    if dp[diff] != -1:
                        subAns = dp[diff]
                    else:
                        subAns = _minCount(diff, coins, dp)
                    if subAns + 1 < ans and subAns != sys.maxsize:
                        ans = subAns + 1

            dp[amount] = ans
            return dp[amount]

        dp = [-1] * (amount + 1)
        dp[0] = 0
        ans = _minCount(amount, coins, dp)

        return ans

    def countCoinsBFS(self, amount, coins):
        """
        Taken from: https://leetcode.com/problems/coin-change/discuss/77361/Fast-Python-BFS-Solution

        Logic when to use BFS vs DFS:
        As a rule of thumbs, When you expect your solution closer to root of the search Tree then BFS is a good choice.
        But when you do expect your solution far from the root DFS is more efficient than BFS.

        The question requires the minimum number of coins, so you need to find a shortest path, hence you need to use BFS.

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


if __name__ == "__main__":
    # coins = [1, 2, 5]
    coins = [7, 5, 1]
    amount = 18
    sol = Solution().countCoins(amount, coins)
    print(sol)
    sol = Solution().countCountWithdp(amount, coins)
    print(sol)
    sol = Solution().countCoinsBFS(amount, coins)
    print(sol)
