"""
Return the number of full chess rounds you have played in the tournament.

https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/description/

Input: loginTime = "09:31", logoutTime = "10:14"
Output: 1
Explanation: You played one full round from 09:45 to 10:00.
You did not play the full round from 09:30 to 09:45 because you logged in at 09:31 after it began.
You did not play the full round from 10:00 to 10:15 because you logged out at 10:14 before it ended.

"""


class Solution:
    def solutionOne(self, loginTime, logoutTime):
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if loginTime > logoutTime:
            return self.solutionOne(loginTime, "24:00") + self.solutionOne(
                "00:00", logoutTime
            )

        # convert to minutes
        sH, sM = map(int, loginTime.split(":"))
        eH, eM = map(int, logoutTime.split(":"))

        start = sH * 60 + sM
        end = eH * 60 + eM

        num_games_end = end // 15
        num_games_start = start // 15 + (
            start % 15 > 0
        )  # handle case when start at 12:01 (need to exclude 12:01 to 12:15 slot)

        return max(0, num_games_end - num_games_start)


if __name__ == "__main__":
    loginTime = "21:30"
    logoutTime = "03:00"
    s = Solution().solutionOne(loginTime, logoutTime)
    print(s)
