"""
Given infinite coins, check if target can be achieved using coins.
https://www.metacareers.com/profile/coding_practice_question/?problem_id=2903692913051025&c=614097939578133&ppid=275492097255885&practice_plan=0

"""
import sys


class Solution:
    def countCoins(self, target, coins):

        """
        Time Complexity: O(m ^ n) 
        Space Complexity: O(m ^ n)
        """

        if target == 0:
            return True

        if target < 0:
            return False

        for coin in coins:
            diff = target % coin
            if diff >= 0 and target >= coin:
                ans = self.countCoins(diff, coins)
                if ans:
                    return True
        return False


if __name__ == "__main__":
    # coins = [1, 2, 5]
    coins = [5, 10, 25, 100, 200]
    amount = 94
    sol = Solution().countCoins(amount, coins)
    print(sol)
    coins = [2, 3, 17, 18, 35, 29]
    amount = 59
    sol = Solution().countCoins(amount, coins)
    print(sol)
    coins = [3]
    amount = 1000000
    sol = Solution().countCoins(amount, coins)
    print(sol)
    coins = [4, 17, 29]
    amount = 80
    sol = Solution().countCoins(amount, coins)
    print(sol)
    coins = [7, 37]
    amount = 49
    sol = Solution().countCoins(amount, coins)
    print(sol)
