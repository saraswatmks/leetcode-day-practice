"""
Given the path, simplify it.
Basically, handle the ..
https://leetcode.com/problems/simplify-path/

Input: path = "/../"  <- here .. means go back one path
Output: "/"

"""


class Solution:
    def simplifyPath(self, path):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = []

        for subpath in path.split("/"):
            if subpath == "..":
                if stack:
                    stack.pop()
            elif subpath == "." or not subpath:
                continue
            else:
                stack.append(subpath)

        res = "/" + "/".join(stack)
        return res


if __name__ == "__main__":
    path = "/home//foo/joo/../joo1/joo2/..///"
    sol = Solution().simplifyPath(path)
    print(sol)
