"""
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

https://leetcode.com/problems/asteroid-collision/description

"""


class Solution:
    """To solve this question, keep in mind certain cases which needs to be handled."""

    def solutionOne(self, asteroids):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = []
        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                # handle cases
                if stack[-1] < abs(asteroid):
                    stack.pop()
                    continue
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        return stack


if __name__ == "__main__":
    s = Solution().solutionOne([10, 2, -5])
    print(s)
