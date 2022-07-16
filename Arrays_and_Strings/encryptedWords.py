"""
Return encrypted encoding given a word. 
https://www.metacareers.com/profile/coding_practice_question/?problem_id=223547538732703&c=614097939578133&ppid=275492097255885&practice_plan=0
"""

class Solution:
    def findEncryptedWords(self, s):
        """
        Time Complexity: O(n)
        """
        if len(s) <= 2: # ab, ba -> remain same
            return s

        mid = (len(s) // 2) -1 if len(s) % 2 == 0 else len(s) // 2

        left = s[:mid]
        right = s[mid+1:]

        return s[mid] + self.findEncryptedWords(left) + self.findEncryptedWords(right)


if __name__ == "__main__":
    s = 'facebook'
    sol = Solution().findEncryptedWords(s)
    print(sol)
    s = 'abcxcba'
    sol = Solution().findEncryptedWords(s)
    print(sol)
    s = 'abcd'
    sol = Solution().findEncryptedWords(s)
    print(sol)
