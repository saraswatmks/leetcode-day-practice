"""
Find number of seats while maintaing social distancing.
https://www.metacareers.com/profile/coding_puzzles/?c=614097939578133&puzzle=203188678289677
https://leetcode.com/discuss/interview-question/1376859/Facebook-Puzzle/1032432

"""
from typing import List
import math


class Solution:
    def getMaxAdditionalDinersCount(self, N: int, M: int, K: int, S: List[int]):
        S.sort()
        start, res = 1, 0
        S.append(N + K + 1)
        for s in S:
            delta = s - K - start
            if delta > 0:
                res += math.ceil(delta / (K + 1))
            start = s + K + 1
        return res


if __name__ == "__main__":
    s = Solution().getMaxAdditionalDinersCount(N=10, K=1, M=2, S=[2, 6])
    print(s)  # expected 3
    s = Solution().getMaxAdditionalDinersCount(N=15, K=2, M=3, S=[11, 6, 14])
    print(s)  # expected 1
