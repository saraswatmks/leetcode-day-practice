"""

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

https://leetcode.com/problems/shortest-way-to-form-string/description/

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
"""

from collections import defaultdict


class Solution:
    def solutionOne(self, source: str, target: str):
        """
        Two pointer greedy approach
        Time Complexity: O(M * N)
        Space Complexity: O(1)
        """
        count = 0
        t_p = 0

        while t_p < len(target):
            s_p = 0
            flag = False
            while s_p < len(source) and t_p < len(target):
                if source[s_p] == target[t_p]:
                    t_p += 1
                    flag = True
                s_p += 1

            if flag:
                count += 1
            else:
                return -1

        return count

    def solutionTwo(self, source, target):
        """
        Time Complexity: O(N logM)
        Space Complexity: O(N)
        """
        dic = defaultdict(list)
        for i, char in enumerate(source):
            dic[char].append(i)

        count = 1
        ind = 0

        for char in target:
            if char not in dic:
                return -1
            else:
                ind, count = self._binarysearch(char, ind, dic, count)
        return count

    def _binarysearch(self, char, ind, dic, count):
        lis = dic[char]

        if lis[-1] < ind:
            count += 1
            ind = 0

        l = 0
        r = len(lis) - 1

        while l < r:
            mid = (l + r) // 2
            if lis[mid] < ind:
                l = mid + 1
            else:
                r = mid

        return lis[l] + 1, count


if __name__ == "__main__":
    source = "xyz"
    target = "xzyxz"
    s = Solution().solutionOne(source, target)
    print(s)
